import pandas as pd
from sqlalchemy import create_engine, DECIMAL, DateTime, TEXT

source_df = pd.read_csv('out/xian.csv').dropna(axis=0, subset=[
    'project_id', 'winning_amt'], how='any')


# order_id_list = []
# winning_order_cnt_list = []
# project_winning_amt_list = []


# def get_order_id(length):
#     result_list = []
#     if length > 1:
#         for index in range(length):
#             result_list.append(str(index + 1))
#     else:
#         result_list = ['1']
#     return ','.join(result_list)


# for index, row in source_df.iterrows():
#     winning_order_cnt = len((row['supplier_name']).split(",")) or '1'
#     winning_order_cnt_list.append(winning_order_cnt)
#     order_id_list.append(get_order_id(winning_order_cnt))
#     project_winning_amt_list.append('')

# source_df["order_id"] = order_id_list
# source_df["winning_order_cnt"] = winning_order_cnt_list
# source_df["project_winning_amt"] = project_winning_amt_list


# source_df.to_csv('out/done/xian/raw_winning_notice_xian3.csv', index=False)


# engine = create_engine(
#     'mysql://root:Freeplus2020@127.0.0.1/infoConnect')
engine = create_engine(
    'mysql://infoconnect:noNaanKAlnX8h1mx@118.195.211.214/infoConnect_test')


dtype = {"cadidate_name": TEXT}

source_df.to_sql('d1_raw_winning_notice', con=engine,
                 if_exists='replace', index=False, dtype=dtype)
# if_exists='append'
