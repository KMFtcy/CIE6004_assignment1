# Env check
# check dataset file exists
import os.path
dataset_path = 'garbage_classification.zip'
if not os.path.isfile(dataset_path):
    print("The dataset is not found. Please put it in the root of the directory and rename it as \"garbage_classification.zip\".")
    exit()

print("hello world")