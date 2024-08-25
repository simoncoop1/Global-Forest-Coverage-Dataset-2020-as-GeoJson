import tempfile
import shapely
from shapely import box
import urllib
import geopandas as gpd
import pandas as pd
import io
import json
import tool
import sys

thefiles=[{'lng': '-180', 'lat': '80'}, {'lng': '-170', 'lat': '80'}, {'lng': '-160', 'lat': '80'}, {'lng': '-150', 'lat': '80'}, {'lng': '-140', 'lat': '80'}, {'lng': '-130', 'lat': '80'}, {'lng': '-120', 'lat': '80'}, {'lng': '-110', 'lat': '80'}, {'lng': '-100', 'lat': '80'}, {'lng': '-90', 'lat': '80'}, {'lng': '-80', 'lat': '80'}, {'lng': '-70', 'lat': '80'}, {'lng': '-60', 'lat': '80'}, {'lng': '-50', 'lat': '80'}, {'lng': '-40', 'lat': '80'}, {'lng': '-30', 'lat': '80'}, {'lng': '-20', 'lat': '80'}, {'lng': '-10', 'lat': '80'}, {'lng': '10', 'lat': '80'}, {'lng': '20', 'lat': '80'}, {'lng': '30', 'lat': '80'}, {'lng': '40', 'lat': '80'}, {'lng': '50', 'lat': '80'}, {'lng': '60', 'lat': '80'}, {'lng': '70', 'lat': '80'}, {'lng': '80', 'lat': '80'}, {'lng': '90', 'lat': '80'}, {'lng': '100', 'lat': '80'}, {'lng': '110', 'lat': '80'}, {'lng': '120', 'lat': '80'}, {'lng': '130', 'lat': '80'}, {'lng': '140', 'lat': '80'}, {'lng': '150', 'lat': '80'}, {'lng': '160', 'lat': '80'}, {'lng': '170', 'lat': '80'}, {'lng': '-180', 'lat': '70'}, {'lng': '-170', 'lat': '70'}, {'lng': '-160', 'lat': '70'}, {'lng': '-150', 'lat': '70'}, {'lng': '-140', 'lat': '70'}, {'lng': '-130', 'lat': '70'}, {'lng': '-120', 'lat': '70'}, {'lng': '-110', 'lat': '70'}, {'lng': '-100', 'lat': '70'}, {'lng': '-90', 'lat': '70'}, {'lng': '-80', 'lat': '70'}, {'lng': '-70', 'lat': '70'}, {'lng': '-60', 'lat': '70'}, {'lng': '-50', 'lat': '70'}, {'lng': '-40', 'lat': '70'}, {'lng': '-30', 'lat': '70'}, {'lng': '-20', 'lat': '70'}, {'lng': '-10', 'lat': '70'}, {'lng': '0', 'lat': '70'}, {'lng': '10', 'lat': '70'}, {'lng': '20', 'lat': '70'}, {'lng': '30', 'lat': '70'}, {'lng': '40', 'lat': '70'}, {'lng': '50', 'lat': '70'}, {'lng': '60', 'lat': '70'}, {'lng': '70', 'lat': '70'}, {'lng': '80', 'lat': '70'}, {'lng': '90', 'lat': '70'}, {'lng': '100', 'lat': '70'}, {'lng': '110', 'lat': '70'}, {'lng': '120', 'lat': '70'}, {'lng': '130', 'lat': '70'}, {'lng': '140', 'lat': '70'}, {'lng': '150', 'lat': '70'}, {'lng': '160', 'lat': '70'}, {'lng': '170', 'lat': '70'}, {'lng': '-180', 'lat': '60'}, {'lng': '-170', 'lat': '60'}, {'lng': '-160', 'lat': '60'}, {'lng': '-150', 'lat': '60'}, {'lng': '-140', 'lat': '60'}, {'lng': '-130', 'lat': '60'}, {'lng': '-120', 'lat': '60'}, {'lng': '-110', 'lat': '60'}, {'lng': '-100', 'lat': '60'}, {'lng': '-90', 'lat': '60'}, {'lng': '-80', 'lat': '60'}, {'lng': '-70', 'lat': '60'}, {'lng': '-60', 'lat': '60'}, {'lng': '-50', 'lat': '60'}, {'lng': '-20', 'lat': '60'}, {'lng': '-10', 'lat': '60'}, {'lng': '0', 'lat': '60'}, {'lng': '10', 'lat': '60'}, {'lng': '20', 'lat': '60'}, {'lng': '30', 'lat': '60'}, {'lng': '40', 'lat': '60'}, {'lng': '50', 'lat': '60'}, {'lng': '60', 'lat': '60'}, {'lng': '70', 'lat': '60'}, {'lng': '80', 'lat': '60'}, {'lng': '90', 'lat': '60'}, {'lng': '100', 'lat': '60'}, {'lng': '110', 'lat': '60'}, {'lng': '120', 'lat': '60'}, {'lng': '130', 'lat': '60'}, {'lng': '140', 'lat': '60'}, {'lng': '150', 'lat': '60'}, {'lng': '160', 'lat': '60'}, {'lng': '170', 'lat': '60'}, {'lng': '-130', 'lat': '50'}, {'lng': '-120', 'lat': '50'}, {'lng': '-110', 'lat': '50'}, {'lng': '-100', 'lat': '50'}, {'lng': '-90', 'lat': '50'}, {'lng': '-80', 'lat': '50'}, {'lng': '-70', 'lat': '50'}, {'lng': '-60', 'lat': '50'}, {'lng': '-10', 'lat': '50'}, {'lng': '0', 'lat': '50'}, {'lng': '10', 'lat': '50'}, {'lng': '20', 'lat': '50'}, {'lng': '30', 'lat': '50'}, {'lng': '40', 'lat': '50'}, {'lng': '50', 'lat': '50'}, {'lng': '60', 'lat': '50'}, {'lng': '70', 'lat': '50'}, {'lng': '80', 'lat': '50'}, {'lng': '90', 'lat': '50'}, {'lng': '100', 'lat': '50'}, {'lng': '110', 'lat': '50'}, {'lng': '120', 'lat': '50'}, {'lng': '130', 'lat': '50'}, {'lng': '140', 'lat': '50'}, {'lng': '150', 'lat': '50'}, {'lng': '-130', 'lat': '40'}, {'lng': '-120', 'lat': '40'}, {'lng': '-110', 'lat': '40'}, {'lng': '-100', 'lat': '40'}, {'lng': '-90', 'lat': '40'}, {'lng': '-80', 'lat': '40'}, {'lng': '-70', 'lat': '40'}, {'lng': '-40', 'lat': '40'}, {'lng': '-30', 'lat': '40'}, {'lng': '-20', 'lat': '40'}, {'lng': '-10', 'lat': '40'}, {'lng': '0', 'lat': '40'}, {'lng': '10', 'lat': '40'}, {'lng': '20', 'lat': '40'}, {'lng': '30', 'lat': '40'}, {'lng': '40', 'lat': '40'}, {'lng': '50', 'lat': '40'}, {'lng': '60', 'lat': '40'}, {'lng': '70', 'lat': '40'}, {'lng': '80', 'lat': '40'}, {'lng': '90', 'lat': '40'}, {'lng': '100', 'lat': '40'}, {'lng': '110', 'lat': '40'}, {'lng': '120', 'lat': '40'}, {'lng': '130', 'lat': '40'}, {'lng': '140', 'lat': '40'}, {'lng': '-180', 'lat': '30'}, {'lng': '-170', 'lat': '30'}, {'lng': '-160', 'lat': '30'}, {'lng': '-120', 'lat': '30'}, {'lng': '-110', 'lat': '30'}, {'lng': '-100', 'lat': '30'}, {'lng': '-90', 'lat': '30'}, {'lng': '-80', 'lat': '30'}, {'lng': '-20', 'lat': '30'}, {'lng': '-10', 'lat': '30'}, {'lng': '0', 'lat': '30'}, {'lng': '10', 'lat': '30'}, {'lng': '20', 'lat': '30'}, {'lng': '30', 'lat': '30'}, {'lng': '40', 'lat': '30'}, {'lng': '50', 'lat': '30'}, {'lng': '60', 'lat': '30'}, {'lng': '70', 'lat': '30'}, {'lng': '80', 'lat': '30'}, {'lng': '90', 'lat': '30'}, {'lng': '100', 'lat': '30'}, {'lng': '110', 'lat': '30'}, {'lng': '120', 'lat': '30'}, {'lng': '130', 'lat': '30'}, {'lng': '140', 'lat': '30'}, {'lng': '150', 'lat': '30'}, {'lng': '-170', 'lat': '20'}, {'lng': '-160', 'lat': '20'}, {'lng': '-120', 'lat': '20'}, {'lng': '-110', 'lat': '20'}, {'lng': '-100', 'lat': '20'}, {'lng': '-90', 'lat': '20'}, {'lng': '-80', 'lat': '20'}, {'lng': '-70', 'lat': '20'}, {'lng': '-60', 'lat': '20'}, {'lng': '-30', 'lat': '20'}, {'lng': '-20', 'lat': '20'}, {'lng': '-10', 'lat': '20'}, {'lng': '0', 'lat': '20'}, {'lng': '10', 'lat': '20'}, {'lng': '20', 'lat': '20'}, {'lng': '30', 'lat': '20'}, {'lng': '40', 'lat': '20'}, {'lng': '50', 'lat': '20'}, {'lng': '70', 'lat': '20'}, {'lng': '80', 'lat': '20'}, {'lng': '90', 'lat': '20'}, {'lng': '100', 'lat': '20'}, {'lng': '110', 'lat': '20'}, {'lng': '120', 'lat': '20'}, {'lng': '130', 'lat': '20'}, {'lng': '140', 'lat': '20'}, {'lng': '160', 'lat': '20'}, {'lng': '170', 'lat': '20'}, {'lng': '-180', 'lat': '10'}, {'lng': '-170', 'lat': '10'}, {'lng': '-160', 'lat': '10'}, {'lng': '-100', 'lat': '10'}, {'lng': '-90', 'lat': '10'}, {'lng': '-80', 'lat': '10'}, {'lng': '-70', 'lat': '10'}, {'lng': '-60', 'lat': '10'}, {'lng': '-50', 'lat': '10'}, {'lng': '-30', 'lat': '10'}, {'lng': '-20', 'lat': '10'}, {'lng': '-10', 'lat': '10'}, {'lng': '0', 'lat': '10'}, {'lng': '10', 'lat': '10'}, {'lng': '20', 'lat': '10'}, {'lng': '30', 'lat': '10'}, {'lng': '40', 'lat': '10'}, {'lng': '50', 'lat': '10'}, {'lng': '70', 'lat': '10'}, {'lng': '80', 'lat': '10'}, {'lng': '90', 'lat': '10'}, {'lng': '100', 'lat': '10'}, {'lng': '110', 'lat': '10'}, {'lng': '120', 'lat': '10'}, {'lng': '130', 'lat': '10'}, {'lng': '140', 'lat': '10'}, {'lng': '150', 'lat': '10'}, {'lng': '160', 'lat': '10'}, {'lng': '170', 'lat': '10'}, {'lng': '-180', 'lat': '0'}, {'lng': '-170', 'lat': '0'}, {'lng': '-160', 'lat': '0'}, {'lng': '-150', 'lat': '0'}, {'lng': '-140', 'lat': '0'}, {'lng': '-100', 'lat': '0'}, {'lng': '-90', 'lat': '0'}, {'lng': '-80', 'lat': '0'}, {'lng': '-70', 'lat': '0'}, {'lng': '-60', 'lat': '0'}, {'lng': '-50', 'lat': '0'}, {'lng': '-40', 'lat': '0'}, {'lng': '-20', 'lat': '0'}, {'lng': '0', 'lat': '0'}, {'lng': '10', 'lat': '0'}, {'lng': '20', 'lat': '0'}, {'lng': '30', 'lat': '0'}, {'lng': '40', 'lat': '0'}, {'lng': '50', 'lat': '0'}, {'lng': '70', 'lat': '0'}, {'lng': '90', 'lat': '0'}, {'lng': '100', 'lat': '0'}, {'lng': '110', 'lat': '0'}, {'lng': '120', 'lat': '0'}, {'lng': '130', 'lat': '0'}, {'lng': '140', 'lat': '0'}, {'lng': '150', 'lat': '0'}, {'lng': '160', 'lat': '0'}, {'lng': '170', 'lat': '0'}, {'lng': '-180', 'lat': '-10'}, {'lng': '-170', 'lat': '-10'}, {'lng': '-160', 'lat': '-10'}, {'lng': '-150', 'lat': '-10'}, {'lng': '-140', 'lat': '-10'}, {'lng': '-80', 'lat': '-10'}, {'lng': '-70', 'lat': '-10'}, {'lng': '-60', 'lat': '-10'}, {'lng': '-50', 'lat': '-10'}, {'lng': '-40', 'lat': '-10'}, {'lng': '-10', 'lat': '-10'}, {'lng': '10', 'lat': '-10'}, {'lng': '20', 'lat': '-10'}, {'lng': '30', 'lat': '-10'}, {'lng': '40', 'lat': '-10'}, {'lng': '50', 'lat': '-10'}, {'lng': '60', 'lat': '-10'}, {'lng': '90', 'lat': '-10'}, {'lng': '100', 'lat': '-10'}, {'lng': '110', 'lat': '-10'}, {'lng': '120', 'lat': '-10'}, {'lng': '130', 'lat': '-10'}, {'lng': '140', 'lat': '-10'}, {'lng': '150', 'lat': '-10'}, {'lng': '160', 'lat': '-10'}, {'lng': '170', 'lat': '-10'}, {'lng': '-180', 'lat': '-20'}, {'lng': '-160', 'lat': '-20'}, {'lng': '-150', 'lat': '-20'}, {'lng': '-140', 'lat': '-20'}, {'lng': '-130', 'lat': '-20'}, {'lng': '-110', 'lat': '-20'}, {'lng': '-90', 'lat': '-20'}, {'lng': '-80', 'lat': '-20'}, {'lng': '-70', 'lat': '-20'}, {'lng': '-60', 'lat': '-20'}, {'lng': '-50', 'lat': '-20'}, {'lng': '-30', 'lat': '-20'}, {'lng': '10', 'lat': '-20'}, {'lng': '20', 'lat': '-20'}, {'lng': '30', 'lat': '-20'}, {'lng': '40', 'lat': '-20'}, {'lng': '50', 'lat': '-20'}, {'lng': '110', 'lat': '-20'}, {'lng': '120', 'lat': '-20'}, {'lng': '130', 'lat': '-20'}, {'lng': '140', 'lat': '-20'}, {'lng': '150', 'lat': '-20'}, {'lng': '160', 'lat': '-20'}, {'lng': '170', 'lat': '-20'}, {'lng': '-180', 'lat': '-30'}, {'lng': '-90', 'lat': '-30'}, {'lng': '-80', 'lat': '-30'}, {'lng': '-70', 'lat': '-30'}, {'lng': '-60', 'lat': '-30'}, {'lng': '-20', 'lat': '-30'}, {'lng': '10', 'lat': '-30'}, {'lng': '20', 'lat': '-30'}, {'lng': '30', 'lat': '-30'}, {'lng': '70', 'lat': '-30'}, {'lng': '110', 'lat': '-30'}, {'lng': '120', 'lat': '-30'}, {'lng': '130', 'lat': '-30'}, {'lng': '140', 'lat': '-30'}, {'lng': '150', 'lat': '-30'}, {'lng': '170', 'lat': '-30'}, {'lng': '-180', 'lat': '-40'}, {'lng': '-80', 'lat': '-40'}, {'lng': '-70', 'lat': '-40'}, {'lng': '-20', 'lat': '-40'}, {'lng': '-10', 'lat': '-40'}, {'lng': '30', 'lat': '-40'}, {'lng': '50', 'lat': '-40'}, {'lng': '60', 'lat': '-40'}, {'lng': '70', 'lat': '-40'}, {'lng': '140', 'lat': '-40'}, {'lng': '160', 'lat': '-40'}, {'lng': '170', 'lat': '-40'}, {'lng': '-80', 'lat': '-50'}, {'lng': '-70', 'lat': '-50'}, {'lng': '-60', 'lat': '-50'}, {'lng': '-50', 'lat': '-50'}, {'lng': '-40', 'lat': '-50'}, {'lng': '-30', 'lat': '-50'}, {'lng': '0', 'lat': '-50'}, {'lng': '70', 'lat': '-50'}, {'lng': '160', 'lat': '-50'}]


mybox=[dict(lng=float(x['lng']), lat=float(x['lat']), box=box(float(x['lng']),float(x['lat']),float(x['lng'])+9.9999999999,float(x['lat'])-9.9999999999)) for x in thefiles]

def downloadURL(lat,lnt):
    lat=round(lat)
    lnt=round(lnt)
    base='https://ies-ows.jrc.ec.europa.eu/iforce/gfc2020/download.py'
    lat = 'S' + str(lat).replace('-', '') if lat < 0 else 'N' + str(lat)
    lnt = 'W' + str(lnt).replace('-', '') if lnt < 0 else 'E' + str(lnt)
    return base + f'?type=tile&lat={lat}&lon={lnt}'

def filename_get(lat,lng):
	lat=round(lat)
	lng=round(lng)
	filename_t = 'JRC_GFC2020_V1_LAT_LNG.tif'
	lat = 'S' + str(lat).replace('-', '') if lat < 0 else 'N' + str(lat)
	lng = 'W' + str(lng).replace('-', '') if lng < 0 else 'E' + str(lng)
	return filename_t.replace('LAT', lat).replace('LNG',lng)


def run(chosen):

    pairs=[z for z in [dict(inter=shapely.intersection(chosenb,x['box']), mybox=x) for x in mybox] if not z['inter'].is_empty]

    gpds=[]

    for x in pairs:
        filename=filename_get(x['mybox']['lat'], x['mybox']['lng'])
        dl=downloadURL(x['mybox']['lat'], x['mybox']['lng'])
        print(dl)
        with urllib.request.urlopen(dl) as response:
            html = response.read()
        print('finished dl')
        with tempfile.NamedTemporaryFile() as tmpGeoTiff:
            with open(tmpGeoTiff.name, 'bw') as g:
                g.write(html)
            lat1=x['inter'].bounds[3]
            lng1=x['inter'].bounds[0]
            lat2=x['inter'].bounds[1]
            lng2=x['inter'].bounds[2]
            j =tool.calc(tmpGeoTiff.name,lat1,lng1,lat2,lng2)
            gpds.append(gpd.read_file(io.StringIO(json.dumps(j))))

    gpd.GeoDataFrame(pd.concat(gpds)).to_file(output)

if __name__ == '__main__':
    topleft = sys.argv[1]
    bottomright = sys.argv[2]
    output = sys.argv[3]

    lat1=float(topleft.split(',')[0])
    lng1=float(topleft.split(',')[1])
    lat2=float(bottomright.split(',')[0])
    lng2=float(bottomright.split(',')[1])

    #chosenb = box(10.5,60.5,9.5,59)
    chosenb = box(lng2,lat1,lng1,lat2)

    run(chosenb)
