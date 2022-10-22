import network

# Setting SSID and Password Variables
ssid = 'MicroPython-Station'
password = '123456789'

# Activating Wifi Broadcast 
wlan = network.WLAN(network.AP_IF)
wlan.config(essid=ssid, password=password) 
wlan.active(True)
print(wlan.ifconfig()[0])

    
    
   
