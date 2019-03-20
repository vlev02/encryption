import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="encryption-SL",
    version="0.0.1",
    author="Sean Lau",
    author_email="vlev02@qq.com",
    description="A small encryption package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlev02/encryption.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)