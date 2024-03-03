# Introduction
"Garbage Dataset" is a compilation of many publicly available datasets that we collected on the internet and put into a single dataloader that the user can easily pull out each of them for Machine Learning training and validation
This dataloader is currently in beta and will have some changes later, includes updating more datasets, fixing bugs, etc...

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

- Choose any dataset from the list of dataset names. For demonstration, this article will get the Datasets_test2 as an example
```python
archive = dataset.choose_dataset("Datasets_test2")
```
- Get the image count of the dataset
```python
dataset.dataset_image_count(archive)
```
- Load the dataset, divided into train and validation
```python
# Note: The value is set to default as below. Change the value at your own will
# dataset_path=archive, validation_split=0.2, subset="training", seed=123, img_height=256, img_width=256, batch_size=32
train_ds = train_ds(dataset_path=archive)
val_ds = val_ds(dataset_path=archive)
```


- Get the list of class names for the collection of files we gathered:
```python
class_names = train_ds.class_names
print(class_names)
```

- Get the image example from matplotlib
```python
dataset.get_images_using_matplotlib(train_ds, class_names)
```




