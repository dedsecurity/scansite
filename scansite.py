import urllib
import urllib.request
import requests

try:
    test = input("\033[36mScansite: \033[m")
    urllib.request.urlopen(test)
except urllib.error.URLError:
    print("\033[31mError \033[m")
else:
    print("\033[32mOkay \033[m")
    info = requests.get(test)
    print(info.text)
