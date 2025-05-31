
# importing all the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import os

print(os.getcwd())  
print(os.listdir())  

#'r'-raw string, is used bcoz  in Python, backslashes (\) are escape characters so the line was breaking.
df = pd.read_csv(r'C:\Users\SHRUTI VAISHNAV\Downloads\Titanic-Dataset.csv')
print(df.head())




