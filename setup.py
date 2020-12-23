from setuptools import find_packages, setup


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="pydantic-django",
    version="0.0.7",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/jordaneremieff/pydantic-django/",
    description="Pydantic model support for Django ORM",
    long_description=get_long_description(),
    python_requires=">=3.7",
    package_data={"pydantic_django": ["py.typed"]},
    long_description_content_type="text/markdown",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
