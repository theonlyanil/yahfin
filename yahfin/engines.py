import pandas as pd
import time
from datetime import datetime
from stealthkit import StealthSession

query1 = 'https://query1.finance.yahoo.com'
query2 = 'https://query2.finance.yahoo.com'

<<<<<<< HEAD
"""
    Advanced Requests

    api_url: The endpoint we want to fetch data from.
    web_url: [Optional] Website url of a particular page, default is available.
"""
def adv_requests(api_url, web_url="https://query2.finance.yahoo.com/v10/finance/quoteSummary/AAPL?modules=assetProfile%2CearningsHistory"):

    # Request Headers
    headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,hi;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://finance.yahoo.com/",
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    session = requests.Session()
    reque = session.get(web_url)
    cookies = dict(reque.cookies)

    res = session.get(api_url, headers=headers)
    session.cookies.clear()

    return res
"""END_OF_ADVANCED_REQUESTS"""

=======
class YFEngine(StealthSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.crumb = None
        self.refresh_session()

    def refresh_session(self):
        # 1. Get cookies
        self.get('https://fc.yahoo.com') 
        # 2. Get Crumb - this is the missing link in your current code
        resp = self.get('https://query2.finance.yahoo.com/v1/test/getcrumb')
        if resp.status_code == 200:
            self.crumb = resp.text
        else:
            print("Failed to retrieve crumb. Check Stealthkit fingerprinting.")
        

yfsession = YFEngine()

""" Yahoo Finance V1 Engine"""
def v1(symbol):
    url = query1 + f'/v1/finance/quoteType/{symbol}?formatted=true&lang=en-US&region=US'
    req = yfsession.get(url)
    jsonData = req.json()
    return jsonData


"""
    Below engines might have deprecated.
    Need to get newer endpoints to make them to work.
"""
>>>>>>> 2611e32 (everything's working)

""" Yahoo Finance V7 Multi Endpoint """
""" Yahoo Finance V7 Multi-Symbol Engine """
def v7multi(symbols):
<<<<<<< HEAD
    url = query2 + f"/v7/finance/quote?symbols={symbols}"
    req = adv_requests(url)#requests.get(url)
    jsonData = req.json()
=======
    # Standardize the endpoint - query2 is often more stable for bulk data
    url = f"{query2}/v7/finance/quote"
    
    # Use params for cleaner URL encoding and crumb injection
    params = {
        "symbols": symbols,
        "crumb": yfsession.crumb
    }

>>>>>>> 2611e32 (everything's working)
    try:
        req = yfsession.get(url, params=params)
        req.raise_for_status() # Catch 401/429/500 errors immediately
        
        jsonData = req.json()
        
        # Safe extraction logic
        if 'quoteResponse' in jsonData and jsonData['quoteResponse']['result']:
            multiData = jsonData['quoteResponse']['result']
            df = pd.DataFrame(multiData)
            return df
        
        # Handle Yahoo's internal error messages
        error_msg = jsonData.get('quoteResponse', {}).get('error') or \
                    jsonData.get('finance', {}).get('error', {}).get('description')
        return error_msg if error_msg else "Unknown API Error"

    except Exception as e:
        # Mentor Note: Don't just return 'e'. Return the response text if possible 
        # to see why Yahoo blocked you (e.g., 'Invalid Crumb').
        return f"v7multi Error: {str(e)}"

""" Yahoo Finance V7 Options Endpoint """
<<<<<<< HEAD
def v7_options(symbol):
    url = query1 + f'/v7/finance/options/{symbol}'
    req = adv_requests(url)#requests.get(url)
    jsonData = req.json()
    optionData = jsonData['optionChain']['result'][0]
    #print(url)
    return optionData

""" Yahoo Finance V10 Single Symbol Endpoint with Module(s) feature """
def v10(symbol, module):
    url = query2 + f'/v10/finance/quoteSummary/{symbol}?modules={module}'
    req = adv_requests(url)
    print(url)
=======
def v7_options(symbol, date=None):
    # Ensure we use the correct query URL
    url = f"{query1}/v7/finance/options/{symbol}"
    
    # Standard Params
    params = {
        'formatted': 'true',
        'straddle': 'false',
        'crumb': yfsession.crumb 
    }
    
    # Dynamic Date Injection
    if date:
        params['date'] = date

    try:
        req = yfsession.get(url, params=params)
        # Check for 401/404 errors immediately
        if req.status_code != 200:
            print(f"Error: API returned {req.status_code}")
            return None

        jsonData = req.json()
        
        # Navigate safely to the result block based on your TSLA.json structure
        result = jsonData.get('optionChain', {}).get('result', [])
        
        if not result:
            return None
            
        return result[0]

    except Exception as e:
        print(f"Engine Error: {e}")
        return None

""" Yahoo Finance V10 Single Symbol Endpoint with Module(s) feature """
def v10(symbol, module):
    # Ensure crumb is present
    url = f'{query2}/v10/finance/quoteSummary/{symbol}'
    params = {
        'modules': module,
        'crumb': yfsession.crumb, # REQUIRED
        'formatted': 'true'
    }
    
    req = yfsession.get(url, params=params)
>>>>>>> 2611e32 (everything's working)
    try:
        jsonData = req.json()
        return jsonData['quoteSummary']['result'][0]
    except Exception as e:
        # Mentor Note: Log the status code to see if it's a crumb issue (401)
        return f'Error: {req.status_code} - Check symbol or crumb.'


""" Yahoo Finance V8 Single Symbol Endpoint with start, end and interval """
def v8_period(symbol, start_date, end_date, interval):
    url = f'{query2}/v8/finance/chart/{symbol}?period1={start_date}&period2={end_date}&interval={interval}'
    return v8(url)

""" Yahoo Finance V8 Single Symbol Endpoint with range and interval """
def v8_range(symbol, range, interval):
    url = f'{query2}/v8/finance/chart/{symbol}?interval={interval}&range={range}&events=divsplit'
    print(url)
    return v8(url)

""" Yahoo Finance V8 """
def v8(url):
<<<<<<< HEAD
    #print(url)
    req = adv_requests(url)
    jsonData = req.json()

=======
    # Optimisation: Automatically append the crumb from the session
    connector = '&' if '?' in url else '?'
    final_url = f"{url}{connector}crumb={yfsession.crumb}"
    
    print(f"Requesting: {final_url}") # Useful for your initial testing
    
>>>>>>> 2611e32 (everything's working)
    try:
        req = yfsession.get(final_url)
        # Check for HTTP errors (401, 429, etc.) before parsing JSON
        req.raise_for_status() 
        
        jsonData = req.json()
        result = jsonData['chart']['result'][0]
        
        # We extract and return only the essential data points
        timestamps = result.get('timestamp', [])
        priceData = result.get('indicators', {}).get('quote', [{}])[0]
        
        return [timestamps, priceData]

    except Exception as e:
        # Fallback to extract Yahoo's specific error description if available
        try:
            error_data = req.json()
            return error_data['chart']['error']['description']
        except:
            return f"Request failed: {str(e)}"