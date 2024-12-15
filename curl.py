import network
import requests
import time

# Wi-Fi credentials

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to Connect")
    time.sleep(5)
if not wlan.isconnected():
    raise Exception("Failed to connect to network")

while True:
    response = requests.get("http://www.google.com")
    # Get response code
    response_code = response.status_code
    # Get response content
    response_content = response.content

    # Print results
    print("Response code: ", response_code)
    print("Response content:", response_content)
# Make GET request

# import network
# import time
