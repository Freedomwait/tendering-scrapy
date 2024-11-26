from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    'mysql://infoconnect:[password]@[IP]/[bd]')

list = [
    {
        'table': 'order_item_cleaned_demo',
        'file': 'order_item_cleaned - Sheet1.csv'
    },
    {
        'table': 'buyer_supplier_all',
        'file': 'buyer_supplier_all - Sheet1.csv'
    }
]


for item in list:
    df = pd.read_csv(item["file"])
    df.to_sql(item["table"], con=engine, if_exists='replace')
