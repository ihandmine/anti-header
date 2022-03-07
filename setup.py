from __future__ import unicode_literals

import os
import io

from setuptools import setup


def list_dir(dir):
    result = [dir]
    for file in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, file)):
            result.extend(list_dir(os.path.join(dir, file)))
    return result


def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


NAME = "anti_header"
PACKAGES = list_dir('anti_header')
DESCRIPTION = "fake chrome, firefox, opera browser header anti header"
# LONG_DESCRIPTION = read('README.md')
LONG_DESCRIPTION = ''
URL = "https://github.com/ihandmine/anti-header.git"
AUTHOR = "handmine"
AUTHOR_EMAIL = "handmine@outlook.com"
VERSION = "0.0.1"
LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    keywords=[
        'header', 'headers', 'crawl header',
        'fake', 'fake header', 'browser', 'spider header',
        'anti', 'anti header', 'scrapy header'
    ],
)
