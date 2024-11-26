import pandas as pd
from sqlalchemy import create_engine, DECIMAL, DateTime, TEXT


result_data_frame = pd.read_csv('out/done/all.csv').dropna(axis=0, subset=[
    'project_id', 'winning_amt'], how='any')

engine = create_engine(
    'mysql://infoconnect:noNaanKAlnX8h1mx@118.195.211.214/infoConnect_test')


dtype = {"cadidate_name": TEXT}

result_data_frame.to_sql('d1_raw_winning_notice_1', con=engine,
                         if_exists='replace', index=False, dtype=dtype)
