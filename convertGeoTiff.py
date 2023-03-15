from satpy import Scene
from satpy import find_files_and_readers
from datetime import datetime
from satpy.writers import compute_writer_results

##from satpy.utils import check_satpy
##check_satpy()


##https://geonetcast.wordpress.com/2018/09/26/processing-sentinel-2-data-with-python/
##https://github.com/pytroll/tutorial-satpy-half-day/blob/main/notebooks/01_introduction.ipynb
##https://www.youtube.com/watch?v=t4a_NrHy7NA
##https://nbviewer.org/github/pytroll/pytroll-examples/blob/main/satpy/hrit_msg_tutorial.ipynb

files = find_files_and_readers(
        base_dir='../demo/Images/Unzip',
        reader='msi_safe')


scn = Scene(filenames = files)

#print(scn.available_composite_ids())
#print(scn.available_dataset_names())

##NDVI = NIR - RED/ NIR + RED
#ndvi = scn.load(['B08']) - scn.load(['B04']) / scn.load(['B08']) + scn/load(['B04'])
scn.load(['B08'])
scn.save_datasets(writer='geotiff')

scn.load(['B04'])
scn.save_datasets(writer='geotiff')


#ndvi = nir - red / nir + red

#ndvi.save_dataset(writer='simple_images')