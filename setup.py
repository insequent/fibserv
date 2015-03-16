#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Copyright 2015 Josh Conant

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='fibserv',
    version='0.1',
    author='Josh Conant',
    author_email='deathbeforedishes@gmail.com',
    url='http://github.com/insequent/fibserv',
    license='Apache License, Version 2.0',
    description='A simple web service with swappable content and backend',
    long_description=readme,
    packages=['fibserv',
              'fibserv.content',
              'fibserv.engines'],
    classifiers=( 
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    )

)
