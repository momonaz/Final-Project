import requests

def fetch_plant_info(api_token, plant_name):
    url = "https://trefle.io/api/v1/plants/search?q=" + plant_name + "&token=" + api_token

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()


        if data.get("data"):
            plant_data = data["data"][0]  # Assuming the first result is the desired plant
            common_name = plant_data.get("common_name", "Unknown")
            scientific_name = plant_data.get("scientific_name", "Unknown")
            year = plant_data.get("year", "Unknown")
            description = plant_data.get("description", "Plant description on growth not available")
            image_url = plant_data.get("image_url", None)


            return {
                "common_name": common_name,
                "scientific_name": scientific_name,
                "year": year,
                "description": description,
                "image_url": image_url,
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching plant information:", e)
        return None

# Replace 'YOUR_API_TOKEN' with your actual Trefle API token
api_token = 'a934db7ornxS2TrWNztoLRdafZo6ZDEv3Sip1GaUZL0'

# Replace 'plant_name' with the name of the plant you want to fetch information for
plant_name = 'European mountain ash'

# Fetch plant information
plant_info = fetch_plant_info(api_token, plant_name)

if plant_info:
    print("Plant Information:")
    print("Common Name:", plant_info['common_name'])
    print("Scientific Name:", plant_info['scientific_name'])
    print("Year:", plant_info['year'])
    print("Description:", plant_info['description'])
    print("Image URL:", plant_info['image_url'])
else:
    print("Failed to fetch plant information.")