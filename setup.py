#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='python-wordpress-xmlrpc',
      version='2.2',
      description='A python fronend for editing wordpress using xmlrpc',
      author='Dilawar Singh',
      author_email='dilawars@iitb.ac.in',
      url='https://github.com/dilawar/pywordress/',
      packages=['wordpress', 'wordpress_xmlrpc', 'wordpress_xmlrpc.methods'],
      license='BSD',
      classifiers=[
          'Programming Language :: Python',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: 1 - Beta',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Utilities',
          'Natural Language :: English',
      ],
      include_package_data=True,
      long_description=open('README.md').read(),
)
