import random
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence

import tinytim.data as data_features


TableFilter = Sequence[bool]
DataMapping = Mapping[str, Sequence]
DataDict = Dict[str, Sequence]


def column_filter(column: Sequence, func: Callable[[Any], bool]) -> List[bool]:
    return [func(item) for item in column]


def indexes_from_filter(f: TableFilter) -> List[int]:
    return [i for i, b in enumerate(f) if b]


def filter_list_by_indexes(values: Sequence, indexes: Sequence[int]) -> List:
    """Return only values in indexes."""
    return [values[i] for i in indexes]


def filter_by_indexes(data: DataMapping, indexes: Sequence[int]) -> DataDict:
    """Return only rows in indexes"""
    return {col: filter_list_by_indexes(values, indexes) for col, values in data.items()}


def filter_data(data: DataMapping, f: TableFilter) -> DataDict:
    indexes = indexes_from_filter(f)
    return filter_by_indexes(data, indexes)


def filter_by_column_func(
    data: DataMapping,
    column_name: str,
    func: Callable[[Any], bool]
) -> DataDict:
    """Return only rows of data where named column equals value."""
    indexes = [i for i, val in enumerate(data[column_name]) if func(val)]
    return filter_by_indexes(data, indexes)


def filter_by_column_eq(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column equals value."""
    return filter_by_column_func(data, column_name, lambda x: x == value)


def filter_by_column_ne(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column does not equal value."""
    return filter_by_column_func(data, column_name, lambda x: x != value)


def filter_by_column_gt(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column is greater than value."""
    return filter_by_column_func(data, column_name, lambda x: x > value)


def filter_by_column_lt(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column is less than value."""
    return filter_by_column_func(data, column_name, lambda x: x < value)


def filter_by_column_ge(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column is greater than or equal value."""
    return filter_by_column_func(data, column_name, lambda x: x >= value)


def filter_by_column_le(data: DataMapping, column_name: str, value) -> DataDict:
    """Return only rows of data where named column is less than or equal value."""
    return filter_by_column_func(data, column_name, lambda x: x <= value)


def filter_by_column_isin(data: DataMapping, column_name: str, values: Sequence) -> DataDict:
    """Return only rows of data where named column is in values."""
    return filter_by_column_func(data, column_name, lambda x: x in values)


def filter_by_column_notin(data: DataMapping, column_name: str, values: Sequence) -> DataDict:
    """Return only rows of data where named column is not in values."""
    return filter_by_column_func(data, column_name, lambda x: x not in values)


def sample(data: DataMapping, n: int, random_state: Optional[int] = None) -> DataDict:
    """return random sample of n rows"""
    if random_state is not None:
        random.seed(random_state)
    indexes = random.sample(range(data_features.row_count(data)), n)
    return filter_by_indexes(data, indexes)


def only_columns(data: DataMapping, column_names: Sequence[str]) -> DataDict:
    """Return new TableDict with only column_names."""
    return {col: data[col] for col in column_names}


def sample_indexes(data: DataMapping, n: int, random_state: Optional[int] = None) -> List[int]:
    """return random sample of n indexes"""
    if random_state is not None:
        random.seed(random_state)
    return random.sample(range(data_features.row_count(data)), n)