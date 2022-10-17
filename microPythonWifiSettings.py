import network

# Setting SSID and Password Variables
ssid = 'MicroPython-Station'
password = '123456789'

# Activating Wifi Broadcast 
wlan = network.WLAN(network.AP_IF)
wlan.config(essid=ssid, password=password) 
wlan.active(True)
# Print Pico's IP Address so we can connect to its Webpage later.
print(wlan.ifconfig()[0])

    
    
   