import os
from setuptools import setup


setup(
    name='exa',
    packages=['exa'],
    version='0.0.1',
    author='tchoedak',
    author_email='tchoedak@gmail.com',
    url='https://tchoedak.com',
    install_requires=[
        'click',
        'bs4',
        'requests',
        'twilio'
    ],
    entry_points={
        'console_scripts': ['exa=exa.app:cli'],
    },
)
