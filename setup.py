from distutils.core import setup
import setuptools


setup(
    name='systemctl',
    version='',
    install_requires=[
        ''
    ],
    packages=[
        'systemctl'
    ],
    entry_points={
        "console_scripts": [
            "systemctl = systemctl:bin"
        ]
    }
)
