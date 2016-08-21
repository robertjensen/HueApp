""" Philips Hue Light control """
from qhue import Bridge

BRIDGE_ADRESS = '192.168.1.3'
USERNAME = 'Ren8Zo7rcIHUCpqI-yTjLGrJBBBolWIpO4B-Qzg4'

def main():
    bridge = Bridge(BRIDGE_ADRESS, USERNAME)

    lights = bridge.lights
    vindue = lights[14]
    print(vindue())
    #vindue.state(bri=255)
    vindue.state(on=False)
if __name__ == '__main__':

    main()
