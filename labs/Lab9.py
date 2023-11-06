import requests 
url = "http://localhost:3000"
response = requests.get(url, verify = False)
data = response.json()
for datapoint in data:
    name = datapoint["name"]
    color = datapoint["color"]
    print(f"{name} is {color}")
