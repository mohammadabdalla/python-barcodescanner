import requests
import serial

url = 'http://localhost:3000/barcode'

my_scanner = serial.Serial("/dev/ttyACM0", 115200, timeout=0.01)
while True:
    if my_scanner.in_waiting > 0:
        line = my_scanner.readline().decode('utf-8')
        data = {"data":line}
        requests.post(url, json=line)






