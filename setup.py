from setuptools import setup, find_packages

setup(
    name="dataloader",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",  # Add other dependencies as needed
    ],
    author="Van Dat Nguyen",
    author_email="",
    description="Smartbin Dataloader is a library installed to facilitate the quick download and loading of data for researchers, allowing them to access this data as swiftly as possible.",
    long_description="Smartbin Dataloader is a compilation of six available datasets that we used in our paper, including Bag classes dataset, Bag 4 classes dataset, a garbage classification dataset, a trash dataset, a trashify image dataset, and a dataset created by our own, and a feature dataset collected by our proposed framework (which includes CSV files).",
    long_description_content_type="text/markdown",
    url="https://github.com/dpkien2809/UIT-Smartbin/tree/Dataloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
