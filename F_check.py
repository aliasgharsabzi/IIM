import copy


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
# def min_distance(position,velocity,pos_F,velo_F,t_now):
#     min_dis=1000
#     if len(pos_F)>t_now:
#         for k in range(len(position)):
# #             print(k+t_now,len(pos_F))
#             if (k+t_now)>=len(pos_F):
#                 break
#             else:
#                 distance_safe=round((((velocity[k]*3600)/15000)*6)*0.1,4)
#                 d=round(abs(position[k]-pos_F[k+t_now]),4)
#                 print("d_s:",distance_safe,"d:",d,"min_dis:",min_dis)
#                 print(position[k],pos_F[k+t_now])
#                 if d<distance_safe:
#                     return("no_safedis",t_f,A0,B0,drop,om1_i)
#                         
# #                 print(min_dis)
#         return (min_dis)
    

def set_toa(om1_i,om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime):
#     v_0=om1_i[3]
    time=[]
    position=[]
    velocity=[]
#     min_dis=1000
    t_R=copy.deepcopy(t)
#     print(v_0,v_f)
    A0=6*((2*x_0)-(2*x_f)+(t_f*v_0)+(t_f*v_f))/(t_f**3)
    B0=-2*((3*x_0)-(3*x_f)+(2*t_f*v_0)+(t_f*v_f))/(t_f**2)
#     print('A0:',A0,'********* B0:',B0,t_f)
    x=x_0
    t=0
    drop1=0
#     print(t,t_f)
    while t<=t_f:
        a=A0*t+B0
        v=(0.5*A0*(t**2))+(B0*t)+v_0
        if v > 22.3:
            return("no",t_f,A0,B0,drop,om1_i,lastTime)
        if (v_0>0 and v<0) or (v_0<0 and v>0):
            drop1=1
        x=((A0*(t**3))/6)+((1/2)*B0*(t**2))+v_0*t+x_0
        time.append(t)
        position.append(x)
        velocity.append(v)
#         print(t,a,v,x)
        t=t+0.1
    if drop1==1:
        drop+=1

    
# *******************check safety in IM *********************************
    temp_line=determination_line(om1_i[1])
#     print(temp_line,om1_i[1])
#     print(position)
    for i in lastTime:
#         print(lastTime)
#         print(i)
        if i in temp_line and lastTime[i]!=0:
            pos_F=lastTime[i][0]
            velo_F=lastTime[i][1]
            t_now=int((t_R-lastTime[i][2])*10)
            if len(pos_F)>t_now:
                for k in range(len(position)):
#                     print(k+t_now,len(pos_F))
                    if (k+t_now)>=len(pos_F):
                        break
                    else:
                        distance_safe=round((((velocity[k]*3600)/15000)*6)*0.1,2)
                        d=round(abs(position[k]-pos_F[k+t_now]),2)
#                         print("d_s:",distance_safe,"d:",d)
#                         print(velocity)
#                         print(position)
#                         print(pos_F)
#                         print(velo_F)
#                         print(k+t_now,k,velocity[k],position[k],pos_F[k+t_now])
                        if d<distance_safe:
                            print("ddddddd:",d,distance_safe)
                            return("no_safedis",t_f,A0,B0,drop,om1_i,lastTime)
#                             n=input("prompt1200")
#             min_dis=min_distance(position,velocity,pos_F,velo_F,t_now)
#             print(min_dis,om1_i[3],om1_i[0])
#             n=input("ali")
#             if min_dis<om1_i[3]:
#                 om1_i[3]=min_dis/1.44
#                 return("no_safedis",t_f,A0,B0,drop,om1_i)
            
#             print(t_R,lastTime[i][2],t_now,len(pos_F))
#             if len(pos_F)>t_now:
#                 for k in range(len(position)):
#                     print(k+t_now,len(pos_F))
#                     if (k+t_now)>=len(pos_F):
#                         break
#                     else:
#                         distance_safe=round(((velocity[k]*3600)/15000)*6,4)
#                         d=round(abs(position[k]-pos_F[k+t_now]),4)
#                         print(distance_safe,d)
#                         print(position[k],pos_F[k+t_now])
#                         print(velocity[k],velo_F[k+t_now])
#                         if d<min_dis:
#                             min_dis=d
#                         print(min_dis)
#                         n=input("salam")
#                         print(t_R,t_now,distance_safe,d,om1_i[3],velo_F[k+t_now])
#                         if d<distance_safe:
#                             om1_i[3]=(d/1.44)
#                             print(om1_i[3])
#                             n=input("salam1")
# #                                 om1_i[3]=velo_F[k+t_now]
#                             return("no_safedis",t_f,A0,B0,drop,om1_i)
    lastTime[om1_i[1]]=position,velocity,t_R
#     print(lastTime)
    return("ok",t_f,A0,B0,drop,om1_i,lastTime)
# *************************** end *****************************
    


def check(om1_i,om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime): 
    temp_line=determination_line(om1_i[1])
#     print(temp_line,om1_i[1], len(om0))
    for i in range(len(om0)-1,-1,-1):
        if om0[i][1] in temp_line :
#             print(om1_i[6],om0[i][6])
            if om1_i[6]<om0[i][6]:
                om1_i[6]=t+(om0[i][6]-om0[i][2])
#                 print(t,(om0[i][6]-om0[i][2]),t_f)
                t_f=om1_i[6]-t
#                 print(t_f)
    response,t_f,A0,B0,drop,om1_i,lastTime=set_toa(om1_i,om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime)
    while True: 
        if response=="no_safedis":
            t_f+=0.1
            response,t_f,A0,B0,drop,om1_i,lastTime=set_toa(om1_i,om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime)
        elif response=="no":
            t_f+=0.1
#             print(om1_i)
            response,t_f,A0,B0,drop,om1_i,lastTime=set_toa(om1_i,om0,x_0,x_f,v_0,v_f,t_f,t,drop,lastTime)
#             print(om1_i)
        else:
            break
    return(t_f,A0,B0,drop,om1_i,lastTime)

# x_0=-96
# x_f=0
# v_0=20.5
# v_f=22.3
# t=0
# t_f=4
# print(check(x_0,x_f,v_0,v_f,t,t_f)) 