#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2007-2012 Christian Dywan <christian@twotoasts.de>
# Copyright (C) 2012-2013 Sean Davis <smd.seandavis@gmail.com>
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import sys
import os

from gi.repository import GObject

import locale
locale.textdomain('catfish')

# Add project root directory (enable symlink and trunk execution)
PROJECT_ROOT_DIRECTORY = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))

python_path = []
if os.path.abspath(__file__).startswith('/opt'):
    locale.bindtextdomain(
        'catfish', '/opt/extras.ubuntu.com/catfish/share/locale')
    syspath = sys.path[:]  # copy to avoid infinite loop in pending objects
    for path in syspath:
        opt_path = path.replace('/usr', '/opt/extras.ubuntu.com/catfish')
        python_path.insert(0, opt_path)
        sys.path.insert(0, opt_path)
    os.putenv("XDG_DATA_DIRS",
              "%s:%s" % ("/opt/extras.ubuntu.com/catfish/share/", os.getenv(
                  "XDG_DATA_DIRS", "/usr/local/share/:/usr/share/")))
if (os.path.exists(os.path.join(PROJECT_ROOT_DIRECTORY, 'catfish'))
        and PROJECT_ROOT_DIRECTORY not in sys.path):
    python_path.insert(0, PROJECT_ROOT_DIRECTORY)
    sys.path.insert(0, PROJECT_ROOT_DIRECTORY)
if python_path:
    os.putenv('PYTHONPATH', "%s:%s" % (os.getenv('PYTHONPATH', ''),
              ':'.join(python_path)))  # for subprocesses

if GObject.pygobject_version < (3, 9, 1):
    GObject.threads_init()

import catfish
catfish.main()
