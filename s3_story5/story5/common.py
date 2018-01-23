import sys;
import story5.validation as validation

stop_fare = [[0, [10, 6], [10,8,'trip_disc(3,2,0.5)'], 45, 60],
             [50, 0, [60, 40], 80, 70],
             [80, 70, 0, [40, 20,'trip_disc(2,2,0.2)'], 20],
             [[90,'trip_disc(3,2,0.2)'], 30, 10, 0, 50],
             [100, 20, 5, [60, 20], 0]
             ]


#adult_max, adult_min, child_max, child_min=(60,13,12,5)
age_limits={'adult_max':60,'adult_min':13,'child_max':12, 'child_min':5}

# type1 On total adult or child discount
check_age=0

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
'''
def trip_disc(flag,type1,disc1):
    global check_age
    if(flag==1):
        if(validation.no_passenger>2):
            total=validation.price*validation.no_passenger
            print("Total:",total-(total*disc1))
        else:
            print("Total:",validation.price*validation.no_passenger)
    elif(flag==2):
        if (check_age == 1) & (validation.no_passenger > 2):
            total = validation.price * validation.no_passenger
            print("Total1:", total - (total * disc1))
        else:
            print("Total2:", validation.price * validation.no_passenger)

    else:
        if (check_age == 2) & (validation.no_passenger > 2):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)
'''

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

def apply_dicount():
    #global adult_max, adult_min, child_max, child_min
    total=0

    if (validation.entry_stop == 0):
        validation.entry_validate()
    if (validation.exit_stop == 0):
        validation.exit_validate()

    if (validation.entry_stop == validation.exit_stop):
        print("Please Enter entry and exit stop different")
        flag_type = validation.user_type
        #make_default_value()
        validation.entry_stop=validation.exit_stop=0
        #print("Flag type ", flag_type, validation.user_type)
    elif (validation.no_passenger == 0):
        validation.no_of_passenger_validate()
        # print(validation.no_passenger)
        for i in range(validation.no_passenger):
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
                #make_default_value()

            #print("Sub total fare", total, passenger_travel)

        print("Final Total Fare :", total)
        #config_passenger_travel(1)
    else:
        print("Invalid passenger")
        #make_default_value()

    '''
    if(validation.no_passenger==0):
        validation.no_of_passenger_validate()
    if (int(validation.age) >= int(adult_min)):
        val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
        if (int(validation.age) <= int(adult_max)):
            if (type(val) == list):
                adult_child_fare(val[0],1,val)
            else:
                adult_child_fare(val, 1, val)
        else:
            if (type(val) == list):
                adult_child_fare(val[0]/2,1,val)
            else:
                adult_child_fare(val/2, 1, val)
    elif (int(validation.age) <= int(child_max)):
        val = stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]
        if (int(validation.age) >= int(child_min)):
            if(type(val)==list):
                    if(len(val)>=2):
                        if (type(val[1]) == int):
                            adult_child_fare(val[1],2,val)
                        else:
                            adult_child_fare(val[0]/2,2,val)
                    else:
                        adult_child_fare(val[0]/2,2,val)
            else:
                adult_child_fare(val/2, 2, val)

        else:
            print("Total: 0.0/ ")
            validation.entry_stop, validation.exit_stop, validation.age,validation.no_passenger = (0, 0, 0,0)
    else:
        print("Incorrect Entry for age")
    '''
