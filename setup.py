from distutils.core import setup
import setuptools


setup(
    name='systemctl',
    version='1.1',
    install_requires=[
        ''
    ],
    packages=[
        'systemctl'
    ],
    entry_points={
        "console_scripts": [
            "systemctl = systemctl.bin:run"
        ]
    }
)
