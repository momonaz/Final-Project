import plant_api


def get_plant_info(plant_name, api_key):
    url = "https://trefle.io/api/v1/plants/search?q=" + plant_name + "&token=" + api_key

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("data"):
            # Extracting relevant information from the API response
            plant_data = data["data"][0]
            common_name = plant_data.get("common_name", "Unknown")
            scientific_name = plant_data.get("scientific_name", "Unknown")
            family_common_name = plant_data.get("family_common_name", "Unknown")
            image_url = plant_data.get("image_url", None)

            return {
                "common_name": common_name,
                "scientific_name": scientific_name,
                "family_common_name": family_common_name,
                "image_url": image_url
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching plant information:", e)
        return None
