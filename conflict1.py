from ChangeLine import changeline,ccc
from calculatTOA import calcuat_TOA
import copy
import math
import time
from F_check import check

def conflict_kol():
    laneWidth = 10
    arc = 2 * 3.14 * (3.5*laneWidth)/4
    smallArc = 2 * 3.14 * (0.5*laneWidth) /4
    c112=[[43,arc/5,4*arc/5],[412,4*arc/5,6*laneWidth],[73,arc/3,4*laneWidth],[82,arc/2,3.5*laneWidth],[91,4*arc/5,3*laneWidth],[109,arc/2,arc/2],[106,arc/3,3.5*laneWidth],[115,arc/5,4*laneWidth],[124,0,4*laneWidth]]
    c19=[[43,1.5*laneWidth,4*arc/5],[412,3*laneWidth,3*laneWidth],[511,4*laneWidth,3*laneWidth],[610,5*laneWidth,3*laneWidth],[76,3*laneWidth,2*arc/3],[106,2*laneWidth,4*laneWidth],[109,5*laneWidth,arc],[115,1*laneWidth,4*laneWidth],[124,0,4*laneWidth]]
    c28=[[43,2*laneWidth,2*arc/3],[412,3*laneWidth,2*laneWidth],[511,4*laneWidth,2*laneWidth],[610,5*laneWidth,2*laneWidth],[76,1*laneWidth,arc],[106,2*laneWidth,5*laneWidth],[115,1*laneWidth,5*laneWidth],[124,0,5*laneWidth]]
    c37=[[43,2*laneWidth,arc/3],[412,3*laneWidth,1*laneWidth],[511,4*laneWidth,1*laneWidth],[610,5*laneWidth,1*laneWidth],[67,5*laneWidth,smallArc],[76,2*laneWidth,arc],[106,2*laneWidth,6*laneWidth],[115,1*laneWidth,6*laneWidth],[124,0,6*laneWidth]]
    c34=[[124,0,6*laneWidth]]
    c43=[[76, 10.99, 43.96], [73, 43.96, 60], [106, 18.316666666666666, 40], [115, 27.475, 35.0], [124, 43.96, 30], [112, 27.475, 27.475], [19, 18.316666666666666, 35.0], [28, 10.99, 40], [37, 0, 40]]
    c412=[[76, 15.0, 43.96], [73, 30, 30], [82, 40, 30], [91, 50, 30], [109, 30, 36.63333333333333], [19, 20, 40], [112, 50, 54.95], [28, 10, 40], [37, 0, 40]]
    c511=[[76, 20, 36.63333333333333], [73, 30, 20], [82, 40, 20], [91, 50, 20], [109, 10, 54.95], [19, 20, 50], [28, 10, 50], [37, 0, 50]]
    c610=[[76, 20, 18.316666666666666], [73, 30, 10], [82, 40, 10], [91, 50, 10], [910, 50, 7.8500000000000005], [109, 20, 54.95], [19, 20, 60], [28, 10, 60], [37, 0, 60]]
    c67=[[37,0,60]]
    c76=[[109, 10.99, 43.96], [106, 43.96, 60], [19, 18.316666666666666, 40], [28, 27.475, 35.0], [37, 43.96, 30], [43, 27.475, 27.475], [412, 18.316666666666666, 35.0], [511, 10.99, 40], [610, 0, 40]]
    c73=[[109, 15.0, 43.96], [106, 30, 30], [115, 40, 30], [124, 50, 30], [112, 30, 36.63333333333333], [412, 20, 40], [43, 50, 54.95], [511, 10, 40], [610, 0, 40]]
    c82=[[109, 20, 36.63333333333333], [106, 30, 20], [115, 40, 20], [124, 50, 20], [112, 10, 54.95], [412, 20, 50], [511, 10, 50], [610, 0, 50]]
    c91=[[109, 20, 18.316666666666666], [106, 30, 10], [115, 40, 10], [124, 50, 10], [121, 50, 7.8500000000000005], [112, 20, 54.95], [412, 20, 60], [511, 10, 60], [610, 0, 60]]
    c910=[[610,0,60]]
    c109=[[112, 10.99, 43.96], [19, 43.96, 60], [412, 18.316666666666666, 40], [511, 27.475, 35.0], [610, 43.96, 30], [76, 27.475, 27.475], [73, 18.316666666666666, 35.0], [82, 10.99, 40], [91, 0, 40]]
    c106=[[112, 15.0, 43.96], [19, 30, 30], [28, 40, 30], [37, 50, 30], [43, 30, 36.63333333333333], [73, 20, 40], [76, 50, 54.95], [82, 10, 40], [91, 0, 40]]
    c115=[[112, 20, 36.63333333333333], [19, 30, 20], [28, 40, 20], [37, 50, 20], [43, 10, 54.95], [73, 20, 50], [82, 10, 50], [91, 0, 50]]
    c124=[[112, 20, 18.316666666666666], [19, 30, 10], [28, 40, 10], [37, 50, 10], [34, 50, 7.8500000000000005], [43, 20, 54.95], [73, 20, 60], [82, 10, 60], [91, 0, 60]]
    c121=[[91,0,60]] 
    conflict=[[112,c112],[19,c19],[28,c28],[37,c37],[34,c34],[43,c43],[412,c412],[511,c511],[610,c610],[67,c67],[76,c76],
              [73,c73],[82,c82],[91,c91],[910,c910],[109,c109],[106,c106],[115,c115],[124,c124],[121,c121]]
    return(conflict)


# lastTime={112:0,19:0,28:0,37:0,34:0,43:0,412:0,511:0,610:0,67:0,76:0,73:0,82:0,91:0,910:0,109:0,106:0,115:0,124:0,121:0}

# om1=[['a',112,1,18,100,15],['b',121,1,15,100,17]]
# om0=[['c',43,0,18,70,15],['d',82,0,22,60,13]]
def com_conflict(i,conflict):
    temp1=[]
    for j in range(len (conflict)):
        if i[1]==conflict[j][0]:
            temp1=conflict[j][1]
            break
    return(temp1)
def priority(e):             
    return(e[0][1])

         
    

conf=[]
# toa_new=0
def Intersection(om1,om0,t,Num_change,om1_main,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime,case):
    start_time = time.time()
#     print(case)
    temp1=[]
    Vmax=22.3
    delay=[]
    
    
#     *****************determinant policy*************
    if case in [2,4]:
        if len(om1)>1:
            om1.sort(reverse=True,key=priority)
            om1=copy.deepcopy(om1)     
            print(om1)


#     *****************end*******************
    for i in range(len (om1)):
        toa_new2=0
        toa_new3=0
        toa_max=0
        toa_new=0
        A0=0
        B0=0
        conf=[]
        conflict= conflict_kol()
        if om1[i][1] in [76,73,82,91,910,109,106,115,124,121]:
            toa_max=((om1[i][4]-60)/Vmax)+t
            toa_new=toa_max
            x_0=om1[i][4]
            x_f=60
            v_0=-1*(om1[i][3])
            v_f=-22.3
        else:
            toa_max=-1*(om1[i][4]/Vmax)+t
            toa_new=toa_max
            x_0=om1[i][4]
            x_f=0
            v_0=om1[i][3]
            v_f=22.3
        if  om0 ==[]:
            toa_new=toa_max
            om1[i][6]=toa_new
            delay.append(0)
#             print("TOA_New:",toa_new,"TOA_Max:",toa_max)   
        else:
            temp1=com_conflict(om1[i], conflict)
            toa_new2=calcuat_TOA(t,om0,Vmax,temp1,toa_new,toa_max)
            om1_last=copy.deepcopy(om1[i])
#             toa_new=toa_new2

# ***********************change line *****************
            if case in [3,4,7,8]:
#             if case in [1]:
                if om1[i][1] in [19,28,37,412,511,610,73,82,91,106,115,124]:
                    om1[i],toa_new2=ccc(om1[i],om1,toa_new2,t,om0,Vmax,toa_new,toa_max,om1_main)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",om1[i])
                if om1[i][1]!=om1_last[1]:
                    print(om1[i],t)
    #                 n=input("asd")
                    Num_change+=1  
# *********************end**************************
            toa_new=toa_new2    
# *********************old change line (Not optimal)**********
#             om1[i]=changeline(om1[i],lastTime,om1,om1_main,om0)
#             if om1[i][1]!=om1_last[1]:
#                 temp1=com_conflict(om1[i], conflict)
#                 toa_new3=calcuat_TOA(t,om0,Vmax,temp1,toa_new,toa_max)+(0.498/om1[i][3])
# #                 toa_new=toa_new3
# #                 Num_change+=1
#                 if toa_new3<toa_new2:
#                     toa_new=toa_new3
#                     print("toa2",toa_new2,"toa3",toa_new3)
#                     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",om1[i])
#                     print("change line********************************************************************")
#                     Num_change+=1
#                 else:
#                     toa_new=toa_new2
#                     om1[i]=copy.deepcopy(om1_last)
#                     print("toa2",toa_new2,"toa3",toa_new3)
#                     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",om1[i])
#                     print("NO change line")
#             else:
#                 toa_new=toa_new2
#                 om1[i]=copy.deepcopy(om1_last)
#                 print("toa2",toa_new2,"toa3",toa_new3)
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",om1[i])
#                 print("NO change line")

# *************************end**********************

#             print("TOA_New:",toa_new,"TOA_Max:",toa_max) 
            if om1[i][0][1]=='1':
                AVG_pri1.append(toa_new-toa_max)
#                 print(AVG_pri1)
#                 n=input("pri")
            elif om1[i][0][1]=='2':
                AVG_pri2.append(toa_new-toa_max)
            delay.append(toa_new-toa_max)
                     
            om1[i][6]=toa_new
#             if toa_new> lastTime[om1[i][1]]:
#                 lastTime[om1[i][1]]=toa_new
#             print(lastTime)
 

        t_f=toa_new-t
#         A0=6*((2*x_0)-(2*x_f)+(t_f*v_0)+(t_f*v_f))/(t_f**3)
#         B0=-2*((3*x_0)-(3*x_f)+(2*t_f*v_0)+(t_f*v_f))/(t_f**2)        
        
# ******************F_Check(for be active, you must commend 2 line above)  ************

        t_f,A0,B0,drop,om1[i],lastTime=check(om1[i],om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime)
        om1[i][6]=t_f+t
#         print(om1[i])
#         n=input("sad")
# *******************end*****************

#         print("delay:",delay)
        om1[i].append(Vmax)
        om1[i].append(A0)
        om1[i].append(B0)
        om1[i].append(om1[i][4])
        om1[i][2]=t
#         print("A,B:",A0,B0)
        if om1[i][1] in [112,19,28,34,37,76,73,82,910,91]:
            om1[i].append(math.radians(90))
        else:
            om1[i].append(0)             
        
#         drop=f_check(om1[i],x_0,v_0,A0,B0,drop)
#         print(drop)
        om0.append(om1[i])
        end_time = time.time()
        runtime_IM = end_time-start_time
    return(om0,delay,Num_change,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime)   
    
