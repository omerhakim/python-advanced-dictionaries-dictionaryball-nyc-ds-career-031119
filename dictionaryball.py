
game_dictionary = {'home':{'team_name':'Brooklyn Nets','colors': ['Black', 'White'],'players':{'Alan Anderson':{'number':0 ,'shoe':16 ,'points':22 , 'rebounds':12, 'assists': 12, 'steals': 3 , 'blocks':1, 'slam_dunks':1 }, 'Reggie Evans':{'number':30  ,'shoe':14 ,'points':12  , 'rebounds':12, 'assists': 12 , 'steals': 12 , 'blocks':12 , 'slam_dunks':7},' Brook Lopez':{'number':11 ,'shoe':17,'points':17  , 'rebounds':19, 'assists': 10, 'steals': 3, 'blocks':1, 'slam_dunks': 15},'Mason Plumlee':{'number':1  ,'shoe':19  ,'points':26 , 'rebounds':12, 'assists': 6 , 'steals': 3, 'blocks':8 , 'slam_dunks': 5 },'Jason Terry':{'number':31 ,'shoe':15 ,'points':19 , 'rebounds':2, 'assists': 2, 'steals': 4, 'blocks':11, 'slam_dunks':  1}}},
                                    
  'away':{'team_name':'Charlotte Hornets','colors': ['Turquoise, Purple'],'players':{'Jeff Adrien':{'number':4 ,'shoe':18 ,'points':10 , 'rebounds':1, 'assists': 1, 'steals': 2, 'blocks':7, 'slam_dunks': 2}, 'Bismak Biyombo':{'number':0 ,'shoe':16 ,'points':12 , 'rebounds':4, 'assists': 1, 'steals': 2, 'blocks':7, 'slam_dunks': 2},'DeSagna Diop': {'number':2 ,'shoe':14 ,'points':24 , 'rebounds':12, 'assists': 12, 'steals': 4, 'blocks':5, 'slam_dunks': 5},'Ben Gordon' :{'number':8 ,'shoe':15 ,'points':33 , 'rebounds':3, 'assists': 2, 'steals': 1, 'blocks':1, 'slam_dunks': 0},'Brendan Haywood':{'number':33 ,'shoe':15,'points':6 , 'rebounds':12, 'assists': 12, 'steals': 22, 'blocks':5, 'slam_dunks': 12}}}}

              
def game_dict():
    return game_dictionary

def num_points_scored(name):
    for i,x, in game_dictionary.items():
        for z in (x['players']):
            
            if z==name:
                return (x['players'][z]['points'])
                
def shoe_size(name):
    for i,x, in game_dictionary.items():
        for z in (x['players']):
            
            if z==name:
                return (x['players'][z]['shoe'])
                
def team_colors(team):
    for i,x, in game_dictionary.items():
        if x['team_name'] ==team:
            return (x['colors']) 

def team_names():
    names=[]
    for i,x, in game_dictionary.items():
        names.append(x['team_name'])
    return names

def player_numbers(team):
    numbers = []
    for i,x, in game_dictionary.items():
        if x['team_name'] ==team:
            for i in x['players']:
                numbers.append(x['players'][i]['number'])
    return numbers

def player_stats(name):
    for i,x, in game_dictionary.items():
        for z,y in x['players'].items():
            if z==name:
                return (y)
                
def most_points_scored():
    mostp = []
    for i,x, in game_dictionary.items():
        for z,y in x['players'].items():
            dic={z:y['points']}
            mostp.append(dic)
    
    p1=0
    for y in range(0,len(mostp)):
        for i,x in mostp[y].items():
            if x>p1:
                p1=x
                
    for y in range(0,len(mostp)):
           for i,x in mostp[y].items():
                  if x==p1:
                    return i
def biggest_shoe():
    largestshoe = []
    game_dict= game_dictionary.items()
    for i,x, in game_dictionary.items():
        for z,y in x['players'].items():
            dic={z:y['shoe']}
            largestshoe.append(dic)
    
    s1=0
    for y in range(0,len(largestshoe)):
        for i,x in largestshoe[y].items():
            if x>s1:
                s1=x
                
    for y in range(0,len(largestshoe)):
           for i,x in largestshoe[y].items():
                  if x==s1:
                        return i
                    
def big_shoe_rebounds():
    b = bigfest_shoe()
    for i,x, in game_dictionary.items():
        for z,y in x['players'].items():
            if z==b:
                return (y['rebounds'])
def home_team_name():
      return game_dict()['home']['team_name']
def away_team_name():
      return game_dict()['away']['team_name']

def winning_team():
    homet = 0
    awayt = 0
    for i,x, in game_dictionary.items():
        if i=='home':
            for z,y in x['players'].items():
                homet+=y['points']
        else:
            for z,y in x['players'].items():
                awayt +=y['points']
    
    if homet>awayt:
        return home_team_name()
    elif homet<awayt:
            return away_team_name()
    else:
            return "Overtime!!!"
        
def player_with_longest_name(name):
    mx=0
    for i,x, in game_dictionary.items():
        for z in (x['players']):
            if len(z)>mx:
                mx=len(z)
    if len(name)==mx:
        return True
    else:
        return False
    
#def long_name_steals_a_ton?()

def max_num_steals():
    mosteals = 0
    playersteals = None
    for i,x, in game_dictionary.items():
        for z,t in (x['players'].items()):
            if t['steals'] > mosteals:
                mosteals = t['steals']
                playersteals = z
    return  mosteals, playersteals 

def long_name_steals_a_ton():
    p_with_mosteals = max_num_steals()
    if player_with_longest_name(p_with_mosteals) ==True:
        return True
    else:
        return False
