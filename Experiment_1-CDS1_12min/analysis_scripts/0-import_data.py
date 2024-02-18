from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np
import shutil
import os
import glob

output_folder = "Experiment_1-CDS1_12min/raw_data/"  ### Change for each experiment

input_folders = [

"B:/Chaperone_subgroup/Bailey/Optimised_Buffer/230503/230503_FlucCDS1_Native/Channel532 - andor_Seq0001/230503_FlucCDS1_Native_123/230503_FlucCDS1_Native_123_allmol/",
"B:/Chaperone_subgroup/Bailey/Optimised_Buffer/230503/230503_FlucCDS1_MF/Channel532 - andor_Seq0001/230503_FlucCDS1_MF_123/230503_FlucCDS1_MF_123_allmol/",
"B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040110/240117_CDS!_7040110/240117_CDS!_7040110_2/12min/",
"B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040110/240117_CDS!_7040110/240117_CDS!_7040110_4/24min/",
'B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040110/240117_CDS!_7040110/240117_CDS!_7040110_6/36min/',
'B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040110/240117_CDS!_7040110/240117_CDS!_7040110_8/48min/',
'B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040110/240117_CDS!_7040110/240117_CDS!_7040110_10/60min/',
'B:/Chaperone_subgroup/Bailey/2024/240116_CDS1_repeat/240117_CDS!_7040/240117_CDS!_7040/240117_CDS!_7040_allmol/'
]

def move_folders(input_folders, filetype, output_folder):
    for folder in input_folders:
        new_folder = folder.split("/")[-2]
        if not os.path.exists(f"{output_folder}{new_folder}/"):
            os.makedirs(f"{output_folder}{new_folder}/")
        filelist = [filename for filename in os.listdir(folder) if filetype in filename] # create list of files
        for filename in filelist:
            shutil.copyfile(f"{folder}{filename}", f"{output_folder}{new_folder}/{filename}")        # if need to change filenames could have a function defined above that changes it
move_folders(input_folders, ".dat", output_folder)

