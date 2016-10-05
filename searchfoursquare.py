import foursquare
import json
from secretkeys import CLIENT_ID, CLIENT_SECRET

# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, 
								client_secret=CLIENT_SECRET)
location = 'lower east side'

query = client.venues.search(params={'query': 'yoga', 
									'near' : location, 
									'radius' : 600})
venues = query['venues']
studios = []

for studio in venues:
	name = studio['name']
	address = studio['location']['formattedAddress']
	lat = studio['location']['lat']
	lng = studio['location']['lng']
	s = {'studio' : name, 
		'address' : address, 
		'latitude' : lat, 
		'longitude' : lng}
	studios.append(s)

for each in studios:
	print(each['studio'])

#print(json.dumps(query, indent=4))
