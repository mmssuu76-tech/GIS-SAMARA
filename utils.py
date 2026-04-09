def load_map_from_shapefile(file_path):
    import geopandas as gpd
    return gpd.read_file(file_path)


def create_folium_map(location=[0, 0], zoom_start=2):
    import folium
    return folium.Map(location=location, zoom_start=zoom_start)


def add_marker(map_obj, location, popup=None):
    folium.Marker(location=location, popup=popup).add_to(map_obj)


def save_map(map_obj, file_path):
    map_obj.save(file_path)


def visualize_geojson(file_path, map_obj=None):
    import folium
    if map_obj is None:
        map_obj = create_folium_map()
    folium.GeoJson(file_path).add_to(map_obj)
    return map_obj