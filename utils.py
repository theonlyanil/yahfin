def formatCell(df_series, dataType):
    results = []
    for item in df_series:
        try:
            item = item[dataType]
            results.append(item)
        except Exception as e:
            results.append(0)
    return results
