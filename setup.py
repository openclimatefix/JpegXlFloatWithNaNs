""" JpegXLFloatWithNaNs

JpegXlFloatWithNaNs is a codec for numcodecs for compressing image data in Zarr/Xarray

For more detailed information, please check the accompanying README.md.
"""
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="jpeg_xl_float_with_nans",
    version="0.0.4",
    license="MIT",
    description="""JpegXlFloatWithNaNs is a codec for numcodecs for compressing image data in Zarr/Xarray""",
    author="Jacob Bieker, Jack Kelly",
    author_email="info@openclimatefix.org",
    company="Open Climate Fix Ltd",
    install_requires=["numpy", "numcodecs", "imagecodecs"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)
