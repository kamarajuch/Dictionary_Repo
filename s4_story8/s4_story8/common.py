import s4_story8.validation as validation
import sys
stop_fare = [[0, [10, 6], [30,'trip_disc(1,2,0.2)'], 45, 60],
             [50, 0, [60, 40], 80, 70],
             [80, [70,'passenger_disc(1,2,0.5)'], 0, [40,20,30,'trip_disc(2,2,0.2)'], 20],
             [[90,'trip_disc(1,2,0.2)'], 30, 10, 0, [50,'passenger_disc(2,3,0.5)']],
             [100, 20, 5, [60, 20], 0]
             ]

#adult_max, adult_min, child_max, child_min=(60,13,12,5)
age_limits={'adult_max':60,'adult_min':13,'child_max':12, 'child_min':5}

check_age=0
passenger_travel={}

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


def apply_dicount():
    global adult_max, adult_min, child_max, child_min
    while True:
        total=0
        if (validation.entry_stop == 0):
            validation.entry_validate()
        if (validation.exit_stop == 0):
            validation.exit_validate()
        if (validation.entry_stop == validation.exit_stop):
            print("Please Enter entry and exit stop different")
            make_default_value()
        elif (validation.no_passenger == 0):
            validation.no_of_passenger_validate()
            #print(validation.no_passenger)
            for i in range(validation.no_passenger):
                validation.get_passenger_validate()
                if (validation.id_passenger in passenger_travel):
                    passenger_travel[validation.id_passenger] += 1
                else:
                    passenger_travel[validation.id_passenger] = 1
                print("Passenger:", i + 1)
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
                print("Sub total fare", total)

            print("Final Total Fare :", total)
            make_default_value()
            #config_passenger_travel(1)
        else:
            print("Invalid passenger")
            make_default_value()

    make_default_value()

def make_default_value():
    validation.entry_stop=validation.exit_stop=validation.age=validation.user_type=validation.disc_type_trip=validation.trip_disc_no_passenger=validation.trip_disc_percent=validation.no_trip_count=validation.no_passenger=validation.id_passenger=0
        #(0, 0, 0, 0, 0)
