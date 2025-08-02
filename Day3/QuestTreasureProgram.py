print('''
                         ___ -___                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""
      
''')

print('Welcome to Gangga Island, Let\'s find ur treasure !\n '
      'Your Mission is to find the Treasure!\n'
      'You\'re at the cross road. Where do u want to go?\n')
quest_1 = input("\t Type 'left' or 'right'\n").lower()

if quest_1 == "left" :
    quest_2 = input(
        'You\'ve come to a lake. '
        'There is an island in the middle of the lake.\n '
        'Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n').lower()
    if quest_2 == "wait":
        quest_3 = input(
            'You arrive at the island unharmed. '
            'There is a house with 3 doors.\n '
            'One red, one yellow and one blue. '
            'Which colour do you choose?\n').lower()
        if quest_3 == "yellow":
            print("You Win, Congrats!")
        elif quest_3 == "blue":
            print(
                "Poor player, U wrong pick the door, there's a tiger gonna eat u, Game Over! ")
        elif quest_3 == "red":
            print(
                "Poor Player, u wrong pick the door, there's a bull gonna butting u, Game Over! ")
        else:
            print("Dumbass!")
    elif quest_2 == "swim":
        print("Hey Brotha ur leg eaten with crocodile, Game Over!")
    else:
        print("dumbass!")
elif quest_1 == "right":
    print("HAHA u eat with the clown. Game Over.")
else:
    print("Choose only left/right dumbass!")

