from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Shruthi Jaksani"
PROJECT_NAME = "Movie Recommender System"
SRC_REPO = "movie_recommender_system"   # underscores, matches your folder name
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="jaksanishruthi@gmail.com",
    description="A movie recommender system application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[SRC_REPO],   # <-- plural, and folder name must match actual code
    python_requires=">=3.7",  # <-- lowercase
    install_requires=LIST_OF_REQUIREMENTS,
)
