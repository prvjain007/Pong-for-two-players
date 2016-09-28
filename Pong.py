import simplegui
import random
wid=600
hei=400
r=20
padwid=8
padlen=80
ballpos=[wid/2,hei/2]
left=False
right=True
pos1=hei/2-padlen/2
pos2=hei/2-padlen/2
vel1,vel2=0,0
ballvel=[0,0]
sc1,sc2=0,0
#Initialize ball pos and vel
def spawn():
    global ballpos,ballvel
#Event handlers
def newgame():
    global pos1,pos2,vel1,vel2,ballvel,ballpos
    global sc1,sc2
    ballpos=[wid/2,hei/2]
    ballvel[0]=random.randrange(-2,2)
    ballvel[1]=random.randrange(-2,2)
    
def draw(c):
    global sc1,sc2,pos1,pos2,ballpos,ballvel,vel1,vel2,r,padlen,padwid
    ballpos[0]+=ballvel[0]
    
    ballpos[1]+=ballvel[1]
    if ballpos[1]<20:
        ballvel[1]=-ballvel[1]
    elif ballpos[1]>hei-20:
        ballvel[1]=-ballvel[1]
    if ballpos[0]<padwid+r and (ballpos[1]>pos1 and ballpos[1]<pos1+padlen):
        ballvel[0]=-ballvel[0]
        if ballvel[0]>0:
            ballvel[0]+=1
        elif ballvel[0]<0:
            ballvel[0]-=1
        if ballvel[1]>0:
            ballvel[1]+=1
        elif ballvel[1]<0:
            ballvel[1]-=1
    elif ballpos[0]<0:
        sc2+=1
        newgame()
    if ballpos[0]>wid-padwid-20 and (ballpos[1]>pos2 and ballpos[1]<pos2+padlen):
        ballvel[0]=-ballvel[0]
        if ballvel[0]>0:
            ballvel[0]+=1
        elif ballvel[0]<0:
            ballvel[0]-=1
        if ballvel[1]>0:
            ballvel[1]+=1
        elif ballvel[1]<0:
            ballvel[1]-=1
    elif ballpos[0]>wid:
        sc1+=1
        newgame()
    
    pos1+=vel1
    pos2+=vel2
    c.draw_circle(ballpos,r,1,"Red","White")
    c.draw_line([padwid,0],[padwid,hei],1,"Red")
    c.draw_line([wid-padwid,0],[wid-padwid,hei],1,"Red")
    c.draw_line([wid/2,0],[wid/2,hei],1,"White")
    c.draw_polygon([(0, pos1), (padwid, pos1), (padwid, pos1+padlen),(0,pos1+padlen)], 12, 'White')
    c.draw_polygon([(wid, pos2), (wid-padwid, pos2), (wid-padwid, pos2+padlen),(wid,pos2+padlen)], 12, 'White')


def keyd(key):
    global vel1,vel2,pos1,pos2
    acc=2
    
    if key==simplegui.KEY_MAP["down"]:
        vel2+=acc
    elif key==simplegui.KEY_MAP["up"]:
        vel2-=acc
    if key==simplegui.KEY_MAP["s"]:
        vel1+=acc
    elif key==simplegui.KEY_MAP["w"]:
        vel1-=acc
def keyu(key):
    global vel1,vel2
    vel1,vel2=0,0

f=simplegui.create_frame("Pong",wid,hei)
f.add_button("Start",newgame,100)
f.set_draw_handler(draw)
f.set_keydown_handler(keyd)
f.set_keyup_handler(keyu)

f.start()