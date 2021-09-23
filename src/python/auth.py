import json
import base64
import requests
import time
import hmac
import hashlib

#general, ads, trade endpoints
api_key = 'N3YJQQCT4ZDQL5SK2OH33QD5C4NZQH2I' #put here your public key
secret_key = 'J3RJ23RXK2AC7DQCIKOD4CJEOXRMAODEXMR2PHKMFN5HYVSJ27JBO5P5OBDH3DNU' #put here your secret key
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