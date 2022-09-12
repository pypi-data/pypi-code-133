import numpy as np

from scipy.sparse import csr_matrix

from small_text.data.datasets import split_data
from small_text.utils.labels import list_to_csr


def get_splits(train_set, validation_set, multi_label=False, validation_set_size=0.1):
    """Helper method to ensure that a validation set is available after calling this method.
    This is only necessary when the previous code did not select a validation set prior to this,
    otherwise the passed `validation_set` variable is not None and no action is necessary here.

    If a split is necessary, stratified sampling is used in the single-label case,
    and random sampling is used in the multi-label case.

    Parameters
    ----------
    train_set : Dataset
        Training set.
    validation_set : Dataset
        Validation set.
    multi_label : bool, default=False
        Indicates if the splits are for a multi-label problem.
    validation_set_size : float, default=0.1
        Specifies the size of the validation set (as a percentage of the training set). Only
        used if a new split is created.

    Returns
    -------
    sub_train : Dataset
        A subset used for training. Defaults to `train_set` if `validation_set` is not `None`.
    sub_valid : Dataset
        A subset used for validation. Defaults to `validation_set` is
    """
    if validation_set is None:
        if multi_label:
            # note: this is not an optimal multi-label strategy right now
            sub_train, sub_valid = split_data(train_set, y=train_set.y.indices, strategy='random',
                                              validation_set_size=validation_set_size)
        else:
            sub_train, sub_valid = split_data(train_set, y=train_set.y, strategy='stratified',
                                              validation_set_size=validation_set_size)
    else:
        sub_train, sub_valid = train_set, validation_set

    return sub_train, sub_valid


def prediction_result(proba, multi_label, num_classes, enc=None, return_proba=False):
    """Helper method which returns a single- or multi-label prediction result.

    Parameters
    ----------
    proba : np.ndarray[float]
        A (dense) probability matrix of shape (num_instances, num_classes).
    multi_label : bool
        If True, this method returns a result suitable for a multi-label classification,
        otherwise for a single-label classification.
    num_classes : int
        The number of classes.
    enc : sklearn.preprocessing.MultiLabelBinarizer, default=None
        A multi-label binarizer which is (optionally) used if `multi-label` is `True`. It is only
        intended to be used in combination with
        `small_text.integrations.pytorch.classifiers.PytorchClassifier`-based classifiers.
    return_proba : bool, default=False
        Also returns the probability if `True`. This is intended to be used with `multi_label=True`
        where it returns a sparse matrix with only the probabilities for the predicted labels. For
        the single-label case this simply returns the given `proba` input.

    Returns
    -------
    result : np.ndarray[int] or csr_matrix
        An empty ndarray of predictions if `return_prediction` is True.
    proba : np.ndarray[float] or csr_matrix[np.float64]
        An empty ndarray of predictions if `return_prediction` is True.
    """
    if multi_label:
        predictions_binarized = np.where(proba > 0.5, 1, 0)
        if enc is not None:
            predictions = enc.inverse_transform(predictions_binarized)
        else:
            def multihot_to_list(x):
                return [i for i, item in enumerate(x) if item > 0]
            predictions = [multihot_to_list(row) for row in predictions_binarized]
        predictions = list_to_csr(predictions, shape=(len(predictions), num_classes))

        if return_proba:
            data = proba[predictions_binarized.astype(bool)]
            proba = csr_matrix((data, predictions.indices, predictions.indptr),
                               shape=predictions.shape,
                               dtype=np.float64)
    else:
        predictions = np.argmax(proba, axis=1)

    if return_proba:
        return predictions, proba

    return predictions


def empty_result(multi_label, num_classes, return_prediction=True, return_proba=True):
    """Helper method which returns an empty classification result. This ensures that all results
    have the correct dtype.

    At least one of `prediction` and `proba` must be `True`.

    Parameters
    ----------
    multi_label : bool
        Indicates a multi-label setting if `True`, otherwise a single-label setting
        when set to `False`.
    num_classes : int
        The number of classes.
    return_prediction : bool, default=True
        If `True`, returns an empty result of prediction.
    return_proba : bool, default=True
        If `True`, returns an empty result of probabilities.

    Returns
    -------
    predictions : np.ndarray[np.int64]
        An empty ndarray of predictions if `return_prediction` is True.
    proba : np.ndarray[float]
        An empty ndarray of probabilities if `return_proba` is True.
    """
    if not return_prediction and not return_proba:
        raise ValueError('Invalid usage: At least one of \'prediction\' or \'proba\' must be True')

    elif multi_label:
        if return_prediction and return_proba:
            return csr_matrix((0, num_classes), dtype=np.int64), csr_matrix((0, num_classes), dtype=float)
        elif return_prediction:
            return csr_matrix((0, num_classes), dtype=np.int64)
        else:
            return csr_matrix((0, num_classes), dtype=float)
    else:
        if return_prediction and return_proba:
            return np.empty((0, num_classes), dtype=np.int64), np.empty(shape=(0, num_classes), dtype=float)
        elif return_prediction:
            return np.empty((0, num_classes), dtype=np.int64)
        else:
            return np.empty((0, num_classes), dtype=float)
