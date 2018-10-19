import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywikiscraper",
    version="0.0.4",
    author="sam-iau",
    author_email="sam-iau@outlook.com",
    description="A litte package to easy scrape any wikipedia page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frier-sam/pywikiscraper",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests==2.19.1','lxml==4.2.5',''
      ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)