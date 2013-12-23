import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
        name='twordpress'
        , version='0.1.3'
        , description='A command-line tool to manage your blogs on wordpress.'
        , long_description=(
            read('README.rst') 
            )
        , url = 'https://github.com/dilawar/pywordpress'
        , author = 'Dilawar Singh'
        , author_email = 'dilawars@iitb.ac.in'
        , 
        , requires = ['Python (>=2.6)']
        , extras_require = {
            'markdown' : ["pandoc", "markdown"]
            }
        , packages=['wordpress'
            , 'wordpress_xmlrpc'
            , 'wordpress_xmlrpc.methods'
            , 'text'
            ]
        , include_package_data = True
        , classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        entry_points="""
        [console_scripts]
        twordpress=wordpress.main:main
        """
        )


