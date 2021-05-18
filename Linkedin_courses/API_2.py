
import requests
import json

url = 'https://api.meteomatics.com/2018-01-01T14:10:00.000+00:00/t_2m:C/17.3887859,78.4610647/csv'
parameters = {'model':'mix'}
response = requests.get(url, params=parameters)
content = response.content
info = json.loads(content)
print(type(info))
print(info)