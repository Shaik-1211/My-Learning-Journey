import pandas as pd
import re

data = pd.read_csv('student.csv')

#Extract only rows that have a status of either pass or fail from student.csv
req_data = data.loc[(data['status'] == 'pass') | (data['status'] == 'fail')]

#write the extracted data to another file
req_data.reset_index(drop=True,inplace = True)
req_data = req_data.rename_axis('index',axis=1)
req_data.to_csv('filtered_data.csv',index_label='index')


#filtering using regex
df = data.dropna()
df = df[df['Name'].str.contains('a|u')]
print(df)
