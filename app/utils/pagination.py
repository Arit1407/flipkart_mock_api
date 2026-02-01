def paginate(df, offset: int, limit: int):
    return df.iloc[offset: offset + limit]
