from dataclasses import dataclass, field
from typing import List, Optional

import tiledb


def default_X_data_row_filters() -> List[tiledb.Filter]:
    return [
        tiledb.RleFilter(),
    ]


def default_X_data_col_filters() -> List[tiledb.Filter]:
    return [
        tiledb.ZstdFilter(3),
    ]


def default_X_data_offset_filters() -> List[tiledb.Filter]:
    return [
        tiledb.DoubleDeltaFilter(),
        tiledb.BitWidthReductionFilter(),
        tiledb.ZstdFilter(),
    ]


def default_X_data_attr_filters() -> List[tiledb.Filter]:
    return [
        tiledb.ZstdFilter(),
    ]


# https://docs.python.org/3/library/dataclasses.html
# ValueError: mutable default <class 'list'> for field X_data_row_filters is not allowed: use default_factory
@dataclass(frozen=True)
class SOMAOptions:
    """
    A place to put configuration options various users may wish to change.
    These are mainly TileDB array-schema parameters.
    """

    # TODO: pending further work on
    # https://github.com/single-cell-data/TileDB-SingleCell/issues/27
    obs_extent: int = 256
    var_extent: int = 2048

    X_data_row_filters: List[tiledb.Filter] = field(
        default_factory=default_X_data_row_filters
    )
    X_data_col_filters: List[tiledb.Filter] = field(
        default_factory=default_X_data_col_filters
    )
    X_data_offset_filters: List[tiledb.Filter] = field(
        default_factory=default_X_data_offset_filters
    )
    X_data_attr_filters: List[tiledb.Filter] = field(
        default_factory=default_X_data_attr_filters
    )

    X_capacity: int = 100000
    X_tile_order: str = "row-major"
    X_cell_order: str = "row-major"

    # https://github.com/single-cell-data/TileDB-SingleCell/issues/27
    string_dim_zstd_level: int = 3

    write_X_chunked: bool = True
    goal_chunk_nnz: int = 20_000_000
    # Allows relocatability for local disk / S3, and correct behavior for TileDB Cloud
    member_uris_are_relative: Optional[bool] = None
    allows_duplicates: bool = False

    max_thread_pool_workers: int = 8
