import os
import io
import re
import sys

from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(cwd, 'README.rst'), encoding='utf-8') as fd:
    long_description = fd.read()


def file_find_version(filepath):

    with io.open(filepath, encoding='utf-8') as fd:

        VERSION = None

        regex = re.compile(
            r"""
        (                # Group and match
            VERSION      #    Match 'VERSION'
            \s*          #    Match zero or more spaces
            =            #    Match and equal sign
            \s*          #    Match zero or more spaces
        )                # End group

        '
        (                # Group and match
            \d\.\d\.\d  #    Match digit.digit.digit e.g. 1.2.3
        )                # End of group
        '
        """, re.VERBOSE)

        for line in fd:

            match = regex.match(line)
            if not match:
                continue

            # The second parenthesized subgroup.
            VERSION = match.group(2)
            break

        else:
            sys.exit('No VERSION variable defined in {} - aborting!'.format(
                filepath))

    return VERSION


def find_version():

    wscript_VERSION = file_find_version(
        filepath=os.path.join(cwd, 'wscript'))

    return wscript_VERSION


VERSION = find_version()

setup(
    name='ghp-index',
    version=VERSION,
    description=("Builds directory index pages for static websites."),
    long_description=long_description,
    url='https://github.com/steinwurf/',
    author='Steinwurf ApS',
    author_email='contact@steinwurf.com',
    license='BSD 3-clause "New" or "Revised" License',
    entry_points={
        'console_scripts': ['ghp_index=ghp_index.__main__:cli'],
    },
    keywords=('ghp-index'),
    packages=find_packages(where='src', exclude=['test']),
    package_dir={"": "src"},
    # How to include data in a package? We use the approach
    # outlined here https://stackoverflow.com/a/14211600 more
    # documentation on this:
    # http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
    #
    package_data={"ghp_index": ["templates/*", "templates/**/*"]},
    install_requires=['click', 'staticjinja'],

)
