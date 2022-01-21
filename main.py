import requests

API_KEY = "8ddd4a5a8845a59a452e1f9df6a43827"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY_NEUISENBURG = "Neu Isenburg"
STAUTS_CODE_OK = 200
request_url = f"{BASE_URL}?appid={API_KEY}&q={CITY_NEUISENBURG}"

response = requests.get(request_url)

# check if the request to the API hast the status code OK (200)
if response.status_code == STAUTS_CODE_OK:
    data = response.json()

    # getting the temperature.
    temperature = round(data["main"]["temp"] - 273.15, 1)

    # getting the cloud condition.
    cloudyness = data["weather"][0]["description"]

    # print(data)
    print(f"{temperature}°C, {cloudyness}")
else:
    print("Something went wrong.")