#! /usr/bin/env python3

from kv260_pinout import som240_1_pins

#print(som240_1_pins)

nc_pins = {}
pwr_pins = {}
func_pins = {}

for som_pin, info in som240_1_pins.items():

    #print(som_pin, info['func'])
    #print(som_pin, info)
    if 'func' in info and info['func'] == 'nc':
        nc_pins[som_pin] = info
        continue

    if info in ["GND", "VCC_BATT", "SOM_5V0", "PL_3V3", "PL_1V2"]:
        pwr_pins[som_pin] = info
        continue

#    if 'func' not in info:
#        print(som_pin, info)

    func_pins[som_pin] = info

print("nr pins       : %d" % len(som240_1_pins.keys()))
print("nr pwr pins   : %d" % len(pwr_pins.keys()))
print("nr nc pins    : %d" % len(nc_pins.keys()))
print("nr func pins  : %d" % len(func_pins.keys()))

for som_pin,info in func_pins.items():

    if 'pin' not in info:
        print(som_pin, info)

