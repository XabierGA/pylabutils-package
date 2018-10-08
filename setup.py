import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'plabutils',
    version = '0.5dev',
    author = 'Mario García',
    author_email = 'mariogarcc@gmail.com',
    description = 'Some utils for working with python and latex for a simple lab environment',
    long_description_content_type ='text/markdown',
    url = 'https://github.com/pypa/sampleproject',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
