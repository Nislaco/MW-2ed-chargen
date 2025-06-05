import random

from flask import Flask, render_template, request, url_for, redirect, session  

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a strong secret key


result = []
results = []
detail = []
results_list = []


# Define the roll_dice_2d10 function here so it can be used by the web app
def roll_dice_2d10():
    dice1 = random.randint(1, 10)
    dice2 = random.randint(1, 10)
    if dice1 == 1:
        dice1 = 0
    if dice1 == 10:
        dice1 = 10
    if dice1 == 2:
        dice1 = 20
    if dice1 == 3:
        dice1 = 30
    if dice1 == 4:
        dice1 = 40
    if dice1 == 5:
        dice1 = 50
    if dice1 == 6:
        dice1 = 60
    if dice1 == 7:
        dice1 = 70
    if dice1 == 8:
        dice1 = 80
    if dice1 == 9:
        dice1 = 90
    if dice2 == 10:
        dice2 = 1
    
    # Calculate the sum of the dice rolls
    sum = dice1 + dice2

    # Initialize an empty output string
    output = ''

    # Display a custom message based on the sum of the dice rolls
    if sum <= 2:
        output = 2
    elif sum <= 7:
        output = 3
    elif sum <= 16:
        output = 4
    elif sum <= 27:
        output = 5
    elif sum <= 41:
        output = 6
    elif sum <= 57:
        output = 7
    elif sum <= 71:
        output = 8
    elif sum <= 82:
        output = 9
    elif sum <= 91:
        output = 10
    elif sum <= 96:
        output = 11
    elif sum >= 97:
        output = 12
    else:
        output += "Error Roll Again"

    # Append the output string to the tuple
    #results = (dice1, dice2, sum, output)
    detail = f"{'The first d10 = '}{dice1}{'.'}{'  The second d10 = '}{dice2}{'.'}{'  Total  =  '}{sum}{'%.  '}{'  2D6 score =  '}{output}"
    results = detail
  
    return results

# Define the roll_dice_1d6 function here so it can be used by the web app
def roll_dice_1d6():
    dice = random.randint(1, 6)
    dice1 = int(dice)
    results = f"{'You Rolled a  '}{dice1}{'.'}"
    return results

def roll_chart_dice_1d6():
    dice = random.randint(1, 6)
    dice1 = int(dice)
    output1 = dice1
    results = output1
    return results  

# Define the roll_dice_2d6 function here so it can be used by the web app
def roll_dice_2d6():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # Calculate the sum of the dice rolls
    sum1 = dice1 + dice2
    detail = f"{'First d6 = '}{dice1}{'.'}\
    {'  Second d6 = '}{dice2}{'.'}\
    {'  The sum for both dice = '}{sum1 }{'.'}"
    results = detail
    #results = (dice1, dice2, sum1)
    return results

def roll_chart_dice_2d6():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    output1 = ''
    sum1 = dice1 + dice2
    output1 = int(sum1)
    results = output1
    return results 

def roll_cluster_table(cluster_roll):
    output1 = ''
    ws = int(cluster_roll)
    output1 = roll_chart_dice_2d6()
    missile = 0    
    if ws == 2:
        missile = 0
        if output1 <= 7:
            missile = 1
        elif output1 >= 8:
            missile = 2
    elif ws == 3:
        missile = 0
        if output1 <= 4:
            missile = 1
        elif output1 >= 5:
            missile = 2
        elif output1 >= 10:
            missile = 3
    elif ws == 4:
        missile = 0
        if output1 == 2:
            missile = 1
        elif output1 <= 6:
            missile = 2
        elif output1 <= 10:
            missile = 3
        elif output1 >= 11:
            missile = 4
    elif ws == 5:
        missile = 0
        if output1 == 2:
            missile = 1
        elif output1 <= 4:
            missile = 2
        elif output1 <= 8:
            missile = 3
        elif output1 <= 10:
            missile = 4
        elif output1 >= 11:
            missile = 5
    elif ws == 6:
        missile = 0
        if output1 <= 3:
            missile = 2
        elif output1 <= 5:
            missile = 3
        elif output1 <= 8:
            missile = 4
        elif output1 <= 10:
            missile = 5
        elif output1 >= 11:
            missile = 6
    elif ws == 7:
        missile = 0
        if output1 <= 3:
            missile = 2
        elif output1 == 4:
            missile = 3
        elif output1 <= 8:
            missile = 4
        elif output1 <= 10:
            missile = 6
        elif output1 >= 11:
            missile = 7
    elif ws == 8:
        missile = 0
        if output1 <= 3:
            missile = 3
        elif output1 <= 5:
            missile = 4
        elif output1 <= 8:
            missile = 5
        elif output1 <= 10:
            missile = 6
        elif output1 >= 11:
            missile = 8
    elif ws == 9:
        missile = 0
        if output1 <= 3:
            missile = 3
        elif output1 == 4:
            missile = 4
        elif output1 <= 8:
            missile = 5
        elif output1 <= 10:
            missile = 7
        elif output1 >= 11:
            missile = 9
    elif ws == 10:
        missile = 0
        if output1 <= 3:
            missile = 3
        elif output1 == 4:
            missile = 4
        elif output1 <= 8:
            missile = 6
        elif output1 <= 10:
            missile = 8
        elif output1 >= 11:
            missile = 10
    elif ws == 11:
        missile = 0
        if output1 <= 3:
            missile = 4
        elif output1 == 4:
            missile = 5
        elif output1 <= 8:
            missile = 7
        elif output1 <= 10:
            missile = 9
        elif output1 >= 11:
            missile = 11
    elif ws == 12:
        missile = 0
        if output1 <= 3:
            missile = 4
        elif output1 == 4:
            missile = 5
        elif output1 <= 8:
            missile = 8
        elif output1 <= 10:
            missile = 10
        elif output1 >= 11:
            missile = 12
    elif ws == 13:
        missile = 0
        if output1 <= 3:
            missile = 4
        elif output1 == 4:
            missile = 5
        elif output1 <= 8:
            missile = 8
        elif output1 <= 10:
            missile = 11
        elif output1 >= 11:
            missile = 13
    elif ws == 14:
        missile = 0
        if output1 <= 3:
            missile = 5
        elif output1 == 4:
            missile = 6
        elif output1 <= 8:
            missile = 9
        elif output1 <= 10:
            missile = 11
        elif output1 >= 11:
            missile = 14
    elif ws == 15:
        missile = 0
        if output1 <= 3:
            missile = 5
        elif output1 == 4:
            missile = 6
        elif output1 <= 8:
            missile = 9
        elif output1 <= 10:
            missile = 12
        elif output1 >= 11:
            missile = 15
    elif ws == 16:
        missile = 0
        if output1 <= 3:
            missile = 5
        elif output1 == 4:
            missile = 7
        elif output1 <= 8:
            missile = 10
        elif output1 <= 10:
            missile = 13
        elif output1 >= 11:
            missile = 16
    elif ws == 17:
        missile = 0
        if output1 <= 3:
            missile = 5
        elif output1 == 4:
            missile = 7
        elif output1 <= 8:
            missile = 10
        elif output1 <= 10:
            missile = 14
        elif output1 >= 11:
            missile = 17
    elif ws == 18:
        missile = 0
        if output1 <= 3:
            missile = 6
        elif output1 == 4:
            missile = 8
        elif output1 <= 8:
            missile = 11
        elif output1 <= 10:
            missile = 14
        elif output1 >= 11:
            missile = 18
    elif ws == 19:
        missile = 0
        if output1 <= 3:
            missile = 6
        elif output1 == 4:
            missile = 8
        elif output1 <= 8:
            missile = 11
        elif output1 <= 10:
            missile = 15
        elif output1 >= 11:
            missile = 19
    elif ws == 20:
        missile = 0
        if output1 <= 3:
            missile = 6
        elif output1 == 4:
            missile = 9
        elif output1 <= 8:
            missile = 12
        elif output1 <= 10:
            missile = 16
        elif output1 >= 11:
            missile = 20
    elif ws == 21:
        missile = 0
        if output1 <= 3:
            missile = 7
        elif output1 == 4:
            missile = 9
        elif output1 <= 8:
            missile = 13
        elif output1 <= 10:
            missile = 17
        elif output1 >= 11:
            missile = 21
    elif ws == 22:
        missile = 0
        if output1 <= 3:
            missile = 7
        elif output1 == 4:
            missile = 9
        elif output1 <= 8:
            missile = 14
        elif output1 <= 10:
            missile = 18
        elif output1 >= 11:
            missile = 22
    elif ws == 23:
        missile = 0
        if output1 <= 3:
            missile = 7
        elif output1 == 4:
            missile = 10
        elif output1 <= 8:
            missile = 15
        elif output1 <= 10:
            missile = 19
        elif output1 >= 11:
            missile = 23
    elif ws == 24:
        missile = 0
        if output1 <= 3:
            missile = 8
        elif output1 == 4:
            missile = 10
        elif output1 <= 8:
            missile = 16
        elif output1 <= 10:
            missile = 20
        elif output1 >= 11:
            missile = 24
    elif ws == 25:
        missile = 0
        if output1 <= 3:
            missile = 8
        elif output1 == 4:
            missile = 10
        elif output1 <= 8:
            missile = 16
        elif output1 <= 10:
            missile = 21
        elif output1 >= 11:
            missile = 25
    elif ws == 26:
        missile = 0
        if output1 <= 3:
            missile = 9
        elif output1 == 4:
            missile = 11
        elif output1 <= 8:
            missile = 17
        elif output1 <= 10:
            missile = 21
        elif output1 >= 11:
            missile = 26
    elif ws == 27:
        missile = 0
        if output1 <= 3:
            missile = 9
        elif output1 == 4:
            missile = 11
        elif output1 <= 8:
            missile = 17
        elif output1 <= 10:
            missile = 22
        elif output1 >= 11:
            missile = 27
    elif ws == 28:
        missile = 0
        if output1 <= 3:
            missile = 9
        elif output1 == 4:
            missile = 11
        elif output1 <= 8:
            missile = 17
        elif output1 <= 10:
            missile = 23
        elif output1 >= 11:
            missile = 28
    elif ws == 29:
        missile = 0
        if output1 <= 3:
            missile = 10
        elif output1 == 4:
            missile = 12
        elif output1 <= 8:
            missile = 18
        elif output1 <= 10:
            missile = 23
        elif output1 >= 11:
            missile = 29
    elif ws == 30:
        missile = 0
        if output1 <= 3:
            missile = 10
        elif output1 == 4:
            missile = 12
        elif output1 <= 8:
            missile = 18
        elif output1 <= 10:
            missile = 24
        elif output1 >= 11:
            missile = 30
    elif ws == 40:
        missile = 0
        if output1 <= 3:
            missile = 12
        elif output1 == 4:
            missile = 18
        elif output1 <= 8:
            missile = 24
        elif output1 <= 10:
            missile = 32
        elif output1 >= 11:
            missile = 40
    else:
        missile = 0
    detail = f"{'With a cluster size of '}{ws}{'  and a 2d6 dice roll of '}{output1}{','}{'  the total number of cluster hits = '}{missile}{'.'}"
    return detail 

def roll_for_crit():
    output1 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 7:
        output2: str = "No Critical Hit"
    elif output1 <= 9:
        output2: str = "Roll 1 Critical Hit Location"
    elif output1 <= 11:
        output2: str = "Roll 2 Critical Hit Locations"
    elif output1 >= 12:
        output2: str = "Head/Limb Blown Off ; Roll 3 Critical Hit Locations*"
    else:
        output2: str = "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The check for a critical hit results in  '}{output2}{'.'}"
    return detail


def roll_basement_table():
    output1 = ''
    output1 = roll_chart_dice_2d6()
    
    if output1 == 2:
        output2: str = "Double basement. The unit falls 2 levels."
    elif output1 <= 4:
        output2: str = "Basement. The unit falls 1 level."
    elif output1 <= 8:
        output2: str = "No Basement."
    elif output1 <= 9:
        output2: str = "Small basement. Infantry may move into the basement as though it were a new level of the building (Sublevel 1); ProtoMechs cannot enter this level. No effect on ’Mechs or vehicles"
    elif output1 <= 11:
        output2: str = "Basement. The unit falls 1 level."
    elif output1 >= 12:
        output2: str = "Double basement. The unit falls 2 levels."
    else:
        output2: str = "Error Roll Again"

    detail = f"{' With a Roll of '}{output1}{'.'}{' There is/an : '}{output2}"
    return detail 

def motive_sys_damage_table():
    output1 = roll_chart_dice_2d6()
    output2 = ''
    if output1 <= 5:
        output2 += "No Effect"
    elif output1 <= 7:
        output2 += "Minor damage; +1 modifier to all Driving Skill Rolls"
    elif output1 <= 9:
        output2 += "Moderate damage; –1 Cruising MP, +2  modifier to all Driving Skill Rolls"
    elif output1 <= 11:
        output2 += "Heavy damage; only half Cruising MP (round fractions up), +3 modifier to all Driving Skill Rolls"
    elif output1 >= 12:
        output2 += "Major damage; no movement for the rest of the game. Vehicle is immobile."
    else:
        output2 += "Error roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Motive system check results in   '}{output2}{'.'}"
    return detail

def roll_for_facing():
    output1 = ''
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
        output2: str = "New Facing = Same direction  : Hit Location = Front"
    if output1 == 2:
        output2: str = "New Facing = 1 Hexside Right : Hit Location = Right Side"
    if output1 == 3:
        output2: str = "New Facing = 2 Hexsides Right : Hit location = Right Side"
    if output1 == 4:
        output2: str = "New Facing = Opposite Direction : Hit location = Rear"
    if output1 == 5:
        output2: str = "New Facing = 2 Hexsides Left : Hit Location = Left Side"
    if output1 == 6:
        output2: str = "Facing = 1 Hexside Left : Hit Location = Left Side"
    detail = f"{'With a Roll of '}{output1}{' ,'}{'  the units    '}{output2}{'.'}"
    return detail 

def mek_kick_table():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 <= 3:
      output2 += "right leg"
    elif output1 >= 4:
      output2 += "left leg"
    else:
        output2 += "Error Roll Again"
     
    detail = f"{'With a Roll of '}{output1}{'  the kick hits the    '}{output2}{'.'}"
    return detail   

def roll_random_movement():
   output1 = ''
   output1 = roll_chart_dice_1d6()
   if output1 == 1:
        output2: str = "Forward 1 hex, turn left 2 hexsides"
   elif output1 == 2:
        output2: str = "Forward 1 hex, turn left 1 hexside"
   elif output1 <= 4:
        output2: str = "Forward 1 hex"
   elif output1 == 5:
        output2: str = "Forward 1 hex, turn right 1 hexside"
   elif output1 == 6:
        output2: str = "Forward 1 hex, turn right 2 hexsides"
   detail = f"{'With a Roll of '}{output1}{' ,'}{'  the units randomly moves,     '}{output2}{'.'}"
   return detail 


def roll_special_protomech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Main Gun"
    elif output1 <= 4:
        output2 += "Legs"
    elif output1 == 5:
        output2 += "Right Arm"
    elif output1 <= 8:
        output2 += "Torso"
    elif output1 == 9:
        output2 += "Left Arm"
    elif output1 <= 11:
        output2 += "Legs"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"
    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Special Protomech takes a hit in the  '}{output2}{'.'}"
    result = detail
    return result

def roll_protomech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Main Gun"
    elif output1 == 3:
        output2 += "* Near Miss"
    elif output1 == 4:
        output2 += "Right Arm"
    elif output1 == 5:
        output2 += "Legs"
    elif output1 <= 8:
        output2 += "Torso"
    elif output1 == 9:
        output2 += "Legs"
    elif output1 == 10:
        output2 += "Left Arm"
    elif output1 == 11:
        output2 += "* Near Miss"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"
    detail = f"{'With a roll of '}{output1}{','}{'  the target Protomech takes a hit in the  '}{output2}{'.'}"
    result = detail
    #result = (output1, output2)
    return result

def mech_front_side_punch():
    output2 = ''   
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Left Arm"    
    if output1 == 2:
      output2 += "Left Torso"
    if output1 == 3:
      output2 += "Center Torso"
    if output1 == 4:
      output2 += "Right Torso"      
    if output1 == 5:
      output2 += "Right Arm"
    if output1 == 6:
      output2 += "Head" 

    detail = f"{'With a roll of '}{output1}{','}{'  the target Mech takes a punch on the front side in the  '}{output2}{'.'}"
    return detail

def mech_left_side_punch():
    output2 = '' 
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Left Torso"
    if output1 == 2:
      output2 += "Left Torso"
    if output1 == 3:
      output2 += "Center Torso"
    if output1 == 4:
      output2 += "Left Arm"      
    if output1 == 5:
      output2 += "Left Arm"
    if output1 == 6:
      output2 += "Head" 

    detail = f"{'With a roll of '}{output1}{','}{'  the target Mech takes a punch on the left side in the  '}{output2}{'.'}"
    return detail

def mech_right_side_punch():
    output2 = ''   
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Right Torso"    
    if output1 == 2:
      output2 += "Right Torso"
    if output1 == 3:
      output2 += "Center Torso"
    if output1 == 4:
      output2 += "Right Arm"      
    if output1 == 5:
      output2 += "Right Arm"
    if output1 == 6:
      output2 += "Head" 

    detail = f"{'With a roll of '}{output1}{','}{'  the target Mech takes a punch on the right side in the  '}{output2}{'.'}"
    result = detail
    return result

def roll_left_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Left Torso [critical]"
    elif output1 == 3:
        output2 += "Left Leg"
    elif output1 == 4:
        output2 += "Left Arm"
    elif output1 == 5:
        output2 += "Left Arm"
    elif output1 == 6:
        output2 += "Left Leg"
    elif output1 == 7:
        output2 += "Left Torso"
    elif output1 == 8:
        output2 += "Center Torso"
    elif output1 == 9:
        output2 += "Right Torso"
    elif output1 == 10:
        output2 += "Right Arm"
    elif output1 == 11:
        output2 += "Right Leg"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"      
    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Mech takes a Left Side hit in the  '}{output2}{'.'}"
    return detail

def roll_front_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Center Torso [critical]"
    elif output1 == 3:
        output2 += "Right Arm"
    elif output1 == 4:
        output2 += "Right Arm"
    elif output1 == 5:
        output2 += "Right Leg"
    elif output1 == 6:
        output2 += "Right Torso"
    elif output1 == 7:
        output2 += "Center Torso"
    elif output1 == 8:
        output2 += "Left Torso"
    elif output1 == 9:
        output2 += "Left Leg"
    elif output1 == 10:
        output2 += "Left Arm"
    elif output1 == 11:
        output2 += "Left Arm"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"
    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Mech takes a Front Side hit in the  '}{output2}{'.'}"
    return detail

def roll_right_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Right Torso [critical]"
    elif output1 == 3:
        output2 += "Right Leg"
    elif output1 == 4:
        output2 += "Right Arm"
    elif output1 == 5:
        output2 += "Right Arm"
    elif output1 == 6:
        output2 += "Right Leg"
    elif output1 == 7:
        output2 += "Right Torso"
    elif output1 == 8:
        output2 += "Center Torso"
    elif output1 == 9:
        output2 += "Left Torso"
    elif output1 == 10:
        output2 += "Left Arm"
    elif output1 == 11:
        output2 += "Left Leg"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"
    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Vtol takes a Right Side hit in the  '}{output2}{'.'}"
    return detail
      
def vtol_front_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Front [critical]"
    elif output1 <= 4:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 5:
        output2 += "Right Side"
    elif output1 <= 8:
        output2 += "Front"
    elif output1 == 9:
        output2 += "Left Side"
    elif output1 <= 11:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 12:
        output2 += "Rotors (critical) [Damage Value / 10 (round up) / -1 Cruising MP]"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Vtol takes a Front Side hit in the  '}{output2}{'.'}"
    return detail   

def vtol_rear_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Rear [critical]"
    elif output1 <= 4:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 5:
        output2 += "Left Side"
    elif output1 <= 8:
        output2 += "Rear"
    elif output1 == 9:
        output2 += "Right Side"
    elif output1 <= 11:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 12:
        output2 += "Rotors (critical) [Damage Value / 10 (round up) / -1 Cruising MP]"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Vtol takes a Rear Side hit in the  '}{output2}{'.'}"
    return detail


def vtol_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Side [critical]"
    elif output1 <= 4:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 5:
        output2 += "Front"
    elif output1 <= 7:
        output2 += "Side"
    elif output1 == 8:
        output2 += "Side (critical)"
    elif output1 == 9:
        output2 += "Rear [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Rotors [Damage Value / 10 (round up) / -1 Cruising MP]"
    elif output1 == 12:
        output2 += "Rotors (critical) [Damage Value / 10 (round up) / -1 Cruising MP]"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Vtol takes a Side hit in the  '}{output2}{'.'}"
    return detail

def roll_aero_nose_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 == "Nose / Weapon"
    if output1 <= 3:
        output2 += "Nose / Sensors"
    elif output1 == 4:
        output2 += "Right Wing / Heat Sink"
    elif output1 == 5:
        output2 += "Right Wing / Weapon"
    elif output1 == 6:
        output2 += "Nose / Avionics"
    elif output1 == 7:
        output2 += "Nose / Control"
    elif output1 == 8:
        output2 += "Nose / FCS"
    elif output1 == 9:
        output2 += "Left Wing / Weapon"
    elif output1 == 10:
        output2 += "Left Wing / Heat Sink"
    elif output1 == 11:
        output2 += "Nose / Gear"
    elif output1 == 12:
        output2 += "Nose / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target AeroFighter takes a Nose hit in the  '}{output2}{'.'}"
    return detail


def roll_aero_aft_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Aft / Weapon"
    elif output1 == 3:
        output2 += "Aft / Heat Sink"
    elif output1 == 4:
        output2 += "Right Side / Fuel"
    elif output1 == 5:
        output2 += "Right Side / Weapon"
    elif output1 == 6:
        output2 += "Aft / Engine"
    elif output1 == 7:
        output2 += "Aft / Control"
    elif output1 == 8:
        output2 += "Aft / Engine"
    elif output1 == 9:
        output2 += "Left Wing / Weapon"
    elif output1 == 10:
        output2 += "Left Wing / Fuel"
    elif output1 == 11:
        output2 += "Aft / Heat Sink"
    elif output1 == 12:
        output2 += "Aft / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target AeroFighter takes a Aft hit in the  '}{output2}{'.'}"
    return detail


def roll_aero_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Nose / Weapon"
    elif output1 == 3:
        output2 += "Wing / Gear"
    elif output1 == 4:
        output2 += "Nose / Sensors"
    elif output1 == 5:
        output2 += "Nose / Crew"
    elif output1 == 6:
        output2 += "Wing / Weapon"
    elif output1 == 7:
        output2 += "Wing / Avionics"
    elif output1 == 8:
        output2 += "Wing / Bomb"
    elif output1 == 9:
        output2 += "Aft / Control"
    elif output1 == 10:
        output2 += "Aft / Engine"
    elif output1 == 11:
        output2 += "Wing / Gear"
    elif output1 == 12:
        output2 += "Aft / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target AeroFighter takes a Side hit in the  '}{output2}{'.'}"
    return detail


def roll_aero_above_below_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Nose / Weapon"
    elif output1 == 3:
        output2 += "Wing / Gear"
    elif output1 == 4:
        output2 += "Nose / Sensors"
    elif output1 == 5:
        output2 += "Nose / Crew"
    elif output1 == 6:
        output2 += "Wing / Weapon"
    elif output1 == 7:
        output2 += "Nose / Avionics"
    elif output1 == 8:
        output2 += "Wing / Weapon"
    elif output1 == 9:
        output2 += "Aft / Control"
    elif output1 == 10:
        output2 += "Aft / Engine"
    elif output1 == 11:
        output2 += "Wing / Gear"
    elif output1 == 12:
        output2 += "Aft / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target AeroFighter takes a Above/Below hit in the  '}{output2}{'.'}"
    return detail

def drop_small_nose_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 == "Nose / Crew"
    if output1 <= 3:
        output2 += "Nose / Avionics"
    elif output1 == 4:
        output2 += "Right Side / Weapon"
    elif output1 == 5:
        output2 += "Right Side / Thruster"
    elif output1 == 6:
        output2 += "Nose / FCS"
    elif output1 == 7:
        output2 += "Nose / Weapon"
    elif output1 == 8:
        output2 += "Nose / Control"
    elif output1 == 9:
        output2 += "Left Side / Thruster"
    elif output1 == 10:
        output2 += "Left Side / Weapon"
    elif output1 == 11:
        output2 += "Nose / Sensors"
    elif output1 == 12:
        output2 += "Nose / K-F Boom"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Drop / Small Craft takes a Nose hit in the  '}{output2}{'.'}"
    return detail


def drop_small_aft_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Aft / Life Support"
    elif output1 == 3:
        output2 += "Aft / Control"
    elif output1 == 4:
        output2 += "Right Side / Weapon"
    elif output1 == 5:
        output2 += "Right Side / Door"
    elif output1 == 6:
        output2 += "Aft / Engine"
    elif output1 == 7:
        output2 += "Aft / Weapon"
    elif output1 == 8:
        output2 += "Aft / Docking Collar"
    elif output1 == 9:
        output2 += "Left Side / Door"
    elif output1 == 10:
        output2 += "Left Side / Weapon"
    elif output1 == 11:
        output2 += "Aft / Gear"
    elif output1 == 12:
        output2 += "Aft / Fuel"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Drop / Small Craft takes an Aft hit in the  '}{output2}{'.'}"
    return detail



def drop_small_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Nose / Weapon"
    elif output1 == 3:
        output2 += "Nose / FCS"
    elif output1 == 4:
        output2 += "Nose / Sensors"
    elif output1 == 5:
        output2 += "Side / Thruster"
    elif output1 == 6:
        output2 += "Side / Cargo"
    elif output1 == 7:
        output2 += "Side / Weapons"
    elif output1 == 8:
        output2 += "Collar Side / Door"
    elif output1 == 9:
        output2 += "Side / Thruster"
    elif output1 == 10:
        output2 += "Aft / Avionics"
    elif output1 == 11:
        output2 += "Aft / Engine"
    elif output1 == 12:
        output2 += "Aft / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Drop / Small Craft takes a side hit in the  '}{output2}{'.'}"
    return detail

def drop_small_above_below_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Nose / Weapon"
    elif output1 == 3:
        output2 += "Nose / FCS"
    elif output1 == 4:
        output2 += "Nose / Sensors"
    elif output1 == 5:
        output2 += "Side / Thruster"
    elif output1 == 6:
        output2 += "Side / Cargo"
    elif output1 == 7:
        output2 += "Side / Weapons"
    elif output1 == 8:
        output2 += "Side / Door"
    elif output1 == 9:
        output2 += "Side / Thruster"
    elif output1 == 10:
        output2 += "Aft / Avionics"
    elif output1 == 11:
        output2 += "Aft / Engine"
    elif output1 == 12:
        output2 += "Aft / Weapon"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Drop / Small Craft takes a Above/Below hit in the  '}{output2}{'.'}"
    return detail  

def ground_front_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Front [critical]"
    elif output1 <= 4:
        output2 += "Front [Roll Motive Check]"
    elif output1 == 5:
        output2 += "Right Side [Roll Motive Check]"
    elif output1 <= 8:
        output2 += "Front"
    elif output1 == 9:
        output2 += "Left Side [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Ground Vehicle takes a Front side hit in the  '}{output2}{'.'}"
    return detail  
  
def ground_rear_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Rear [critical]"
    elif output1 <= 4:
        output2 += "Rear [Roll Motive Check]"
    elif output1 == 5:
        output2 += "Left Side [Roll Motive Check]"
    elif output1 <= 8:
        output2 += "Rear"
    elif output1 == 9:
        output2 += "Right Side [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Ground Vehicle takes a Rear side hit in the  '}{output2}{'.'}"
    return detail

def ground_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Side [critical]"
    elif output1 <= 4:
        output2 += "Side [Roll Motive Check]"
    elif output1 == 5:
        output2 += "Front [Roll Motive Check]"
    elif output1 <= 7:
        output2 += "Side"
    elif output1 == 8:
        output2 += "Side [critical]"
    elif output1 == 9:
        output2 += "Rear [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Ground Vehicle takes a Side hit in the  '}{output2}{'.'}"
    return detail

def large_support_front_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 == "Front (critical)"
    elif output1 == 3:
        output2 += "Right Side [Roll Motive Check]"
    elif output1 <= 5:
        output2 += "Front [Roll Motive Check]"
    elif output1 <= 8:
        output2 += "Front"
    elif output1 == 9:
        output2 += "Front [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Large Support takes a Front hit in the  '}{output2}{'.'}"
    return detail

def large_support_rear_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Rear (critical)"
    elif output1 == 3:
        output2 += "Left Side [Roll Motive Check]"
    elif output1 <= 5:
        output2 += "Rear [Roll Motive Check]"
    elif output1 <= 8:
        output2 += "Rear"
    elif output1 == 9:
        output2 += "Rear [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Large Support takes a REar hit in the  '}{output2}{'.'}"
    return detail


def large_support_front_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Side  (critical)"
    elif output1 == 3:
        output2 += "Front [Roll Motive Check]"
    elif output1 == 4:
        output2 += "Side [Roll Motive Check]"
    elif output1 <= 7:
        output2 += "Side"
    elif output1 == 8:
        output2 += "Side (critical)"
    elif output1 == 9:
        output2 += "Side [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Large Support takes a Front Side hit in the  '}{output2}{'.'}"
    return detail


def large_support_rear_side_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Side  (critical)"
    elif output1 == 3:
        output2 += "Rear  [Roll Motive Check]"
    elif output1 == 4:
        output2 += "Side  [Roll Motive Check]"
    elif output1 <= 7:
        output2 += "Side"
    elif output1 == 8:
        output2 += "Side (critical)"
    elif output1 == 9:
        output2 += "Side [Roll Motive Check]"
    elif output1 <= 11:
        output2 += "Turret"
    elif output1 == 12:
        output2 += "Turret (critical)"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{'.'}{'  The Target Large Support takes a Rear Side hit in the  '}{output2}{'.'}"
    return detail  


def quad_left_side_punch():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Left Torso"
    if output1 == 2:
      output2 += "Left Torso"
    if output1 == 3:
      output2 += "Center Torso"
    if output1 == 4:
       output2 += "Left Front Leg"
    if output1 == 5:
      output2 += "Left Rear Leg"
    if output1 == 6:
      output2 += "Head"

    detail = f"{'With a Roll of '}{output1}{', Using left side punch table; The quad mech is punched in the    '}{output2}{'.'}"
    return detail  

def quad_front_side_punch():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Left Front Leg / Left Rear Leg"
    if output1 == 2:
      output2 += "Left Torso"
    if output1 == 3:
      output2 += "Center Torso"
    if output1 == 4:
      output2 += "Right Torso"
    if output1 == 5:
      output2 += "Right Front Leg / Right Rear Leg"
    if output1 == 6:
      output2 += "Head"

    detail = f"{'With a Roll of '}{output1}{', Using front side punch table; The quad mech is punched in the    '}{output2}{'.'}"
    return detail  

def quad_right_side_punch():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
      output2 += "Right Torso"
    elif output1 == 2:
      output2 += "Right Torso"
    elif output1 == 3:
      output2 += "Center Torso"
    elif output1 == 4:
      output2 += "Right Front Leg"
    elif output1 == 5:
      output2 += "Right Rear Leg"
    elif output1 == 6:
      output2 += "Head"

    detail = f"{'With a Roll of '}{output1}{', Using right side punch table; The quad mech is punched in the    '}{output2}{'.'}"
    return detail  

def quad_left_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Left Torso [critical]"
    elif output1 == 3:
        output2 += "Left Rear Leg"
    elif output1 == 4:
        output2 += "Left Front Leg"
    elif output1 == 5:
        output2 += "Left Front Leg"
    elif output1 == 6:
        output2 += "Left Rear Leg"
    elif output1 == 7:
        output2 += "Left Torso"
    elif output1 == 8:
        output2 += "Center Torso"
    elif output1 == 9:
        output2 += "Right Torso"
    elif output1 == 10:
        output2 += "Right Front Leg"
    elif output1 == 11:
        output2 += "Right Rear Leg"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using left side hit table; The quad mech is hit in the    '}{output2}{'.'}"
    return detail  


def quad_front_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Center Torso [critical]"
    elif output1 == 3:
        output2 += "Right Front Leg"
    elif output1 == 4:
        output2 += "Right Front Leg"
    elif output1 == 5:
        output2 += "Right Rear Leg"
    elif output1 == 6:
        output2 += "Right Torso"
    elif output1 == 7:
        output2 += "Center Torso"
    elif output1 == 8:
        output2 += "Left Torso"
    elif output1 == 9:
        output2 += "Left Rear Leg"
    elif output1 == 10:
        output2 += "Left Front Leg"
    elif output1 == 11:
        output2 += "Left Front Leg"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using front side hit table;  The quad mech is hit in the    '}{output2}{'.'}"
    return detail


def quad_right_side_mech_hit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 == 2:
        output2 += "Right Torso [critical]"
    elif output1 == 3:
        output2 += "Right Rear Leg"
    elif output1 == 4:
        output2 += "Right Front Leg"
    elif output1 == 5:
        output2 += "Right Front Leg"
    elif output1 == 6:
        output2 += "Right Rear Leg"
    elif output1 == 7:
        output2 += "Right Torso"
    elif output1 == 8:
        output2 += "Center Torso"
    elif output1 == 9:
        output2 += "Left Torso"
    elif output1 == 10:
        output2 += "Left Front Leg"
    elif output1 == 11:
        output2 += "Left Rear Leg"
    elif output1 == 12:
        output2 += "Head"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using right side hit table; The quad mech is hit in the    '}{output2}{'.'}"
    return detail

def quad_left_mek_kick_table():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 <= 3:
      output2 += "Left Front Leg"
    elif output1 >= 4:
      output2 += "Left Rear Leg"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using left side kick table; The quad mech is kicked in the    '}{output2}{'.'}"
    return detail  


def quad_front_mek_kick_table():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 <= 3:
      output2 += "Right Front Leg / Right Rear Leg"
    elif output1 >= 4:
      output2 += "Left Front Leg / Left Rear Leg"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using front side kick table; The quad mech is kicked in the    '}{output2}{'.'}"
    return detail 

def quad_right_mek_kick_table():
    output2 = ''
    output1 = roll_chart_dice_1d6()
    if output1 <= 3:
      output2 += "Right Front Leg"
    elif output1 >= 4:
      output2 += "Right Rear Leg"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{', Using right side kick table; The quad mech is kicked in the    '}{output2}{'.'}"
    return detail 

def vtol_rotors_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 <= 8:
        output2 += "Rotor Damage"
    elif output1 <= 10:
        output2 += "Flight Stabilizer Hit"
    elif output1 <= 12:
        output2 += "Rotors Destroyed"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The crit check for the vtols rotors results in : '}{output2}{'.'}"
    return detail  

def front_ground_combat_vee_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Driver Hit"
    elif output1 == 7:
        output2 += "Weapon Malfunction"
    elif output1 == 8:
        output2 += "Stabilizer"
    elif output1 == 9:
        output2 += "Sensors"
    elif output1 == 10:
        output2 += "Commander Hit"
    elif output1 == 11:
        output2 += "Weapon Destroyed"
    elif output1 == 12:
        output2 += "Crew Killed"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The front critical check for the target ground vehicle results in : '}{output2}{'.'}"
    return detail 


def side_ground_combat_vee_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Cargo/Infantry Hit"
    elif output1 == 7:
        output2 += "Weapon Malfunction"
    elif output1 == 8:
        output2 += "Crew Stunned"
    elif output1 == 9:
        output2 += "Stabilizer"
    elif output1 == 10:
        output2 += "Weapon Destroyed"
    elif output1 == 11:
        output2 += "Engine Hit"
    elif output1 == 12:
        output2 += "Engine Hit / Fuel Tank"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The side critical check for the target ground vehicle results in : '}{output2}{'.'}"
    return detail 


def rear_ground_combat_vee_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Weapon Malfunction"
    elif output1 == 7:
        output2 += "Cargo/Infantry Hit"
    elif output1 == 8:
        output2 += "Stabilizer"
    elif output1 == 9:
        output2 += "Weapon Destroyed"
    elif output1 == 10:
        output2 += "Engine Hit"
    elif output1 == 11:
        output2 += "Ammunition / Weapon Destroyed"
    elif output1 == 12:
        output2 += "Engine Hit / Fuel Tank"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The rear critical check for the target ground vehicle results in : '}{output2}{'.'}"
    return detail  


def turret_ground_combat_vee_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Stabilizer"
    elif output1 == 7:
        output2 += "Turret Jam"
    elif output1 == 8:
        output2 += "Weapon Malfunction"
    elif output1 == 9:
        output2 += "Turret Locks"
    elif output1 == 10:
        output2 += "Weapon Destroyed"
    elif output1 == 11:
        output2 += "Ammunition / Weapon Destroyed"
    elif output1 == 12:
        output2 += "Turret Blown Off"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The turret critical check for the target ground vehicle results in : '}{output2}{'.'}"
    return detail  


def vtol_front_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Co-Pilot Hit"
    elif output1 == 7:
        output2 += "Weapon Jam"
    elif output1 == 8:
        output2 += "Stabilizer"
    elif output1 == 9:
        output2 += "Sensors"
    elif output1 == 10:
        output2 += "Pilot Hit"
    elif output1 == 11:
        output2 += "Weapon Destroyed"
    elif output1 == 12:
        output2 += "Crew Killed"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The front side critical check for the target vtol results in : '}{output2}{'.'}"
    return detail  


def vtol_side_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Weapon Jam"
    elif output1 == 7:
        output2 += "Cargo / Infantry Hit"
    elif output1 == 8:
        output2 += "Stabilizer"
    elif output1 == 9:
        output2 += "Weapon Destroyed"
    elif output1 == 10:
        output2 += "Engine Hit"
    elif output1 == 11:
        output2 += "Ammunition / Weapon Destroyed"
    elif output1 == 12:
        output2 += "Engine Hit / Fuel Tank*"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The side critical check for the target vtol results in : '}{output2}{'.'}"
    return detail  


def vtol_rear_crit_table():
    output2 = ''
    output1 = roll_chart_dice_2d6()
    if output1 <= 5:
        output2 += "No Critical Hit"
    elif output1 == 6:
        output2 += "Cargo / Infantry Hit"
    elif output1 == 7:
        output2 += "Weapon Jam"
    elif output1 == 8:
        output2 += "Stabilizer"
    elif output1 == 9:
        output2 += "Weapon Destroyed"
    elif output1 == 10:
        output2 += "Sensors"
    elif output1 == 11:
        output2 += "Engine Hit"
    elif output1 == 12:
        output2 += "Engine Hit / Fuel Tank"
    else:
        output2 += "Error Roll Again"

    detail = f"{'With a Roll of '}{output1}{',  The rear side crit check for the target vtol results in : '}{output2}{'.'}"
    return detail    

def roll_for_facing():
    output1 = ''
    output1 = roll_chart_dice_1d6()
    if output1 == 1:
        output2: str = "New Facing = Same direction  : Hit Location = Front"
    if output1 == 2:
        output2: str = "New Facing = 1 Hexside Right : Hit Location = Right Side"
    if output1 == 3:
        output2: str = "New Facing = 2 Hexsides Right : Hit location = Right Side"
    if output1 == 4:
        output2: str = "New Facing = Opposite Direction : Hit location = Rear"
    if output1 == 5:
        output2: str = "New Facing = 2 Hexsides Left : Hit Location = Left Side"
    if output1 == 6:
        output2: str = "Facing = 1 Hexside Left : Hit Location = Left Side"
    detail = f"{'With a Roll of '}{output1}{' ,'}{'  the units    '}{output2}{'.'}"
    return detail 


@app.route('/', methods=['GET', 'POST'])
def index():

    output = ''
    if request.method == 'POST':
        selected_option = request.form['option']
        session['selected_option'] = selected_option
        if 'button1' in request.form:
            output = roll_dice_2d10()  
            results.append(output)
        elif 'button2' in request.form:
            output = roll_dice_1d6()
            results.append(output)
        elif 'button3' in request.form:
            output = roll_dice_2d6()
            results.append(output)
        elif 'button4' in request.form:
            return redirect(url_for('clear_results'))
        elif 'button5' in request.form:
            cluster_roll = request.form.get("cluster-roll")
            output = roll_cluster_table(cluster_roll)
            results.append(output)
        elif request.form['button'] == 'RollforCrit':
            output = roll_for_crit()
            results.append(output) 
        elif request.form['button'] == 'randommove': 
            output = roll_random_movement()
            results.append(output) 
        elif request.form['button'] == 'mech-kick':
            output = mek_kick_table()
            results.append(output)  
        elif request.form['button'] == 'motive-check':
            output = motive_sys_damage_table()
            results.append(output) 
        elif request.form['button'] == 'mech-kick':
            output = mek_kick_table()
            results.append(output)  
        elif request.form['button'] == 'basementroll':
            output = roll_basement_table()  
            results.append(output)
        elif request.form['button'] == 'prototable':
            output = roll_protomech_hit_table()
            results.append(output)
        elif request.form['button'] == 'specproto':
            output = roll_special_protomech_hit_table() 
            results.append(output)
        elif request.form['button'] == 'mek-left-hit':
            output = roll_left_side_mech_hit_table()
            results.append(output)
        elif request.form['button'] == 'mek-front-hit':
            output = roll_front_side_mech_hit_table()
            results.append(output)
        elif request.form['button'] == 'mek-right-hit':
            output = roll_right_side_mech_hit_table()
            results.append(output)
        elif request.form['button'] == 'vt-fr-hit':
            output = vtol_front_hit_table()
            results.append(output)
        elif request.form['button'] == 'vt-side-hit':
            output = vtol_side_hit_table()
            results.append(output)
        elif request.form['button'] == 'vt-rear-hit':
            output = vtol_rear_hit_table()   
            results.append(output)
        elif request.form['button'] == 'aero-nse-hit':
            output = roll_aero_nose_hit_table()
            results.append(output)
        elif request.form['button'] == 'aero-side-hit':
            output = roll_aero_side_hit_table()
            results.append(output)
        elif request.form['button'] == 'aero-aft-hit':
            output = roll_aero_aft_hit_table()
            results.append(output)
        elif request.form['button'] == 'aero-abol-hit':
            output = roll_aero_above_below_hit_table()   
            results.append(output)
        elif request.form['button'] == 'drop_small-nse-hit':
            output = drop_small_nose_hit_table()
            results.append(output)
        elif request.form['button'] == 'drop_small-side-hit':
            output = drop_small_side_hit_table()
            results.append(output)
        elif request.form['button'] == 'drop_small-aft-hit':
            output = drop_small_aft_hit_table()
            results.append(output)
        elif request.form['button'] == 'drop_small-abol-hit':
            output = drop_small_above_below_hit_table()
            results.append(output)
        elif request.form['button'] == 'gr-fr-hit':
            output = ground_front_side_hit_table()
            results.append(output)
        elif request.form['button'] == 'gr-side-hit':
            output = ground_side_hit_table()
            results.append(output)
        elif request.form['button'] == 'gr-rear-hit':
            output = ground_rear_hit_table()
            results.append(output)
        elif request.form['button'] == 'mek-left-punch':
            output = mech_left_side_punch()
            results.append(output)
        elif request.form['button'] == 'mek-front-punch':
            output = mech_front_side_punch()
            results.append(output)
        elif request.form['button'] == 'mek-right-punch':
           output = mech_right_side_punch()      
           results.append(output)
        elif request.form['button'] == 'gr-fr-crit':
           output = front_ground_combat_vee_crit_table()
           results.append(output)
        elif request.form['button'] == 'gr-side-crit':
           output = side_ground_combat_vee_crit_table() 
           results.append(output)
        elif request.form['button'] == 'gr-rear-crit':
           output = rear_ground_combat_vee_crit_table()
           results.append(output)
        elif request.form['button'] == 'gr-tr-crit':
          output = turret_ground_combat_vee_crit_table()
          results.append(output)
        elif request.form['button'] == 'vt-fr-crit':
          output = vtol_front_crit_table()
          results.append(output)
        elif request.form['button'] == 'vt-side-crit':
          output = vtol_side_crit_table()
          results.append(output)
        elif request.form['button'] == 'vt-rear-crit':
          output = vtol_rear_crit_table()
          results.append(output)
        elif request.form['button'] == 'vt-rt-crit':
          output = vtol_rotors_crit_table()      
          results.append(output)
        elif request.form['button'] == 'vt-rt-crit':
          output = vtol_rotors_crit_table()      
          results.append(output)
        elif request.form['button'] == 'quad-left-hit':
          output = quad_left_side_mech_hit_table()
          results.append(output)
        elif request.form['button'] == 'quad-front-hit':
          output = quad_front_side_mech_hit_table()
          results.append(output)
        elif request.form['button'] == 'quad-right-hit':
         output = quad_right_side_mech_hit_table()  
         results.append(output)
        elif request.form['button'] == 'quad-front-punch':
         output = quad_front_side_punch()
         results.append(output)
        elif request.form['button'] == 'quad-left-punch':
         output = quad_left_side_punch()
         results.append(output)
        elif request.form['button'] == 'quad-right-punch':
         output = quad_right_side_punch()
         results.append(output)
        elif request.form['button'] == 'quad-front-kick':
         output = quad_front_mek_kick_table()
         results.append(output)
        elif request.form['button'] == 'quad-left-kick':
         output = quad_left_mek_kick_table()
         results.append(output)
        elif request.form['button'] == 'quad-right-kick':
         output = quad_right_mek_kick_table()   
         results.append(output)
        elif request.form['button'] == 'mech-kick':
         output = mek_kick_table()      
         results.append(output)
        elif request.form['button'] == 'lg-sup-front-hit':
         output = large_support_front_hit_table()
         results.append(output)
        elif request.form['button'] == 'lg-sup-fside-hit':
         output = large_support_front_side_hit_table()
         results.append(output)
        elif request.form['button'] == 'lg-sup-rear-hit':
         output = large_support_rear_hit_table()
         results.append(output)
        elif request.form['button'] == 'lg-sup-rside-hit':
         output = large_support_rear_side_hit_table()      
         results.append(output)
        elif request.form['button'] == 'rollforfacing':
          output = roll_for_facing()   
          results.append(output)
 
    return render_template('index.html',  results=results)



@app.route('/script', methods=['GET', 'POST'])
def run_script():

 
    detail = ''
    result = ''



    if request.method == 'POST':
        gunnery_skill = int(request.form['gunnerySkill'])
        attacker_movement = int(request.form['attackerMovement'])
        target_movement = int(request.form['targetMovement'])
        target_condition = request.form['targetCondition']
        other_modifiers = int(request.form['otherModifiers'])
        selected_range = request.form['range']
        target_movement_modifier = calculate_target_movement_modifier(target_movement, target_condition)
        range_modifier = calculate_range_modifier(selected_range)
        to_hit_number = calculate_to_hit_number(gunnery_skill, attacker_movement, target_movement_modifier,other_modifiers, range_modifier)

        #results['to_hit_number'] = to_hit_number
        result = to_hit_number

    return render_template('index.html', results=results, results_list=results_list)


def calculate_target_movement_modifier(target_movement, target_condition):
    modifier = 0
    if 0 <= target_movement <= 2:
        modifier = 0
    elif 3 <= target_movement <= 4:
        modifier = 1
    elif 5 <= target_movement <= 6:
        modifier = 2
    elif 7 <= target_movement <= 9:
        modifier = 3
    elif 10 <= target_movement <= 17:
        modifier = 4
    elif 18 <= target_movement <= 24:
        modifier = 5
    elif target_movement >= 25:
        modifier = 6

    if target_condition == "prone_adjacent":
        modifier -= 2
    elif target_condition == "prone":
        modifier += 1
    elif target_condition == "immobile":
        modifier -= 4

    return modifier


def calculate_range_modifier(selected_range):
    if selected_range == "short":
        return 0
    elif selected_range == "medium":
        return 2
    elif selected_range == "long":
        return 4
    else:
        return 0


def calculate_to_hit_number(gunnery_skill, attacker_movement, target_movement_modifier, other_modifiers,range_modifier):
    target_condition = request.form['targetCondition']
    selected_range = request.form['range']

    if 'results_list' in session:
        results_list = session['results_list']
    else:
        session['results_list'] = []

    
    detail = []
    nl_char = '\n'    
    gs = gunnery_skill
    am = attacker_movement
    tm = target_movement_modifier
    rm = range_modifier
    om = other_modifiers
    tc = target_condition

    total = (gunnery_skill + attacker_movement + target_movement_modifier + other_modifiers + range_modifier)

    detail = f"{total}{nl_char}{nl_char}{' With a gunnery skill of '}{gs}{' and movement modifier of +'}{am}{';'}{nl_char}{' As well as including the '}{tc}{' targets movement modifier of '}{tm}{','}{nl_char}{' plus the total of all other modifiers '}{om}{','}{' the '}{selected_range}{' ranged shot +'}{rm}{';'}{nl_char}{' Would require '}{'('}{total}{')'}{' or better to hit the selected target'}{'.'}"
    
    session['results_list'] = detail

    return session['results_list']
  

@app.route('/clear', methods=['GET', 'POST'])
def clear_results():
    #session.pop('results', '')
    global results
    global detail    
    results = []
    detail = []
    session['results_list'] = ''
    return render_template('index.html' )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
  
