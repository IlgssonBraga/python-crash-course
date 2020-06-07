# Core modules

# import datetime
from datetime import date
# import time
from time import time

# Pip modules

from camelcase import CamelCase

# today = datetime.date.today()

today = date.today()

print(today)

# timestamp = time.time()
timestamp = time()

print(timestamp)

# pip

c = CamelCase()

print(c.hump('hello there world'))