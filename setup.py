import pathlib
from setuptools import find_packages, setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cryptowatch-sdk",
    version="1.0.0",
    description="Python bindinds for the Cryptowatch API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cryptowatch/cw-sdk-python",
    author="Cryptowatch",
    author_email="infra@cryptowat.ch",
    keywords="cryptowatch sdk bitcoin crypto",
    license="BSD-2",
    classifiers=[
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["marshmallow", "requests", "pyyaml"],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    tests_require=[
        "pytest >= 5.3.1",
        "pytest-mock >= 1.12",
        "requests-mock >= 1.7"
    ]
)
