from setuptools import setup, find_packages

setup(
    name="ttsimport",
    version="0.4.0",
    packages=find_packages(),
    author="LDericher",
    author_email="ldericher@gmx.de",
    setup_requires="setuptools-pipfile",
    data_files=[
        ("", ["ttsimport/carddb.zip"])
    ],
    include_package_data=True,
    use_pipfile=True,
    license="LICENSE",
    # description="",
    # long_description=open("README.md").read(),
)
