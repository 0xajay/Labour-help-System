from resonance.modules.utils.googlelocation import get_location, get_locationbyplaceid


def get_short_description(placeid):
    location_display = []
    location_result = get_locationbyplaceid(placeid)
    location_result = location_result.json()["results"][0]
    location_display.append(location_result["address_components"][2]["long_name"])
    for field in location_result["address_components"]:
        if "locality" in field["types"]:
            location_display.append(field["long_name"])
        if "administrative_area_level_1" in field["types"]:
            location_display.append(field["short_name"])
    return ', '.join(location_display)
