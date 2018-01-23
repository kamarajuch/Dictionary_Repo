import story4_9.validation as validation

def cal_disc(flag,no_time_travel,disc1,passenger_travel,check_age):

    if (flag == 1):
        if ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)
    elif ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
        if (check_age == 2) & ((passenger_travel[validation.id_passenger] % no_time_travel) == 0):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)

    validation.entry_stop, validation.exit_stop, validation.age, validation.no_passenger,validation.id_passenger = (0, 0, 0, 0,0)


def cal_trip_disc(flag,no_passenger,disc1,check_age):
    if (flag == 1):
        if (validation.no_passenger > no_passenger):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)
    elif (flag == 2):
        if (check_age == 1) & (validation.no_passenger > no_passenger):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)

    else:
        if (check_age == 2) & (validation.no_passenger > no_passenger):
            total = validation.price * validation.no_passenger
            print("Total:", total - (total * disc1))
        else:
            print("Total:", validation.price * validation.no_passenger)
    validation.entry_stop, validation.exit_stop, validation.age, validation.no_passenger, validation.id_passenger = (
    0, 0, 0, 0, 0)