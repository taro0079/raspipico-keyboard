import network
import requests
import time
import json
from machine import Pin
# import urequests


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

def hit_endpoint():
    send={}
    # head={'Content-Type': 'application/json'}
    # response = requests.post("http://moritatarounoMacBook-Air.local:3000/rpst/test_endpoint",
    #                         data=json.dumps(send),
    #                         headers=head
    #                         )
    response = requests.post("https://awesome-morita-dev.tplinkdns.com//rpst/test_endpoint",
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

pin = Pin.cpu.GPIO15
process_led_pin = Pin.cpu.GPIO16
end_led_pin = Pin.cpu.GPIO17
pin.init(Pin.IN, Pin.PULL_UP)
process_led_pin.init(Pin.OUT, value=0)
end_led_pin.init(Pin.OUT, value=0)
is_pressed = False
while True:
    if pin.value() == 0 and is_pressed == False:
        print("Button pressed")
        process_led_pin.value(1)
        hit_endpoint()
        process_led_pin.value(0)
        end_led_pin.value(1)
        is_pressed = True
    time.sleep(0.1)



    
# # Make GET request
#
#
