import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyutil_json",
    version="0.0.1",
    author="chhsiao",
    author_email="hsiao.chuanheng@gmail.com",
    description="python util for json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chhsiao1981/pyutil_json",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=[
        'python-rapidjson==0.8.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
