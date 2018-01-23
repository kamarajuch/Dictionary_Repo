import s4_story10.validation as validation
import sys

def modify_file(stop_fare,flag):
    disc_add_modify=''
    #print("Validation",validation.user_type,flag,validation.disc_type)
    if(validation.disc_type == 1):
        disc_add_modify=str('trip_disc('+str(validation.disc_type_trip)+','+str(validation.trip_disc_no_passenger)+','+str(validation.trip_disc_percent)+')')
    elif(validation.disc_type == 2):
        disc_add_modify = str('passenger_disc(' + str(validation.disc_type_trip) + ',' + str(validation.no_trip_count) + ',' + str(validation.trip_disc_percent)+ ')')
    else:
        print("Not enter particular discount to modify ")
        sys.exit()
    with open("passenger.txt", 'r') as FH:
        line_all = ''
        discount_flag = 0
        line_source=0
        for line in FH:
            line1 = line.rstrip()
            if (line1 == '</discount>'):
                discount_flag = 0
            elif (line1 == '<discount>'):
                discount_flag = 1
            elif (discount_flag == 1):
                line_source+=1
                if(validation.entry_stop ==line_source):
                    line2=eval(line1)
                    line2[validation.exit_stop-1]=disc_add_modify
                    line=str(line2)+"\n"
            line_all+=line
        else:
            with open("passenger.txt", 'w') as FH1:
                FH1.write(line_all)
                print("Successfully Updated file ")
