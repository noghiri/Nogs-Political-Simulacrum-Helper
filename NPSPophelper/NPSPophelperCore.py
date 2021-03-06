"""
Nog's Political Simulacrum Helper v1.0

Created 2015 by Kenneth Sison
Licensed under the MIT License
<http://opensource.org/licenses/MIT/>

One of the modules uses GNU GPL.
Full Licenses and stuff are in the Licenses folder.
"""

#Imports
import NPSPopcalc.NPSPopcalc as PopCalc
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#and Noghiri, as himself.

#Variables
currentPopulation = 0 #7 billion and counting, last I checked. 
growthRate = 0        #It seems every time I see you, you're taller.
newPopulation = 0     #Population after the time change.
def popHandler(text_input):
    global currentPopulation
    try:
        currentPopulation = int(text_input)
    except ValueError:
        print("Error: NaNaNaNaNaNa BATMAN! Seriously, though, NOT AN INT!")

def frameInit():
    simplegui.create_frame("Nog's Political Simulacrum Helper", 500, 200)
    frame.add_label("Input Population")
    frame.add_input('Current Population', popHandler, 50)
    return

    