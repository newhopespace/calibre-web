#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  This file is part of the Calibre-Web (https://github.com/janeczku/calibre-web)
#    Copyright (C) 2019 decentral1se
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#  """Calibre-web distribution package setuptools installer."""

#setup python-ldap for Windows: https://www.python-ldap.org/en/python-ldap-3.3.0/installing.html#windows
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap
# https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels
# For python 3.10 try: pip install https://download.lfd.uci.edu/pythonlibs/archived/python_ldap-3.4.0-cp310-cp310-win_amd64.whl
# https://anaconda.org/conda-forge/python-ldap
# conda install -c conda-forge python-ldap

from setuptools import setup
import os
import re
import codecs

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^STABLE_VERSION\s+=\s+{['\"]version['\"]:\s*['\"](.*)['\"]}",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    version=find_version("src", "calibreweb", "cps", "constants.py")
)
