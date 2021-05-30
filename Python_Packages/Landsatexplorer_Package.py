####### Searching for scenes #############

import json
from landsatxplore.api import API

# Initialize a new API instance and get an access key
api = landsatxplore.api.API('maria_sum123', 'EARTHmaria123')

# Perform a request. Results are returned in a dictionnary
response = api.request('<request_endpoint>',params={
        "param_1": value_1,
        "param_2": value_2})

# Search for Landsat TM scenes
scenes = api.search(
    dataset='landsat_tm_c1',
    latitude=50.85,
    longitude=-4.35,
    start_date='1995-01-01',
    end_date='1995-10-01',
    max_cloud_cover=10
)
print(f"{len(scenes)} scenes found.")

# Process the result
for scene in scenes:
    print(scene['acquisition_date'])
    
    # Write scene footprints to disk
    file_name = f"{scene['landsat_product_id']}.geojson"
    with open(file_name, "w") as f:
        json.dump(scene['spatialCoverage'], f)

# Log out
api.logout()
