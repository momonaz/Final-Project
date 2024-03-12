import requests

def fetch_plant_info(api_token, plant_name):
    url = f"https://trefle.io/api/plants?q={plant_name}&token={api_token}"

    # Send GET request to the Trefle API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        plant_data = response.json()

        # Extract relevant information from the response
        if plant_data.get("data"):
            plant = plant_data["data"][0]  # Assuming the first result is the desired plant
            common_name = plant.get("common_name", "Unknown")
            scientific_name = plant.get("scientific_name", "Unknown")
            family = plant.get("family", "Unknown")

            return {
                "common_name": common_name,
                "scientific_name": scientific_name,
                "family": family
            }
        else:
            return None
    else:
        print(f"Failed to fetch plant information: {response.status_code}")
        return None

# Replace 'YOUR_API_TOKEN' with your actual Trefle API token
api_token = 'a934db7ornxS2TrWNztoLRdafZo6ZDEv3Sip1GaUZL0'

# Replace 'plant_name' with the name of the plant you want to fetch information for
plant_name = 'rose'

# Fetch plant information
plant_info = fetch_plant_info(api_token, plant_name)

if plant_info:
    print("Plant Information:")
    print(f"Common Name: {plant_info['common_name']}")
    print(f"Scientific Name: {plant_info['scientific_name']}")
    print(f"Family: {plant_info['family']}")
else:
    print("Failed to fetch plant information.")
