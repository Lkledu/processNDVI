import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt

plt.show(block=True)
red = rasterio.open('B04_20230304_104211.tif')
nir = rasterio.open('B08_20230304_104211.tif')

#show(red)
print("number of bands(red img): ", red.count)
print("-----------------------------")
print("number of bands(nir img): ", nir.count)
print("#############################")
print("CRS (red img): ", red.crs)
print("-----------------------------")
print("CRS (nir img): ", nir.crs)
print("#############################")
print("Metadata (red img):\n{metadata}".format(metadata=red.meta))
print("-----------------------------")
print("Metadata (nir img):\n{metadata}".format(metadata=nir.meta))
print("#############################")
print("Geotransforma (red img):\n",red.transform)
print("Geotransforma (nir img):\n",nir.transform)

#show(nir)

red_img = red.read(1, out_shape=(1, int(red.height // 2), int(red.width //2))) #resize image, cut in half
#red_img = red_img[1000:3000, 1000:3000]

nir_img = nir.read(1, out_shape=(1, int(nir.height // 2), int(nir.width //2))) #resize image, cut in half
#nir_img = nir_img[1000:3000, 1000:3000]


red_img_float = red_img.astype('f4') #float32
nir_img_float = nir_img.astype('f4') #float32

ndvi = (nir_img_float - red_img_float) / (nir_img_float + red_img_float)
plt.imshow(ndvi, cmap='viridis')
plt.colorbar()
plt.show()
