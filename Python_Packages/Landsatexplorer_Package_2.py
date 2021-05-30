import landsatxplore.api

# Initialize a new API instance and get an access key
api = landsatxplore.api.API('maria_sum123', 'EARTHmaria123')

# Request
scenes = api.search(
    dataset='LANDSAT_8',
    latitude=19.53,
    longitude=-1.53,
    start_date='2015-01-01',
    end_date='2016-01-01',
    max_cloud_cover=10)

print('{} scenes found.'.format(len(scenes)))

for scene in scenes:
    print(scene['acquisitionDate'])

api.logout()