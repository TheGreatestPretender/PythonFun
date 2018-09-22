#get library from http://code.google.com/p/pygeoip
import pygeoip

#this should be the uncompromised DB that we are querrying 
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	longi = rec['longitude']
	lat = rec['latitude']

	print '[*] Target: ' + tgt + ' Geo-located.'
	print '[+] ' + str(city) + ', ' + str(region) + ', ' + str(country)
	print '[+] Latitude: ' + str(lat) + ', Longitude' +  str(longi)

tgt = '173.255.226.98'
printRecord(tgt)
#should be in Jersey City, NJ