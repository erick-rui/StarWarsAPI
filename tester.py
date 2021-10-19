import json
import requests
from SW import *
from os import system, name 
from SWenum import type


data = {}
starShipLinks = {}
planetLinks = {}
vehicleLinks = {}
allLinks = []

# function from https://www.geeksforgeeks.org/clear-screen-python/ 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def showMenu():
    clear()
    print("=== Star Wars Database ===")
    print("1. Starships")
    print("2. Planets")
    print("3. Vehicles")
    print("9. quit")

def gatherLinks():
    global starShipLinks, planetLinks, vehicleLinks, allLinks
    starShipLinks = getLinks("https://www.swapi.co/api/starships/?page=")
    planetLinks = getLinks("https://www.swapi.co/api/planets/?page=")
    vehicleLinks = getLinks("https://www.swapi.co/api/vehicles/?page=")
    allLinks.append(starShipLinks)
    allLinks.append(planetLinks)
    allLinks.append(vehicleLinks)
    

def getLinks(link):
    pageNum = 1
    links = {}
    while True:
            response = requests.get(link + str(pageNum))
            allData = json.loads(response.text)
            results = allData.get("results")
            for i in range(len(results)):
                name = results[i].get("name")
                url = results[i].get("url")
                links[name] = url
            morePages = allData.get("next")
            if(morePages == None):
                break
            pageNum += 1
    return links


def showStarships():
    global starShipLinks
    print("  ///////////////////////////  ")
    print("  //     STARSHIP LIST     //   ")
    print("  ///////////////////////////  ")
    for name in sorted(starShipLinks.keys()):
        print(name)

def showPlanets():
    global planetLinks
    print("  ///////////////////////////  ")
    print("  //     PLANETS  LIST     //   ")
    print("  ///////////////////////////  ")
    for name in sorted(planetLinks.keys()):
        print(name)

def showVehicles():
    global vehicleLinks
    print("  ///////////////////////////  ")
    print("  //     VEHICLES LIST     //   ")
    print("  ///////////////////////////  ")
    for name in sorted(vehicleLinks.keys()):
        print(name)
    

def getData(name, choice):
    global allLinks
    validName = False
    for i in range(len(allLinks)):
        dataDict = allLinks[i]
        if name in dataDict:
            response = requests.get(dataDict.get(name))
            data = json.loads(response.text)
            validName = True
            if(choice == type.STARSHIP):
                ship = Starship(data)
                ship.__repr__()
            elif (choice == type.PLANET):
                planet = Planet(data)
                planet.__repr__()
            elif (choice == type.VEHICLE):
                vehicle = Vehicle(data)
                vehicle.__repr__()
    if(validName == False):
        print("This is not a valid name")
    input("press any key to go back")
    #Cannot use except,  it will
    #  always spit an exceptionm, it checks all lists rather that just one


def main():
    gatherLinks()
    while (True):
        try:
            showMenu()
            currentDir = int(input("Enter a number:"))

            if(currentDir == 1):
                showStarships()
                print("  ------------------------  ")
                name = input("Enter a starship name: ")
                getData(name, type.STARSHIP)
            elif(currentDir == 2):
                showPlanets()
                print("  ------------------------  ")
                name = input("Enter a planet name: ")
                getData(name, type.PLANET)
            elif(currentDir == 3):
                showVehicles()
                print("  ------------------------  ")
                name = input("Enter a vehicle name: ")
                getData(name, type.VEHICLE)
            else:
                break
        except Exception as e:
            print("Something went wrong", e)
            input("press enter to try again")

if __name__ == "__main__":
    main()