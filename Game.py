import pygame
import random


pygame.mixer.init()
pygame.init()
Dead=[pygame.image.load(r'img\d1.png'),pygame.image.load(r'img\d2.png'),pygame.image.load(r'img\d3.png'),pygame.image.load(r'img\d4.png'),pygame.image.load(r'img\d5.png'),pygame.image.load(r'img\d6.png')]
Walk=[pygame.image.load(r'img\r1.png'),pygame.image.load(r'img\r2.png'),pygame.image.load(r'img\r3.png'),pygame.image.load(r'img\r4.png'),pygame.image.load(r'img\r5.png'),pygame.image.load(r'img\r6.png')]
BirdLeft=[pygame.image.load(r'img\batl1.png'),pygame.image.load(r'img\batl2.png'),pygame.image.load(r'img\batl3.png'),pygame.image.load(r'img\batl4.png')]
BirdRight=[pygame.image.load(r'img\batr1.png'),pygame.image.load(r'img\batr2.png'),pygame.image.load(r'img\batr3.png'),pygame.image.load(r'img\batr4.png')]
Walkl=[pygame.image.load(r'img\l1.png'),pygame.image.load(r'img\l2.png'),pygame.image.load(r'img\l3.png'),pygame.image.load(r'img\l4.png'),pygame.image.load(r'img\l5.png'),pygame.image.load(r'img\l6.png')]
Deadleft=[pygame.image.load(r'img\dl1.png'),pygame.image.load(r'img\dl2.png'),pygame.image.load(r'img\dl3.png'),pygame.image.load(r'img\dl4.png'),pygame.image.load(r'img\dl5.png'),pygame.image.load(r'img\dl6.png')]
win = pygame.display.set_mode((700,400))
pygame.display.set_caption("First Game")
bg = pygame.image.load(r'img\back.png')
GunPoint=pygame.image.load(r'img\gun.png')
GirlImg=pygame.image.load(r'img\girl.png')
Zombihead=pygame.image.load(r'img\zombihead.png')
li=list(range(700,800,20))
lk=list(range(-100,-1,20))
by=list(range(100,250,10))
Score=0
Speed=0.5  #Zombi speed
BirdSpeed = 1
font = pygame.font.SysFont('comicsans',30,True)


######################################################################################################################################################################
def into():
        window = pygame.display.set_mode((700,400))
        pygame.display.set_caption('Save My Girlfriend')
        back = pygame.image.load(r'img\nightback.png')
        back = pygame.transform.scale(back,(700,400))
        message = pygame.image.load(r'img\message.png')
        message = pygame.transform.scale(message,(690,250))
        soldire = pygame.image.load(r'img\Army.png')
        soldire = pygame.transform.scale(soldire,(100,100))
        run = True
        font = pygame.font.SysFont('comicsans',50,True)
        while run:
            window.blit(back,(0,0))
            window.blit(soldire,(10,250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False



            text = font.render(' LEVEL 1 ',1,(255,0,0))
            mission = font.render('Mission : Kill 100 Zombies ',1,(255,0,0))
            space = font.render('PRESS  :  SPACE ',1,(0,0,0))
            window.blit(text,(250,10))
            window.blit(mission,(70,40))
            window.blit(message,(2,70))
            window.blit(space,(200,350))
            pygame.display.update()



######################################################################################################################################################################
def Loss():
        window = pygame.display.set_mode((700,400))
        pygame.display.set_caption('Save My Girlfriend')
        back = pygame.image.load(r'img\back.png')
        back = pygame.transform.scale(back,(700,400))
        soldire = pygame.image.load(r'img\Army.png')
        soldire = pygame.transform.scale(soldire,(100,100))
        run = True
        font = pygame.font.SysFont('comicsans',50,True)
        while run:
            window.blit(back,(0,0))
            window.blit(soldire,(90,270))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False


            
            mission = font.render('Mission Fail ',1,(255,0,0))
            space = font.render('PRESS  :  ENTER ',1,(0,0,0))
            zombi = font.render('You Killed : ' + str(Score),1,(255,0,0))
            window.blit(mission,(240,40))
            window.blit(zombi,(200,100))
            window.blit(space,(200,370))
            pygame.display.update()
        pygame.quit()


        


###################################################################################################################################################################
def Win():
        window = pygame.display.set_mode((700,400))
        pygame.display.set_caption('Save My Girlfriend')
        back = pygame.image.load(r'img\back.png')
        back = pygame.transform.scale(back,(700,400))
        girlps = pygame.image.load(r'img\girlpos.png')
        girlps = pygame.transform.scale(girlps,(100,100))
        thank = pygame.image.load(r'img\thanks.png')
        thank = pygame.transform.scale(thank,(120,120))
        run = True
        font = pygame.font.SysFont('comicsans',50,True)
        while run:
            window.blit(back,(0,0))
            window.blit(girlps,(290,270))
            window.blit(thank,(330,200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False


            #congratulations
            text = font.render('Congratulations',1,(255,0,0))
            mission = font.render('Mission  Completed ',1,(255,0,0))
            space = font.render('PRESS  :  ENTER ',1,(0,0,0))
            zombi = font.render('You Killed : ' + str(Score),1,(255,0,0))
            window.blit(text,(200,40))
            window.blit(mission,(170,80))
            window.blit(zombi,(230,150))
            window.blit(space,(200,370))
            
            pygame.display.update()
        pygame.quit()

        



#################################################################################################################################################################

into()
#######################################################################################################################################################################
class Gun(object):
    def __init__(self,x,y,width,height):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        


    def draw(self,win):
        global GunPoint
        GunPoint=pygame.transform.scale(GunPoint,(self.width,self.height))
        win.blit(GunPoint,(self.x,self.y))
        

class Girl(object):
    def __init__(self,x,y,width,height):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.health=40
        self.Visibal=False
        self.count=0

        
    def draw(self,win):
        global GirlImg
        
        pygame.draw.rect(win,(255,0,0),(self.x+10,self.y-20,40,5))
        pygame.draw.rect(win,(0,128,0),(self.x+10,self.y-20,self.health,5))
        GirlImg=pygame.transform.scale(GirlImg,(self.width,self.height))
        win.blit(GirlImg,(self.x,self.y))


        if self.Visibal:
            saveme=pygame.image.load(r'img\save.png')
            saveme=pygame.transform.scale(saveme,(100,100))
            win.blit(saveme,(self.x+20,self.y-80))
            self.count+=1
            if self.count>10:
                self.Visibal=False
                self.count=0

class ZombieLeft(object):
    
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walkCount=0
        self.deadCount=0
        self.hit=False
        self.dead=False

    def draw(self,win):
        global Score
        if self.dead:
            if self.deadCount +1>=18:
                self.dead=False
                Score+=1
                self.x=li[random.randint(0,4)]
                self.deadCount=0
            Deadleft[self.deadCount//3]=pygame.transform.scale((Deadleft[self.deadCount//3]),(self.width,self.height))
            win.blit(Deadleft[self.deadCount//3],(self.x,self.y))
            self.deadCount +=1
        else:
            self.move()
            if self.walkCount +1 >=18:
                self.walkCount=0
            Walkl[self.walkCount//3]=pygame.transform.scale((Walkl[self.walkCount//3]),(self.width,self.height))
            win.blit(Walkl[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
            if self.hit:
                self.check()
    def move(self):
        if self.x>360:
            self.x -=Speed
        else:
            girl.health-=0.5
            girl.Visibal=True
            

    def check(self):
        if (gun.x>= (self.x-5)) and (gun.x<=(self.x+self.width-30)):
            if (gun.y>=(self.y-5)) and (gun.y<=(self.y+self.height-30)):
                self.dead=True
        self.hit=False



        
class Zombie(object):
    def __init__(self,x,y,width,height):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walkCount=0
        self.deadCount=0
        self.hit=False
        self.dead=False

    def draw(self,win):
        global Score
        if self.dead:
            if self.deadCount +1>=18:
                self.dead=False
                Score+=1
                self.x=lk[random.randint(0,4)]
                self.deadCount=0
            Dead[self.deadCount//3]=pygame.transform.scale((Dead[self.deadCount//3]),(self.width,self.height))
            win.blit(Dead[self.deadCount//3],(self.x,self.y))
            self.deadCount +=1
        else:
            self.move()
            if self.walkCount +1 >=18:
                self.walkCount=0
            Walk[self.walkCount//3]=pygame.transform.scale((Walk[self.walkCount//3]),(self.width,self.height))
            win.blit(Walk[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
            if self.hit:
                self.check()
    def move(self):
        
        if self.x<300:
            self.x +=Speed
        else:
            girl.health-=0.5
            girl.Visibal=True
    def check(self):
        if (gun.x>= (self.x-5)) and (gun.x<=(self.x+self.width-30)):
            if (gun.y>=(self.y-5)) and (gun.y<=(self.y+self.height-30)):
                self.dead=True
        self.hit=False




class Bird(object):
    
    def __init__(self,x,y,widht,height):
        self.x=x
        self.y=y
        self.widht=widht
        self.height=height
        self.flyCount=0
        self.hit=False
        self.dead=False
        self.left=False
        self.right=False
        self.attack=False
        self.headx=0
        self.heady=0

    def draw(self,win):
        global Score
        self.move()
        if self.left:
            if self.dead:
                if self.y>450:
                    self.dead=False
                    Score+=1
                    self.y = by[random.randint(0,14)]
                    if random.randint(1,2) == 1:
                        self.x = -10
                        self.right = True
                        self.left= False
                    else:
                        self.x = 750
                        self.right = False
                        self.left= True
                
                fall = pygame.image.load(r'img\bathitl.png')
                fall=pygame.transform.scale(fall,(self.widht,self.height))
                win.blit(fall,(self.x,self.y))
                self.y+=5
            else:
                if self.flyCount + 1>=12:
                    self.flyCount=0
                BirdLeft[self.flyCount//3]=pygame.transform.scale((BirdLeft[self.flyCount//3]),(self.widht,self.height))
                win.blit(BirdLeft[self.flyCount//3],(self.x,self.y))
                self.flyCount+=1
        if self.right:
            if self.dead:
                if self.y>450:
                    self.dead=False
                    Score+=1
                    self.y = by[random.randint(0,14)]
                    if random.randint(1,2) == 1:
                        self.x = -10
                        self.right = True
                        self.left= False
                    else:
                        self.x = 750
                        self.right = False
                        self.left= True

                fall = pygame.image.load(r'img\bathitr.png')
                fall = pygame.transform.scale(fall,(self.widht,self.height))
                win.blit(fall,(self.x,self.y))
                self.y+=5

            else:
                if self.flyCount + 1>=12:
                    self.flyCount=0
                BirdRight[self.flyCount//3]=pygame.transform.scale((BirdRight[self.flyCount//3]),(self.widht,self.height))
                win.blit(BirdRight[self.flyCount//3],(self.x,self.y))
                self.flyCount+=1
        if self.hit:
            self.check()

        if self.x==girl.x:
            self.attack=True
            self.headx=self.x+10
            self.heady=self.y+10
           
        if self.attack:
            global Zombihead
            Zombihead=pygame.transform.scale(Zombihead,(30,30))
            win.blit(Zombihead,(self.headx,self.heady))
            self.heady+=5
            if self.heady>300:
                self.attack=False
                girl.health-=5
                girl.Visibal=True


    def move(self):
        if self.x<20:
            self.left=False
            self.right=True
            
        if self.x>650:
            self.left=True
            self.right=False
        if self.right:
            self.x+=BirdSpeed
        if self.left:
            self.x-=BirdSpeed
        



    def check(self):
        if (gun.x>= (self.x-5)) and (gun.x<=(self.x+self.widht-30)):
            if (gun.y>=(self.y-5)) and (gun.y<=(self.y+self.height-30)):
                self.dead=True
        self.hit=False


            
def redrawGameWindow():
    win.blit(bg,(0,0))
    text= font.render('Score : ' + str(Score),1,(0,0,0))
    win.blit(text,(0,0))
    Zr.draw(win)
    Zl.draw(win)
    Zr1.draw(win)
    Zl1.draw(win)
    bird.draw(win)
    bird1.draw(win)
    bird2.draw(win)
    bird3.draw(win)
    gun.draw(win)
    girl.draw(win)
    pygame.display.update()


bird=Bird(700,200,60,60)
bird1=Bird(0,100,60,60)
bird2=Bird(0,50,60,60)
bird3=Bird(700,250,60,60)
Zr= Zombie(10,310,60,60)
Zr1= Zombie(-60,310,60,60)
Zl = ZombieLeft(750,310,60,60)
Zl1 = ZombieLeft(810,310,60,60)
gun = Gun(50,200,40,40)
girl = Girl(330,310,60,60)
#mainloop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and gun.x>0:
        gun.x-=5
    if keys[pygame.K_RIGHT] and gun.x<665:
        gun.x+=5
    if keys[pygame.K_UP] and gun.y>0:
        gun.y-=5
    if keys[pygame.K_DOWN] and gun.y<363:
        gun.y+=5
    if keys[pygame.K_SPACE]:
        pygame.mixer.music.load(r'img\gun.mp3')
        pygame.mixer.music.play()
        Zr.hit=True
        Zl.hit=True
        Zr1.hit=True
        Zl1.hit=True
        bird.hit=True
        bird1.hit=True
        bird2.hit=True
        bird3.hit=True
    redrawGameWindow()
    if girl.health<=0:
        Loss()
    if Score > 100:
        Win()
pygame.quit()
