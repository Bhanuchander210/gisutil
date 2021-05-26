import fiona
import geopandas as gpd
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_layers(file_path):
    return fiona.listlayers(file_path)


def get_plots(file_path):

    plots = dict()
    layers = get_layers(file_path)

    for layer in layers:
        layer_df = gpd.read_file(file_path, layer=layer)
        fig, ax = plt.subplots(1, 1, figsize=(20, 10))
        ax.axis('off')
        layer_df.plot(ax=ax)
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        img_str = f"<img src='data:image/png;base64,{data}'/>"
        plots[layer] = img_str

    return plots
