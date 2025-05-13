from setuptools import setup, find_packages

setup(
    name="lemonbreak",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.6",
        # Añade otras dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'lemonbreak=src.lemonbreak:main',
        ],
    },
)
