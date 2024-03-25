import requests

#URL
def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    return response.json()

def count_breweries(breweries):
    return len(breweries)

def count_brewery_types(breweries):
    brewery_types = {}
    for brewery in breweries:
        brewery_type = brewery.get("brewery_type", "Unknown")
        brewery_types[brewery_type] = brewery_types.get(brewery_type, 0) + 1
    return brewery_types

#Count breweries with website
def count_breweries_with_website(breweries):
    websites_count = 0
    for brewery in breweries:
        if brewery.get("website_url"):
            websites_count += 1
            print(f"Brewery with website in {brewery['state']} ({brewery['name']}): {brewery['website_url']}")
    return websites_count

#Define name
if __name__ == "__main__":
    states = ["Alaska", "Maine", "New York"]

    for state in states:
        breweries = get_breweries_by_state(state)

        print(f"\nBreweries in {state}:")
        for brewery in breweries:
            print(brewery["name"])

# brewery count
        brewery_count = count_breweries(breweries)
        print(f"Total number of breweries in {state}: {brewery_count}")
# types
        brewery_types = count_brewery_types(breweries)
        print(f"Brewery types in {state}: {brewery_types}")
#websites count
        websites_count = count_breweries_with_website(breweries)
        print(f"Number of breweries with websites in {state}: {websites_count}")