import random
import time
import sys
import unicodedata
## The array that holds random monster.
arr_mons = [
    "monster", "fairy", "pirate", "dragon",
    "troll", "gorgon", "Golem", "Oni",
    "Ogre", "Leprechaun", "Gnome", "Goblin",
    "Aqrabuamelu", "Minotaur", "Centaur", "Faun",
    "Werewolf", "Griffin", "Phoenix", "Basilisk",
    "Bigfoot", "Chimera", "Hydra", "Pontianak",
    "Banshee", "Dybbuk", "Vampire", "Bogeyman"
    ]
randmons = random.choice(arr_mons)
score = 5
vic = ""
## The scenarios.
## The first scenario.
s_1_v_1 = " You have rid the town of the "
s_1_v_2 = " takes one look at your shiny"
s_1_v_3 = s_1_v_2 + " new dagger of Ogoroth and runs away," + s_1_v_1
s_1_v_4 = ". You are victorious."
sc_1 = "But the " +  randmons + s_1_v_3 + randmons + s_1_v_4
## +1 score.
## The second scenario.
s2v0 = "And the "
s2v1 = " was about to cast a spell, but you finished the job by"
s2v2 = " the killing and you have rid the town of the "
s2v3 = " before the spell came near you, congratulations"
s2v4 = " you are victorious!!"
sc_2 =  s2v0 +  randmons + s2v1 + s2v2 + randmons + s2v3 + s2v4
## +1 score.
## The third scenario.
s3v0 = "And as you are ready to stab, but the "
s3v1 = " looks at you and just does a backflip while your hand goes for the"
s3v2 = " neck so you fall on the floor and the "
s3v3 = " cast a spell on you and you are now a goat."
sc_3 =  s3v0 +  randmons + s3v1 + s3v2 + randmons +  s3v3
## -1 score.
## The fourth scenario.
s4v0 = "And as you go for the neck the "
s4v1 =  " does a kung fu move and just dodge the hit and cast a spell"
s4v2 = " that goes straight to your head, you are a goat now."
sc_4 = s4v0 + randmons + s4v1 + s4v2
## -1 score.
vic_sc = [sc_1, sc_2, sc_3, sc_4]
vic = random.choice(vic_sc)
    

def print_pause(a):
    ## Makes the computer print then wait for two seconds.
    print(a)
    time.sleep(2)


def game_desc():
    ## The main function that will connect to most of the functions.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    wild = "You find yourself standing in an open field full"
    print(wild + " of grass and yellow wildflowers.")
    time.sleep(2)
    rumor = "Rumor has it that there is an evil "
    somewhere = " somewhere here, "
    it = somewhere + "and it has been terrorizing the nearby village."
    print(rumor + randmons +  it)
    time.sleep(2)
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    hand = "In your hand you hold your trusty"
    print_pause(hand + " (but not very effective) old dagger.")
    print_pause("Enter 1 to knock on the door.")
    print_pause("Enter 2 to look at the cave.")
    print_pause("what do you want to do?")
    print_pause("(Please enter 1 or 2).")
    while 1:
        inp6 = input()
        if (inp6 == "1"):
            fir_house()
            while 1:
                inp7 = input()
                if (inp7 == "1"):
                    fir_figh()
                    break
                elif (inp7 == "2"):
                    run_away_1()
                    break
                else:
                    print_pause("(Please enter 1 or 2).")
            break
        elif (inp6 == "2"):
            fir_cave()
            break
        else:
            print_pause("(Please enter 1 or 2).")


def choice():
    ##The first choice of the game(either a cave or knock on the door).
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    print_pause("Enter 1 to knock on the door.")
    print_pause("Enter 2 to look at the cave.")
    print_pause("(Please enter 1 or 2).")
    while 1:
       inp6 = input()
       if (inp6 == "1"):
           fir_house()
           while 1:
               inp7 = input()
               if (inp7 == "1"):
                   fir_figh()
                   break
               elif (inp7 == "2"):
                   run_away_1()
                   break
               else:
                   print_pause("(Please enter 1 or 2).")
           break
       elif (inp6 == "2"):
           fir_cave()
           break
       else:
           print_pause("(Please enter 1 or 2).")


def choice_2():
    ## The second choice in the game.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    print_pause("Enter 1 to knock on the door.")
    print_pause("Enter 2 to look at the cave.")
    while 1:
        inp9 = input()
        if (inp9 == "1"):
            sec_house()
            break
        elif (inp9 == "2"):
            sec_cave()
            break
        else:
            print_pause("(Please enter 1 or 2).")


def fir_house():
    ## Knocking the door without a weapon.
     global sc_1
     global sc_2
     global sc_3
     global sc_4
     global score
     global vic
     knock = "You knock on the door of the house and it opens"
     print_pause(knock + " with a little squeaky sound")
     you = "You try to look inside of the house"
     print_pause(you + " but you see no one there")
     are = "As you are about to leave you sense"
     print_pause(are + " heavy breathing near your shoulder")
     look = "You look behind you in a very slow"
     print_pause(look + " motion like horror movies")
     noth = "And then, you see nothing...."
     print_pause(noth + "and you look back towards the house")
     print("it is the",randmons,"with a scary smile!!!")
     time.sleep(2)
     feel = "You feel under-prepared for this, what with"
     print_pause(feel + " only having a not very effective old dagger")
     print_pause("would you like to:")
     print_pause("(1) Stab")
     print_pause("(2) Run away")
     while 1:
         inp11 = input()
         if (inp11 == "1"):
             fir_figh()
             break
         elif (inp11 == "2"):
             run_away_1()
             break
         else:
             print_pause("(Please enter 1 or 2).")


def score_ ():
    ## The scoring system.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    if (score == 6):
        win = "You win!!But not yet, you have to answer this question,"
        answer = " if you answer it you will win and the game will close,"
        print_pause(win + answer + " think carefully!!")
        race = "You’re in a race and you pass the person in second place"
        print_pause(race + ". What place are you in now?")
        print_pause("(1) You are in the first place")
        print_pause("(2) You are in the second place")
        print_pause("(Please choose 1 or 2).")
        while 1:
            inp12 = input()
            if (inp12 == "1"):
                print_pause("You are wrong!!! Now your score is 0")
                score = 0
                play_again()
            elif (inp12 == "2"):
                cong = "Congratulations!!!You won, now the program will "
                close = "close, thank you for playing my game"
                print_pause(cong + close +  " ##### Khaled Alhalwagy #####")
                sys.exit(0)
    elif (score < 0):
        print_pause("come on man, you have so little points, You lost now!!")
        sys.exit()


def play_again():
    ## After you win or lose this is the play again message.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    global randmons
    global arr_mons
    print_pause(f"your score is: {score}")
    score_()
    print_pause("Would you like to play again? (y/n)")                                                    
    while 1:                                                                                              
        inp3 = input()                                                                                                            
        if (inp3 == "y"):
            randmons = random.choice(arr_mons)
            game_desc()
        elif (inp3 == "n"):
            sys.exit(0)
        else:
            print_pause("(Please enter y or n).")


def run_away_1():
    ## If you knock on the door for the first time.    
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    run = "You run back to the field. And luckily,"
    print_pause(run + " you do not seem to have been followed")
    choice()


def run_away_2():
    ## If you knock on the door for the second time.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    run = "You run back to the field. And luckily,"
    print_pause(run + " you do not seem to have been followed")
    choice_2()


def fir_figh():
    ## If you fight without a weapon.
     global sc_1
     global sc_2
     global sc_3
     global sc_4
     global score
     global vic
     print_pause("You try your best...")
     print_pause("You hold tight to your old dagger and ready to stab")
     print("but your old dagger is no match for the", randmons)
     time.sleep(2)
     print_pause("You have been turned to a goat")
     score -= 1
     play_again()
     

def fir_cave():
    ## If you enter the cave for the first time.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    print_pause("You peer cautiously to the cave")
    print_pause("It turns out to be only a very small cave")
    print_pause("You see something shiny behind a rock")
    print_pause("You have found the magical dagger of Ogoroth")
    discard = "You discard your rusty old dagger"
    print_pause(discard + " and take the dagger of Ogoroth with you")
    print_pause("You walk back out to the cave")
    print_pause("You walk to the field")
    choice_2()


def sec_cave():
    ## If you enter the cave after collecting the loot.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic
    print_pause("You peer cautiously to the cave")
    peer = "You have been here before, and gotten all the good stuff."
    print_pause(peer + " It is just an empty cave now")
    print_pause("You walk back out to the cave")
    print_pause("You walk to the field")
    choice_2()


def sec_house():
    ## If you enter the house with your new weapon.
     global sc_1
     global sc_2
     global sc_3
     global sc_4
     global score
     global vic
     knock = "You knock on the door of the house and it opens"
     print_pause(knock + " with a little squeaky sound")
     you = "You try to look inside of the house"
     print_pause(you + " but you see no one there")
     are = "As you are about to leave you sense"
     print_pause(are + " heavy breathing near your shoulder")
     look = "You look behind you in a very slow"
     print_pause(look + " motion like horror movies")
     noth = "And then, you see nothing...."
     print_pause(noth + "and you look back towards the house")
     print("it is the",randmons,"with a scary smile!!!")
     time.sleep(2)
     print_pause("would you like to:")
     print_pause("(1) Stab")
     print_pause("(2) Run away")
     while 1:
         inp10 = input()
         if (inp10 == "1"):
             sec_figh()
             break
         elif (inp10 == "2"):
             run_away_2()
             break
         else:
             print_pause("(Please enter 1 or 2).")


def sec_figh():
    ## If you fight but with the new dagger.
    global sc_1
    global sc_2
    global sc_3
    global sc_4
    global score
    global vic_sc
    global vic
    ## The scenarios.
    ## The first scenario.
    s_1_v_1 = " You have rid the town of the "
    s_1_v_2 = " takes one look at your shiny"
    s_1_v_3 = s_1_v_2 + " new dagger of Ogoroth and runs away," + s_1_v_1
    s_1_v_4 = ". You are victorious."
    sc_1 = "But the " +  randmons + s_1_v_3 + randmons + s_1_v_4
    ## +1 score.
    ## The second scenario.
    s2v0 = "And the "
    s2v1 = " was about to cast a spell, but you finished the job by"
    s2v2 = " the killing and you have rid the town of the "
    s2v3 = " before the spell came near you, congratulations"
    s2v4 = " you are victorious!!"
    sc_2 =  s2v0 +  randmons + s2v1 + s2v2 + randmons + s2v3 + s2v4
    ## +1 score.
    ## The third scenario.
    s3v0 = "And as you are ready to stab, but the "
    s3v1 = " looks at you and just does a backflip while your hand goes for the"
    s3v2 = " neck so you fall on the floor and the "
    s3v3 = " cast a spell on you and you are now a goat."
    sc_3 =  s3v0 +  randmons + s3v1 + s3v2 + randmons +  s3v3
    ## -1 score.
    ## The fourth scenario.
    s4v0 = "And as you go for the neck the "
    s4v1 =  " does a kung fu move and just dodge the hit and cast a spell"
    s4v2 = " that goes straight to your head, you are a goat now."
    sc_4 = s4v0 + randmons + s4v1 + s4v2
    ## -1 score.
    vic_sc = [sc_1, sc_2, sc_3, sc_4]
    vic = random.choice(vic_sc)
    cast = " moves to cast a spell, you raise your new dagger of Ogoroth"
    print("As the",randmons + cast)
    time.sleep(2)
    shine = "The dagger of Ogoroth shines brightly in your hand"
    print(shine + " as you brace yourself to kill the", randmons)
    time.sleep(2)
    print_pause(vic)
    if vic.strip() == sc_1:
        score += 1
    elif vic.strip() == sc_2:
        score += 1
    elif vic.strip() == sc_3:
        score -= 1
    elif vic.strip() == sc_4:
        score -= 1
    vic = random.choice(vic_sc)
    play_again()
           
  
while 1:
    game_desc()