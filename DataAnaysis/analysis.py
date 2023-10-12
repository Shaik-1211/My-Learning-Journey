import pandas as pd
import json

data = pd.read_csv('enterprise-survey-2021.csv')

df = pd.DataFrame(data)
file_shape = df.shape
file_overview = {
    "file_meta": {
        "rows" : file_shape[0],
    "columns" : file_shape[1]}
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
    col_type = str(df[col].dtype)
    if col_type == 'object':
        prxint('string')
        null_count = df[col].isna().sum()
        distinct = df[col].unique().tolist()
        col_data = {
            "col_data": {
                "type": 'string',
                "null_count": int(null_count),
                "distinct_values" : distinct
            }
        }
        with open(str(col)+'.json','w') as json_file:
                json.dump(col_data,json_file)
    else : 
        null_count = df[col].isna().sum()
        distinct = df[col].unique().tolist()
        col_data = {
            "col_data": {
                "type": str(col_type),
                "null_count": int(null_count),
                "max":float(df[col].max()),
                "min":float(df[col].min()),
                "avg":float(df[col].mean()),
                "distinct_values" : distinct
            }
        }
        with open(str(col)+'.json','w') as json_file:
                json.dump(col_data,json_file)

   