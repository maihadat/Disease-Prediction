
import pandas as pd
import numpy as np
import random


dataset = pd.read_csv("Data_sets/dataset.csv")
Symptom_severity = pd.read_csv("Data_sets/Symptom-severity.csv", index_col="Symptom")


# Handle covid datafile from raw to add too dataset.csv
df = pd.read_csv("Data_sets/Cleaned-Data.csv")
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


# Data transforming from raw to binary with weight on  file
dataset = pd.read_csv("Data_sets/dataset.csv")
symptoms = []
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
                #dict[symptom] = Symptom_severity.loc[symptom.replace(" ", ""), "weight"]
                #dict["Severity"] += Symptom_severity.loc[symptom.replace(" ", ""), "weight"]
                dict[symptom] = 1
            else:
                dict[symptom] = 0
    dict["Disease"] = tmp[1]
    list_of_dict.append(dict)
df = pd.DataFrame(list_of_dict)
df.to_csv("Data_sets/out.csv")


# Change value of similar symptoms with covid symptom to 1
df = pd.read_csv("Data_sets/out.csv")
Symptom_severity = pd.read_csv("Data_sets/Symptom-severity.csv", index_col="Symptom")
similar_symptoms = {
    'Fever': [' high_fever', ' mild_fever'],
    'Tiredness': [' fatigue'],
    'Dry-Cough': [' cough'],
    'Difficulty-in-Breathing': [' breathlessness'],
    'Sore-Throat': [' patches_in_throat', ' throat_irritation'],
    'None_Sympton': [],
    'Pains': [' painful_walking', ' malaise', ' muscle_pain', ' muscle_weakness', ' back_pain'],
    'Nasal-Congestion': [],
    'Runny-Nose': [' runny_nose'],
    'Diarrhea': [' diarrhoea']
}
for case_idx in range(4920, 5159):
    for symptom in similar_symptoms:
        if df.loc[case_idx, symptom] != 0:
            list_of_similar_symp = similar_symptoms[symptom]
            for similar_symp in list_of_similar_symp:
                #df.loc[case_idx, similar_symp] = Symptom_severity.loc[similar_symp.replace(" ", ""), "weight"]
                #df.loc[case_idx, "Severity"] += Symptom_severity.loc[similar_symp.replace(" ", ""), "weight"]
                df.loc[case_idx, similar_symp] = 1
(df.iloc[:, 1:]).to_csv("Data_sets/out.csv")


# Add some outliers
out = pd.read_csv("Data_sets/out.csv")
out_added_outliers = pd.read_csv("Data_sets/out.csv")
for i in range(250):
    outlier_idx = random.randint(0, out.shape[0]-1)
    diseases = out["Disease"].unique()
    disease_idx = random.randint(0, len(diseases)-1)
    out.loc[outlier_idx, "Disease"] = diseases[disease_idx]
    out_added_outliers = out_added_outliers.append(out.iloc[outlier_idx], ignore_index=True)
(out_added_outliers.iloc[:, 1:]).to_csv("Data_sets/out.csv")


