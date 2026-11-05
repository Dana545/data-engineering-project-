import requests
import json
url= 'https://api.restcountries.com/countries/v5'
headers= {
    'Authorization': 'Bearer rc_live_cc8c301474e5432b903394a19ce4ee26'
}
res= requests.get(url, headers=headers)
data= res.json()
json_string= json.dumps(data)
with open("countries_raw.json", "w")as f:
    f.write(json_string)
print('Saved raw data to countries_raw.json succesfully')

