#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""
setup.py script for the ansicolortags project (https://bitbucket.org/lbesson/ansicolortags)

References:
- https://packaging.python.org/en/latest/distributing/#setup-py
- http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html#setup-py-description
"""

from distutils.core import setup
import generatewordcloud
# FIXED change name of the file to be a valid Python module name


setup(name='generatewordcloud',
      version=generatewordcloud.version,
      description='A simple Python (2 or 3) script to generate a PNG word-cloud image from a bunch of text files. Based on word_cloud.',
      long_description=''.join(open('README.rst', 'r').readlines()),
      author='Lilian Besson',
      author_email='naereen@crans.org',
      url='https://github.com/Naereen/generate-word-cloud.py',
      download_url='https://github.com/Naereen/generate-word-cloud.py',
      license='MIT',
      platforms=['Windows', 'Windows Cygwin', 'GNU/Linux', 'MacOS'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Terminals',
          'Topic :: Utilities'
      ],
      py_modules=['generatewordcloud'],
      )

# End of setup.py
