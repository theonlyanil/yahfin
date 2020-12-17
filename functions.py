import requests
import pandas as pd
from utils import formatCell

base_query = 'https://query2.finance.yahoo.com'

def getIncomeStatementHistory(symbol):
    url = base_query + f'/v10/finance/quoteSummary/{symbol}?modules=incomeStatementHistory'
    req = requests.get(url)
    jsonData = req.json()
    income_statements = jsonData['quoteSummary']['result'][0]['incomeStatementHistory']['incomeStatementHistory']
    df = pd.DataFrame(income_statements)

    # Format cells
    df['endDate'] = formatCell(df['endDate'], 'fmt')
    df['totalRevenue'] = formatCell(df['totalRevenue'], 'raw')
    df['costOfRevenue'] = formatCell(df['costOfRevenue'], 'raw')
    df['grossProfit'] = formatCell(df['grossProfit'], 'raw')
    df['researchDevelopment'] = formatCell(df['researchDevelopment'], 'raw')
    df['sellingGeneralAdministrative'] = formatCell(df['sellingGeneralAdministrative'], 'raw')
    df['nonRecurring'] = formatCell(df['nonRecurring'], 'raw')
    df['otherOperatingExpenses'] = formatCell(df['otherOperatingExpenses'], 'raw')
    df['operatingIncome'] = formatCell(df['operatingIncome'], 'raw')
    df['totalOperatingExpenses'] = formatCell(df['totalOperatingExpenses'], 'raw')
    df['totalOtherIncomeExpenseNet'] = formatCell(df['totalOtherIncomeExpenseNet'], 'raw')
    df['ebit'] = formatCell(df['ebit'], 'raw')
    df['interestExpense'] = formatCell(df['interestExpense'], 'raw')
    df['incomeBeforeTax'] = formatCell(df['incomeBeforeTax'], 'raw')
    df['incomeTaxExpense'] = formatCell(df['incomeTaxExpense'], 'raw')
    df['minorityInterest'] = formatCell(df['minorityInterest'], 'raw')
    df['netIncomeFromContinuingOps'] = formatCell(df['netIncomeFromContinuingOps'], 'raw')
    df['discontinuedOperations'] = formatCell(df['discontinuedOperations'], 'raw')
    df['extraordinaryItems'] = formatCell(df['extraordinaryItems'], 'raw')
    df['effectOfAccountingCharges'] = formatCell(df['effectOfAccountingCharges'], 'raw')
    df['otherItems'] = formatCell(df['otherItems'], 'raw')
    df['netIncome'] = formatCell(df['netIncome'], 'raw')
    df['netIncomeApplicableToCommonShares'] = formatCell(df['netIncomeApplicableToCommonShares'], 'raw')

    return df
