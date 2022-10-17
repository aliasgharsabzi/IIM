t_mn=[[(3,7.5),(7,16.25),(9,13.5),(10,5.25)],
      [(3,11),(4,15.75),(6,10),(10,5.25)],
      [],
      [(0,13.5),(1,5.25),(6,7.5),(10,16.25)],
      [(1,5.25),(6,11),(7,15.75),(9,10)],
      [],
      [(1,16.25),(3,13.5),(4,5.25),(9,7.5)],
      [(0,10),(4,5.25),(9,11),(10,15.75)],
      [],
      [(0,7.5),(4,16.25),(6,13.5),(7,5.25)],
      [(0,11),(1,15.75),(3,10),(7,5.25)],
      []]
# H_min=[]
# for  i in range(len(V)):
#     H_min.append((V[i][1]/15)*6)
# # print(H_min)
# OT=[3.33,3,3]
# V=[['a',45],['b',50],['d',50],['n',45]]
# omega1=[['a', 0], ['b', 3], ['d', 0],['n', 10]]

def calculation_conflicts(om1):
#     V=v
    omega1=om1
    t_mn=[[(3,7.5),(7,16.25),(9,13.5),(10,5.25)],
      [(3,11),(4,15.75),(6,10),(10,5.25)],
      [],
      [(0,13.5),(1,5.25),(6,7.5),(10,16.25)],
      [(1,5.25),(6,11),(7,15.75),(9,10)],
      [],
      [(1,16.25),(3,13.5),(4,5.25),(9,7.5)],
      [(0,10),(4,5.25),(9,11),(10,15.75)],
      [],
      [(0,7.5),(4,16.25),(6,13.5),(7,5.25)],
      [(0,11),(1,15.75),(3,10),(7,5.25)],
      []]
    def T_mn_New(t_mn,omega1):       
        for i in range(len_omega1):
            temp1=[]
            temp=t_mn[omega1[i][1]]
            for x,y in temp:
                y=y/omega1[i][3]
                temp1.append((x,y))
            t_mn_new.append([omega1[i][1]])
            t_mn_new[i].append(temp1)
        return t_mn_new
     
    t_mn_new=[]
    len_omega1=len(omega1)
    t_mn_new=T_mn_New(t_mn, omega1)
#     print(t_mn)
#     print(t_mn_new)
    output=[]
    def get_conflicts(temp_line,omaga1):
        conf=[]
        len_temp_line=len(temp_line)
        for i in range(len_omega1):
            for item2 in range(len_temp_line):
                if omaga1[i][1]==temp_line[item2][0]:
                    conf.append(temp_line[item2])
                    break
        return conf
   

    for i in range(len_omega1):
        temp_line=t_mn_new[i][1]
#         print(temp_line)
        conflicts=get_conflicts(temp_line, omega1)
        l=len(conflicts)
        temp=[]
        p=[]
        for k in range(l):
            p.append(omega1[i][1])
            t=conflicts[k][0]
            p.append(t)
            t=conflicts[k][1]
            p.append(t)
            temp.append(p)
            p=[]
  
        output.append(temp)
 
    return(output,t_mn)
# conf=calculation_conflicts(V,omega1)
# print("conf:",conf)