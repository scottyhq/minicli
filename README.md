# minicli

The purpose of this repository is to demo how to creat a CLI app that can be installed as a package into an *existing* Python virtual environment.

For demo purposes, we recommend creating a new virtual environment: `conda create -n testcli pip` and `conda activate testcli`. When you're done simply `conda env remove -n testcli`

This example app is called `hdf-info` and it prints out the tree structure of an HDF5 file using `xarray`.

## Install

```
pip install git+https://github.com/scottyhq/minicli.git
```

Get an HDF file to work with:

```bash
HDF_URL=https://nisar.asf.earthdatacloud.nasa.gov/NISAR-SAMPLE-DATA/GCOV/NISAR_L2_PR_GCOV_001_030_A_019_2800_SHNA_A_20081012T060911_20081012T060925_D00404_N_F_J_001/NISAR_L2_PR_GCOV_001_030_A_019_2800_SHNA_A_20081012T060911_20081012T060925_D00404_N_F_J_001.h5

wget $HDF_URL -O /tmp/myhdf.h5
```

## CLI Usage

```bash
hdf-info --help
hdf-info -i /tmp/myhdf.h5
```

## Package Usage

```python
from minicli import hdfutils
hdfutils.dump_datatree("/tmp/myhdf.h5")
```

## Recommended References

* essential setup:
https://learn.scientific-python.org/development/guides/packaging-compiled/#command-line

* full tutorial on using argparse for CLI apps:
  https://realpython.com/command-line-interfaces-python-argparse/

* slightly more sophisticated setup using [Typer](https://typer.tiangolo.com/) (automate CLI help messages etc):
  https://packaging.python.org/en/latest/guides/creating-command-line-tools/#creating-the-package

    * here’s a small app example using [cyclopts](https://cyclopts.readthedocs.io/en/latest/), which I've found to be a more user-friendly alternative to Typer: https://github.com/uw-cryo/lidar_tools?tab=readme-ov-file#cli-commands
