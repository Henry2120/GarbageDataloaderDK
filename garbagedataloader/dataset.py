import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds

import pathlib

dataset_url = "http://clouds.iec-uit.com/smartbin.dataset/Datasets_test2.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0LL7CN2X7HRX7JBTGWLN%2F20240110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240110T145840Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiIwTEw3Q04yWDdIUlg3SkJUR1dMTiIsImV4cCI6MTcwNDk0MTkxNSwicGFyZW50Ijoic21hcnRiaW4ifQ.FCx85mCiSDRx82R1JQXHw3WukfZd1CtyeCqGpSJ7pYd8bvY-2LmTusaZg_QXR7jzjAIoxXF4tSt5R-_MpG67Eg&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=9ca1b4093115b9d2195223833d263bd026e048c3fc39823b835d9ee093148eee"
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
