# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')

options = {"py2exe": {
    "compressed": 1,  # 压缩
    "optimize": 2,
    "bundle_files": 1,  # 所有文件打包成一个exe文件
}}

setup(
    console=[{'script': "wangye.py", "icon_resources": [(1, "robot.ico")]}],
    options=options,
    zipfile=None
)