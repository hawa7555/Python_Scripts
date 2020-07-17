import requests

URL = "https://heroku-hms.herokuapp.com/api/get/students"

response = requests.get(url = URL)
print( response.content )


