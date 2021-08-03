#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:42:59 2021

@author: aghotekar
"""

rarebirds = {
    'Gold-crested Toucan' : {
        'Height (m)' : 1.1,
        'Weight (kg)' : 35,
        'Colour' : 'Gold',
        'Endangered' : True,
        'Aggressive' : True
    },
    'Pearlescent Kingfisher' : {
        'Height (m)' : 0.25,
        'Weight (kg)' : 0.5,
        'Colour' : 'White',
        'Endangered' : False,
        'Aggressive' : False
    },
    'Four-metre Hummingbird' : {
        'Height (m)' : 0.6,
        'Weight (kg)' : 0.5,
        'Colour' : 'Blue',
        'Endangered' : True,
        'Aggressive' : False
    },
    'Giant Eagle' : {
        'Height (m)' : 1.5,
        'Weight (kg)' : 52,
        'Colour' : 'Black and White',
        'Endangered' : True,
        'Aggressive' : True
    },
    'Ancient Vulture' : {
        'Height (m)' : 2.1,
        'Weight (kg)' : 70,
        'Colour' : 'Brown',
        'Endangered' : False,
        'Aggressive' : False
    }
}

birdlocation = ['In the canopy directly above our heads.',
                "Between my 6 and 9 o'clock above.",
                "Between my 9 and 12 o'clock above.",
                "Between my 12 and 3 o'clock above.",
                "Between my 3 and 6 o'clock above.",
                "In a nest on the ground.",
                "Right behind you."
                ]

codes = {'111' : birdlocation[0],
         '110' : birdlocation[1],
         '101' : birdlocation[2],
         '100' : birdlocation[3],
         '011' : birdlocation[4],
         '010' : birdlocation[5],
         '001' : birdlocation[6]
         }

actions = ['Back Away',
           'Cover our Heads',
           'Take a Photograph'
           ]

#print(rarebirds['Giant Eagle']['Aggressive'])

#newList = list(rarebirds['Giant Eagle'])
#print(newList)

'''for k, v in rarebirds.items():
    print('We are looking for a ' + k + '.')
    if v['Aggressive'] == True:
        print(actions[1])
    if v['Endangered'] == True:
        print(actions[0])

for k, v in codes.items():
    print(k, v)'''

for k in rarebirds.values():
    k['Seen'] = False

#print(rarebirds)

encounter = True

sighting = input('What do you see?: ')
#print(type(sighting))

rarebirdsList = []

for i in rarebirds.keys():
    rarebirdsList.append(i)

#print(rarebirdsList)

# if sighting in rarebirdsList:
#     print("This is one of the birds we're are looking for!")
# else:
#     print("That's not one of the birds we're looking for.")

# ask the use for correct code for the bird's location
code = input('Where do you see it? Input the correct code: ')

location = codes[code]

# print("You have seen a", sighting, location, "My goodness.")

# use if-statement to check if sighted bird is aggressive or endangered and print out action
# if (rarebirds[sighting]['Aggressive']):
#     print("We need to", actions[0], 'and', actions[1], ". We need to photograph", sighting, 'at', location)
# elif (rarebirds[sighting]['Endangered']):
#     print("It's endangered and we need to", actions[0], ". We need to photograph", sighting, 'at', location)
# else:
#     print("We need to photograph the ultra rare", sighting, 'at', location)

while encounter == True:
    if sighting not in rarebirdsList:
        sighting = input('That bird is not in our list, please look for another bird: ')
    elif (rarebirds[sighting]['Aggressive']):
        print("We need to", actions[0], 'and', actions[1], ". We need to photograph", sighting, 'at', location)
        encounter = False
    elif (rarebirds[sighting]['Endangered']):
        print("It's endangered and we need to", actions[0], ". We need to photograph", sighting, 'at', location)
        encounter = False
    else:
        print("We need to photograph the ultra rare", sighting, 'at', location)
        encounter = False