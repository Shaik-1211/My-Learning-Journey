import pandas as pd
import json

data = pd.read_csv('enterprise-survey-2021.csv')

df = pd.DataFrame(data)
file_shape = df.shape
file_overview = {
    "rows" : file_shape[0],
    "columns" : file_shape[1]
}
print(file_overview)
with open("file_overview.json","w") as json_file:
    json.dump(file_overview,json_file)

# This is another method of writing data to a json file.
# result = json.dumps(file_overview)
# print(result)

col_types = df.dtypes.tolist()
print(col_types,type(col_types))
col_names = df.columns.tolist()

for col in col_names:
    i=0
    col_type = df[col].dtype
    print(type(col_type))
    if col_type == dtype('O'):
        print('yes object')
    else : print('no')
    i+=1
    if i == 3:
        break
    pass