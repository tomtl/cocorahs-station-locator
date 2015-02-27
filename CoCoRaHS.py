"""
TITLE:          CoCoRaHs Station Locator

CREATION DATE:  2/27/2015
CREATED BY:     Tom Lee

STATUS:         It works. Enter the input and output files manually.
                Input file is a text file, one station ID per row.
"""

from mechanize import Browser
from bs4 import BeautifulSoup

def getInfo(station_number):
    # Open and read the CoCoRaHs Station webpage
    mech = Browser()
    url = "http://www.cocorahs.org/Stations/Station.aspx?StationNumber=" + station_number
    page = mech.open(url)
    html = page.read()
    soup = BeautifulSoup(html)

    # Find station info data

    # Station number
    start = html.find("ucStationInfo_lblStationNumber")
    start = html.find(">", start)
    end = html.find("<", start)
    station_number = html[(start+1):end]

    # Station Name
    start = html.find("ucStationInfo_lblStationName")
    start = html.find(">", start)
    end = html.find("<", start)
    station_name = html[(start+1):end]

    # Latitude
    start = html.find("ucStationInfo_lblLatitude")
    start = html.find(">", start)
    end = html.find("<", start)
    station_lat = html[(start+1):end]

    # Longitude
    start = html.find("ucStationInfo_lblLongitude")
    start = html.find(">", start)
    end = html.find("<", start)
    station_lon = html[(start+1):end]

    # Elevation
    start = html.find("ucStationInfo_lblElevation")
    start = html.find(">", start)
    end = html.find("<", start)
    station_elev = html[(start+1):end]

    # print ("%s, %s, %s, %s, %s") % (station_number, station_name, station_lat, station_lon, station_elev)
    return("%s, %s, %s" % (station_lat, station_lon, station_elev))


input_file = open(r"C:\Users\Lee\Documents\Misc\Scripts\Stations_20150227a.txt", 'r')

# Output file - start writing
output_file = open(r"C:\Users\Lee\Documents\Misc\Scripts\Stations_out20150227a.txt", "w")
print "Process started",

for station_number in input_file.readlines():
    coords = getInfo(station_number)
    output_file.write("%s, %s" % (coords, station_number))
    print ".",

output_file.close()

# Print end
print "Process Completed" 
