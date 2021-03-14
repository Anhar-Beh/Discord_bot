import random
global games

#######################################Modules####################################
#Main loop that shows the user the chosen game
def main_loop(Lottery):
    percentage()
    roll = input('\ndo you want to roll?: ')
    if roll == 'yes':
        chosen = random.choice(Lottery)
        print ('\nIt has been decided! Don\'t cry\n' + chosen + '\n')
        
        #If user is not happy and wants to reroll (will not include chosen game into statistics until users play the game)
        stop = False
        while stop == False:
            option = input('Reroll?')
            if option == 'yes': 
                chosen = random.choice(Lottery)
                print ('\nIt has been decided! Don\'t cry\n' + chosen + '\n')
            else:
                save_data(chosen)
                stop = True
            
#Fetches past data from a saved file. If not, create the first save file    
def read_data():
    data = []
    try:
        with open('Data.txt','r') as r:
            info = r.readlines()
            for row in info:
                cleanUp = row.strip('\n').split(',')
                data.append([cleanUp[0],int(cleanUp[1])])
        return (data)
    #If the save file does not exist
    except:
        f = open('Data.txt','a+')
        for game in games:
            f.write(game + ',1\n')
            data.append([game,1])
        return (data)

#Saves the new version of the save file        
def save_data(game,data):
    with open('Data.txt','r') as r:
            info = r.readlines()
            del info
            
    with open('Data.txt','w') as w:
        new_data = data
        for row in new_data:
            if row[0] != game:
                row[1] = row[1] + 1
            row[1] = str(row[1])
            w.write(row[0] + ',' + row[1] + '\n')
    
#Creating the games lottery list to be used       
def lottery_creation(data):
    lottery = []
    for row in data:
        for i in range(0,row[1]):
            lottery.append(row[0])
    return (lottery)

def percentage(data,lottery):
    for game in data:
        print(game[0] + ': ' + str(game[1]) + '/' + str(len(lottery)))
        
##################################################################################        
#Game List
games = ['Rainbow Six Siege', 'Rec Room', 'Zombies', 'For Honor']

print('Game Decider is online')
