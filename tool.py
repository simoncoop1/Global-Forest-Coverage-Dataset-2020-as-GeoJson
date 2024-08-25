import sys
import rasterio.features
import rasterio.warp
import geopandas as gpd
import json
import rasterio.plot
from rasterio.windows import Window
import tempfile

# first argument top left coordinate,
# second arument bottom left coordingate, e.g
#python3 -i tool.py "52.5647,-1.6219" "52.0356,-1.1261"
#and
#python3 -i tool.py "52.67826,-3.17385" "52.60816, -3.09025"

#breaks it
#python3 -i tool.py "61,9.0" "60.0000000001, 9.9999999999"


def calc(the_file,lat1,lng1,lat2,lng2):
    dataset=rasterio.open(the_file)

    bb1=dataset.index(lng1,lat1)
    bb2=dataset.index(lng2,lat2)

    w = Window.from_slices((bb1[0],bb2[0]), (bb1[1], bb2[1]))
    wr = dataset.read(1,window=w)

    kwargs = dataset.meta.copy()
    kwargs.update({'height': w.height,'width': w.width,'transform': rasterio.windows.transform(w , dataset.transform)})

    with tempfile.NamedTemporaryFile() as tmpfilecropped:
        with rasterio.open(tmpfilecropped.name, 'w', **kwargs) as dst:
            dst.write(dataset.read(window=w))

        datasetcrop=rasterio.open(tmpfilecropped.name)
        geoj = list(rasterio.features.dataset_features(datasetcrop, as_mask=True, precision=6))

        collection={'type' : 'FeatureCollection', 'features' : geoj}
        with open("tmpcrop.geojson", 'w',encoding="utf-8") as f:
            f.write(json.dumps(collection))
        return collection

if __name__ == '__main__':
    topleft = sys.argv[1]
    bottomright = sys.argv[2]

    lat1=float(topleft.split(',')[0])
    lng1=float(topleft.split(',')[1])
    lat2=float(bottomright.split(',')[0])
    lng2=float(bottomright.split(',')[1])

    #theGeoTIFF = '../../Downloads//JRC_GFC2020_V1_N60_W10.tif'
    theGeoTIFF = '../../Downloads/JRC_GFC2020_V1_N70_E0.tif'
    calc(theGeoTIFF,lat1,lng1,lat2,lng2)
