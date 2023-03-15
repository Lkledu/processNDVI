##from flask import Flask
from satpy import Scene
from satpy import find_files_and_readers
from datetime import datetime
from glob import glob

##from satpy.utils import check_satpy
##check_satpy()

##app = Flask(__name__)

##https://geonetcast.wordpress.com/2018/09/26/processing-sentinel-2-data-with-python/
##https://github.com/pytroll/tutorial-satpy-half-day/blob/main/notebooks/01_introduction.ipynb
##https://www.youtube.com/watch?v=t4a_NrHy7NA
##https://nbviewer.org/github/pytroll/pytroll-examples/blob/main/satpy/hrit_msg_tutorial.ipynb

##@app.route("/")
##def hello_world():
##    return "<p>Hello, World!</p>"


files = find_files_and_readers(
        base_dir='../demo/Images/Unzip',
        reader='msi_safe')


scn = Scene(filenames = files)
##print(scn.available_dataset_names())
##true color
#scn.load(['true_color'])
##print(scn)

#scn.save_dataset('true_color', filename='true_color_S2_gnc_tutorial.png')

##vegetation red edge
#scn.load(['B05'])
##print(scn)

#scn.save_dataset('B05', filename='vegetation_red_edge_S2_gnc_tutorial.png')

#water vapour
#scn.load(['B09'])
##print(scn)

#scn.save_dataset('B09', filename='water_vapour_S2_gnc_tutorial.png')

print(scn.available_composite_ids())
print(scn.available_dataset_names())

##NDVI = NIR - RED/ NIR + RED
#ndvi = scn.load(['B08']) - scn.load(['B04']) / scn.load(['B08']) + scn/load(['B04'])

#ndvi.save_dataset(filename='file_ndvi.png')


