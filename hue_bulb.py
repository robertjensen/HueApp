""" A single Philips Hue Bulb """

import threading
import time

class HueBulb(threading.Thread):
    """ An instance of a Philips Hue Bulb """
    def __init__(self, bulb):
        threading.Thread.__init__(self)
        self.bulb = bulb
        self.state = self.bulb()
        self.quit = False

    def reachable(self):
        """ Returns true if the bulb is avaiable on the network """
        return self.state['state']['reachable']

    def turn_on_off(self, on_off_state):
        """ Turns the bulb on or off """
        if self.reachable():
            self.bulb.state(on=on_off_state)
        return self.reachable()
        
    def run(self):
        while not self.quit:
            time.sleep(5)
            self.state = self.bulb()
