# PyLucene (packaged)

This repo automatically packages [PyLucene](https://lucene.apache.org/pylucene/) so it can be pip-installable!

## Installation

Since it is [not possible](https://921kiyo.com/python-packaging-edge-cases/) (
seriously!) to package a python module that depends on local wheel dependencies and packages installed from PyPI cannot
depend on packages which are not also hosted on PyPI, pylucene can only be installed from this repository:

```bash
pip install git+https://github.com/hscells/pylucene-packaged.git
```

Essentially, this repo acts as a dummy wrapper which installs the correct version of pylucene for your platform as its
only dependency.

## Supported Platforms

See: [dist/](dist/) for a list of supported platforms.