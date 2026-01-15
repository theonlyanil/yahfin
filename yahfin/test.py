from stealthkit import StealthSession

class Test(StealthSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fetch_cookies('https://finance.yahoo.com')
        
    
test = Test()
res = test.get("https://query2.finance.yahoo.com/v10/finance/quoteSummary/TSLA?modules=incomeStatementHistory")
print(res.json())
