import random
import string
import copy
from ACC import control_distance
# om1=[]
min_v=11.2
max_v=22.3 
last_om1=[]
def G_car(om1,t,all_vehicle,line_num):
    temp=[]
    f_list =[]
    last_om1=copy.deepcopy(om1)
#     l_om1=random.randint(0,12)
    l_om1=len(line_num)
    all_vehicle+=l_om1
#     print(l_om1)
    for i in range(l_om1):
        m=[]
#             line=random.randint(1,12)
        if line_num[i]==1:
            line= random.choice([19,112])
            x=-200
            y=25
        elif line_num[i]==2:
            line=28
            x=-200
            y=15
        elif line_num[i]==3:
            line= random.choice([37,34])
            x=-200
            y=5
        elif line_num[i]==4:
            line= random.choice([412,43])
            x=35
            y=-200
        elif line_num[i]==5:
            line=511
            x=45
            y=-200
        elif line_num[i]==6:
            line= random.choice([610,67])
            x=55
            y=-200
        elif line_num[i]==7:
            line= random.choice([73,76])
            x=260
            y=35
        elif line_num[i]==8:
            line=82
            x=260
            y=45
        elif line_num[i]==9:
            line= random.choice([91,910])
            x=260
            y=55
        elif line_num[i]==10:
            line= random.choice([106,109])
            x=25
            y=260
        elif line_num[i]==11:
            line=115
            x=15
            y=260
        elif line_num[i]==12:
            line= random.choice([124,121])
            x=5
            y=260
#         line= random.choice([112,19,28,37,34,43,412,511,610,67,76,73,82,91,910,109,106,115,124,121])
        Id1=random.choice(string.ascii_letters)
        while Id1 in f_list:
            Id1=random.choice(string.ascii_letters)
        f_list.append(Id1)
#         Id=Id1+random.choice(string.ascii_letters)+str(t) 
        s=random.choices([0,1,2], weights=(80, 15, 5))
        Id=Id1+str(s[0])+str(t)
#         if t<=0.1:
#             v=21
#         else:
#             v=22.3
        v=min_v+(max_v-min_v)*random.random()
#         v=22.3
#             ot=(-1*((-100*3600)/(v*1000)))+t
        ot=0


        m.append(Id)
        m.append(line)
        m.append(t)
        m.append(v)
        if line in [43,412,511,610,67,109,106,115,124,121]:
            m.append(y)
            m.append(x)
        else:
            m.append(x)
            m.append(y)
#         m.append(x)
        m.append(ot)
#         m=control_distance(m,last_om1)
        om1.append(m)
        temp.append(m)

    
    return(om1,all_vehicle,temp)
# f.close()