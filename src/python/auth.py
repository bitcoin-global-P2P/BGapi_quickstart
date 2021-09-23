import json
import base64
import requests
import time
import hmac
import hashlib

#general, ads, trade endpoints
api_key = '' #put here your public key
secret_key = '' #put here your secret key
path = '/api/v1/ads' #put here request path. 
getParams = 'currency=USD' #request params (if any)
nonce = str(int(time.time() * 1000)) #nonce is a timestamp in miliseconds
baseUrl = 'https://api.bitcoin.global'  #base URL: api.bitcoin.global

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
