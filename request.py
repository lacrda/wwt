import requests

r = requests.request("GET", "https://maps.googleapis.com/maps/api/geocode/json?address=Vila+Isabel+RJ&key=AIzaSyCKcYQ2LlOZYPn8C42rUYRE4T_y9OZrGpM")
print(r.json())