""" Philips Hue Light control """
from __future__ import print_function
import threading
import time
from qhue import Bridge  # pylint: disable=F0401
import wiringpi as wp # pylint: disable=F0401
import hue_bulb

BRIDGE_ADRESS = '192.168.1.3'
USERNAME = 'Ren8Zo7rcIHUCpqI-yTjLGrJBBBolWIpO4B-Qzg4'

class HueControl(threading.Thread):
    """ App for controlling a set of Hue Bulbs """
    def __init__(self):
        threading.Thread.__init__(self)
        self.bridge = Bridge(BRIDGE_ADRESS, USERNAME)
        self.alarm_mode = False
        self.quit = False
        lights = self.bridge.lights
        self.bulbs = {}
        for key in list(lights().keys()):
            print(key)
            bulb = lights[key]
            self.bulbs[key] = hue_bulb.HueBulb(bulb)

    def turn_on_alarm_mode(self):
        """ Keep an eye on movement and turn on all lights """
        wp.wiringPiSetup()
        self.alarm_mode = True
        print('Alarm mode_activated')

    def turn_all_on_off(self, turn_on, notify=False):
        """ Turn all bulbs on or off
        If notify is true, a message will be send"""
        for bulb in self.bulbs:
            self.bulbs[bulb].turn_on_off(turn_on)
            if turn_on:
                self.bulbs[bulb].max_brightness()
        if notify:
            pass
        
    def run(self):
        while not self.quit:
            time.sleep(1)
            print('!')
            if self.alarm_mode:
                movement = wp.digitalRead(0) != 0
                if movement:
                    self.turn_all_on_off(True, notify=True)



if __name__ == '__main__':
    HUE = HueControl()
    HUE.start()
    HUE.turn_all_on_off(False)
    time.sleep(2)
    HUE.turn_on_alarm_mode()
    
