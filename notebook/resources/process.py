# Set Global Variables
RANDOM_STATE=42

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler


def getDir():
    return os.getcwd()

def changeDir(path):
    os.chdir(path)
    return getDir()

def readCSV(fpath):
    return pd.read_csv(fpath, sep=",")

def writeCSV(DF, fpath):
    return DF.to_csv(fpath, mode = 'w', index=False)

def getDummies(column):
    return pd.get_dummies(column, prefix=column.name)

def mergeDF(origDF, joinDF):
    origDF = pd.merge (
                        left=origDF
                        , right=joinDF
                        , left_index=True
                        , right_index=True
             )
    
    return origDF

def scaleDataFrame(featuresDF):
    scaler = StandardScaler(with_mean=True, with_std=True)
    features_scaled = pd.DataFrame(scaler.fit_transform(featuresDF), columns=featuresDF.columns)
    
    return features_scaled
