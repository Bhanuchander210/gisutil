import folium
import geopandas as gpd
from gisutil import util


def get_plot(file_path, head=500):
    m = folium.Map(prefer_canvas=True)
    layers = util.get_layers(file_path)

    for layer in layers:
        layer_df = gpd.read_file(file_path, layer=layer).head(head)
        folium.GeoJson(layer_df, name=layer).add_to(m)
    folium.LayerControl().add_to(m)
    return m
