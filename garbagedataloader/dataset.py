import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds

import pathlib

dataset_url = "http://clouds.iec-uit.com/smartbin.dataset/Datasets_test2.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=7MLCQ3OIV5012VWFPS9B%2F20240110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240110T021101Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiI3TUxDUTNPSVY1MDEyVldGUFM5QiIsImV4cCI6MTcwNDg5NTgzMiwicGFyZW50Ijoic21hcnRiaW4ifQ.9BPzedddwL9kZ6pqRhZUrrSXH619EB2XEW1HS2zHEL4-n6vvqv5ee-3_AyAA0_o5SWt8_tom4w32_J8i7Z_TNA&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=454bfbd3436c71b432193f436f91b45b62ba625edab1adc789cf2619a2a4b76d"
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
