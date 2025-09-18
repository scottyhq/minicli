import xarray as xr
from rich import print

def dump_datatree(file_path):
    """Dump the data tree of an HDF5 file."""
    with xr.open_datatree(file_path, engine='h5netcdf') as ds:
        print(ds)
