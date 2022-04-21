import math
import time as sleep
import ev_script_2_ev as sampleEv
import stat_script_1_stat as sampleStat

atknat = 1
defnat = 1
spatknat = 1
spdefnat = 1
spdnat = 1

test = int(input("Enter 2 for EV 1 for STAT: "))
if test == 2:
    stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense" , "Speed"]
    base = [6]
    ivv = [6]
    evv = [0,0,0,0,0,0,0]
    evs = 0
    lvl = int(input("Input the level of your pokemon: "))
    if(lvl<0 or lvl>100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()

    print("Input Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input "+stat[x]+": ")))


    print("Input Iv's on each Stats")
    for y in range(1, 7):
        ivv.append(int(input("Input "+stat[y]+" Iv: ")))
        if (ivv[y] < 0 or ivv[y] > 31):
                print("You can only set Ivs from 0 to 31!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
    nature = str.lower(input("Enter Nature: "))
    #Neutral Nature
    if nature in ['quirky','bashful','serious','docile','hardy']:
        atknat = 1
        defnat = 1
        spatknat = 1
        spdefnat = 1
        spdnat = 1
    #Attack bonus
    elif nature in ['lonely','brave','adamant','naughty']:
        atknat = 1.1
        if nature in ['lonely']:
            defnat = 0.9
        elif nature in ['brave']:
            spdnat = 0.9
        elif nature in ['adamant']:
            spatknat = 0.9
        elif nature in ['naughty']:
            spdefnat = 0.9
    #Defense bonus
    elif nature in ['bold','relaxed','impish','lax']:
        defnat = 1.1
        if nature in ['bold']:
            atknat = 0.9
        elif nature in ['relaxed']:
            spdnat = 0.9
        elif nature in ['impish']:
            spatknat = 0.9
        elif nature in ['lax']:
            spdefnat = 0.9
    #Speed bonus
    elif nature in ['timid','hasty','jolly','naive']:
        spdnat = 1.1
        if nature in ['timid']:
            atknat = 0.9
        elif nature in ['hasty']:
            defnat = 0.9
        elif nature in ['jolly']:
            spatknat = 0.9
        elif nature in ['naive']:
            spdefnat = 0.9
    #Special Attack bonus
    elif nature in ['modest','mild','quiet','rash']:
        spatknat = 1.1
        if nature in ['modest']:
            atknat = 0.9
        elif nature in ['mild']:
            defnat = 0.9
        elif nature in ['quiet']:
            spdnat = 0.9
        elif nature in ['rash']:
            spdefnat = 0.9
    #Special Defense bonus
    elif nature in ['calm','gentle','sassy','careful']:
        spdefnat = 1.1
        if nature in ['calm']:
            atknat = 0.9
        elif nature in ['gentle']:
            defnat = 0.9
        elif nature in ['sassy']:
            spdnat = 0.9
        elif nature in ['careful']:
            spatknat = 0.9
    
    opt = int(input(" [1] Attack \n [2] Defense \n [3] Special Attack \n [4] Special Defense \n [5] Speed "))
    if opt == 1:
        mod = atknat
    elif opt == 2:
        mod = defnat
    elif opt == 3:
        mod = spatknat
    elif opt == 4:
        mod = spdefnat
    elif opt == 5:
        mod = spdnat

    des = int(input("Enter desired increase: "))

    d = ((2*base[opt+1]+ivv[opt+1]+(evv[opt+1]/4))*lvl/100)

    tot = ((((des/mod)-(d))*400/lvl)/4)*4

    print("This is the amount of needed Ev for your pokemon "+tot)
    
elif test == 1:
    pokemon = str(input("Enter Pokemon: "))
    lvl = int(input("Enter level: "))
    nature = str.lower(input("Enter Nature: "))
    #Neutral Nature
    if nature in ['quirky','bashful','serious','docile','hardy']:
        atknat = 1
        defnat = 1
        spatknat = 1
        spdefnat = 1
        spdnat = 1
    #Attack bonus
    elif nature in ['lonely','brave','adamant','naughty']:
        atknat = 1.1
        if nature in ['lonely']:
            defnat = 0.9
        elif nature in ['brave']:
            spdnat = 0.9
        elif nature in ['adamant']:
            spatknat = 0.9
        elif nature in ['naughty']:
            spdefnat = 0.9
    #Defense bonus
    elif nature in ['bold','relaxed','impish','lax']:
        defnat = 1.1
        if nature in ['bold']:
            atknat = 0.9
        elif nature in ['relaxed']:
            spdnat = 0.9
        elif nature in ['impish']:
            spatknat = 0.9
        elif nature in ['lax']:
            spdefnat = 0.9
    #Speed bonus
    elif nature in ['timid','hasty','jolly','naive']:
        spdnat = 1.1
        if nature in ['timid']:
            atknat = 0.9
        elif nature in ['hasty']:
            defnat = 0.9
        elif nature in ['jolly']:
            spatknat = 0.9
        elif nature in ['naive']:
            spdefnat = 0.9
    #Special Attack bonus
    elif nature in ['modest','mild','quiet','rash']:
        spatknat = 1.1
        if nature in ['modest']:
            atknat = 0.9
        elif nature in ['mild']:
            defnat = 0.9
        elif nature in ['quiet']:
            spdnat = 0.9
        elif nature in ['rash']:
            spdefnat = 0.9
    #Special Defense bonus
    elif nature in ['calm','gentle','sassy','careful']:
        spdefnat = 1.1
        if nature in ['calm']:
            atknat = 0.9
        elif nature in ['gentle']:
            defnat = 0.9
        elif nature in ['sassy']:
            spdnat = 0.9
        elif nature in ['careful']:
            spatknat = 0.9

    opt = int(input(" [1] HP \n [2] Attack \n [3] Defense \n [4] Special Attack \n [5] Special Defense \n [6] Speed \n [0] All \nCalculate: "))
    if opt == 1:
        basehp = int(input("Enter base HP: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))
        print("Total HP: ", sampleStat.SampleClassStat.hpReturn(basehp,iv,ev,lvl), end='\n\n')
    elif opt == 2:
        baseatk = int(input("Enter base Attack: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))        
        print("Total Attack: ", sampleStat.SampleClassStat.attackReturn(baseatk,iv,ev,lvl,atknat), end='\n\n')
    elif opt == 3:
        basedef = int(input("Enter base Defense: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))        
        print("Total Defense: ", sampleStat.SampleClassStat.defenseReturn(basedef,iv,ev,lvl,defnat), end='\n\n')
    elif opt == 4:
        basespatk = int(input("Enter base Special Attack: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))        
        print("Total Special Attack: ", sampleStat.SampleClassStat.spattackReturn(basespatk,iv,ev,lvl,spatknat), end='\n\n')    
    elif opt == 5:
        basespdef = int(input("Enter base Special Defense: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))  
        print("Total Special Defense: ", sampleStat.SampleClassStat.spdefenseReturn(basespdef,iv,ev,lvl,spdefnat), end='\n\n')
    elif opt == 6:
        basespd = int(input("Enter base Speed: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))
        print("Total Speed: ", sampleStat.SampleClassStat.speedReturn(basespd,iv,ev,lvl,spdnat), end='\n\n')
    elif opt == 0:
        
        basehp = int(input("Enter base HP: "))
        baseatk = int(input("Enter base Attack: "))
        basedef = int(input("Enter base Defense: "))
        basespatk = int(input("Enter base Special Attack: "))
        basespdef = int(input("Enter base Special Defense: "))
        basespd = int(input("Enter base Speed: "))
        iv = int(input("Enter IV: "))
        ev = int(input("Enter EV: "))
        print("HP: ", sampleStat.SampleClassStat.hpReturn(basehp,iv,ev,lvl))
        print("Attack: ", sampleStat.SampleClassStat.attackReturn(baseatk,iv,ev,lvl,atknat))
        print("Defense: ", sampleStat.SampleClassStat.defenseReturn(basedef,iv,ev,lvl,defnat))
        print("Speocial Attack: ", sampleStat.SampleClassStat.spattackReturn(basespatk,iv,ev,lvl,spatknat))
        print("Special Defense: ", sampleStat.SampleClassStat.spdefenseReturn(basespdef,iv,ev,lvl,spdefnat))
        print("Speed: ", sampleStat.SampleClassStat.speedReturn(basespd,iv,ev,lvl,spdnat))
