import numpy as np

# Boxing divisions
# variables

atomweight_range = np.arange(0, 103, 1)
strawweight_range = np.arange(103, 106, 1)
light_flyweight_range = np.arange(106, 109, 1)
flyweight_range = np.arange(109, 113, 1)
super_flyweight_range = np.arange(113, 116, 1)
bantamweight_range = np.arange(116, 119, 1)
super_bantamweight_range = np.arange(119, 123, 1)
featherweight_range = np.arange(123, 127, 1)
super_featherweight_range = np.arange(127, 131, 1)
lightweight_range = np.arange(131, 136, 1)
super_lightweight_range = np.arange(136, 141, 1)
welterweight_range = np.arange(141, 148, 1)
super_welterweight_range = np.arange(148, 161, 1)
middleweight_range = np.arange(161, 169, 1)
super_middleweight_range = np.arange(169, 176, 1)
light_heavyweight_range = np.arange(176, 186, 1)
cruiserweight_range = np.arange(186, 201, 1)
heavyweight_range = np.arange(201, 1000, 1)


# dictionary
list_of_divisions = {

    'Atomweight':tuple(atomweight_range),
    'Strawweight': tuple(strawweight_range),
    'Light Flyweight': tuple(light_flyweight_range),
    'Flyweight': tuple(flyweight_range),
    'Super Flyweight': tuple(super_flyweight_range),
    'Bantamweight': tuple(bantamweight_range),
    'Super Bantamweight': tuple(super_bantamweight_range),
    'Featherweight': tuple(featherweight_range),
    'Super Featherweight': tuple(super_featherweight_range),
    'Lightweight': tuple(lightweight_range),
    'Super Lightweight': tuple(super_lightweight_range),
    'Welterweight': tuple(welterweight_range),
    'Super Welterweight': tuple(super_welterweight_range),
    'Middleweight': tuple(middleweight_range),
    'Super Middleweight': tuple(super_middleweight_range),
    'Light Heavyweight': tuple(light_heavyweight_range),
    'Cruiserweight': tuple(cruiserweight_range),
    'Heavyweight': tuple(heavyweight_range)

}


