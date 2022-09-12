import os

from serotiny.io.image import image_loader
from .abstract_loader import Loader


_DEFAULT_LOADER_KWARGS = dict(
    select_channels=None,
    transform=None,
    reader=None,
    dtype=None,
    return_as_torch=True,
    force_3d=False,
    ome_zarr_level=0,
    ome_zarr_image_name="default",
)


class LoadImage(Loader):
    """Loader class, used to retrieve images from paths given in a dataframe
    column."""

    def __init__(
        self,
        column: str,
        file_type: str = "tiff",
        use_cache: bool = False,
        **loader_kwargs,
    ):
        """
        Parameters
        ----------
        column: str
            Dataframe column which contains the image path

        file_type: str
            File format of the image. For now, "tiff" is the
            only supported format. But in the future other formats (like zarr)
            might be supported too

        use_cache: bool = True
            Whether to cache images after downloading them once

        **loader_kwargs
            Additional kwargs passed to `serotiny.io.image.image_loader`

        """
        super().__init__()
        self.column = column

        if file_type not in ("tiff", "zarr"):
            raise NotImplementedError(f"File type {file_type} not supported.")

        self.file_type = file_type
        self.use_cache = use_cache

        self.loader_kwargs = _DEFAULT_LOADER_KWARGS.copy()
        self.loader_kwargs.update(loader_kwargs)

    def _get_cached_path(self, path):
        if not self.use_cache:
            return path

        conf_path = os.getenv("FSSPEC_CONFIG_DIR")
        if conf_path is not None:
            if "simplecache::" not in str(path):
                return "simplecache::" + path
        return path

    def __call__(self, row):
        if self.file_type in ("tiff", "zarr"):
            path = self._get_cached_path(row[self.column])
            return image_loader(path, **self.loader_kwargs)
