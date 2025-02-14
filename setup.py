#! /usr/bin/env python
#
# Copyright (C) 2015 Chris Holdgraf
# <choldgraf@gmail.com>
#
# Adapted from MNE-Python

import os
import setuptools
from numpy.distutils.core import setup

version = "0.1"
with open(os.path.join('modelingtools','__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')


descr = """Tools for analyzing electrocorticography data."""

DISTNAME = 'modelingtools'
DESCRIPTION = descr
MAINTAINER = 'Chris Holdgraf'
MAINTAINER_EMAIL = 'choldgraf@gmail.com'
URL = 'https://github.com/choldgraf/paper-encoding_decoding_electrophysiology'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/choldgraf/paper-encoding_decoding_electrophysiology'
VERSION = version


if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=False,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.md').read(),
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=['Intended Audience :: Science/Research',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved',
                       'Programming Language :: Python',
                       'Topic :: Software Development',
                       'Topic :: Scientific/Engineering',
                       'Operating System :: OSX'],
          platforms='any',
          packages=['modelingtools'],
          package_data={},
          scripts=[])
