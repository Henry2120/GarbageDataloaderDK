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

- Load the "Dataset" dataset as a dataframe for example (Will have modifications
```python
dataset_path = dataset.choose_dataset("Dataset")
```

- Load the Dataset dataset, divided into train and test sets as mentioned in the paper:
```python
batch_size = 32
img_height = 180
img_width = 180
```
```python
import tensorflow as tf
train_ds = tf.keras.utils.image_dataset_from_directory(
  dataset_path,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
```
```python
val_ds = tf.keras.utils.image_dataset_from_directory(
  dataset_path,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
```
- Get the list of class names for the collection of APK files we gathered:
```python
class_names = train_ds.class_names
print(class_names)
```

