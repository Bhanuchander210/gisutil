# GeoUtil

### Basic packages

- [fiona](https://pypi.org/project/Fiona/)
- [geopandas](https://geopandas.org/index.html)

### Web App

- [matplotlib](https://geopandas.org/docs/user_guide/mapping.html)
- [folium](https://geopandas.org/gallery/plotting_with_folium.html)
- [Django leaflet](https://django-leaflet.readthedocs.io/en/latest/index.html)

### GUI App

- [PyQT5](https://pypi.org/project/PyQt5/)
- [TKInter](https://docs.python.org/3/library/tkinter.html)
- [afourmy/pyGISS](https://github.com/afourmy/pyGISS) example project
- [Customizing QGIS with Python](https://courses.spatialthoughts.com/pyqgis-in-a-day.html)

### Frameworks

- [GeoDjango](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/)


### Useful posts

- https://medium.com/@h4k1m0u/displaying-a-map-in-a-django-webapp-1-3-creating-a-gis-database-with-postgresql-and-postgis-e596d3c2310


# Guide

### Prerequisites and Steps to run app

- Python 3.7.* . If not available use [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

- Don't forget to export the lib to your python path.

```
cd /path/to/git/repo/gisutil
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

- Install requirements.

```
pip install -r requirements.txt 
```

- Run app

```
python gisutil/app.py
```

### Load data and plot output

- Create `data` directory and put your gdb file there.

```
cd /path/to/git/repo/gisutil
mkdir /data
cp -r /path/from/gdbfile.gdb data
```

- Use the api url with `file_name` param to plot the output.

```
http://localhost:8484/folium_plot?file_name=latest_googledec20.gdb.zip
http://localhost:8484/plot?file_name=latest_googledec20.gdb.zip
```
