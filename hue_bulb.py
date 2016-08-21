""" A single Philips Hue Bulb """

import threading
import time
#from qhue import Bridge

class HueBulb(threading.Thread):
    """ An instance of a Philips Hue Bulb """
    def __init__(self, bridge):
        threading.Thread.__init__(self)
        self.bridge = bridge
        self.quit = False
        
    def run(self):
        while not self.quit:
            time.sleep(1)
