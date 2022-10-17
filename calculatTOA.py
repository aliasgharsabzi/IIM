

def calcuat_TOA(t,om0,Vmax,temp1,toa_new,toa_max):
    for k in range(len(om0)):
        for m in range(len (temp1)):
            if t < om0[k][6]:
                if om0[k][1]==temp1[m][0]:
                    toa=om0[k][6]+(((temp1[m][2])/(Vmax))-((temp1[m][1])/(Vmax)))
#                     print("TOA_Car  "+om0[k][0]+":",om0[k][6])
#                     print("TimeConflict  "+om1[0]+"+TOA_Car  "+om0[k][0]+":",toa)
                    if toa > toa_new:
                        toa_new=toa
#                             conf.append(temp[m])
                    break
    if toa_max > toa_new:
        toa_new=toa_max 
    return(toa_new)