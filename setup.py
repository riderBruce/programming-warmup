from setuptools import setup, find_packages

setup(
    name="my_logger",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "my-logger = my_logger.logger_core:main",
        ]
    },
)
