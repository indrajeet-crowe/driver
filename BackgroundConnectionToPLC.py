import time
import threading
from pycomm3 import LogixDriver


class BackgroundConnectionClass(object):

    def __init__(self,ip_address):
        self.connected = True
        self.ip_address = ip_address
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            try:

                # connection code goes here
                with LogixDriver(self.ip_address) as plc:
                    pass
                print("maintaining connection with " + self.ip_address)
                time.sleep(10)
            except Exception as e:

                # print(e)
                print("PLC {} disconnected, Stopping background connection".format(self.ip_address))
                self.connected = False
                exit(1)


