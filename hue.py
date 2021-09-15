import requests
def change_state():
   api_url = "https://192.168.0.230/api/7kMWhVbulfgbU6A7ltuJEZidPxEvg7NVzcAJ0nbl/lights/1/state"
   response = requests.put(api_url)
   response.json({"on":true}) 


change_state()
