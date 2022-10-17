import copy
from calculatTOA import calcuat_TOA
laneWidth = 10
arc = 2 * 3.14 * (3.5*laneWidth)/4
smallArc = 2 * 3.14 * (0.5*laneWidth) /4
c112=[[43,arc/5,4*arc/5],[412,4*arc/5,6*laneWidth],[73,arc/3,4*laneWidth],[82,arc/2,3.5*laneWidth],[91,4*arc/5,3*laneWidth],[109,arc/2,arc/2],[106,arc/3,3.5*laneWidth],[115,arc/5,4*laneWidth],[124,0,4*laneWidth]]
c19=[[43,1.5*laneWidth,4*arc/5],[412,3.5*laneWidth,3.5*laneWidth],[511,4*laneWidth,3*laneWidth],[610,5*laneWidth,3*laneWidth],[76,3*laneWidth,2*arc/3],[106,2*laneWidth,4*laneWidth],[109,5*laneWidth,arc],[115,1*laneWidth,4*laneWidth],[124,0,4*laneWidth]]
c28=[[43,2*laneWidth,2*arc/3],[412,3*laneWidth,2*laneWidth],[511,4*laneWidth,2*laneWidth],[610,5*laneWidth,2*laneWidth],[76,1*laneWidth,arc],[106,2*laneWidth,5*laneWidth],[115,1*laneWidth,5*laneWidth],[124,0,5*laneWidth]]
c37=[[43,2*laneWidth,arc/3],[412,3*laneWidth,1*laneWidth],[511,4*laneWidth,1*laneWidth],[610,5*laneWidth,1*laneWidth],[67,5*laneWidth,smallArc],[76,2*laneWidth,arc],[106,2*laneWidth,6*laneWidth],[115,1*laneWidth,6*laneWidth],[124,0,6*laneWidth]]
c34=[[124,0,6*laneWidth]]
c43=[[76, 10.99, 43.96], [73, 43.96, 60], [106, 18.316666666666666, 40], [115, 27.475, 35.0], [124, 43.96, 30], [112, 27.475, 27.475], [19, 18.316666666666666, 35.0], [28, 10.99, 40], [37, 0, 40]]
c412=[[73, 15.0, 43.96], [76, 35.0, 35.0], [82, 40, 30], [91, 50, 30], [109, 30, 36.63333333333333], [112, 20, 40], [19, 50, 54.95], [28, 10, 40], [37, 0, 40]]
c511=[[76, 20, 36.63333333333333], [73, 30, 20], [82, 40, 20], [91, 50, 20], [109, 10, 54.95], [19, 20, 50], [28, 10, 50], [37, 0, 50]]
c610=[[76, 20, 18.316666666666666], [73, 30, 10], [82, 40, 10], [91, 50, 10], [910, 50, 7.8500000000000005], [109, 20, 54.95], [19, 20, 60], [28, 10, 60], [37, 0, 60]]
c67=[[37,0,60]]
c76=[[109, 10.99, 43.96], [106, 43.96, 60], [19, 18.316666666666666, 40], [28, 27.475, 35.0], [37, 43.96, 30], [43, 27.475, 27.475], [412, 18.316666666666666, 35.0], [511, 10.99, 40], [610, 0, 40]]
c73=[[109, 15.0, 43.96], [106, 35.0, 35.0], [115, 40, 30], [124, 50, 30], [112, 30, 36.63333333333333], [43, 20, 40], [412, 50, 54.95], [511, 10, 40], [610, 0, 40]]
c82=[[109, 20, 36.63333333333333], [106, 30, 20], [115, 40, 20], [124, 50, 20], [112, 10, 54.95], [412, 20, 50], [511, 10, 50], [610, 0, 50]]
c91=[[109, 20, 18.316666666666666], [106, 30, 10], [115, 40, 10], [124, 50, 10], [121, 50, 7.8500000000000005], [112, 20, 54.95], [412, 20, 60], [511, 10, 60], [610, 0, 60]]
c910=[[610,0,60]]
c109=[[112, 10.99, 43.96], [19, 43.96, 60], [412, 18.316666666666666, 40], [511, 27.475, 35.0], [610, 43.96, 30], [76, 27.475, 27.475], [73, 18.316666666666666, 35.0], [82, 10.99, 40], [91, 0, 40]]
c106=[[112, 15.0, 43.96], [19, 35.0, 35.0], [28, 40, 30], [37, 50, 30], [43, 30, 36.63333333333333], [76, 20, 40], [73, 50, 54.95], [82, 10, 40], [91, 0, 40]]
c115=[[112, 20, 36.63333333333333], [19, 30, 20], [28, 40, 20], [37, 50, 20], [43, 10, 54.95], [73, 20, 50], [82, 10, 50], [91, 0, 50]]
c124=[[112, 20, 18.316666666666666], [19, 30, 10], [28, 40, 10], [37, 50, 10], [34, 50, 7.8500000000000005], [43, 20, 54.95], [73, 20, 60], [82, 10, 60], [91, 0, 60]]
c121=[[91,0,60]]
conflict=[[112,c112],[19,c19],[28,c28],[37,c37],[34,c34],[43,c43],[412,c412],[511,c511],[610,c610],[67,c67],[76,c76],
          [73,c73],[82,c82],[91,c91],[910,c910],[109,c109],[106,c106],[115,c115],[124,c124],[121,c121]]
def com_conflict(i,conflict):
    temp1=[]
    for j in range(len (conflict)):
        if i[1]==conflict[j][0]:
            temp1=conflict[j][1]
            break
    return(temp1)
 
 
ch_line_possible=[[19,28],[28,19,37],[37,28],[412,511],[511,412,610],[610,511],[73,82],[82,73,91],[91,82],
                  [106,115],[115,106,124],[124,115]]

def determination_line(line):
    temp_line=[]
    if line==19 or line==112:
        temp_line=[19,112]
    elif line==28:
        temp_line=[28]
    elif line==37 or line==34:
        temp_line=[37,34]
    elif line==412 or line==43:
        temp_line=[412,43]
    elif line==51:
        temp_line=[511]
    elif line==610 or line==67:
        temp_line=[610,67]
    elif line==73:
        temp_line=[73,76]
    elif line==82:
        temp_line=[82]
    elif line==91 or line==910:
        temp_line=[91,910]
    elif line==106 or line==109:
        temp_line=[106,109]
    elif line==115:
        temp_line=[115]
    elif line==124 or line==121:
        temp_line=[124,121]
    return(temp_line)


def check_safety(om1,om1_kol,om1_main,om0):
    response1="OK"
    om1_main=copy.deepcopy(om1_main+om1_kol)
    temp_line=determination_line(om1[1])
    for i in range(len(om1_main)-1,-1,-1):
        if om1_main[i][0]!=om1[0] and om1_main[i][1] in temp_line: 
            distance_safe=((om1_main[i][3]*3600)/15000)*6
            if(abs(om1_main[i][4]-om1[4]))<=distance_safe:
                response1="NO"
                break
#                     print(abs(om1_main[i][4])-abs(om1[4]),distance_safe)
#                     n=input("dakhal")
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",old_om1)
#                 return("NO")
        response1="OK"
    if response1=="NO":
        return(response1)
    else:
        om0=copy.deepcopy(om1_kol+om0)
        temp_line=determination_line(om1[1])
        for i in range(len(om0)):
            if om0[i][0]!=om1[0] and om0[i][1]in temp_line: 
                distance_safe=((om1[3]*3600)/15000)*6
                if(abs(om1[4]-om0[i][4]))<=distance_safe:
#                     print((abs(om1[4])-abs(om0[i][4])),distance_safe)
#                     n=input("dakhalom0")
                    return("NO")
    #                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",old_om1)             
        return("OK")
        


def ccc(om1,om1_kol,toa_new2,t,om0,Vmax,toa_new,toa_max,om1_main):
    new_om1=copy.deepcopy(om1)
    for i in ch_line_possible:
        if om1[1]==i[0]:
            if len(i)==2:
                new_om1[1]=i[1]
                response=check_safety(new_om1, om1_kol,om1_main,om0)
                if response=="OK":
                    temp1=com_conflict(new_om1,conflict)
                    toa_new3=calcuat_TOA(t,om0,Vmax,temp1,toa_new,toa_max)+(0.498/om1[3])
#                     print(toa_new2,toa_new3)
#                     n=input("aa2")
                    if toa_new2>toa_new3:
                        print("$$$$$$$$$$$$$$$$$$$$$:",toa_new2,toa_new3,om1[1],i[1])
#                         n=input("aa")
                        toa_new2=toa_new3
                        om1[1]=i[1]
                return(om1,toa_new2)            
            else:
                for j in range(2):
                    new_om1[1]=i[j+1]
                    response=check_safety(new_om1, om1_kol,om1_main,om0)
                    if response=="OK":
                        temp1=com_conflict(new_om1, conflict)
                        toa_new3=calcuat_TOA(t,om0,Vmax,temp1,toa_new,toa_max)+(0.498/om1[3])
                        if toa_new2>toa_new3:
                            print("$$$$$$$$$$$$$$$$$$$$$:",toa_new2,toa_new3,om1[1],i[j+1])
#                             print(toa_new2,toa_new3)
#                             n=input("aa2")
                            toa_new2=toa_new3
                            om1[1]=i[j+1]
                return(om1,toa_new2) 
         
#     
        
        
        
def changeline(om1,lastTime,om1_kol,om1_main,om0):
    old_om1=copy.deepcopy(om1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",om1)
    if om1[1]==19 and lastTime[19]>lastTime[28]:
        om1[1]=28
    elif om1[1]==28 and lastTime[28]>lastTime[19] and lastTime[37]>lastTime[19]:
        om1[1]=19
    elif om1[1]==28 and lastTime[28]>lastTime[37]:
        om1[1]=37
    elif om1[1]==37 and lastTime[37]>lastTime[28]:
        om1[1]=28
    elif om1[1]==412 and lastTime[412]>lastTime[511]:
        om1[1]=511
    elif om1[1]==511 and lastTime[511]>lastTime[412]and lastTime[610]>lastTime[412]:
        om1[1]=412
    elif om1[1]==511 and lastTime[511]>lastTime[610]:
        om1[1]=610
    elif om1[1]==610 and lastTime[610]>lastTime[511]:
        om1[1]=511
    elif om1[1]==73 and lastTime[73]>lastTime[82]:
        om1[1]=82
    elif om1[1]==82 and lastTime[82]>lastTime[73]and lastTime[91]>lastTime[73]:
        om1[1]=73
    elif om1[1]==82 and lastTime[82]>lastTime[91]:
        om1[1]=91
    elif om1[1]==91 and lastTime[91]>lastTime[82]:
        om1[1]=82
    elif om1[1]==106 and lastTime[106]>lastTime[115]:
        om1[1]=115
    elif om1[1]==115 and lastTime[115]>lastTime[106]and lastTime[124]>lastTime[106]:
        om1[1]=106
    elif om1[1]==115 and lastTime[115]>lastTime[124]:
        om1[1]=124
    elif om1[1]==124 and lastTime[124]>lastTime[115]:
        om1[1]=115
        
        
    if old_om1[1]!=om1[1]:    
        response1="OK"
        om1_main=om1_main+om1_kol
        for i in range(len(om1_main)-1,-1,-1):
            if om1_main[i][0]!=om1[0] and om1_main[i][1]==om1[1]: 
                distance_safe=((om1_main[i][3]*3600)/15000)*6
                if(abs(om1_main[i][4])-abs(om1[4]))<=distance_safe:
                    print(abs(om1_main[i][4]-om1[4]),distance_safe)
                    response1="NO"
                    break
    #                     n=input("dakhal")
    #                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",old_om1)             
            response1="OK"
        if response1=="NO":
            return(old_om1)
        else:
            om0=copy.deepcopy(om1_kol+om0)
            for i in range(len(om0)):
                if om0[i][0]!=om1[0] and om0[i][1]==om1[1]: 
                    distance_safe=((om1[3]*3600)/15000)*6
                    if(abs(om1[4])-abs(om0[i][4]))<=distance_safe:
                        print((abs(om1[4]-om0[i][4])),distance_safe)
#                         n=input("dakhalom0")
                        return(old_om1)
        #                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",old_om1)             
            return(om1)  
    else:
        return(om1)     


# x_0=-100
# y_0=5
# x_1=0
# y_1=10
# m=(y_1-y_0)/(x_1-x_0)
# while (x_0<=0):
#     y_0=m*(x_0-x_1)+y_1
#     x_0=x_0+2.23
#      
#      
#     print(x_0,y_0)

def position(item):  
    if item[1]==19 and item[5]!=25:
#         m=(25-item[5])/(0-item[4])
        m=0.1020
        item[5]=m*(item[4]-0)+25
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5]) 
    elif item[1]==28:
        m=0
        if 15<item[5]<=25:
            m=-0.1020
            item[5]=m*(item[4]-0)+25
        elif 5<=item[5]<15:
            m=0.1020
            item[5]=m*(item[4]-0)+5
        item[5]=m*(item[4]-0)+15
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==37 and item[5]!=5:
#         m=(5-item[5])/(0-item[4])
        m=-0.1020
        item[5]=m*(item[4]-0)+5
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==412 and item[5]!=35:
        m=-0.1020
        item[5]=m*(item[4]-0)+35
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==511:
        m=0
        if 45<item[5]<=55:
            m=-0.1020
            item[5]=m*(item[4]-0)+55
        elif 35<=item[5]<45:
            m=0.1020
            item[5]=m*(item[4]-0)+35
        item[5]=m*(item[4]-0)+45
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==610 and item[5]!=55:
        m=0.1020
        item[5]=m*(item[4]-0)+55
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==73 and item[5]!=35:
        m=0.1020
        item[5]=m*(item[4]-60)+35
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==82:
        m=0
        if 45<item[5]<=55:
            m=0.1020
            item[5]=m*(item[4]-60)+55
        elif 35<=item[5]<45:
            m=-0.1020
            item[5]=m*(item[4]-60)+35
        item[5]=m*(item[4]-60)+45
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==91 and item[5]!=55:
        m=-0.1020
        item[5]=m*(item[4]-60)+55
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==106 and item[5]!=25:
        m=-0.1020
        item[5]=m*(item[4]-60)+25
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==115:
        m=0
        if 15<item[5]<=25:
            m=0.1020
            item[5]=m*(item[4]-60)+25
        elif 5<=item[5]<15:
            m=-0.1020
            item[5]=m*(item[4]-60)+5
        item[5]=m*(item[4]-60)+15
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    elif item[1]==124 and item[5]!=5:
        m=0.1020
        item[5]=m*(item[4]-60)+5
        if m!=0:
            print('*'*10,m,item)
#             n=input("fgh")
        return(item[5])
    else:
        return(item[5])
    
    
#     