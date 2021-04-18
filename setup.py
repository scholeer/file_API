import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file_api",
    version="0.0.11",
    author="Richard Paprok",
    author_email="scholeer@seznam.cz",
    description="Flask restful file api package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scholeer/file_API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["flask", "flask_restful"],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={"console_scripts": ["file-api=src.app:main"]},
)