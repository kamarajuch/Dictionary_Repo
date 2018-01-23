import s2_story4.validation as validation
import s2_story4.modify_file as modify

import sys
stop_fare=[]

#adult_max, adult_min, child_max, child_min=(60,13,12,5)
age_limits={'adult_max':0,'adult_min':0,'child_max':0, 'child_min':0}

def make_data_structure():
    with open("passenger.txt",'r') as FH:
        adult_flag = 0
        adult_list = []
        child_flag = 0
        child_list = []
        age_flag = 0
        for line in FH:
            line = line.rstrip()
            if (line == '</adult>'):
                adult_flag = 0
            elif (line == '<adult>'):
                adult_flag = 1
            elif (adult_flag == 1):
                #print("All Adult", line)
                adult_list.append(eval(line))
            elif (line == '</child>'):
                child_flag = 0
            elif (line == '<child>'):
                child_flag = 1
            elif (child_flag == 1):
                #print("All child", line)
                child_list.append(eval(line))

            elif (line == '</age_limit>'):
                age_flag = 0
            elif (line == '<age_limit>'):
                age_flag = 1
            elif (age_flag == 1):
                age_list=line.split('=')
                age_limits[age_list[0]]=age_list[1]
            else:
                #print("Wrong line")
                pass;

        #print(adult_list,child_list)

        if(len(adult_list)==(len(child_list))):
            for i in range(len(adult_list)):
                adult_child_list = []
                for adult_val,child_val in zip(adult_list[i],child_list[i]):
                    if(child_val):
                        adult_child_list.append([adult_val,child_val])
                    else:
                        adult_child_list.append(adult_val)
                stop_fare.append(adult_child_list)
        else:
            print("File formate was wrong")

    #print("FINALLY CREATED DATA STRUCTURE \n",stop_fare,age_limits)
    #sys.exit()


def adult_child_fare(price,flag):
    if(validation.user_type==1):
        #print("Need Modify",stop_fare)
        validation.modify_fare_validate()
        modify.modify_file(stop_fare,flag)

       # sys.exit()
    elif (validation.user_type == 2):
        print("Total:",price)
    else:
        print("Wrong User Input")
    validation.entry_stop, validation.exit_stop, validation.age,validation.user_type,validation.modify_fare = (0, 0, 0,0,0)


def apply_dicount():
    global stop_fare
    #print(adult_max, adult_min, child_max, child_min)
    #make_data_structure()
    #print(stop_fare)
    while True:
        stop_fare = []
        make_data_structure()
        if (validation.user_type == 0):
            validation.user_type_validate()
        if (validation.user_type == 3):
            sys.exit()
        if (validation.entry_stop == 0):
            validation.entry_validate()
        if (validation.exit_stop == 0):
            validation.exit_validate()
        if (validation.age == 0):
            validation.age_validate()
        if (int(validation.age) >= int(age_limits['adult_min'])):
            val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
            if (int(validation.age) <= int(age_limits['adult_max'])):
                if (type(val) == list):
                    adult_child_fare(val[0],1)
                else:
                    adult_child_fare(val,1)
            else:
                if (type(val) == list):
                    adult_child_fare(val[0]/2,1)
                else:
                    adult_child_fare(val/2,1)
        elif (int(validation.age) <= int(age_limits['child_max'])):
            val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
            if (int(validation.age) >= int(age_limits['child_min'])):
                if(type(val)==list):
                        if(len(val)>=2):
                            if (type(val[1]) == int):
                                adult_child_fare(val[1],2)
                            else:
                                adult_child_fare(val[0]/2,2)
                        else:
                            adult_child_fare(val[0]/2,2)
                else:
                    adult_child_fare(val/2,2)

            else:
                print("Total: 0.0/ ")
                validation.entry_stop, validation.exit_stop, validation.age,validation.user_type,validation.modify_fare = (0, 0, 0,0,0)
        else:
            print("Incorrect Entry for age")
            validation.entry_stop, validation.exit_stop, validation.age,validation.user_type,validation.modify_fare = (0, 0, 0,0,0)
