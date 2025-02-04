import urllib.request
import urllib.parse
import json

# Define the service URL (make sure to replace this with the correct one)
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# Prompt user for input
address = input("Enter location: ").strip()

# Prepare the parameters for the API request
parms = dict()
parms['q'] = address

# Construct the full URL
url = serviceurl + urllib.parse.urlencode(parms)

# Print the URL being retrieved
print('Retrieving', url)

# Open the URL and retrieve the data
try:
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
except Exception as e:
    print(f"Error retrieving data: {e}")
    exit()

# Try to parse the JSON data
try:
    js = json.loads(data)
except json.JSONDecodeError:
    print('Failed to parse JSON')
    exit()

# Check if the expected 'features' key is present in the JSON
if not js or 'features' not in js:
    print('==== Download error ===')
    print(data)
    exit()

# If no features found, print error
if len(js['features']) == 0:
    print('==== Object not found ====')
    print(data)
    exit()

# Extract latitude, longitude, and location information
lat = js['features'][0]['properties']['lat']
lon = js['features'][0]['properties']['lon']
print('Latitude:', lat, 'Longitude:', lon)

# Get the formatted location and Plus code
location = js['features'][0]['properties']['formatted']
print('Formatted Location:', location)

plus_code = js['features'][0]['properties'].get('plus_code', 'No Plus Code available')
print('Plus Code:', plus_code)
