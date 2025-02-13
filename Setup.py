from setuptools import setup, find_packages

setup(
    name="Install n Use",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Roshan D Roy",
    author_email="roshandeepuroy@gmail.com",
    description="A package that installs and imports a Python package if it's not found.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/R-D-R248/Install-n-Use",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
