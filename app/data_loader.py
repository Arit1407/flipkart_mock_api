import pandas as pd
from functools import lru_cache
from app.config import DATA_PATH

@lru_cache()
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    # Drop index column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # 🔥 CRITICAL FIX: convert NaN → None
    df = df.where(pd.notnull(df), None)

    return df
