import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tvpdownloader",
    version="0.2.0",
    author="Patrick Kubiak",
    author_email="pk9948@rit.edu",
    description="Download episodes from vod.tvp.pl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patkub/tvpdownloader",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
