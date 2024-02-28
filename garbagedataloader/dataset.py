import numpy as np
import os
import pathlib
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from pathlib import Path

# Function to get list of a dataset
def get_list_dataset():
  return[
    "Garbage_classification_dataset",
    "Garbage_dataset",
    "TrashType_Image_Dataset",
    "dataset_capstone_9",
    "Drinking_waste_classification",
    "Garbage_classification_2",
    "garbage1_dataset",
    "GIGO",
    "Garbage_Classification_5",
    "Outdoor_garbage_classification_dataset",
    "GARBAGE_DATASET",
    "Garbage_Classification_3",
    "Garbage_classification_4",
    "clean_dirty_garbage",
    "garbage_classification_enhanced",
    "dataset_224",
    "AquaTrash",
    "Neural_Ocean_Dataset",
    "Domestic Trash",
    "trash_dataset",
    "trashify_image_dataset",
    "Bag_classes",
    "Bag4classes",
    "Garbage_Classification",
    "Dataset",
    "waste_dataset",
    "Datasets_test2"
]

# Choose dataset and get archive
def choose_dataset(selected_dataset):
  main_url = "http://clouds.iec-uit.com/smartbin.dataset/"
  dataset_url = main_url + selected_dataset + '.zip'
  archive = tf.keras.utils.get_file(origin=dataset_url, extract=True)
  archive, _ = os.path.splitext(archive)
  archive = Path(archive)
  return archive

archive = choose_dataset_and_get_archive("Datasets_test2")

# Image count inside of a dataset
def dataset_image_count(archive):
    return len(list(archive.glob('*/*.jpg')))

# Train dataset
def train_ds(dataset_path=archive, validation_split=0.2, subset="training", seed=123, img_height=256, img_width=256, batch_size=32):
    train_ds = tf.keras.utils.image_dataset_from_directory(
      dataset_path,
      validation_split=validation_split,
      subset=subset,
      seed=seed,
      image_size=(img_height, img_width),
      batch_size=batch_size
    )
    return train_ds

# Validation dataset
def val_ds(dataset_path=archive, validation_split=0.2, subset="validation", seed=123, img_height=256, img_width=256, batch_size=32):
    val_ds = tf.keras.utils.image_dataset_from_directory(
      dataset_path,
      validation_split=validation_split,
      subset=subset,
      seed=seed,
      image_size=(img_height, img_width),
      batch_size=batch_size
    )
    return val_ds

# Function to get classnames
def get_classnames():
  return train_ds.class_names

# Function to print out samples 
def get_images_using_matplotlib(dataset, class_names):
  plt.figure(figsize=(10, 10))
  for images, labels in train_ds.take(1):
    for i in range(9):
      ax = plt.subplot(3, 3, i + 1)
      plt.imshow(images[i].numpy().astype("uint8"))
      plt.title(class_names[labels[i]])
      plt.axis("off")
  plt.show()



















