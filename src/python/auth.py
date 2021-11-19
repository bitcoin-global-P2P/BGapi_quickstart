import json
import base64
import requests
import time
import hmac
import hashlib

api_key = 'DZG726DFJYOXYHWC44FJV6AJO7642AKU' #put here your public key
secret_key = 'L7YGHHB6544C3MG4ZSMZODHMQTQNLZNPHTZIJQUDVYBBTQQFY2NUPDYDB77VPH3Q' #put here your secret key
path = '/api/v1/dashboard' #put here request path. 
getParams = 'ticker=BTC&limit=15&offset=0' #request params (if any)
#If the nonce is similar to or lower than the previous request number, you will receive the 'too many requests' error message
nonce = str(int(time.time() * 1000)) #nonce is a number that is always higher than the previous request number
request = '/api/v1/dashboard' #put here your request with base URL
baseUrl = 'https://t2api.coinmoney.net.ua'  #base URL: api.bitcoin.global

#preparing payload
completeUrl = baseUrl + request
payload = nonce + api_key + path + getParams
signature = hmac.new(secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest().upper()


#preparing headers
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Apiauth-Key': api_key,
    'Apiauth-Nonce': nonce,
    'Apiauth-Signature': signature
}

#sending request
resp = requests.get(completeUrl, headers=headers)

print(resp)
