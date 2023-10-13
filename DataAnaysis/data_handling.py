import pandas as pd
import os

# data_frames = []

# folder_path = 'Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data'
# files = os.listdir(folder_path)
# print(files)
# for file in files:
#     if file.endswith('.csv'):
#         file_path = os.path.join(folder_path, file)
#         # print(str(file_path))
#         df = pd.read_csv(file_path)
#         data_frames.append(df)
#         # print(len(data_frames))
# data = pd.concat(data_frames)
# data.to_csv('sales-data.csv',index=False)

# Add a month column to data dataframe
data['Month'] = data['Order Date'].str[0:2]
data = data['Month'].astype('int32')
print(data.head())
