import os
from setuptools import setup, find_packages

with open('VERSION', 'r') as f:
    version = f.read().strip()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='spotify-cli',
    version=version,
    author='Benj Ledesma',
    author_email='benj.ledesma@gmail.com',
    description=(
        'Control Spotify playback on any device through the command line.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ledesmablt/spotify-cli',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'Click',
        # PyPI release does not support Python v3.10 (causes ImportError)
        'PyInquirer @ git+https://github.com/CITGuru/PyInquirer',
        'tabulate',
    ],
    entry_points='''
        [console_scripts]
        spotify=cli.spotify:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)
