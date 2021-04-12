#Imports 
import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split


def clean_mushroom(df):
    labelencoder=LabelEncoder()
    for column in df.columns:
        df[column] = labelencoder.fit_transform(df[column])
    df = df.drop(["veil-type"],axis=1)
    return df


def split_data(df, stratify_by=None):
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    return train, validate, test