import s2_story4.validation as validation
import sys

def modify_file(stop_fare,flag):
    #print(validation.entry_stop,validation.exit_stop,validation.age)
    with open("passenger.txt", 'r') as FH:

        line_all = ''
        adult_flag = 0
        adult_list = []
        child_flag = 0
        child_list = []
        age_flag = 0
        line_source=0
        line_source1 = 0
        for line in FH:
            line1 = line.rstrip()
            if(flag==1):
                if (line1 == '</adult>'):
                    adult_flag = 0
                elif (line1 == '<adult>'):
                    adult_flag = 1
                elif (adult_flag == 1):
                    line_source+=1
                    if(validation.entry_stop ==line_source):
                        line2=eval(line1)
                        line2[validation.exit_stop-1]=validation.modify_fare
                        line=str(line2)+"\n"
                        #break
            elif(flag==2):
                #print("INSIDE Child")
                if (line1 == '</child>'):
                    child_flag = 0
                elif (line1 == '<child>'):
                    child_flag = 1
                elif (child_flag == 1):
                    line_source1+=1
                    if(validation.entry_stop ==line_source1):
                        line2=eval(line1)
                        line2[validation.exit_stop-1]=validation.modify_fare
                        line=str(line2)+"\n"
            else:
                print("Wrong User input")
            #print("ONE BY LINE",line)
            line_all+=line
        else:
            with open("passenger.txt", 'w') as FH1:
                FH1.write(line_all)
        #print("All lines",line_all)
    #sys.exit()
