import os

from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
        name='pywordpress'
        , version='0.1.0'
        , description='Client to manage your wordpress.org blog'
        , long_description=(
            read('README.rst') + '\n\n' +
            read('HISTORY.rst') + '\n\n' +
            read('AUTHORS.rst'))
        , url = 'https://github.com/dilawar/pywordpress'
        , licence = 'GNU-GPL'
        , author = 'Dilawar Singh'
        , author_email = 'dilawars@iitb.ac.in'
        , py_modules=['pywordpress']
        , include_package_data = True
        , packages=find_packages(exclude=['tests'])
        , classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Wordpress Users',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        )


