from datetime import datetime

"""
    Column Cell Formatting based on 'raw' or 'fmt'.
    It takes in a dataframe series and formats it based on input dataType.
    Before formatting, cell's data has a dict of data e.g.:
        {'raw': 12321, 'fmt':'12,321'}
    Input: formatCell(columnData, 'raw')
    Output: 12321
"""
def formatColumnCells(df_series, dataType):
    results = []
    for item in df_series:
        try:
            item = item[dataType]
            results.append(item)
        except Exception as e:
            results.append(item)
    return results

def formatColumns(df):
    # Column Formatting
    for col in df:
        if col == 'endDate':
            df[col] = formatColumnCells(df[col], 'fmt')
        else:
            df[col] = formatColumnCells(df[col], 'raw')

    return df

"""
    Breaks a list into a chunk of pre defined size.
    Code sourced from Internet.
"""
def chunk_list(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]

def epochToDatetimeList(listOfTimestamps):
    result = []
    for timestamp in listOfTimestamps:
        date_time = datetime.fromtimestamp(timestamp)
        result.append(date_time)

    return result
