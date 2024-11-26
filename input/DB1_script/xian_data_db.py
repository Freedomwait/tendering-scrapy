import pandas as pd
from sqlalchemy import create_engine, DECIMAL, DateTime, TEXT

# engine = create_engine(
#     'mysql://root:Freeplus2020@127.0.0.1/infoConnect')
engine = create_engine(
    'mysql://infoconnect:noNaanKAlnX8h1mx@118.195.211.214/infoConnect_test')

source_df = pd.read_csv('./out/done/xian/schoolaugdata_shanxi1.csv')


# dtype = {"cadidate_name": TEXT}

source_df.to_sql('school_data_demo', con=engine,
                 if_exists='append', index=False)
