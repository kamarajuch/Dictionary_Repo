import story7_1.validation as validation
import story7_1.fare_calculation as fare_cal
import sys
stop_fare=[]

age_limits={'adult_max':0,'adult_min':0,'child_max':0, 'child_min':0}
check_age=0
passenger_travel={}

def trip_disc(flag1,no_passenger,disc1):
    global check_age
    if (flag1 == 1):
        if (validation.no_passenger >= no_passenger):
            return float(validation.price - (validation.price * disc1))
        else:
            return float(validation.price)
    elif (flag1 == 2):
        if (check_age == 2) & (validation.no_passenger >= no_passenger):
            return float(validation.price - (validation.price * disc1))
        else:
            return float(validation.price)
    elif (flag1 == 3):
        if (check_age == 3) & (validation.no_passenger >= no_passenger):
            return float(validation.price - (validation.price * disc1))
        else:
            return float(validation.price)

    else:
        print("Invalid Entry ")
        sys.exit()


def adult_child_fare(price,flag,val):
    global check_age
    check_age = flag;
    validation.price = price;

    if (type(val) == list):
        list1 = list(filter(lambda x: type(x) == str, val))
        if (list1):
            for func_disc in list1:
                return (eval(func_disc))
        else:
            return price
    else:
        return price

def make_data_structure():
    with open("passenger.txt",'r') as FH:
        adult_flag = 0
        adult_list = []
        child_flag = 0
        child_list = []
        disc_list =[]
        disc_flag=0
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
            elif (line == '</discount>'):
                disc_flag = 0
            elif (line == '<discount>'):
                disc_flag = 1
            elif (disc_flag  == 1):
                disc_list.append(eval(line))
            elif (line == '</age_limit>'):
                age_flag = 0
            elif (line == '<age_limit>'):
                age_flag = 1
            elif (age_flag == 1):
                age_list = line.split('=')
                age_limits[age_list[0]] = age_list[1]

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
            for index_val,dis_val in enumerate(disc_list):
                for index_val1,l in enumerate(dis_val):
                    if(l):
                        if(type(stop_fare[index_val][index_val1])== list):
                            stop_fare[index_val][index_val1].append(l)
                        else:
                            temp=stop_fare[index_val][index_val1]
                            stop_fare[index_val][index_val1]=[]
                            stop_fare[index_val][index_val1].append(temp)
                            stop_fare[index_val][index_val1].append(l)
        else:
            print("File formate was wrong")
    #print("FINALLY CREATED DATA STRUCTURE \n",stop_fare)

def apply_dicount():
    global stop_fare
    make_data_structure()
    while True:
        total = 0
        if (validation.entry_stop == 0):
            validation.entry_validate()
        if (validation.exit_stop == 0):
            validation.exit_validate()
        if (validation.entry_stop == validation.exit_stop):
            print("Please Enter entry and exit stop different")
            #flag_type = validation.user_type
            #validation.entry_stop=validation.exit_stop=0
            make_default_value()

        elif (validation.no_passenger == 0):
            validation.no_of_passenger_validate()
            #print(validation.no_passenger)
            for i in range(validation.no_passenger):
                print("Passenger:",i+1)
                validation.age_validate()
                if (float(validation.age) >= float(age_limits['adult_min'])):
                    val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
                    # print(val)
                    if (float(validation.age) <= float(age_limits['adult_max'])):
                        if (type(val) == list):
                            total1 = (adult_child_fare(val[0], 2, val))
                            total = total + total1
                        else:
                            total += adult_child_fare(val, 2, val)
                    else:
                        if (type(val) == list):
                            total += adult_child_fare(val[0] / 2, 2, val)
                        else:
                            total += adult_child_fare(val / 2, 2, val)
                elif (float(validation.age) <= float(age_limits['child_max'])):
                    val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
                    if (float(validation.age) >= float(age_limits['child_min'])):
                        #print("I came inside child")
                        if (type(val) == list):
                            if (len(val) >= 2):
                                if (type(val[1]) == int):
                                    total += adult_child_fare(val[1], 3, val)
                                else:
                                    total += adult_child_fare(val[0] / 2, 3, val)
                            else:
                                total += adult_child_fare(val[0] / 2, 3, val)
                        else:
                            total += adult_child_fare(val / 2, 3, val)

                    else:
                        print("No Charge ")
                        # make_default_value()
                        # validation.entry_stop, validation.exit_stop, validation.age, validation.user_type, validation.modify_fare = (0, 0, 0, 0, 0)
                        # print("Total fare",total)
                else:
                    print("Incorrect Entry for age")
                    make_default_value()
                #print("Sub total fare", total, passenger_travel)
            print("Final Total Fare :", total)
            make_default_value()
        else:
            print("Invalid passenger",validation.no_passenger)
    make_default_value()

def make_default_value():
    validation.entry_stop=validation.exit_stop=validation.age=validation.user_type=validation.disc_type_trip=validation.trip_disc_no_passenger=validation.trip_disc_percent=validation.no_trip_count=validation.no_passenger=validation.id_passenger=0
        #(0, 0, 0, 0, 0)