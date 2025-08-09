import pandas as pd
from config import DATA_PATH

def load_sales_data():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    return df
