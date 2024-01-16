import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf

import pathlib

dataset_url = "smartbin.dataset/Datasets_test2.zip"
archive = tf.keras.utils.get_file(origin=dataset_url, extract=True)

# Dataset path
data_dir = pathlib.Path(archive).with_suffix("")


# print(data_dir)
# Define get_list_dataset function
def get_list_dataset():
    dataset_contents = os.listdir(data_dir)
    print(dataset_contents)


# Example to get_list_dataset()
# get_list_dataset()


# Choose dataset from get_list_dataset()
def choose_dataset(classnames):
    return os.path.join(data_dir, classnames)


# Examples to get a specific dataset path
# dataset_path = choose_dataset("Dataset")
# print(dataset_path)
