from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

    setup(
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        name="preln",
        packages=find_packages(include=["Preln", "Preln.core", "Preln.core.__features"]),
        version="0.5.2",
        description="A preprocessing libray for text in spanish",
        author="Adrián H.S & Raúl M.R",
        author_email="adrihs.dev@gmail.com",
        license="MIT",
        install_requires=[
            "pandas",
            "nltk",
            "numpy",
            "openpyxl",
            "lxml",
            "sqlalchemy",
            "es_core_news_sm",
        ],
        setup_requires=["pytest-runner"],
        url="https://github.com/Adri-Hdez/Preln",
        tests_require=["pytest"],
        test_suite="tests",
        include_package_data=True,
    )
