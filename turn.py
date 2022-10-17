import math



def turn(item):
    if item[1]==112:
        if item[4]<34.99:
            r=35
            a=0
            b=25
            l=0.06362
            item[11]+=l
            x=r*math.cos(item[11]+math.radians(180))
            y=r*math.sin(item[11]+math.radians(180))
            item[4]=a+x
            item[5]=(b+(r-abs(y)))
            return(item)
        else:
            item[5]=item[5]+item[7]*0.1
            return(item)
    elif item[1]==34:
        if item[4]<4.9:
            r=5
            l=0.4195
            print(item[11])
            item[11]-=l
            x=r*math.cos(item[11])
            y=r*math.sin(item[11])
            item[4]=x
            item[5]=y
            return(item)
        else:
            item[5]=item[5]-item[7]*0.1
            return(item)
    elif item[1]==43:
        if item[5]>0:
            r=35
            l=0.06362
            item[11]+=l
            x=r*math.cos(item[11])
            y=r*math.sin(item[11])
            item[4]=y
            item[5]=x
            return(item)
        else:
            item[5]=item[5]-item[7]*0.1
            return(item)
    elif item[1]==67:
        if item[5]<59.4:
            r=5
            a=55
            b=0
            l=0.4195
            item[11]-=l
            x=r*math.cos(item[11]+math.radians(180))
            y=r*math.sin(item[11]+math.radians(180))
            item[4]=y
            item[5]=a+(r-abs(x))
            return(item)
        else:
            item[5]=item[5]+item[7]*0.1
            return(item)
    elif item[1]==76:
        if item[5]>0:
            r=35
            a=60
            b=35
            l=0.06362
            item[11]+=l
            x=r*math.cos(item[11])
            y=r*math.sin(item[11])
            item[4]=a-abs(x)
            item[5]=y
            return(item)
        else:
            item[5]=item[5]-item[7]*0.1
            return(item)
    elif item[1]==910:
        if item[5]<59:
            r=5
            a=60
            b=55
            l=0.4195
            item[11]-=l
            x=r*math.cos(item[11]+math.radians(180))
            y=r*math.sin(item[11])
            item[4]=a+x
            item[5]=b+(r-abs(y))
            return(item)
        else:
            item[5]=item[5]+item[7]*0.1
            return(item)
    elif item[1]==109:
        if item[4]>25.6:
            r=35
            a=25
            b=60
            l=0.06362
            item[11]+=l
            x=r*math.cos(item[11]+math.radians(180))
            y=r*math.sin(item[11]+math.radians(180))
            item[4]=b-abs(y)
            item[5]=a+(r-abs(x)) 
            return(item)
        else:
            item[5]=item[5]+item[7]*0.1
            return(item)
    elif item[1]==121:
        if item[4]>55.3:
            r=5
            a=5
            b=60
            l=0.4195
            item[11]-=l
            x=r*math.cos(item[11]+math.radians(360))
            y=r*math.sin(item[11]+math.radians(360))
            item[4]=b+y
            item[5]=a-(r-x)
            return(item)
        else:
            item[5]=item[5]-item[7]*0.1
            return(item)
    else:
        return(item)
    
