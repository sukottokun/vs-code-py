import math
import sys

import requests

# prclearint(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://prolificsys.com")
print(r.status_code)
