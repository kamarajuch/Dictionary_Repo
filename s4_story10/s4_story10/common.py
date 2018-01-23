import s4_story10.validation as validation
import s4_story10.modify_file as modify
import s4_story10.fare_calculation as fare_cal
import sys
stop_fare=[]

stop_fare1=[[10, [2, 'trip_disc(3,2,0.02)'], [4, 4], [5, 'trip_disc(1,2,0.2)'], [6, 6]],
     [[3, 3], 0, [8, 5, 'trip_disc(3,6,0.33)'], 3, [4, 4, 'passenger_disc(1,3,0.5)']],
     [[5, 5], [6, 6, 'passenger_disc(2,4,0.45)'], 0, 7, [2, 2]],
     [[4, 4, 'passenger_disc(1,2,0.5)'], 5, [6, 6], 0, [20, 20]], [[3, 3, 'trip_disc(1,2,0.2)'], 2, 1, [3, 3], 0]]


age_limits={'adult_max':0,'adult_min':0,'child_max':0, 'child_min':0}
passenger_travel={}
check_age=0
def config_passenger_travel(flag=0):
    global passenger_travel
    with open("passenger_travel.txt","r+") as F:
        if(flag==0):
            for line in F:
                line=line.rstrip()
                passenger_travel=eval(line)
                #print(passenger_travel)
        elif(flag==1):
            F.write(str(passenger_travel))


def passenger_disc(flag,no_time_travel,disc1):
    global check_age
    if (flag == 1):
        if ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
            return float(validation.price -(validation.price * disc1))
        else:
            return float(validation.price)
    elif(flag==2):
        if (check_age == 2) & ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
            return float(validation.price- (validation.price*disc1))
        else:
            return float(validation.price)
    elif(flag==3):
        if (check_age == 3) & ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
            return float(validation.price- (validation.price*disc1))
        else:
            return float(validation.price)

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
    global stop_fare,passenger_travel
    total=0
    flag_type=5
    while True:
        stop_fare=[]
        passenger_travel = {}
        make_data_structure()
        config_passenger_travel()
        print(passenger_travel)
        print(stop_fare)
        if (validation.user_type == 0):
            validation.user_type_validate()
        # -----------------------------------------------------------------------------------------
        # ____________________________________ADMIN PART START_______________________________________
        if (validation.user_type == 1):
            validation.validate_modify_fare()
            if(validation.disc_type_modify==3):
                validation.all_age_val()
                age_limits['child_min']=validation.child_min_age
                age_limits['child_max'] = validation.adult_min_age-1
                age_limits['adult_min']=validation.adult_min_age
                age_limits['adult_max']=validation.senior_min_age-1
                modify.modify_file(4, age_limits)
            elif (validation.disc_type_modify == 4):
                sys.exit()
            else:
                validation.entry_validate()
                validation.exit_validate()
                if (validation.entry_stop == validation.exit_stop):
                    print("Please Enter entry and exit stop different to modify")
                    flag_type = validation.user_type
                   # flag1=validation.disc_type_modify
                    make_default_value()


                elif (validation.disc_type_modify == 1):
                    validation.adult_child_type()
                    validation.modify_fare_validate()
                    modify.modify_file(validation.child_adult, validation.modify_fare)
                elif(validation.disc_type_modify==2):
                    print("Add passenger discount")
                    validation.validate_discount_type()
                    print(validation.disc_type);
                    if(validation.disc_type==1):
                        validation.validate_trip_disc()
                        validation.validate_trip_disc_no_passenger()
                        validation.validate_trip_disc_percent()
                        values=str('trip_disc('+str(validation.disc_type_trip)+','+str(validation.trip_disc_no_passenger)+','+str(validation.trip_disc_percent)+')')
                        modify.modify_file(3, values)
                    elif(validation.disc_type==2):
                        validation.validate_trip_disc()
                        validation.validate_no_trip_count()
                        validation.validate_trip_disc_percent()
                        values =str('passenger_disc(' + str(validation.disc_type_trip)+','+str(validation.no_trip_count)+','+str(validation.trip_disc_percent) + ')')
                        modify.modify_file(3, values)
                    else:
                        print("Wrong Input")
                        sys.exit()
                else:
                    validation.user_type_validate()
    #-----------------------------------------------------------------------------------------
    #____________________________________ADMIN PART END_______________________________________
        if (validation.user_type == 2):
            validation.entry_validate()
            validation.exit_validate()
            if(validation.entry_stop == validation.exit_stop ):
                print("Please Enter entry and exit stop different")
                flag_type = validation.user_type
                make_default_value()

                print("Flag type ",flag_type,validation.user_type)
            elif (validation.no_passenger == 0):
                validation.no_of_passenger_validate()
                #print(validation.no_passenger)
                for i in range(validation.no_passenger):
                    validation.get_passenger_validate()
                    if (validation.id_passenger in passenger_travel):
                        passenger_travel[validation.id_passenger] += 1
                    else:
                        passenger_travel[validation.id_passenger] = 1
                    validation.age_validate()
                    if (float(validation.age) >= float(age_limits['adult_min'])):
                        val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
                        #print(val)
                        if (float(validation.age) <= float(age_limits['adult_max'])):
                            if (type(val) == list):
                                total1=(adult_child_fare(val[0], 2, val))
                                total=total+total1
                            else:
                                total +=adult_child_fare(val, 2, val)
                        else:
                            if (type(val) == list):
                                total +=adult_child_fare(val[0] / 2, 2, val)
                            else:
                                total +=adult_child_fare(val / 2, 2, val)
                    elif (float(validation.age) <= float(age_limits['child_max'])):
                        val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
                        if (float(validation.age) >= float(age_limits['child_min'])):
                            if (type(val) == list):
                                if (len(val) >= 2):
                                    if (type(val[1]) == int):
                                        total +=adult_child_fare(val[1], 3, val)
                                    else:
                                        total +=adult_child_fare(val[0] / 2, 3, val)
                                else:
                                    total +=adult_child_fare(val[0] / 2, 3, val)
                            else:
                                total +=adult_child_fare(val / 2, 3, val)

                        else:
                            print("No Charge ")
                            #make_default_value()
                            # validation.entry_stop, validation.exit_stop, validation.age, validation.user_type, validation.modify_fare = (0, 0, 0, 0, 0)
                        #print("Total fare",total)
                    else:
                        print("Incorrect Entry for age")
                        make_default_value()
                    print("Sub total fare", total,passenger_travel)

                print("Final Total Fare :", total)
                config_passenger_travel(1)
            else:
                print("Invalid passenger")
                make_default_value()

        if (validation.user_type == 3):
            sys.exit()
        if(flag_type==5):
            make_default_value()
            total=0
        else:
            make_default_value()
            validation.user_type=flag_type;
            flag_type=5
            total = 0
        #sys.exit()


def make_default_value():
    validation.entry_stop=validation.exit_stop=validation.age=validation.user_type=validation.disc_type_trip=validation.trip_disc_no_passenger=validation.trip_disc_percent=validation.no_trip_count=validation.no_passenger=validation.id_passenger=0
        #(0, 0, 0, 0, 0)
