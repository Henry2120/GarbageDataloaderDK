# Introduction
"Garbage Dataset" is a compilation of many publicly available datasets that we collected on the internet and put into a single dataloader that the user can easily pull out each of them for Machine Learning training and validation

# Installation
```sh
pip install git+https://github.com/Henry2120/GarbageDataloaderDK.git
```

# Instructions

- Get the list of dataset names:
```python
from garbagedataloader import dataset
dataset.get_list_dataset()
```

- Load the "AndroVul" dataset as a dataframe:
```python
dataset.load_data("AndroVul")
```

- Load the AndroAnalyzer dataset, divided into train and test sets as mentioned in the paper:
```python
dataset.load_data("AndroAnalyzer", train_set=True)
dataset.load_data("AndroAnalyzer", train_set=False)
```

- Get the list of class names for the collection of APK files we gathered:
```python
dataset.get_classname()
```

- Get the list of "Banking" files in the training set:
```python
dataset.get_sha256("Banking", train_set=True)
```
