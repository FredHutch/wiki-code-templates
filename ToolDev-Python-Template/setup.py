"""
This setup.py allows your python package to be installed. 
Please completely update the parameters in the opts dictionary. 
For more information, see https://stackoverflow.com/questions/1471994/what-is-setup-py
"""

from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name='ProjectName',
            maintainer='Name1, Name2, etc',
            maintainer_email='your_email',
            description='Add short description',
            long_description=("""Add an even more detailed description"""),
            url='your_repo_url_here',
            license='MIT', # default license, change here and in the git repo if using a different license
            author='Name1, Name2, etc',
            author_email='your_email',
            version='0.1',
            packages=PACKAGES
           )

setup(**opts)
