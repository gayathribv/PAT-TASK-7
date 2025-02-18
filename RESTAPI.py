"""

RESTAPI.py

file to communicate with REST Server


"""

import requests
from collections import defaultdict
base_url=("https://api.openbrewerydb.org/v1/breweries"
          "")
def get_breweries_by_state_by_city(state):
    #Initialize dictionary to store count by city and type
    city_brewery_count=defaultdict(lambda:defaultdict(int))
    #Fetch breweries by state
    url=f"{base_url}?by_state"
    response=requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data for {state}")
        return {}

    breweries=response.json()
    for brewery in breweries:
        city=brewery['city']
        brewery_type=brewery['brewery_type']
        city_brewery_count[city][brewery_type]+=1
    return city_brewery_count




#Fetching data from the API
states={"Alaska", "Maine", "New York"}

Alaska_count = 0
Maine_count = 0
NY_count = 0
A_brwry_url=0
M_brwry_url=0
Ny_brwry_url=0
brewery_types={"micro", "nano","regional", "brewpub", "large","planning", "bar","contract","proprietor", "closed"}

def main():
    for state in states:
        print(f"\n Brewery by type in cities of {state}:\n")
        city_brewery_count=get_breweries_by_state_by_city(state)

        for city, brewery_types in city_brewery_count.items():
            print(f"City:{city}", end=" ")
            for brewery_type, count in brewery_types.items():
                print(f"{brewery_type}:{count} ")
        print()

if __name__ == "__main__":
    main()
    for state in states:
        url="https://api.openbrewerydb.org/v1/breweries?by_state="+state
        response=requests.get(url)
        if Alaska_count == 1:
            print("Breweries in the state of Alaska")
        elif Maine_count == 1:
            print("Breweries in the state of Maine")
        elif NY_count == 1:
            print("Breweries in the state of New York")
        else:
            pass

        if response.status_code == 200:
            breweries=response.json()
            for brewery in breweries:
                State=brewery.get('state')
                City=brewery.get('city')
                Brewery_type=brewery.get('brewery_type')
                website=brewery.get('website_url', 'NA')
                Name=brewery.get('name')
                #Count the Number of breweries in each state
                if state == "Alaska" and state == State:
                    Alaska_count = Alaska_count + 1
                    if website != '' or website != 'NA':
                        A_brwry_url = A_brwry_url + 1
                elif state == "Maine" and state == State:
                    Maine_count = Maine_count + 1
                    if website != '' or website != 'NA':
                        M_brwry_url = M_brwry_url + 1
                elif state == "New York" and state == State:
                    NY_count = NY_count + 1
                    if website != '' or website != 'NA':
                        Ny_brwry_url = Ny_brwry_url + 1



                print(f"Name: {brewery['name']}")
                print(f"Brewery Type: {brewery['brewery_type']}")
                print(f"Address: {brewery['street']}, {brewery.get('city', 'NA')}, {brewery.get('state', 'N/A')}")
                print(f"Postal Code: {brewery.get('postal_code', 'NA')}")
                print(f"Phone No: {brewery.get('phone', 'NA')}")
                print(f"Website: {brewery.get('website_url', 'NA')}")
                print(f"Brewery_type: {brewery.get('brewery_type','NA')}")
                print("_" * 40)
        else:
            print("Failed to fetch data. Status Code:", response.status_code)

        print("Breweries in the state of Alaska are:", Alaska_count)
        print(f"{A_brwry_url} breweries have websites ")
        print("Breweries in the state of Maine are:", Maine_count)
        print(f"{M_brwry_url} breweries have websites ")
        print("Breweries in the state of New York are:", NY_count)
        print(f"{Ny_brwry_url} breweries have websites ")


