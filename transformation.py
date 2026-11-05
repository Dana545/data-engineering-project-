import pandas as pd 
import json 
with open("countries_raw.json", "r")as f:
    data=json.load(f)
countries_list= data['data']['objects']
extracted_data=[]
for country in countries_list:
    name= country.get('names', {}).get('common', 'Unknown')
    area= country.get('area', {}).get('kilometers', 0.0)
    region= country.get('region','Unknown')
    subregion= country.get('subregion', 'Unknown')

    borders_list= country.get('borders', [])
    if borders_list:
        borders= ', '.join(borders_list)
    else:
        borders= 'None'

    currencies_list= country.get('currencies', [])
    if currencies_list:
        codes=[]
        for c in currencies_list:
            codes.append(c.get('code', ''))
        currencies= ', '.join(codes)
    else:
        currencies='None'

    languages_data= country.get('languages', {})
    if languages_data:
        lang_list=[]
        if type(languages_data)==dict:
            for val in languages_data.values():
                lang_list.append(str(val))
        elif type(languages_data)==list:
            for l in languages_data:
                lang_list.append(str())
        languages=', '.join(lang_list)if lang_list else 'None'
    else:
        languages='None'

    extracted_data.append({
        'name': name, 
        'area': area, 
        'region': region,
        'subregion': subregion,
        'borders': borders, 
        'currencies': currencies,
        'languages': languages,
    })
    df= pd.DataFrame(extracted_data)
    df.to_csv("countries_intial.csv", index=False)
print("Saved countries_intial.csv successfully with", len(df), "rows")