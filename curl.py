import network
import requests
import time
import json
# import urequests

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

send={}
head={'Content-Type': 'application/json'}
response = requests.post("http://moritatarounoMacBook-Air.local:3000/rpst/test_endpoint",
                        data=json.dumps(send),
                        headers=head
                        )
#response = requests.get("https://google.com")
# Get response code
response_code = response.status_code
# Get response content
response_content = response.content

# Print results
print("Response code: ", response_code)
print("Response content:", response_content)
# Make GET request


