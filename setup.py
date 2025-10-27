from setuptools import setup

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Shruthi Jaksani"
PROJECT_NAME = "Movie Recommender System"
SRC_REPO = "movie-recommender-system"
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="jaksanishruthi@gmail.com",
    description="A movie recommender system application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package = [SRC_REPO],
    PYTHON_REQUIRES=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
)
