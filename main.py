# Env check
# check dataset file exists
import os.path
dataset_path = 'garbage_classification.zip'
if not os.path.isfile(dataset_path):
    print("The dataset is not found. Please put it in the root of the directory and rename it as \"garbage_classification.zip\".")
    print("The link of the dataset is: https://drive.google.com/file/d/1kcwBy_yG47Mp2iyq6Oo6ACojgdXRt4Bs/view?pli=1")
    exit()

# extract the dataset
import zipfile
if not os.path.exists("garbage_classification/"):
    print("extracting the dataset... ")
    with zipfile.ZipFile(dataset_path, 'r') as zip_ref:
        zip_ref.extractall("./")
print("The dataset has been extracted.")

print("hello world")