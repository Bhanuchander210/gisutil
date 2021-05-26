from flask import Flask, request, render_template
import os
from gisutil import folium_util, util


app = Flask(__name__)

data_prefix = "data"


def check_file(file_name):

    if file_name is None:
        return False, "file_name required."

    file_path = os.path.join(data_prefix, file_name)

    if not os.path.exists(file_path):
        return False, "file not exists in data dir."

    return True, file_path


@app.route("/")
def index():
    return "gisutil"


@app.route("/plot")
def plot():
    file_name = request.args.get("file_name")

    is_valid, file_detail = check_file(file_name)

    if not is_valid:
        return file_detail

    figs = util.get_plots(file_detail)

    return render_template('index.html', title='GIS Plot', figs=figs)


@app.route("/folium_plot")
def folium_plot():
    file_name = request.args.get("file_name")

    is_valid, file_detail = check_file(file_name)

    if not is_valid:
        return file_detail

    return folium_util.get_plot(file_detail)._repr_html_()


def main():
    app.run(host='0.0.0.0', port=8484, debug=False, threaded=True)


if __name__ == "__main__":
    main()
