#This function will validate source point
import sys;

price=0
entry_stop,exit_stop, age,no_passenger,id_passenger,user_type,modify_fare,disc_type =(0,0,0,0,0,0,0,0)
disc_type_trip,trip_disc_no_passenger,trip_disc_percent,no_trip_count=(0,0,0,0)
disc_type_modify=0;
adult_child=0
child_min_age,adult_min_age,senior_min_age=(0,0,0)
def entry_validate():
    #print(mn.entry_stop)
    global entry_stop
    entry_stop=input("Please Enter entery stop from 1 to 5");

    if(entry_stop.isdigit()):
        entry_stop = int(entry_stop)
        if((entry_stop >=6)|(entry_stop <=0)):
            print("Wrong entry stop...")
            entry_validate()
        return entry_stop;
    else:
        print("Please enter stop in digits ")
        entry_validate()

#This function will validate destination point

def exit_validate():
    global exit_stop
    exit_stop = input("Please Enter exit stop from 1 to 5");
    if (exit_stop.isdigit()):
        exit_stop = int(exit_stop)
        if ((exit_stop >= 6) | (exit_stop <= 0)):
            print("Wrong exit stop...")
            exit_validate()
        return exit_stop;
    else:
        print("Please enter stop in digits ")
        exit_validate()


#This function will validate age from (0 to 110)
def child_age_validation():
    global child_min_age
    child_min_age = input("Please Enter minimum age of child:");
    if (child_min_age.isdigit()):
        child_min_age = int(child_min_age)
        if (child_min_age <= 0):
            print("Please enter child age greater than 0 ")
            child_age_validation()
    else:
        print("Please enter child age in digits ")
        child_age_validation()
def adult_age_validation():
    global child_min_age,adult_min_age,senior_min_age
    adult_min_age = input("Please Enter minimum age of adult:");
    if (adult_min_age.isdigit()):
        adult_min_age = int(adult_min_age)
        if ((adult_min_age <= 0) | ((adult_min_age <= child_min_age))):
            print("Please enter adult age greater than child age ")
            adult_age_validation()
    else:
        print("Please enter adult age in digits ")
        adult_age_validation()

def senior_age_validation():
    global child_min_age,adult_min_age,senior_min_age
    senior_min_age = input("Please Enter minimum age of senior citizen:");
    if (senior_min_age.isdigit()):
        senior_min_age = int(senior_min_age)
        if ((senior_min_age <= 0) | (senior_min_age <= adult_min_age) | (senior_min_age >=121)):
            print("Please enter age of senior citizen is less than 121 and greater than adult age")
            senior_age_validation()
    else:
        print("Please enter senior citizen age in digits ")
        senior_age_validation()

def all_age_val():
    global child_min_age,adult_min_age,senior_min_age
    child_age_validation()
    adult_age_validation()
    senior_age_validation()

    '''
    if(child_min_age<=0):
        child_min_age=input("Please Enter minimum age of child:");
        if (child_min_age.isdigit()):
            child_min_age = int(child_min_age)
            if (child_min_age <= 0):
                all_age_validation()
        else:
            all_age_validation()
    if ((adult_min_age <= 0) | ((adult_min_age <= child_min_age))):
        adult_min_age = input("Please Enter minimum age of adult:");
        if (adult_min_age.isdigit()):
            adult_min_age = int(adult_min_age)
            if ((adult_min_age <= 0)|((adult_min_age <= child_min_age))):
                all_age_validation()
        else:
            all_age_validation()
    if ((senior_min_age <= 0) | ((senior_min_age <= adult_min_age))):
        senior_min_age = input("Please Enter minimum age of senior citizen:");
        if (senior_min_age.isdigit()):
            senior_min_age = int(senior_min_age)
            if ((senior_min_age <= 0)|((senior_min_age <= adult_min_age))):
                all_age_validation()
        else:
            all_age_validation()
    if((child_min_age<=0) | (adult_min_age <= child_min_age) | (senior_min_age >=121)):
        child_min_age, adult_min_age, senior_min_age=(0,0,0)
        print("Please enter age of child > 0 and senior citizen age <121 ")
        all_age_validation()
    return ;
    '''

def age_validate():
    global age
    age = input("Please Enter the age of passenger");
    if (age.isdigit()):
        age = int(age)
        if ((age >= 110) | (age <= 0)):
            print("Age must be in between 1 to 110")
            age_validate()
        return age;
    else:
        print("Please enter age in digits ")
        age_validate()


def no_of_passenger_validate():
    global no_passenger
    no_passenger = input("Please Enter the no. of passenger");
    if (no_passenger.isdigit()):
        no_passenger = int(no_passenger)
        if (no_passenger <= 0):
            print("Please enter no. of passenger greater than zero (0)")
            no_of_passenger_validate()
        return no_passenger;
    else:
        print("Please enter no. of passenger in digits ")
        no_of_passenger_validate()

def get_passenger_validate():
    global id_passenger
    id_passenger = input("Please Enter the passenger Id");
    if (id_passenger.isdigit()):
        id_passenger = int(id_passenger)
        if (id_passenger <= 0):
            print("Please enter passenger ID greater than zero (0)")
            get_passenger_validate()
        return no_passenger;
    else:
        print("Please enter passenger ID in digits ")
        get_passenger_validate()
def user_type_validate():
    global user_type
    user_type = input("Please Enter Admin:1 User:2 Exit:3");
    if (user_type.isdigit()):
        user_type = int(user_type)
        if ((user_type == 1) | (user_type == 2)| (user_type == 3)):
            return user_type;
        print("Please enter below option...")
        user_type_validate()
    else:
        print("Please enter options in digits ")
        user_type_validate()

def modify_fare_validate():
    global modify_fare
    modify_fare = input("Please Enter fare to modify");
    if (modify_fare.isdigit()):
        modify_fare = int(modify_fare)
        if ((modify_fare >= 1)):
            return modify_fare;
        print("Please enter fare greater than one ")
        modify_fare_validate()
    else:
        print("Please enter fare in digits ")
        modify_fare_validate()

def validate_discount_type():
    global disc_type
    disc_type = input("Please Enter Trip Discount:1 Passenger Discount:2");
    if (disc_type.isdigit()):
        disc_type = int(disc_type)
        if ((disc_type == 1) | (disc_type == 2)):
            return disc_type;
        print("Please enter below option... ")
        validate_discount_type()
    else:
        print("Please enter option in digits ")
        validate_discount_type()


def validate_trip_disc():
    global disc_type_trip

    disc_type_trip = input("Please Enter Discount On Total:1 Adult:2 Child:3");
    if (disc_type_trip.isdigit()):
        disc_type_trip = int(disc_type_trip)
        if ((disc_type_trip == 1) | (disc_type_trip == 2)| (disc_type_trip == 3)):
            return disc_type_trip;
        print("Please enter below option... ")
        validate_trip_disc()
    else:
        print("Please enter option in digits ")
        validate_trip_disc()

def validate_trip_disc_no_passenger():
    global trip_disc_no_passenger
    trip_disc_no_passenger = input("Please enter minimum number of  passenger to get discount");
    if (trip_disc_no_passenger.isdigit()):
        trip_disc_no_passenger = int(trip_disc_no_passenger)
        if ((trip_disc_no_passenger >= 1)):
            return trip_disc_no_passenger;
        print("Please enter no. of passenger greater than one ")
        validate_trip_disc_no_passenger()
    else:
        print("Please enter no. of passenger in digits")
        validate_trip_disc_no_passenger()

def validate_trip_disc_percent():
    global trip_disc_percent;
    trip_disc_percent = input("Please enter percentage (1 to 99)");
    if (trip_disc_percent.isdigit()):
        trip_disc_percent = int(trip_disc_percent)
        if ((trip_disc_percent >= 1) & (trip_disc_percent <= 99)):
            trip_disc_percent=(trip_disc_percent/100)
            return trip_disc_percent;
        print("Please enter percentage in between 1 to 99 ")
        validate_trip_disc_percent()
    else:
        print("Please enter percentage in digits...")
        validate_trip_disc_percent()

def validate_no_trip_count():
    global no_trip_count
    no_trip_count = input("Please enter minimum no. of travel");
    if (no_trip_count.isdigit()):
        no_trip_count = int(no_trip_count)
        if (no_trip_count >= 1):
            return no_trip_count;
        print("Please enter no. of travel greater than zero")
        validate_no_trip_count()
    else:
        print("Please enter no. of travel in digit")
        validate_no_trip_count()


def modify_disc_validate():
    validate_discount_type()
    if(disc_type == 1):
        validate_trip_disc()
        validate_trip_disc_no_passenger()
        validate_trip_disc_percent()
        print("On Adult percentagre values",disc_type_trip,trip_disc_percent,trip_disc_no_passenger)

    elif(disc_type == 2):
        validate_trip_disc()
        validate_trip_disc_percent()
        validate_no_trip_count()
        print("On Adult percentagre values", disc_type_trip, trip_disc_percent, no_trip_count)
    else:
        print("Wrong Offer discount modifying")
        sys.exit()

def validate_modify_fare():
    global disc_type_modify

    disc_type_modify = input("Please enter below options for modify/add... \n"
                             "1: Change Fare "
                             "2: Add discounts "
                             "3: Change age limit "
                             "4: Exit ");
    if (disc_type_modify.isdigit()):
        disc_type_modify = int(disc_type_modify)
        if ((disc_type_modify == 1) | (disc_type_modify == 2) | (disc_type_modify == 3)| (disc_type_modify == 4)):
            return disc_type_modify;
        print("Please enter below options... ")
        validate_modify_fare()
    else:
        print("Please enter options in digits... ")
        validate_modify_fare()

def adult_child_type():
    global child_adult
    child_adult=input("Please Enter below options for fare change on 1:Adult 2:Child ")
    if(child_adult.isdigit()):
        child_adult=int(child_adult)
        if(child_adult==1)|(child_adult==2):
            return child_adult
        print("Please enter below option...")
        adult_child_type()
    else:
        print("Please enter option in digit")
        adult_child_type()

