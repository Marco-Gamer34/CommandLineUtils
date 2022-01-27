import requests
import sys
url = str(sys.argv[1])
r = requests.get(url, allow_redirects=True)
open(str(sys.argv[2]), 'wb').write(r.content)