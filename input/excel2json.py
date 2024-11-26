import pandas as pd

df = pd.read_csv('./zj_school_list.csv')

df.to_json('./school_list.json', force_ascii=False)

# print(df)