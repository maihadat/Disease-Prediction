import numpy
import pandas as pd
import numpy as np
import random


# Compact into out.csv
dataset = pd.read_csv("Data_sets/dataset.csv")
Symptom_severity = pd.read_csv("Data_sets/Symptom-severity.csv", index_col="Symptom")


# Handle covid datafile
'''
df = pd.read_csv("Data_sets/Cleaned-Data.csv")
print(df.columns)
tmp = [0]
first_row = df.loc[0, "Fever":"Diarrhea"].values.tolist()
arr = np.array([first_row])

def mapping(lst):
    rs = ["Covid"]
    symptoms = ['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing',
       'Sore-Throat', 'None_Sympton', 'Pains', 'Nasal-Congestion',
       'Runny-Nose', 'Diarrhea']
    for i in range(len(lst[0])):
        if lst[0][i] == 1:
            rs.append(symptoms[i])
    while len(rs) < 18:
        rs.append(np.NAN)
    return rs
added_lst = []

while len(tmp) <= 240:
    index = random.randint(1, 316799)
    if index not in tmp:
        tmp.append(index)
        tmp_lst = [df.loc[index, "Fever":"Diarrhea"].values.tolist()]
        arr = np.concatenate((arr, np.array(tmp_lst)), axis=0)
        added_lst.append(mapping(tmp_lst))

df = pd.DataFrame(added_lst, columns=['Disease', 'Symptom_1', 'Symptom_2', 'Symptom_3',
                                                          'Symptom_4', 'Symptom_5', 'Symptom_6', 'Symptom_7',
                                                          'Symptom_8', 'Symptom_9', 'Symptom_10', 'Symptom_11',
                                                          'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15',
                                                          'Symptom_16', 'Symptom_17'])

dataset.append(df, ignore_index=True).to_csv("Data_sets/dataset.csv")
'''


# Data transforming
symptoms = ['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing',
       'Sore-Throat', 'None_Sympton', 'Pains', 'Nasal-Congestion',
       'Runny-Nose', 'Diarrhea']
for i in range(2, 18):
    for symptom in dataset.iloc[:, i].unique().tolist():
        if symptom not in symptoms:
            symptoms.append(symptom)

diseases = []
for disease in dataset.iloc[:, 1].unique().tolist():
    if disease not in diseases:
        diseases.append(disease)
list_of_dict = []
for i in range(1, dataset.shape[0]):
    dict = {}
    dict["Severity"] = 0
    tmp = dataset.iloc[i].tolist()
    for symptom in symptoms:
        if type(symptom) is str:
            if symptom in tmp:
                dict[symptom] = Symptom_severity.loc[symptom.replace(" ", ""), "weight"]
                dict["Severity"] += Symptom_severity.loc[symptom.replace(" ", ""), "weight"]
            else:
                dict[symptom] = 0
    dict["Disease"] = tmp[1]
    list_of_dict.append(dict)
df = pd.DataFrame(list_of_dict)
df.to_csv("Data_sets/out.csv")
