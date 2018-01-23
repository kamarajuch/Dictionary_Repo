import sprint2_1.validation as validation

stop_fare = [[0, 10, 30, 45, 60],
             [50, 0, 60, 80, 70],
             [80, 70, 0, 40, 20],
             [90, 30, 10, 0, 50],
             [100, 20, 5, 60, 0]
             ]

def make_default_value():
    validation.entry_stop=validation.exit_stop=validation.age = 0

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
        else:
            if (validation.age > 13) & (validation.age < 60):
                print("Total: ", stop_fare[validation.entry_stop - 1][validation.exit_stop - 1])
            else:
                print("Total:",(stop_fare[validation.entry_stop - 1][validation.exit_stop - 1]) / 2)
            make_default_value()  # Default value decleration

#Starting point of project
if __name__=='__main__':
    get_fare()
    #print("Total:",total)