# Global Forest Coverage Dataset 2020 as GeoJson

## Intro
There is public dataset for global Forest cover released 2020 by organisation European Union,  and is available as web map, map tiles, and GeoTIF. This tool generates GeoJSON from the dataset.

e.g to generate GeoJSON for London region of United Kingdom I give three parameters, `"51.7083, -0.5260"` the coordinates for norwest west london, `"51.3023, 0.2362"` the coordinates for south east London, `result.geojson` the script output

    python selector.py "51.7083, -0.5260" "51.3023, 0.2362" result.geojson

## Requirements

The following python libraries should be installed: geopandas, rasterio, shapely

# Notes
You may read more about the dataset [here](https://data.jrc.ec.europa.eu/dataset/10d1b337-b7d1-4938-a048-686c8185b290)
