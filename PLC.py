from pycomm3 import LogixDriver
from BackgroundConnectionToPLC import BackgroundConnectionClass
import time
import threading


# while True:
#     try:
#         with LogixDriver('127.0.0.1') as plc:
#
#             #todo
#             back_conn = BackgroundConnectionClass()
#             while True:
#                 print(plc)
#                 print(plc.read('S'))
#                 time.sleep(12)
#
#     except Exception as ex:
#         print(ex)
#         print("PLC Disconnected, trying to reconnect in 2 seconds ")
#         time.sleep(2)




class PLCReader(object):

    def __init__(self,ip_address, tags):
        self.ip_address = ip_address
        self.tags = tags
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            blueOn = False
            try:
                with LogixDriver(self.ip_address) as plc:
                    print("PlC {} Connected".format(self.ip_address))
                    back_conn = BackgroundConnectionClass(self.ip_address)
                    while True:
                    
                        if back_conn.connected:
                            #todo - Code for reading tags should be here
                            for tag in self.tags:
                                val = plc.read(tag)
                                # val = plc.read('O:0/0')
                            print(val)
                            time.sleep(2)
                           

            except Exception as ex:
                print(ex)
                print("PLC {} Disconnected, trying to reconnect in 2 seconds ".format(self.ip_address))
                time.sleep(2)



