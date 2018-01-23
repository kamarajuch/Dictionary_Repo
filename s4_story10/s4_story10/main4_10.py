#import s4_story10.common as common
import copy as copy


def get_fare():
    print("Nothing")
 #   common.apply_dicount()

if __name__ == "__main__":
    l=[1,2,3,45,6]
    l1=copy.copy(l)
    l2=copy.deepcopy(l)
    print("Befor any modify",l)
    l1[1]=200
    print("After shallo copy any modify",l)
    l2[1] = 300
    print("After deep copy any modify",l)
    total=get_fare();
    #print(total)
