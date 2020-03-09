from datetime import datetime, timedelta
import random

files = []
for i in range(20):
    name = '5.html@' + (datetime.now() + timedelta(hours=random.randint(0, 100))).strftime('%Y-%m-%d_%H:%M:%S')
    files.append(name)
print(sorted(files, key=lambda y: y[-20:]))
