"""Contains the code for the story-based game."""

import time
import random

# player attributes/items:
covid = 0
mask = False

# day's variables:
tod = "8AM"
cases = 0

class color:
    """Defines different colors and text formatting settings to be used for CML output printing."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

#The story is broken into sections, starting with "intro"
def intro():
    print("You have just awoken and it is 8AM! Today is finally the day! After living in near-isolation during the COVID-19 pandemic, the vaccine is finally available! As the head of your town's COVID response team, it is your job to open the doors to the vaccine distribution center for the public! The doors are supposed to open at 10AM and it is currently 8AM. You have about 100,000 residents in your town and have received enough for all of them to get the vaccine. Cases have been on the rise lately and the vaccine should help slow them, so you better get to the vaccine center and open the doors as soon as possible to help stop the spread, while trying to avoid contracting the virus yourself.")
    time.sleep(1)
    option_find_morning_transportation()


def option_find_morning_transportation():
    print("After enjoying a brief breakfast, showering, and petting your dog, it is time to start the day! It's already 9AM and your car is still in the shop! That might make it a little bit harder to get to work :(. Let's get on the road! How do you want to get to the vaccine center?: ")

    print("\tA. Car-pool (maskless) with your co-worker\n\tB. Take the bus\n\tC. Take the subway")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        option_transportation_carpool()
    elif choice.upper() == "B":
        option_transportation_bus()
    elif choice.upper() == "C":
        option_transportation_subway()
    else:
        print("error")

def option_transportation_carpool():
    global covid # get the global var
    global mask
    print("You hear loud honking outside of your house! Alright, your co-worker Nathan just pulled up to take you to work. Oh no! You get in the car and notice Nathan is not wearing his mask, he must be excited that it is vaccine distribution day! Will you: ")
    time.sleep(1)
    print("\tA. Put on your mask\n\tB. Wear no mask\n\tC. Put on your mask and ask Nathan to wear his")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        covid += 5
        mask = True
    elif choice.upper() == "B":
        covid += 20
        mask = False
    elif choice.upper() == "C":
        mask = True
        print("Luckily Nathan is accomodating and was more than happy to put his mask on! That should help you stay safe!")
        # no change in covid
    else:
        print("error")

    print("You get into the car and put on your seatbelt and begin to drive into town, luckily traffic doesn't seem to bad this morning.\nAbout halfway there, Nathan says, \"Oh no, looks like the tank is almost on empty! Why don't we go grab some coffee and gas at Sheetz!\" A hot coffee does sound nice you think to yourself. He then pulls off the highway into the parking lot, and once the car is off he begins pumping gas.\nGetting coffee sounds good, but there are a lot of people walking in and out of the store without masks. Is it worth it? Will you:")
    time.sleep(1)
    print("\tA. Go in and get coffee\n\tB. Forgo your favorite hot drink")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("You tell Nathan you are going to go grab something to drink and head into the store. As you walk in, a nice man wearing a mask holds the door for you, but once you get inside you can see there are people everywhere without masks. They are at the made-to-order food counter, the register, the drink fridges, and most importantly: the coffee station.\n Will you: ")
        time.sleep(1)
        print("\tA. Grab your coffee \n\tB. Turn around and leave")
        nested_choice = input(">>> ") #Here is your first choice.
        if nested_choice.upper() == "A":
            print("Well, you do need your morning coffee. If not you'll be grouchy and tired all day. You approach the coffee station, where a young lady is preparing her drink maskless. Undeterred, you fill your cup of coffee up and put some sugar in, then checkout without incident. You walk outside and unfortunately it has suddenly started raining, so you race to Nathan's car and hop in, ready to hit the road.")
            if mask == True:
                covid += 2
            else:
                covid += 7.5
        elif nested_choice.upper() == "B":
            print("You head back out to the car and get inside.")
        else:
            print("error")
    elif choice.upper() == "B":
        print("Probably the right move, there are people everywhere without masks at the gas station.")
    else:
        print("error")

    print("Nathan starts the car up and says, \"Let's get going.\" You can see your town's skyline approaching from afar, but all of a sudden Nathan's car starts to make a strange noise. Pulling off to the side of the road, Nathan goes \"It must be the radiotor again! I just got it replaced last week, I guess my mechanic doesn't know what he's doing.\" Looking frustrated, he gets out of the car to see what's going on under the hood while you wonder why you chose to carpool with Nathan to yourself.")
    print("You pull out your phone and look at the current time. It is 8:30AM already after the stop and you have to open the doors to the vaccine center at 10AM. How will you try to get there in time: ")
    time.sleep(1)
    print("\tA. Call another co-worker\n\tB. Try to hitch a ride\n\tC. Call your Mom")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("You look through your contacts list, looking to see which of your co-workers might be able to grab you on their way to the downtown vaccine distribution center. You call 3 of your co-workers, with no success. Nancy is already downtown getting breakfast, Jason is waiting at the vaccine center, and Karen didn't even answer. Nathan gets back in the car and says, \"Is anybody able to pick us up?.\" You shake your head, no. An hour passes and it is now 9:30AM. Finally, you think to yourself that Braeden probably isn't even downtown yet, that guy is always running late, so you give him a call. Sure enough, he isn't even in town yet and will pass you in about 15 minutes, where he tells you that he can pick you up.")
    elif choice.upper() == "B":
        print("Nathan gets back in the car and goes, \"Well I am calling Triple A.\" Whatever, you think. You get out of the car and put your thumb to the sky. It's time to try and catch a ride. After waiting about 30 minutes, watching traffic whip by, a beat-up green truck pulls over. You go up to the window and a maskless man wearing a hat hollers, \"You looking for a ride bud?\" Well this isn't exactly the ride you were looking for, you think to yourself, but you get in nonetheless. You sit down on the crusty old, car seat.")
        if mask == True:
            print("\"Why don't you take off that silly old mask?\", the man says to you, as he coughs violently.")
        else:
            print("\"I'm glad you don't wear those silly masks!\", the man says as he coughs violently.")
        print("Will you: ")
        time.sleep(1)
        print("\tA. Wear Mask \n\tB. Go Maskless")
        choice = input(">>> ") #Here is your first choice.
        if choice.upper() == "A":
            covid += 15
            mask = True
            print("\"Well I am actually the vaccine distribution center manager! Are you going to get your vaccine today? They are finally available!\", you say. The man, still coughing, replies, \"NO! I am not going to get one of those silly vaccines!\" After that, the conversation pretty much died. About 10 minutes later, you are in the center of the town, about a mile and a half from the vaccine distribution center. After you informed him of your job, the man just dropped you off downtown, sped off, and basically abandoned you. Good riddance, you think.")
        elif choice.upper() == "B":
            covid += 30
            mask = False
            print("The man speeds downtown, his rickety truck rattling as it rolls down the highway. The man continues coughing violently, hopefully he isn't sick with COVID. He drops you off outside of a McDonald's downtown, where he is going to grab breakfast, and now you are a mile or so from the vaccine distribution center.")
    elif choice.upper() == "C":
        mask = True
        print("Well, mom isn't a bad choice. Let's see if she answers you think to yourself as you call her. Luckily she does and you beg for her to come pick you up on the side of the road so you can get the town it's much needed vaccine. \"Really?\", she says, \"This is so typical of you! But I will come get you, be careful and don't get near traffic.\" Nathan gets back in the car dejected and says, \"Well, I am calling Triple A.\" Luckily your mom is on the way.")
        print("About 30 minutes later, your mom pulls up behind you on the highway. You get out the car and embrace her, then get in the car and head downtown. \"Well, I will give you credit this time, at least you left for work early it's only 9AM. But really, you got a ride with Nathan? His car looked like it could fall apart at anytime!\" You roll your eyes and think, well I guess I deserve it.")
        print("Since you have an hour before the center is supposed to open, your mom takes you to Starbucks and buys you an orange juice along with your favorite breakfast sandwich. After giving your Mom an awkward in-car hug, you get out right in front of the vaccine center.")
        vaccine_center()
    else:
        print("error")


def option_transportation_bus():
    global covid # get the global var
    global mask
    # people at bus station without masks -- should you wait away from the bus and risk missing it?
    # getting on the bus minigame
    print("Well, the bus is always makes for an interesting trip, you think as you head out the door. You begin your walk to the bus stop, luckily it's a brisk but sunny morning, some of the perfect walking weather. Listening to your favorite song in your headphones, you approach the bus station and are surprised to see there are about 20 people waiting. Normally, there is almsot nobody there, there is already a line forming for the bus which will fill up quick! You observe that 14 of the bus riders waiting in line are not wearing masks. Will you:")
    time.sleep(1)
    print("\tA. Get in line\n\tB. Wait away from the bus and risk missing it")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("Well, it is probably smart to get in line now, that bus will fill up quick and you don't want to miss it. You walk up to the bus station and eventually the bus arrives. Unfortunately there are a lot of people without masks on the bus but at least you have a ride into work. Will you:")
        time.sleep(1)
        print("\tA. Put on Mask \n\tB. Go Maskless")
        nested_choice = input(">>> ") #Here is your first choice.
        if nested_choice.upper() == "A":
            covid += 5
            mask = True
        elif nested_choice.upper() == "B":
            covid += 15
            mask = False
    elif choice.upper() == "B":
        print("You walk over to a nearby bench where you can still view the bus station. The length of the line is beginning to increase a little bit though, hopefully it doesn't fill up!\nFinally, you see the bus pull up to the station and boarding begins. You walk over and join the back of the line.")
        rand_full = random.randint(0,1)
        if rand_full == 0:
            print("As you approach the bus doors, they begin to close. Unfortunately the bus is full, you will have to find another way to work.")
            ##
        else:
            print("Will you:")
            time.sleep(1)
            print("\tA. Put on Mask \n\tB. Go Maskless")
            nested_choice = input(">>> ") #Here is your first choice.
            if nested_choice.upper() == "A":
                covid += 2.5
                mask = True
            elif nested_choice.upper() == "B":
                covid += 12.5
                mask = False
            print("The bus driver, waves at you to get on the bus as you walk up. You are the last to board. Unfortunately there are a lot of people without masks on the bus but at least you have a ride into work.")
    else:
        print("error")
    downtown()

def option_transportation_subway():
    global covid # get the global var
    global mask
    print("You walk out your door, on a brisk but sunny morning, to go to the subway stop. The morning frost covers the grass and the sunlight glistens off of it. Walking down the sidewalk, you approach the subway station steps and descend into the darkness. You buy your subway ticket and head thru the turnstiles. Once inside the subway boarding area, you notice there are about 30 people waiting for the subway. Only about half of them are wearing masks. Will you: ")
    time.sleep(1)
    print("\tA. Put on your mask\n\tB. Wear no mask")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("You put on your mask and join the crowd of people waiting for the subway.")
        covid += 5
        mask = True
    elif choice.upper() == "B":
        print("You'll be fine without the mask this time, you think to yourself, as you join the crowd of people waiting for the subway.")
        covid += 15
        mask = False
    else:
        print("error")
    print("Finally you here the clattering of the subway on the tracks and see it's lights emerge from the darkness as it races down the tunnel, hurtling to a stop at the subway station. The doors open and you get onto the subway, navigating through maskless people on your way to an open seat.")
    print("After a 20-minute ride, the subway screeches to a halt and the stop location is announced by the conductor. Despite this, there are so many people on the subway, that you cannot hear the conductor. Will you: ")
    print("\tA. Get off now \n\tB. Try to wait it out for the right stop")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("You get off the subway and soon realize you are nowhere near where you intended to go. You are in the heart of downtown.")
        downtown()
    elif choice.upper() == "B":
        print("You decide to wait it out.")
        rand_loc = random.randint(0,1)
        if rand_loc == 0:
            print("The next stop, the subway conductor announces that you are on the other side of town from where you need to be. You know the subway will make another loop back up to the suburbs soon and frantically exit it. You will walk.")
            downtown()
        else:
            print("You arrive two streets away from the vaccine distribution center with lots of time to spare. You walk up the steps and out of the subway station, only to see that it is raining!")
            old_lady()



def vaccine_center():
    global covid

    print("\"What a day\", you think to yourself as you walk up to the doors of the vaccine distribution center. There are already a few hundred socially-distanced people outside of the distribution center and they begin cheering upon your arrival! Finally after over a year of living in the pandemic, it is time to stop the spread - for good. You open up the doors to the vaccine center and begin allowing people in. Despite everything that happened, today is a great day!")

    covid_status = virus_status(covid)

    if covid_status == True:
        print("You let your admittance workers take over the task of letting people enter the building and walk towards the back of the building observing the procedings. All of a sudden, you start coughing a bit! That's not good! You must have gotten COVID!")

        print("\n\nYou opened the doors to the Vaccine Center, but contracted the virus. You saved the community, but could not save yourself, maybe you should have worn your mask more.")
    else:
        print("\n\nYou Opened the Doors to the Vaccine Center and didn't contract the virus. You saved the community and kept yourself save in the process. Now, let's get that vaccine!")

def downtown():
    global covid # get the global var
    global mask
    print("You are standing, almost directly, in the center of the city. Welp, you better get walking so you can get to the vaccine distribution center, it is a little over a mile away, on the outskirts of town. It's about 9AM, so you should be able to make there in time by walking.")
    print("Walking down the streets, you approach a large crowd waiting outside of a building. Many of the people in the crowd are maskless and you will basically have to walk thru it since they are all over the sidewalk, and obviously you don't want to get run over. Will you: ")
    time.sleep(1)
    print("\tA. Wear Mask \n\tB. Go Maskless")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("You make sure your mask is on tight.")
        mask = True
        covid += 5
    else:
        print("Whatever about the mask. You are getting your vaccine later! Who cares?.....")
        mask = False
        covid += 10

    print("\"What the heck are all of these people waiting for\", you wonder to yourself. There are a ton of people waiting? Will you: ")
    time.sleep(1)
    print("\tA. Push through to the front of the crowd \n\tB. Get to the other side of the crowd and keep moving")
    choice = input(">>> ") #Here is your first choice.
    if choice.upper() == "A":
        print("There are even more maskless people towards the front of the crowd, you approach the doors of the building the people are crowded around and peer over shoulders to see what is going on. You can't believe it, but Elon Musk is in the lobby of the hotel! You ask someone nearby what is going on and they reply, \"Elon is here to give a free 45-minute talk to the town about Dogecoin today! Anyone can go, the doors open in a minute!\" Hmm, you think to yourself. Elon Musk is here, should you go try and see the talk? It's only 9AM, but you have to open the doors at 10AM! Will you: ")
        covid += 5
        time.sleep(1)
        print("\tA. View the entire talk \n\tB. View part of the talk \n\tC. Skip the talk")
        choice = input(">>> ") #Here is your first choice.
        if choice.upper() == "A":
            covid += 5
            print("You go in and listen to Elon speak. He always has something interesting to say and you never thought he would come to your town. Thank goodness you went, because you got free Dogecoin too!")
            print("It is now 9:50AM and there is no way you make it on time unless you run! You begin running down the road, but trip and fall, injuring your knee. It looks like the COVID center will be opening late.")
            vaccine_center()
        elif choice.upper() == "B":
            covid += 2.5
            print("You go in and listen to Elon speak. He always has something interesting to say and you never thought he would come to your town. About 20 minutes into the talk, you look at your watch and realize it is time to go! You have to be on time to open the doors!")
        else:
            print("You love Elon, but the right move would be to get going and open the doors to the vaccine center.")
    else:
        print("Probably the right move, there are a ton of people waiting out front without masks!")

        print("You walk down the street, in the direction of the vaccine distribution center. You see dark clouds looming in the distance and know rain is on the way, so you begin walking a little bit faster. As you walk down the road you get a call from one of your co-workers who is already at the vaccine center setting things up with the nurses. He frantically explains that half of the syringe applicators that were allocated to your vaccine distribution center were accidentally sent to the local hospital instead, but that they would be willing to give them back for opening day! You look at the map on your phone and realize you are only a street over from the hospital, then tell your co-worker you will handle it and change course to the hospital. You enter the front-doors of the hospital and explain the situation to the worker at the front-desk. She seems confused about all of this, will you: ")
        time.sleep(1)
        print("\tA. Wait a minute for her boss despite your time constraints \n\tB. Leave and open the vaccine center with the existing supplies \n\tC. Freak out and try to get the supplies")
        choice = input(">>> ") #Here is your first choice.
        if choice.upper() == "A":
            print("You wait a minute or so and the hospital director walks down the stairs, into the hospital lobby. Luckily you two know each other as you are both on the town's COVID response team. \"Ahh, I heard why you are here, come with me and we will grab your syringe applicators\", she says. You walk into the back of the hospital and grab the three large boxes of syringe applicators, then head out on your way. As you walk out with the hospital director, she offers to give you a ride over to the vaccine distribution center. You gladly oblige, especially now that it is raining outside. She quickly drives you over to the vaccine center, and you arrive with time to spare.")
        elif choice.upper() == "B":
            print("Well, you can always get the supplies later, opening the doors is probably more important.")
        elif choice.upper() == "C":
            print("\"I don't know what you are talking about, but you need to stop yelling or I will call hospital security to deal with you!\", the receptionist says. Disgruntled, you walk outside of the hospital.")

        print("You walk outside and notice that the streets are almost barren, the weather has gotten much worse during the time you were inside and the clouds look darker than before. You begin your trek down the street and it begins to rain. It is almost 9:45 after all of your stops! Will you?: ")
        time.sleep(1)
        print("\tA. Sprint down the slick streets in the rain \n\tB. Walk through the desolate streets and get soaked \n\tC. Get on a nearby bus you see")
        choice = input(">>> ") #Here is your first choice.
        if choice.upper() == "A":
            print("You begin sprinting down the streets and are making good time as the rain begins to pour down harder. The vaccine distribution center is close by, only a few streets away! You keep running fast and as you cross the street, you run over a street gate. All of a sudden you slip, badly hurting your knee. It looks like you will be going back to the hospital instead of to the vaccine center, the cases will likely rise.")
        elif choice.upper() == "B":
            print("You continue your trek through the rain, eventually nearing the vaccine distribution center.")
        elif choice.upper() == "C":
            print("You run to the nearby bus, trying to avoid getting soaked! As you get on, you ask the bus driver where the bus is going to be going. Hopefully it is nearby the vaccine distribution center!")
            rand_loc = random.randint(0,1)
            if rand_loc == 0:
                print("The bus is going to the vaccine distribution center! You got lucky!")
                vaccine_center()
            else:
                print("The bus is not going to the vaccine distribution center! You might be late, after wasting more time trying to get a ride.")
    old_lady()


def old_lady():
    global covid
    print("You keep walking down the streets, but as you near the vaccine distribution center you notice a old lady slip in the middle of the street due to the rain! She is not wearing a mask and is having trouble getting up, so you still rush out to the middle of the crosswalk and help her up.")
    rand_lady = random.randint(0,1)
    if rand_lady == 0:
        print("The lady thanks you for helping her up and you walk her to the other side of the street! \"Try to stay dry,\" she says, laughing. You walk to the vaccine center, arriving right at 10AM!")
        vaccine_center()
    else:
        print("You help her up, but while maskless she begins wheezing on you. Despite this, you help her up and walk her to the other side of the street. Thanking you, she says \"God bless you! Sorry for coughing on you, I promise I don't have covid. Well, maybe.\"")
        rand_lady_covid = random.randint(0,1)
        if rand_lady_covid == 0:
            covid += 2.5
        else:
            covid += 25
        vaccine_center()

def virus_status(probability):
    rand = random.randint(1, 100)
    if rand <= probability:
        return True
    elif rand >= probability:
        return False
    else:
        return "Error"
