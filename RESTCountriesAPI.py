"""

RESTAPI.py

file to communicate with REST Server


"""
import requests
import re

#Recursive traversal of dictionary and print the dict entry
def recursive_traversal(data, depth=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print("  "* depth + f"Key:{key}")
            recursive_traversal(data, depth + 1) #(Recursion of dictionary)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print("  "* depth + f"Index:{index}")
            country=data[0]
            common_name=country['name']['common']
            official_name=country['name']['official']
    else:
        print("  "* depth + f"Value:{data}")#Simple value

#Fetching data from the API
url="https://restcountries.com/v3.1/all"
response=requests.get(url)

if response.status_code == 200:
    countries=response.json()

#Print countries with Dollar (not just USD) as currency

    for country in countries:

    #Populate the variables with country information
        name=country.get('name',{}).get('common','NA')
        region=country.get('region','NA')
        subregion=country.get('subregion','NA')
        capital=country.get('capital','NA')
        languages=', '.join(country.get('languages', {}).values()) if country.get('languages') else 'NA'
        population=country.get('population', 'NA')
        area=country.get('area','NA')
        flag_url=country.get('flags', {}).get('png', 'N/A')
        currencies=', '.join([currency['name'] for currency in country.get('currencies', {}).values()]) if country.get('currencies') else 'N/A'
    #Print Country Information
        split_currency=currencies.split()
        for i in split_currency:
            if i == "dollar":
                print(f"Name: {name}")
                print(f"Region: {region}")
                print(f"Subregion: {subregion}")
                print(f"Capital: {capital}")
                print(f"Languages: {languages}")
                print(f"Population: {population}")
                print(f"Area: {area} sq km")
                print(f"Flag URL: {flag_url}")
                print(f"Currencies: {currencies}")
                print("_" * 40)
            else:
                continue
#Print countries with euro (not just USD) as currency

    for country in countries:

    #Populate the variables with country information
        name=country.get('name',{}).get('common','NA')
        region=country.get('region','NA')
        subregion=country.get('subregion','NA')
        capital=country.get('capital','NA')
        languages=', '.join(country.get('languages', {}).values()) if country.get('languages') else 'NA'
        population=country.get('population', 'NA')
        area=country.get('area','NA')
        flag_url=country.get('flags', {}).get('png', 'N/A')
        currencies=', '.join([currency['name'] for currency in country.get('currencies', {}).values()]) if country.get('currencies') else 'N/A'
    #Print Country Information
        split_currency=currencies.split()
        for i in split_currency:
            if i == "Euro" or i == "euro":
                print(f"Name: {name}")
                print(f"Region: {region}")
                print(f"Subregion: {subregion}")
                print(f"Capital: {capital}")
                print(f"Languages: {languages}")
                print(f"Population: {population}")
                print(f"Area: {area} sq km")
                print(f"Flag URL: {flag_url}")
                print(f"Currencies: {currencies}")
                print("_" * 40)
            else:
                continue
else:
    print("Failed to fetch data. Status Code:", response.status_code)