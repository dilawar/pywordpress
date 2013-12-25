import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
        name='pyblog'
        , version='0.9.0'
        , description='A command-line tool to manage your blogs on wordpress and blogger'
        , long_description=(
            read('README.rst') 
            )
        , url = 'https://github.com/dilawar/pywordpress'
        , licence = 'GNU-GPL'
        , author = 'Dilawar Singh'
        , author_email = 'dilawars@iitb.ac.in'
        , maintainer = 'Dilawar Singh'
        , maintainer_email = 'dilawars@iitb.ac.in'
        , requires = ['Python (>=2.6)', 'python-gdata']
        , extras_require = {
            'markdown' : ["pandoc", "markdown"]
            }
        , packages=['wordpress'
            , 'wordpress_xmlrpc'
            , 'wordpress_xmlrpc.methods'
            , 'blogger'
            , 'pyblog'
            ]
        , include_package_data = True
        , classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Environment :: Console',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            ],
        entry_points="""
        [console_scripts]
        pyblog=pyblog.main:main
        """
        )


