import sys
import random as r
number=[' 6',' 7',' 8',' 9','10',' в',' д',' к',' т']
class card:
    num=''
    type=''
    pass
class table1:
    enemy_hand=[]
    you_hand=[]
    enemy_table=[]
    you_table=[]
    deck=[]
    koz=''
    pass
def creating_cards():
    a=[]
    for h in ' 6', ' 7', ' 8', ' 9','10', ' в', ' д', ' к', ' т':
        for k in '♠', '♣', '♦', '♥':
            cardd=card()
            cardd.num=h
            cardd.type=k
            a.append(cardd)
    return(a)
def shufling(a):
    b=[]
    for i in range(36):
        rand=r.randint(0,len(a)-i-1)
        b.append(a[rand])
        for j in range(rand,len(a)-i-1):
            a[j]=a[j+1]
    return(b)
def taking_card():
    global table
    card_one=table.deck[0]
    deck_new=[]
    for i in range(1,len(table.deck)):
        deck_new.append(table.deck[i])
    table.deck=deck_new
    return(card_one)
#==============================================================================================================================================    
def show_table():
    print('      ',end='')
    for i in range(len(table.enemy_hand)):
##        if table.enemy_hand[i].type in ['♦', '♥']:
##            print('['+table.enemy_hand[i].num+' '+table.enemy_hand[i].type+']',end='',file=sys.stderr)
##        else:
##            print('['+table.enemy_hand[i].num+' '+table.enemy_hand[i].type+']',end='')
        print('[    ]',end='')
    print()
    print()
#----------enemy_table--------------------
    if table.enemy_table==[]:
        print('  '+str(len(table.deck)))
    else:
        if len(table.deck)//10!=0:                         # |
            print('  '+str(len(table.deck))+'  ',end='')   #/ кол-во карт в колоде
        else:                                              #\ 
            print('   '+str(len(table.deck))+'  ',end='')  # |
        for i in range(len(table.enemy_table)):
            if table.enemy_table[i].type in ['♦', '♥']:
                print('['+table.enemy_table[i].num+' '+table.enemy_table[i].type+']', end='',file=sys.stderr)
            else:
                 print('['+table.enemy_table[i].num+' '+table.enemy_table[i].type+']', end='')
        print()
#-----------you_table------------------------
    if table.you_table==[]:
        try:                                                                                                                    #_
            if table.deck[len(table.deck)-1].type in ['♦', '♥']:                                                                # \
                print('['+table.deck[len(table.deck)-1].num+' '+table.deck[len(table.deck)-1].type+']', end='',file=sys.stderr) # | 
            else:                                                                                                               # |
                print('['+table.deck[len(table.deck)-1].num+' '+table.deck[len(table.deck)-1].type+']', end='')                 #  \    
        except IndexError:                                                                                                      #   \   вывод козырной карты
            print('[    ]', end='')                                                                                                     #   /
    else:                                                                                                                       #  /
        try:                                                                                                                    # |
            if table.deck[len(table.deck)-1].type in ['♦', '♥']:                                                                # |
                print('['+table.deck[len(table.deck)-1].num+' '+table.deck[len(table.deck)-1].type+']', end='',file=sys.stderr) # |
            else:                                                                                                               #_/
                print('['+table.deck[len(table.deck)-1].num+' '+table.deck[len(table.deck)-1].type+']', end='')                 #
        except IndexError:
            print('[    ]', end='')
        for i in range(len(table.you_table)):
            if table.you_table[i].type in ['♦', '♥']:
                print('['+table.you_table[i].num+' '+table.you_table[i].type+']', end='',file=sys.stderr)
            else:
                print('['+table.you_table[i].num+' '+table.you_table[i].type+']', end='')
    print()
    print()
    print('      ',end='')
    for i in range(len(table.you_hand)):
        if table.you_hand[i].type in ['♦', '♥']: 
            print('['+table.you_hand[i].num+' '+table.you_hand[i].type+']', end='',file=sys.stderr)
        else:
            print('['+table.you_hand[i].num+' '+table.you_hand[i].type+']', end='')
    print()
    print('      ',end='')
    for i in range(len(table.you_hand)):
        if len(str(i))==1:
            print('   '+str(i+1)+'  ',end='')
        else:
            print('  '+str(i+1)+'',end='')
    print()
def cleaning(hand,i):
    hand_new=[]
    if i>=0:
        for j in range(i):
            hand_new.append(hand[j])
        for j in range(i+1,len(hand)):
            hand_new.append(hand[j])
    return(hand_new)
#===================================================================================================================================================        
def you_turn(type):
    if (len(table.enemy_table)==0) and type==1:
        action=0
        while (action<=0) or (action>len(table.you_hand)):
            try:
                action=int(input())
            except ValueError:
                print('ошибка')
        action-=1
        table.you_table.append(table.you_hand[action])
        table.you_hand=cleaning(table.you_hand,action)
    else:
        if type==2:
            action=-2
            check=1
            while (action<-1) or (action>=len(table.you_hand)) or (check==1):
                bul=1
                try:
                    action=int(input())
                    action-=1
                except ValueError:
                    print('ошибка')
                    bul=0
                try:
                    if (action==-1) or ((bul==1) and ((table.you_hand[action].type==table.enemy_table[len(table.enemy_table)-1].type) and
                                                                          (number.index(table.you_hand[action].num)>number.index(table.enemy_table
                                                                                                                                 [len(table.enemy_table)-1].num)) or ((table.you_hand[action].type==table.koz) and (table.enemy_table[len(table.enemy_table)-1].type!=table.koz)))):
                        check=0
                except IndexError:
                    print('неверный ход')
            if action!=-1:
                table.you_table.append(table.you_hand[action])
                table.you_hand=cleaning(table.you_hand,action)
        else:
            if type==1:
                action=-1
                check=1
                mass_check=[]
                for i in range(len(table.enemy_table)):
                    mass_check.append(table.enemy_table[i].num)
                for i in range(len(table.you_table)):
                    mass_check.append(table.you_table[i].num)
##                for i in range(len(mass_check)):
##                    print(mass_check[i])
                while (action<-1) or (action>=len(table.you_hand)) or (check==1):
                    try:
                        action=int(input())
                        action-=1
                    except ValueError:
                        print('ошибка')
                        action=-2
                    if action!=-1:
                        try:
                            if mass_check.index(table.you_hand[action].num)>=0:
                                check=0
                        except ValueError :
                            check=1
                        except IndexError:
                            check=1
                    else:
                        check=0
                if action!=-1:
                    table.you_table.append(table.you_hand[action])
                    table.you_hand=cleaning(table.you_hand,action)
    return(action)
#==============================================================================================================================================================
def enemy_turn(type):
    if (len(table.you_table)==0) and type==1:
        min_counter=table.enemy_hand[0].num
        action=0
        for i in range(1,len(table.enemy_hand)):
            if (number.index(min_counter)>number.index(table.enemy_hand[i].num)) and (table.enemy_hand[i].type!=table.koz):
                min_counter=table.enemy_hand[i].num
                action=i
        table.enemy_table.append(table.enemy_hand[action])
        table.enemy_hand=cleaning(table.enemy_hand,action)
    else:
        if type==1:
            action=-1
            i=0
            check=1
            mass_check=[]
            min_el=' т'
            for i in range(len(table.enemy_table)):
                mass_check.append(table.enemy_table[i].num)
            for i in range(len(table.you_table)):
                mass_check.append(table.you_table[i].num)
            for i in range(len(table.enemy_hand)):
                try:
                    b=mass_check.index(table.enemy_hand[i].num)
                    if (number.index(min_el)>=number.index(table.enemy_hand[i].num)) and (table.enemy_hand[i].type!=table.koz):
                        min_el=table.enemy_hand[i].num
                        action=i
                except  ValueError:
                    b=0
            if action==-1:
                min_el=' т'
                for i in range(len(table.enemy_hand)):
                    try:
                        b=mass_check.index(table.enemy_hand[i])
                        if (number.index(min_el)>=number.index(table.enemy_hand[i].num)) and (table.enemy_hand[i].type==table.koz):
                            min_el=table.enemy_hand[i].num
                            action=i
                    except  ValueError:
                        b=0
            if action!=-1:
                table.enemy_table.append(table.enemy_hand[action])
                table.enemy_hand=cleaning(table.enemy_hand,action)       
        else:
            if type==2:
                check=1
                min_counter=' т'
                action=-1
                for i in range(len(table.enemy_hand)):
                    if (table.enemy_hand[i].type==table.you_table[len(table.you_table)-1].type) and(number.index(table.enemy_hand[i].num)>number.index(table.you_table[len(table.you_table)-1].num))and (number.index(table.enemy_hand[i].num)<=number.index(min_counter)):
                        min_counter=table.enemy_hand[i].num
                        action=i
                if (action==-1) and (table.you_table[len(table.you_table)-1].type!=table.koz):
                    min_counter=' т'
                    for i in range(len(table.enemy_hand)):
                        if (table.enemy_hand[i].type==table.koz) and (number.index(table.enemy_hand[i].num)<=number.index(min_counter)):
                            min_counter=table.enemy_hand[i].num
                            action=i
                if action!=-1:
                    table.enemy_table.append(table.enemy_hand[action])
                    table.enemy_hand=cleaning(table.enemy_hand,action)                     
    return(action)
#===================================================================================================================================================
def you_turns():
    global table
    bul=0
    while bul==0:
        show_table()
        if you_turn(1)==-1:
            bul=2
            print('бито')
            table.enemy_table=cleaning(table.enemy_table,-1)
            table.you_table=cleaning(table.you_table,-1)
            if len(table.you_hand)<6:
                if len(table.deck)<=(6-len(table.you_hand)):
                    for i in range(len(table.deck)):
                        table.you_hand.append(taking_card())
                else:
                    for i in range(6-len(table.you_hand)):
                        table.you_hand.append(taking_card())
            if len(table.enemy_hand)<6:
                if len(table.deck)<=(6-len(table.enemy_hand)):
                    for i in range(len(table.deck)):
                        table.enemy_hand.append(taking_card())
                else:
                    for i in range(6-len(table.enemy_hand)):
                        table.enemy_hand.append(taking_card())
        else:
            if enemy_turn(2)==-1:
                bul=1
                print('противник забирает карты')
                for i in range(len(table.enemy_table)):
                    table.enemy_hand.append(table.enemy_table[i])
                for i in range(len(table.you_table)):
                    table.enemy_hand.append(table.you_table[i])
                table.enemy_table=[]
                table.you_table=[]
                if len(table.you_hand)<6:
                    if len(table.deck)<=(6-len(table.you_hand)):
                        for i in range(len(table.deck)):
                            table.you_hand.append(taking_card())
                    else:
                        for i in range(6-len(table.you_hand)):
                            table.you_hand.append(taking_card())
    return(bul)
#==============================================================================================================================
def enemy_turns():
    global table
    bul=0
    while bul==0:
        if enemy_turn(1)==-1:
            bul=1
            print('бито')
            table.enemy_table=cleaning(table.enemy_table,-1)
            table.you_table=cleaning(table.you_table,-1)
            if len(table.enemy_hand)<6:
                if len(table.deck)<=(6-len(table.enemy_hand)):
                    for i in range(len(table.deck)):
                        table.enemy_hand.append(taking_card())
                else:
                    for i in range(6-len(table.enemy_hand)):
                        table.enemy_hand.append(taking_card())
            if len(table.you_hand)<6:
                if len(table.deck)<=(6-len(table.you_hand)):
                    for i in range(len(table.deck)):
                        table.you_hand.append(taking_card())
                else:
                    for i in range(6-len(table.you_hand)):
                        table.you_hand.append(taking_card())
        else:
            show_table()
            if you_turn(2)==-1:
                bul=2
                print('вы забираете карты')
                for i in range(len(table.enemy_table)):
                    table.you_hand.append(table.enemy_table[i])
                for i in range(len(table.you_table)):
                    table.you_hand.append(table.you_table[i])
                table.enemy_table=[]
                table.you_table=[]
                if len(table.enemy_hand)<6:
                    if len(table.deck)<=(6-len(table.enemy_hand)):
                        for i in range(len(table.deck)):
                            table.enemy_hand.append(taking_card())
                    else:
                        for i in range(6-len(table.enemy_hand)):
                            table.enemy_hand.append(taking_card())
    return(bul)
#==================================
def right_turn(bul):
    if bul==1:
        bul2=you_turns()
    else:
        bul2=enemy_turns()
    return(bul2)
#====================================
def game():
    global table
    koz_min1=10
    for i in range(len(table.you_hand)):
        if (table.you_hand[i].type==table.koz) and (number.index(table.you_hand[i].num)<=koz_min1):
            koz_min1=number.index(table.you_hand[i].num)
    koz_min2=11
    for i in range(len(table.enemy_hand)):
        if (table.enemy_hand[i].type==table.koz) and (number.index(table.enemy_hand[i].num)>=koz_min2):
            koz_min2=number.index(table.enemy_hand[i].num)
    if koz_min1<koz_min2:
        bulean=1
    else:
        bulean=2
    while not((len(table.deck)<=0) and ((len(table.you_hand)<=0) or (len(table.enemy_hand)<=0))):
        if bulean==1:
            print('ваш ход')
        else:
            print('ход противника')
        bulean=right_turn(bulean)
    if len(table.you_hand)==len(table.enemy_hand)==0:
        print('ничья')
    else:
        if len(table.enemy_hand)==0:
            print('вы проиграли')
        else:
            print('вы победили')
#===================================
table=table1()
table.deck=creating_cards()
table.deck=shufling(table.deck)
table.koz=table.deck[35].type
for i in range(12):
    if i%2==0:
        table.you_hand.append(taking_card())
    else:
        table.enemy_hand.append(taking_card())
print('игра дурак (не переводной) правила такие же как и в обычной')
print('карточной игре')
print('игра идет последовательно, т.е. карты выкладываются друг за другом:')
print('атака - отбитие')
print('чтобы сыграть карту, ввидите ее номер в консоль')
print('(номера указываются непосредственно под картами)')
print('чтобы завершить ход введите "0"')
print('чтобы начать игру введите что-нибудь')
input()
game()
##show_table()
##you_turn(1)
##enemy_turn(2)
##show_table()
##you_turn(1)
##enemy_turn(2)
##show_table()
##you_turn(1)
##enemy_turn(2)
##show_table()
