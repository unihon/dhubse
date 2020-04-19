from setuptools import setup, find_packages

NAME = 'dhubse'
AUTHOR = 'unihon'


with open('src/dhubse/VERSION', 'r') as fh:
    VERSION = fh.read()

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email='unihon@outlook.com',
    license='LGPLv3',
    description='Docker image search tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/unihon/dhubse',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
    ],
    python_requires='>=3.5',
    install_requires=['requests', 'tabulate'],
    keywords='docker image tag search registry',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': ['dhubse=dhubse.dhubse:main'],
    },
    include_package_data=True,
    package_data={'': ['VERSION']},
    project_urls={
        'Bug Reports': 'https://github.com/unihon/dhubse/issues',
        'Funding': 'https://pypi.org/project/dhubse/',
        'Source': 'https://github.com/unihon/dhubse',
    },
)
