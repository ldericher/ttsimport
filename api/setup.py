from setuptools import setup, find_packages

setup(
    name="fftcgtool-api",
    version="0.1",
    packages=find_packages(),
    author="LDericher",
    author_email="ldericher@gmx.de",
    setup_requires="setuptools-pipfile",
    data_files=[
        ("", ["fftcgtool-api/carddb.zip"])
    ],
    include_package_data=True,
    use_pipfile=True,
    license="LICENSE",
    # description="",
    # long_description=open("README.md").read(),
)