from setuptools import find_packages, setup

# Read the requirements from the requirements.txt file
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

# Read the long description from README.md
with open("README.md", "r",encoding="utf-8") as fh:
    LONG_DESC = fh.read()

setup(
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    name="preln",
    packages=find_packages(include=["Preln", "Preln.core", "Preln.core.__features"]),
    version="0.5.9",
    description="A preprocessing library for text in Spanish",
    author="Adrián H.S & Raúl M.R",
    author_email="adrihs.dev@gmail.com",
    license="MIT",
    install_requires=[],  # Use requirements.txt here
    url="https://github.com/Adri-Hdez/Preln",
    include_package_data=True,
)

