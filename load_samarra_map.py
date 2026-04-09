import folium
import geopandas as gpd

# Load the city map of Samarra
samarra_gdf = gpd.read_file('https://example.com/path/to/samarra_shapefile.shp')  # URL of the shapefile

# Create a Folium map centered around Samarra
map_samarra = folium.Map(location=[34.2, 43.9], zoom_start=12)

# Add the Samarra map layer
folium.GeoJson(samarra_gdf).add_to(map_samarra)

# Save to an HTML file
map_samarra.save('samarra_map.html')

# Display map
map_samarra