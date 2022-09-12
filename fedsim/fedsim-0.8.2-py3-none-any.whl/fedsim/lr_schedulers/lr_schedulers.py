r"""
Round to Round Learning Rate Schedulers
---------------------------------------

This module provides the learning rate schedulers for fedsim.

"""
from functools import partial

import torch
from torch.optim import SGD
from torch.optim import lr_scheduler


def get_scheduler(name, init_lr=None, optimizer=None, **kwargs):
    r"""makes and returns a modification of torch schedulers which optionally accepts
    either an optimizer or a learning rate.

    Args:
        name (str): name of the lr scheduler. It can be any of pytorch learning rate
            schedulers (``torch.optim.lr_schedulers``) at `torch optim`_.
        init_lr (float, optional): initial learnin rate. Defaults to None.
        optimizer (torch.optim.Optimizer, optional): optimizer to scheduler its
            learning rate. Defaults to None.

    Returns:
        torch.optim.lr_scheduler._LRScheduler: learning scheduler object

    .. warning::
        The arguments ``init_lr`` and ``optimizer`` are mutually exclusive,
        meaning that only one of them must have a value (that is not None).

    .. note::
        For complete list of arguemtns of each scheduler check it on pytorch
        documentation.

    .. _torch optim: https://pytorch.org/docs/stable/optim.html
    """
    if not ((init_lr is None) ^ (optimizer is None)):
        raise Exception("either init_lr should be None or optimizer")
    is_optim_none = optimizer is None
    if is_optim_none:
        dummy_params = [
            torch.tensor([1.0, 1.0], requires_grad=True),
        ]
        optimizer = SGD(params=dummy_params, lr=init_lr)
        optimizer.step()
    scheduler = getattr(lr_scheduler, name)(optimizer, **kwargs)
    if is_optim_none:
        optimizer.step()

    def last_lr(sch):
        return sch.get_last_lr()

    def last_private_lr(sch):
        return sch._last_lr

    if name == "ReduceLROnPlateau":
        scheduler._last_lr = None

    if hasattr(scheduler, "get_last_lr"):
        scheduler.get_the_last_lr = partial(last_lr, scheduler)
    elif hasattr(scheduler, "_last_lr"):
        scheduler.get_the_last_lr = partial(last_private_lr, scheduler)
    else:
        raise Exception("lr scheduler provides neither get_last_lr() nor _last_lr")

    return scheduler


def LambdaLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("LambdaLR", init_lr, optimizer, **kwargs)


def MultiplicativeLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("MultiplicativeLR", init_lr, optimizer, **kwargs)


def StepLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("StepLR", init_lr, optimizer, **kwargs)


def ConstantLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("ConstantLR", init_lr, optimizer, **kwargs)


def LinearLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("LinearLR", init_lr, optimizer, **kwargs)


def ExponentialLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("ExponentialLR", init_lr, optimizer, **kwargs)


def CosineAnnealingLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("CosineAnnealingLR", init_lr, optimizer, **kwargs)


def ChainedScheduler(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("ChainedScheduler", init_lr, optimizer, **kwargs)


def SequentialLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("SequentialLR", init_lr, optimizer, **kwargs)


def CyclicLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("CyclicLR", init_lr, optimizer, **kwargs)


def OneCycleLR(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("OneCycleLR", init_lr, optimizer, **kwargs)


def CosineAnnealingWarmRestarts(init_lr=None, optimizer=None, **kwargs):
    return get_scheduler("CosineAnnealingWarmRestarts", init_lr, optimizer, **kwargs)


def ReduceLROnPlateau(
    init_lr=None,
    optimizer=None,
    trigger_metric="cross_entropy_loss",
    **kwargs,
):
    scheduler = get_scheduler("ReduceLROnPlateau", init_lr, optimizer, **kwargs)
    scheduler.trigger_metric = trigger_metric
    return scheduler
