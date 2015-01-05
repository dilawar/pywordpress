import os
import sys
import shutil
from setuptools import setup

#configDir = os.path.join(os.environ['HOME'], '.config', 'twordpress')

#if not os.path.isdir(configDir):
    #os.makedirs(configDir, )

#shutil.copy('config', configDir)

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
        name='twordpress'
        , version='0.9.8'
        , description='A command-line tool to manage your blogs on wordpress'
        , long_description= read('README.rst') 
        , url = 'https://dilawar.github.io/pywordpress'
        , license = 'GNU-GPL'
        , author = 'Dilawar Singh'
        , author_email = 'dilawars@iitb.ac.in'
        , maintainer = 'Dilawar Singh'
        , maintainer_email = 'dilawars@iitb.ac.in'
        , requires = ['Python (>=2.6)']
        , extras_require = {
            'markdown' : ["pandoc", "markdown"]
            }
        , packages=['wordpress'
            , 'wordpress_xmlrpc'
            , 'wordpress_xmlrpc.methods'
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
        twordpress=pyblog.main:main
        """
        )


