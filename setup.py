import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myproj",
    version="0.0.1",
    author="Jatinder Grewal",
    author_email="jt@grewal.co",
    description="A myproj template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamgrewal/",
    packages=setuptools.find_packages(),
    install_requires=[
          'more-itertools',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
