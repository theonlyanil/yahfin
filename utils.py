"""
    Column Formatting based on 'raw' or 'fmt'.
    It takes in a dataframe series and formats it based on input dataType.
    Before formatting, cell's data has a dict of data e.g.:
        {'raw': 12321, 'fmt':'12,321'}
    Input: formatCell(columnData, 'raw')
    Output: 12321
"""
def formatColumn(df_series, dataType):
    results = []
    for item in df_series:
        try:
            item = item[dataType]
            results.append(item)
        except Exception as e:
            results.append(0)
    return results
