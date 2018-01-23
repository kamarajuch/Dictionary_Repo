import sprint2_2.validation as validation

#from sprint2_1.validation import entry_stop,exit_stop,age

stop_fare = [[0, [10, 6], 30, 45, 60],
                 [50, 0, [60, 40], 80, 70],
                 [80, 70, 0, [40, 20], 20],
                 [90, 30, 10, 0, 50],
                 [100, 20, 5, [60, 20], 0]
                 ]


def make_default_value():
    validation.entry_stop = validation.exit_stop = validation.age = 0

#flag=1, flag=2 indicates child adult respectively and disc=1 is default discount(divide/1 no effect)

def adult_child_fare(flag=1, disc=1):
    if (flag == 2):
        if (type(stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]) == list):
            print("Total : ", stop_fare[validation.entry_stop - 1][validation.exit_stop - 1][0] / disc)
        else:
            print("Total :", stop_fare[validation.entry_stop - 1][validation.exit_stop - 1] / disc)
    elif (flag == 1):
        if (type(stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]) == list):
            print("Total :", stop_fare[validation.entry_stop - 1][validation.exit_stop - 1][1] / disc)
        else:
            print("Total :", (stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]) / 2)
    else:
        print("Incorrect age ")
    make_default_value()


def get_fare():
    while True:
        if (validation.entry_stop == 0):
            validation.entry_validate()
        elif (validation.exit_stop == 0):
            validation.exit_validate()
        elif (validation.entry_stop == validation.exit_stop):
            print("Entry and exit stop should be different")
            make_default_value()
        elif (validation.age == 0):
            validation.age_validate()
        elif(validation.entry_stop == validation.exit_stop):
            print("Entry and exit stop should be different")
            make_default_value()
        else:
            if (validation.age >= 13):
                if (validation.age <= 60):
                    adult_child_fare(2)
                else:
                    adult_child_fare(2, 2)
            elif (validation.age <= 12):
                if (validation.age >= 5):
                    adult_child_fare(1)
                else:
                    print("Total: 0.0/ ")
                    make_default_value()
            else:
                print("Incorrect Entry for age")
                make_default_value()
