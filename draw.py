from pylab import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib.patches as patches
import random




def draw (X_kol,Y_kol,numberkol,line_kol,angle):
    fig = plt.figure(figsize=(6, 6))
    ax=plt.subplot()
    plt.axis('equal')

#     ax.set_xlim(-200,260),ax.set_xticks([i for i in range(-200,260,20)])
#     ax.set_ylim(-200,260), ax.set_yticks([i for i in range(-200,260,20)])
    ax.set_xlim(-110,170)
    ax.set_ylim(-110,170)
    left,right = ax.get_xlim()
    low,high = ax.get_ylim()
    # arrow( left, 0, right-5.25, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 0, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 10, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 20, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 30, right-60, 0, length_includes_head = True, head_width = 0.15,color='r')
    arrow( left, 40, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 50, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( left, 60, right-60, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 0, 260, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 10, 260, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 20, 260, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 30, 260, 0, length_includes_head = True, head_width = 0.15,color='r' )
    arrow( 60, 40, 260, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 50, 260, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 60, 60, 260, 0, length_includes_head = True, head_width = 0.15 )
    # *****************************************************************************************xxx
    arrow( 0, low, 0, high-60, length_includes_head = True, head_width = 0.15 )
    arrow( 10, low, 0, high-60, length_includes_head = True, head_width = 0.15 ) 
    arrow( 20, low, 0, high-60, length_includes_head = True, head_width = 0.15 )
    arrow( 30, low, 0, high-60, length_includes_head = True, head_width = 0.15,color='r' )
    arrow( 40, low, 0, high-60, length_includes_head = True, head_width = 0.15 )
    arrow( 50, low, 0, high-60, length_includes_head = True, head_width = 0.15 )
    arrow( 60, low, 0, high-60, length_includes_head = True, head_width = 0.15 )
    arrow( 0,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    arrow( 10,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    arrow( 20,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    arrow( 30,60, 0, high-low, length_includes_head = True, head_width = 0.15,color='r')
    arrow( 40,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    arrow( 50,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    arrow( 60,60, 0, high-low, length_includes_head = True, head_width = 0.15 )
    
    x=[-100,-100]
    y=[0,60]
    plt.plot(x,y,ls="--",color="blue")
    x=[160,160]
    y=[0,60]
    plt.plot(x,y,ls="--",color="blue")
    x=[0,60]
    y=[160,160]
    plt.plot(x,y,ls="--",color="blue")
    x=[0,60]
    y=[-100,-100]
    plt.plot(x,y,ls="--",color="blue")
    x=[0,60]
    y=[60,60]
    plt.plot(x,y,ls="--",color="g")
    x=[0,60]
    y=[0,0]
    plt.plot(x,y,ls="--",color="g")
    x=[0,0]
    y=[0,60]
    plt.plot(x,y,ls="--",color="g")
    x=[60,60]
    y=[0,60]
    plt.plot(x,y,ls="--",color="g")
    
    # grid() 
    patch = patches.Rectangle((0, 0), 0, 0, fc='y')
     
    def init():
        ax.add_patch(patch)
    
        return patch,
    # RB=[]
#     color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(numberkol)])for i in range(numberkol)]
    def animate(i):
        RB = []   
#         print(i)
        for a in range (len(X_kol[i])):
            if line_kol[i][a] in [43,412,511,610,67,109,106,115,124,121]:
                if line_kol[i][a]==43:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='red'))
                elif line_kol[i][a]==412:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='red'))
                elif line_kol[i][a]==511:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='purple'))
                elif line_kol[i][a]==610:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='black'))
                elif line_kol[i][a]==67:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='black'))
                elif line_kol[i][a]==109:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='navy'))
                elif line_kol[i][a]==106:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='navy'))
                elif line_kol[i][a]==115:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='pink'))
                elif line_kol[i][a]==124:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='olive'))
                elif line_kol[i][a]==121:
                    RB.append(patches.Rectangle((X_kol[i][a]-1,Y_kol[i][a]-2.5), 2, 5, angle=math.degrees(angle[i][a]), color='olive'))
            else:
                if line_kol[i][a]==112:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='blue'))
                elif line_kol[i][a]==19:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='blue'))
                elif line_kol[i][a]==28:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='black'))
                elif line_kol[i][a]==34:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='orange'))
                elif line_kol[i][a]==37:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='orange'))
                elif line_kol[i][a]==76:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='violet'))
                elif line_kol[i][a]==73:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='violet'))
                elif line_kol[i][a]==82:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='turquoise'))
                elif line_kol[i][a]==910:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='yellow'))
                elif line_kol[i][a]==91:
                    RB.append(patches.Rectangle((X_kol[i][a]+2.5,Y_kol[i][a]-1), 2, 5, angle=math.degrees(angle[i][a]), color='yellow'))

        for r in RB:
            ax.add_patch(r)
        return RB
    ani = animation.FuncAnimation(fig,animate,init_func=init,frames=4600 ,interval=100,blit=True,save_count=4600)
    plt.show()

# x=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
# y=[5,5,5,5,5,5,5,5,5,5]
# draw(X_kol,Y_kol,numberkol)
