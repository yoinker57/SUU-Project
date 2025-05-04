import requests
import time
import random

url = "http://localhost:8080/"
url2 = "http://localhost:8080/asdf"

while True:
    try:
        if random.randint(0, 1) == 0:
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
        else:
            response = requests.get(url2)
            print(f"Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    time.sleep(0.25)  # Czeka 0.25 sekundy przed kolejnym zapytaniem