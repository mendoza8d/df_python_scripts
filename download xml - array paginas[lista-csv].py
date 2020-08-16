import requests
import csv
from datetime import datetime
count = 0
results = []
with open('Lista.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader: 
        count += 1
        results.append(row)
        
for i in range(count):
    URL = str(results[i])[2:-2]
    print(URL)
    name_xml = datetime.now().strftime('file_xml_%Y-%m-%d_%H_%M_%S.%f.xml')
    response = requests.get(URL)
    with open(name_xml, 'wb') as file:
        file.write(response.content)
