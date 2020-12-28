from datetime import datetime
import pandas as pd

"""
    Column Cell Formatting based on 'raw' or 'fmt'.
    It takes in a dataframe series and formats it based on input dataType.
    Before formatting, cell's data has a dict of data e.g.:
        {'raw': 12321, 'fmt':'12,321'}
    Input: formatColumnCells(columnData, 'raw')
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

"""
    This function iterates through all the columns in a DataFrame, and formats
    each cell of that column, one by one.
"""
def formatColumns(df):
    # Column Formatting
    for col in df:
        if col == 'endDate':
            df[col] = formatColumnCells(df[col], 'fmt')
        else:
            df[col] = formatColumnCells(df[col], 'raw')
    return df


"""
    This was taking more lines of code in functions.py,
    so I added it as one function in utils.py to be accessed
    multiple times without writing the same lines again and again.
"""
def returnDf(dataFrame):
    df = pd.DataFrame(dataFrame)
    # Format cells
    df = formatColumns(df)
    return df

"""
    Breaks a list into a chunk of pre defined size.
    Code sourced from Internet.
"""
def chunk_list(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]

"""
    Converts a list of timestamps (epochs) into formatted dateTime
"""
def epochToDatetimeList(listOfTimestamps):
    result = []
    for timestamp in listOfTimestamps:
        date_time = datetime.fromtimestamp(timestamp)
        result.append(date_time)

    return result
