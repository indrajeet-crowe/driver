from PLC import PLCReader
import time
import configuration


ip_addresses = configuration.get_addresses()

tags = configuration.get_tags()



for ip in ip_addresses:
    PLCReader(ip, tags)

while True:
    time.sleep(10000)





