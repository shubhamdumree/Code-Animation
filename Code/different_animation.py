#!/usr/bin/env python

#importing libraries
import opc
import time
from random import randint
import random
from datetime import datetime


#displaying hello in random lights function
def Animation1() :
    
    r = randint(1,256)
    g = randint(1,256)
    b = randint(1,256)
 
    led_colour = [(0,0,0)] * 360
    client.put_pixels(led_colour)

    # displaying HELLO in the simulator
    led_colour[0] = (r,g,b)
    led_colour[1] = (r,g,b)
    #to display on simulator
    client.put_pixels(led_colour)
    #to pause for 0.1 seconds
    time.sleep(0.03)
    
    led_colour[60]= (r,g,b)
    led_colour[61]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[120]= (r,g,b)
    led_colour[121]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[180]= (r,g,b)
    led_colour[181]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[240]= (r,g,b)
    led_colour[241]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[300]= (r,g,b)
    led_colour[301]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[122]= (r,g,b)
    led_colour[182]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[123]= (r,g,b)
    led_colour[183]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[124]= (r,g,b)
    led_colour[184]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[5]= (r,g,b)
    led_colour[6]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[65]= (r,g,b)
    led_colour[66]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[125]= (r,g,b)
    led_colour[126]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[185]= (r,g,b)
    led_colour[186]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[245]= (r,g,b)
    led_colour[246]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[305]= (r,g,b)
    led_colour[306]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[8]= (r,g,b)
    led_colour[9]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[68]= (r,g,b)
    led_colour[69]= (r,g,b)
    led_colour[70]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[128]= (r,g,b)
    led_colour[129]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[188]= (r,g,b)
    led_colour[189]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[248]= (r,g,b)
    led_colour[249]= (r,g,b)
    led_colour[250]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[308]= (r,g,b)
    led_colour[309]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[10]= (r,g,b)
    led_colour[11]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[12]= (r,g,b)
    led_colour[13]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[130]= (r,g,b)
    led_colour[190]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[131]= (r,g,b)
    led_colour[191]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[132]= (r,g,b)
    led_colour[133]= (r,g,b)
    led_colour[192]= (r,g,b)
    led_colour[193]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[310]= (r,g,b)
    led_colour[311]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[312]= (r,g,b)
    led_colour[313]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[17]= (r,g,b)
    led_colour[18]= (r,g,b)
    led_colour[19]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[77]= (r,g,b)
    led_colour[78]= (r,g,b)
    led_colour[79]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[137]= (r,g,b)
    led_colour[138]= (r,g,b)
    led_colour[139]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[197]= (r,g,b)
    led_colour[198]= (r,g,b)
    led_colour[199]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[257]= (r,g,b)
    led_colour[258]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[317]= (r,g,b)
    led_colour[318]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[259]= (r,g,b)
    led_colour[319]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[260]= (r,g,b)
    led_colour[320]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[261]= (r,g,b)
    led_colour[321]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[262]= (r,g,b)
    led_colour[322]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[263]= (r,g,b)
    led_colour[323]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[25]= (r,g,b)
    led_colour[26]= (r,g,b)
    led_colour[27]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[85]= (r,g,b)
    led_colour[86]= (r,g,b)
    led_colour[87]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[145]= (r,g,b)
    led_colour[146]= (r,g,b)
    led_colour[147]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[205]= (r,g,b)
    led_colour[206]= (r,g,b)
    led_colour[207]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[265]= (r,g,b)
    led_colour[266]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[325]= (r,g,b)
    led_colour[326]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[267]= (r,g,b)
    led_colour[327]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[268]= (r,g,b)
    led_colour[328]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[269]= (r,g,b)
    led_colour[329]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[270]= (r,g,b)
    led_colour[330]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[271]= (r,g,b)
    led_colour[331]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[33]= (r,g,b)
    led_colour[34]= (r,g,b)
    led_colour[35]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[93]= (r,g,b)
    led_colour[94]= (r,g,b)
    led_colour[95]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[153]= (r,g,b)
    led_colour[154]= (r,g,b)
    led_colour[155]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[213]= (r,g,b)
    led_colour[214]= (r,g,b)
    led_colour[215]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[273]= (r,g,b)
    led_colour[274]= (r,g,b)
    led_colour[275]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[333]= (r,g,b)
    led_colour[334]= (r,g,b)
    led_colour[335]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[276]= (r,g,b)
    led_colour[336]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[277]= (r,g,b)
    led_colour[337]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[278]= (r,g,b)
    led_colour[338]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[279]= (r,g,b)
    led_colour[339]= (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[280] = (r,g,b)
    led_colour[340] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[281] = (r,g,b)
    led_colour[341] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[281] = (r,g,b)
    led_colour[341] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[219] = (r,g,b)
    led_colour[220] = (r,g,b)
    led_colour[221] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[159] = (r,g,b)
    led_colour[160] = (r,g,b)
    led_colour[161] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[99] = (r,g,b)
    led_colour[100] = (r,g,b)
    led_colour[101] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[39] = (r,g,b)
    led_colour[40] = (r,g,b)
    led_colour[41] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[36] = (r,g,b)
    led_colour[37] = (r,g,b)
    led_colour[38] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)

    led_colour[96] = (r,g,b)
    led_colour[97] = (r,g,b)
    led_colour[98] = (r,g,b)
    client.put_pixels(led_colour)
    time.sleep(0.03)


#displaying blinking hi in orange function
def Animation2():

    #number of times message will appear and display(blink animation)
    strobecount = 20
    red = 255
    blue = 165
    green = 0
    #flash delay of 0.04s
    delay = 0.04
    pause = 0.1
    
    for x in range(0, strobecount):
        
        place = [(32,32,32)] * 360
        client.put_pixels(place)
        time.sleep(delay)
        
        place[5] = (red, blue, green)
        place[65] = (red, blue, green)
        place[125] = (red, blue, green)
        place[185] = (red, blue, green)
        place[245] = (red, blue, green)
        place[126] = (red, blue, green)
        place[127] = (red, blue, green)
        place[128] = (red, blue, green)
        place[9] = (red, blue, green)
        place[69] = (red, blue, green)
        place[129] = (red, blue, green)
        place[189] = (red, blue, green)
        place[249] = (red, blue, green)
        place[13] = (red, blue, green)
        place[253] = (red, blue, green)
        place[14] = (red, blue, green)
        place[254] = (red, blue, green)
        place[15] = (red, blue, green)
        place[75] = (red, blue, green)
        place[135] = (red, blue, green)
        place[195] = (red, blue, green)
        place[255] = (red, blue, green)
        place[16] = (red, blue, green)
        place[256] = (red, blue, green)
        place[17] = (red, blue, green)
        place[257] = (red, blue, green)
        
        client.put_pixels(place)
            

        time.sleep(delay)
        time.sleep(pause)


#displaying steady & reversing blue lights
def Animation3():

    #assign c random colour
    c1 = randint(1,256)
    c2 = randint(1,60)
    c3 = randint(1,256)
    c4 = randint(1,60)
    c5 = randint(1,256)
    c6 = randint(1,60)
    red = 0
    blue = 256
    #defining led_colour
    led_colour = [(0,0,0)]*360

    for i in range (0,60) :
        
        led_colour[i] = (red,c1,blue)
        led_colour[i+60] = (red,c2,blue)
        led_colour[i+120] = (red,c3,blue)
        led_colour[i+180] = (red,c4,blue)
        led_colour[i+240] = (red,c5,blue)
        led_colour[i+300] = (red,c6,blue)
        #to display on simulator
        client.put_pixels(led_colour)
        #to pause for 0.1 seconds
        time.sleep(0.1)
        
    
    c1 = randint(1,60)
    c2 = randint(1,256)
    c3 = randint(1,60)
    c4 = randint(1,256)
    c5 = randint(1,60)
    c6 = randint(1,256)
    

    #reverse the animation   
    for i in reversed(range(0,60)) :
        
        led_colour[i] = (red,c1,blue)
        led_colour[i+60] = (red,c2,blue)
        led_colour[i+120] = (red,c3,blue)
        led_colour[i+180] = (red,c4,blue)
        led_colour[i+240] = (red,c5,blue)
        led_colour[i+300] = (red,c6,blue)
        client.put_pixels(led_colour)
        time.sleep(0.01)
        

#displaying blinking random lights function
def Animation4():
    
        my_pixels = [(255, 0, 0),(0, 255, 0),(0, 0, 255)] * 60
        random.shuffle(my_pixels)
        client.put_pixels(my_pixels)
        time.sleep(0.3)


#displaying fading pink lights function
def Animation5():
    
        color = randint(1,256)
        my_anim = [(color, 0, color)] * 360
        random.shuffle(my_anim)
        client.put_pixels(my_anim)
        time.sleep(0.5)


#displaying reversing gold lights function
def Animation6():

    #defining led_colour
    led_colour = [(0,0,0)]*360
    
    try:
      
       for i in range (0,60) :

        #random colours to each LED for the 6 rows
            led_colour[i] = (randint(0,256), randint(0,256), randint(0,256))
            led_colour[i+60] = (randint(0,256), randint(0,256), randint(0,256))
            led_colour[i+120] = (randint(0,256), randint(0,256), randint(0,256))
            led_colour[i+180] = (randint(0,256), randint(0,256), randint(0,256))
            led_colour[i+240] = (randint(0,256), randint(0,256), randint(0,256))
            led_colour[i+300] = (randint(0,256), randint(0,256), randint(0,256))
            client.put_pixels(led_colour)
            time.sleep(0.03)

       #reverse the animation with gold	
       for i in reversed(range(0,60)) :
            led_colour[i] = (212,175,55)
            led_colour[i+60] = (212,175,55)
            led_colour[i+120] = (212,175,55)
            led_colour[i+180] = (212,175,55)
            led_colour[i+240] = (212,175,55)
            led_colour[i+300] = (212,175,55)
            client.put_pixels(led_colour)
            time.sleep(0.03)
            
    except KeyboardInterrupt:
           print("\nAnimation Stopped !")


#function for clearing the screen after animation has finished executing
def clearSimulator() :
    
   #reset all LEDs to black
    
   reset = [(0,0,0)] * 360
   client.put_pixels(reset)
   
        

ADDRESS = 'localhost:7890'


#to use simulator
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print ('connected to %s' % ADDRESS)
else:
    # print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('WARNING: could not connect to %s' % ADDRESS)        
        
        
# Displaying Hi before the menu starts and then clear the simulator after 1 sec   
Animation2()
time.sleep(1)
clearSimulator()


print("\nWelcome! Please select the type of animation you want to display on your simulator\n")
print("Animation 1 -> Displaying Hello In Random Lights\n")
print("Animation 2 -> Displaying Blinking Hi In Orange Lights\n")
print("Animation 3 -> Steady & Reversing Blue Lights\n")
print("Animation 4 -> Blinking Random Lights\n")
print("Animation 5 -> Fading Pink Lights\n")
print("Animation 6 -> Reversing Gold Lights\n")
print("\nPress 7 to exit!\n")


#function with user_input as parameter
def inputAnimationNumber(user_input):
  #while loop which is infinite  
  while True:
    try:
       #user input his choice and the input choice is converted to an integer
       userInput = int(input(user_input))       
    except ValueError:
        #validation
       print("Not an integer! Try again!")
       continue
    #exit loop with user's valid choice
    else:
        if(userInput>0 and userInput<8):
           return userInput 
           break
        else:
            print("Not in range")
            continue

def inputSec(message):
  while True:
    try:
       #user input his choice and the input choice is converted to an integer 
       userInput = int(input(message))       
    except ValueError:
        #validation
       print("Not an integer! Try again!")
       continue
    #exit loop with user's valid choice
    else:
        if(userInput > 0):
           return userInput 
           break
        else:
            #validation
            print("Greater than zero required!")
            continue


#user selectionstored in value_c variable
value_c = 0


#loop will continue unless user enters 7
while value_c != 7:
    
    #calling inputAnimationNumber function for user to enter his selection from the menu
    value_c = inputAnimationNumber("Enter animation number OR Press 7 to exit program: ")
    
    #user enter number of seconds he wants to display animation on the simulator
    if value_c != 7:
        secs = inputSec("Enter the number of seconds for the animation: ")

    #if statements for user selection
        
    if value_c == 1:
        t1 = datetime.now()
        #while loop will contine until number of seconds has completed
        while (datetime.now()-t1).seconds <= secs:
            Animation1()
            clearSimulator()

    if value_c == 2:
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= secs:
            Animation2()
            clearSimulator()
          
    if value_c == 3:
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= secs:
            Animation3()
            clearSimulator()

    if value_c == 4:
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= secs:
            Animation4()
            clearSimulator()
            
    if value_c == 5:
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= secs:
            Animation5()
            clearSimulator()

    if value_c == 6:
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= secs:
            Animation6()
            clearSimulator()

    if value_c == 7:
        print("Thank you! Program exited successfully")


        











































