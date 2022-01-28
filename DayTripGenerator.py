parks = ['Magic Kingdom', 'Animal Kingdom', "Disney's Hollywood Studios", 'EPCOT']
mk_resturants = ['Be Our Guest Resturant', "Cinderella's Royal Table", "Casey's Corner", 'Columbia Harbour House']
ak_resturants = ['Rainforest Cafe', 'Restaurantosaurus', 'Tiffins Resturant', 'Tusker House Resturant']
hs_resturants = ["50's Prime Time Cafe", 'Docking Bay 7 Food and Cargo', 'Backlot Expres', 'PizzeRizzo']
epcot_resturants= ['Chefs de France', 'Rose & Crown Dining Room', 'Space 220 Resturant', 'Garden Grill Resturant']
mode_of_trans = ['Bus', 'Minnie Van', 'Uber or Lyft', 'Personal car']
mk_rides = ["It's a Small World", 'Big Thunder Mountian', "Peter Pan's Flight", 'Pirates of the Caribbean']
ak_rides = ['DINOSAR!', 'Expidition Everest', 'Flight of Passage', 'Kilimanjaro Safaris']
hs_rides = ["Mickey and Minnie's Runaway Railway", 'Rock ''n'' Roller Coaster', 'Millennium Falcon: Smugglers Run', 'Tower of Terror']
epcot_rides = ['Frozen Ever After', 'Spaceship Earth', 'Test Track', "Remy's Ratatuille Adventure"]

print("Welcome to your Random Disney World Trip! Let's get the Magic started!")

import random
def randomizer(parks):
    return(random.choice(parks))

#Select Park
def select_destination():
    destination = randomizer(parks)
    confirmation = input(f'Does {destination} work for your park? yes or no?: ')
    while confirmation == 'no':
            parks.remove(destination)
            destination = randomizer(parks)
            confirmation = input(f'Sorry about that, does {destination} work better? yes or no?: ')       
    if(destination == 'Magic Kingdom'):
        plan_mk ()
    elif(destination == 'Animal Kingdom'):
        plan_ak ()
    elif(destination == "Disney's Hollywood Studios"):
        plan_hs ()
    elif(destination == 'EPCOT'):
        plan_epcot ()
    return destination

#plan magic kingdom funct
def plan_mk ():
    ride = randomizer(mk_rides)
    confirmation = input(f'Would you like to ride {ride} today? yes or no?: ')
    while confirmation == 'no':
            mk_rides.remove(ride)
            ride = randomizer(mk_rides)
            confirmation = input (f'No problem! Does {ride} work better? yes or no?: ')
    resturant = randomizer(mk_resturants)
    confirmation = input(f'Would you like to eat at {resturant}? yes or no?: ')
    while confirmation == 'no':
            mk_resturants.remove(resturant)
            confirmation = input (f'Sorry that does not work for you, how about {resturant} instead? yes or no?: ')
    select_transportation('Magic Kingdom', ride, resturant)  # passing in destination,ride, restarant


#plan animal kingdom funct
def plan_ak ():
    ride = randomizer(ak_rides)
    confirmation = input(f'Would you like to ride {ride} today? yes or no?: ')
    while confirmation == 'no':
            ak_rides.remove(ride)
            ride = randomizer(ak_rides)
            confirmation = input(f'No problem! Does {ride} work better? yes or no?: ')
    resturant = randomizer(ak_resturants)
    confirmation = input(f'Would you like to eat at {resturant}? yes or no?: ')
    while confirmation == 'no':
            ak_resturants.remove(resturant)
            resturant = randomizer(ak_resturants)
            confirmation = input(f'Sorry that does not work for you, how about {resturant} instead?: yes or no?: ')
    select_transportation('Animal Kingdom', ride, resturant)  # passing in destination,ride, restarant


#plan hollywood studios funct
def plan_hs ():
    ride = randomizer(hs_rides)
    confirmation = input(f'Would you like to ride {ride} today? yes or no?: ')
    while confirmation == 'no':
            hs_rides.remove(ride)
            ride = randomizer(hs_rides)
            confirmation = input(f'No problem! Does {ride} work better? yes or no?: ')
    resturant = randomizer(hs_resturants)
    confirmation = input(f'Would you like to eat at {resturant}? yes or no?: ')
    while confirmation == 'no':
            hs_resturants.remove(resturant)
            resturant = randomizer(hs_resturants)
            confirmation = input(f'Sorry that does not work for you, how about {resturant} instead?: yes or no?: ')
    select_transportation("Disney's Hollywood Studios", ride, resturant)  # passing in destination,ride, restarant


#plan epcot funct
def plan_epcot ():
    ride = randomizer(epcot_rides)
    confirmation = input(f'Would you like to ride {ride} today? yes or no?: ')
    while confirmation == 'no':
            epcot_rides.remove(ride)
            ride = randomizer(epcot_rides)
            confirmation = input(f'No problem! Does {ride} work better? yes or no?: ')
    resturant = randomizer(epcot_resturants)
    confirmation = input(f'Would you like to eat at {resturant}? yes or no?: ')
    while confirmation == 'no':
            epcot_resturants.remove(resturant)
            resturant = randomizer(epcot_resturants)
            confirmation = input(f'Sorry that does not work for you, how about {resturant} instead?: yes or no?: ')
    select_transportation('EPCOT', ride, resturant)  # passing in destination,ride, restarant




# Select transport mode
def select_transportation(destination, ride, resturant):
    transportation = randomizer(mode_of_trans)
    confirmation = input(f'Does {transportation} work for your mode of transportation? yes or no?: ')
    while confirmation == 'no':
            mode_of_trans.remove(transportation)
            transportation = randomizer(mode_of_trans)
            confirmation = input(f'Sorry about that, will {transportation} work? yes or no?: ')
    print(f'Get ready for the magic! Your day will be spent at {destination} getting there via {transportation}. Then you will spend all day riding {ride}. You will end the night with dinner at {resturant}! We hope you have a magicail day!')


select_destination()