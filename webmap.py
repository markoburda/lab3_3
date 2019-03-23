import folium
from geopy import geocoders


def locate(dct):
    """
    Creates map with different layers and saves into html file
    """
    geolocator = geocoders.Bing("AvTwq-4RAgtYf7_QjeCylW_rnqmA_FLYOUte8pWYNK19EhWbAbve6A-FMvgDRL4t", timeout=None)
    map = folium.Map(location=[48.314775, 25.082925], zoom_start=2)
    fg_fr = folium.FeatureGroup(name="Friends")
    for key in dct:
        if len(dct[key]) > 0:
            location = geolocator.geocode(dct[key])
            print("Location object type: ", type(location))
            if location is not None:
                fg_fr.add_child(folium.Marker(location=[location.latitude, location.longitude], popup=key))
    map.add_child(fg_fr)
    map.save('templates/map.html')
