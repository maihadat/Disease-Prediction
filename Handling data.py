import pandas as pd

dataset = pd.read_csv("Data_sets/dataset.csv")
Symptom_severity = pd.read_csv("Data_sets/Symptom-severity.csv", index_col="Symptom")

symptoms = []
for i in range(1, 18):
    for symptom in dataset.iloc[:, i].unique().tolist():
        if symptom not in symptoms:
            symptoms.append(symptom)
            
diseases = []
for disease in dataset.iloc[:, 0].unique().tolist():
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
    dict["Disease"] = tmp[0]
    list_of_dict.append(dict)
    
    
df = pd.DataFrame(list_of_dict)
df.to_csv("Data_sets/out.csv")
