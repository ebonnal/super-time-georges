import pygame
from pygame.locals import *
from time import *
def ini():
    
    pygame.mixer.pre_init(100000,-16,2,2048)
    pygame.init()
    pygame.key.set_repeat(10000000,3)
    fenetre = pygame.display.set_mode((1000,400))
    pygame.display.set_caption("TMTC Morray")
    rang=0
    t0,t1,ti,tc,tc2,tanim,tr=time(),time(),time(),time(),time(),time(),time()
    tanimtrue=t0
    tjauge=time()
    listealpha={}
    for l in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","p1","p2","p3","p4","p5","p6","p7","p8","p9","p0"]:
        listealpha[l]=pygame.transform.scale(pygame.image.load("Alpha\\"+l+".png").convert_alpha(), (60, 60))

    ppic=[490,195]
    pbg1=[0,0]
    pbg2=[1000,0]
    tactu1=([195,104],[496,126],[1497,127],[2195,103],[2739,197])
    tactd1=([195,272],[739,252],[1195,271],[1739,252],[2195,273],[2496,263])
    tactu2=([3195,104],[3496,126],[4497,127],[5195,103],[5739,197])
    tactd2=([3195,272],[3739,252],[4195,271],[4739,252],[5195,273],[5496,263])    
    
    bg = pygame.transform.scale(pygame.image.load("bgf0.png").convert(), (3000, 400))
    bg2 = pygame.transform.scale(pygame.image.load("bgf.png").convert(), (3000, 400))
    
    hm = pygame.transform.scale(pygame.image.load("hm2.png").convert_alpha() , (62, 50))
    hmb = pygame.transform.scale(pygame.image.load("hm2b.png").convert_alpha() , (62, 50))
    hma = pygame.transform.scale(pygame.image.load("hm2a.png").convert_alpha() , (62, 50))
    q = pygame.transform.scale(pygame.image.load("quit.png").convert_alpha() , (50, 50))
    jauge=pygame.image.load("slowred.png").convert_alpha()
    jauge.set_colorkey((255,255,255))
    go=pygame.image.load("go.png").convert_alpha()
    s=pygame.image.load("shade0.png").convert_alpha()
    jauge1=pygame.image.load("slowred1.png").convert()
    jauge1.set_colorkey((255,255,255))
    jauge2=pygame.image.load("slowred2.png").convert()
    jauge2.set_colorkey((255,255,255))
    jauge3=pygame.image.load("slowred3.png").convert()
    jauge3.set_colorkey((255,255,255))
    jauge4=pygame.image.load("slowred4.png").convert()
    jauge4.set_colorkey((255,255,255))
    jauge5=pygame.image.load("slowred5.png").convert()
    jauge5.set_colorkey((255,255,255))
    jauge6=pygame.image.load("slowred6.png").convert()
    jauge6.set_colorkey((255,255,255))
    jauge7=pygame.image.load("slowred7.png").convert()
    jauge7.set_colorkey((255,255,255))
    jauge8=pygame.image.load("slowred8.png").convert()
    jauge8.set_colorkey((255,255,255))
    jauge9=pygame.image.load("slowred9.png").convert()
    jauge9.set_colorkey((255,255,255))
    jauge10=pygame.image.load("slowred10.png").convert()
    jauge10.set_colorkey((255,255,255))
    jauge11=pygame.image.load("slowred11.png").convert()
    jauge11.set_colorkey((255,255,255))
    jauge12=pygame.image.load("slowred12.png").convert()
    jauge12.set_colorkey((255,255,255))
    jauge13=pygame.image.load("slowred13.png").convert()
    jauge13.set_colorkey((255,255,255))
    jauge14=pygame.image.load("slowred14.png").convert()
    jauge14.set_colorkey((255,255,255))
    jauge15=pygame.image.load("slowred15.png").convert()
    jauge15.set_colorkey((255,255,255))
    jauge16=pygame.image.load("slowred16.png").convert()
    jauge16.set_colorkey((255,255,255))
    jauge17=pygame.image.load("slowred17.png").convert()
    jauge17.set_colorkey((255,255,255))
    jauge18=pygame.image.load("slowred18.png").convert()
    jauge18.set_colorkey((255,255,255))
    Lj=[jauge,jauge1,jauge2,jauge3,jauge4,jauge5,jauge6,jauge7,jauge8,jauge9,jauge10,jauge11,jauge12,jauge13,jauge14,jauge15,jauge16,jauge17,jauge18]
    
    fenetre.blit(bg, [0,0])
    pygame.display.flip()
    continuer = 1
    Lo=[[bg,[0,0]],[bg,[3000,0]],[hm,[10,195]],[q,[950,0]],[s,[0,0]],[jauge,[800,330]],[listealpha["0"],[810,0]],[listealpha["0"],[870,0]]]
    j=0
    used=0
    cent=0
    save=0
    slowon=0
    slow=0.0008
    slowpossible=1
    def end():
        c=1
        fenetre.blit(go,(0,0))
        pygame.display.flip()
        while c==1:
            for e in pygame.event.get():
                if e.type==MOUSEBUTTONUP:
                    if 390>e.pos[1]>323 and 563<e.pos[0]<898:
                        c=0
                    if e.pos[0]>950 and e.pos[1]<50:
                        pygame.quit()
                if e.type==QUIT :pygame.quit()
        ini()
    def tuyin():
        hauteurhd=Lo[2][1][1]
        hauteurbd=Lo[2][1][1]+35
        for i in tactu1:
            if 43<i[0]<68:
                if Lo[2][1][1]<i[1]:
                    end()
        for i in tactu2:
            if 43<i[0]<68:
                if Lo[2][1][1]<i[1]:
                    end()
        for i in tactd1:
            if 43<i[0]<68:
                if Lo[2][1][1]+35>i[1]:
                    end()
        for i in tactd2:
            if 43<i[0]<68:
                if Lo[2][1][1]+35>i[1]:
                    end()
    
    while continuer:
        if slowon==1:
            used=time()-timer
        if slowon==0 :
            save+=used
            used=0
        if time()-tjauge>0.001:
            tjauge=time()
            if used+save<18.001:
                Lo[5][0]=Lj[int(save+used)]
            else:
                slowpossible=0
                slowon=0
                slow=0.0008
                Lo[4][0]=pygame.image.load("shade0.png").convert_alpha()
                Lo[0][0]=bg
                Lo[1][0]=bg
                Lo[2][0]=hm
        if time()-tanimtrue>0.2 and slowon==0:
            if Lo[2][0]==hm:Lo[2][0]=hma
            else :Lo[2][0]=hm
            tanimtrue=time()
        
        if time()-t0>0.001:
            for a in Lo:
                fenetre.blit(a[0],a[1])
            pygame.display.flip()
            t0=time()
        if time()-t1>0.9:
            ta=time()-tr
            if ta<10:
                Lo[7][0]=listealpha[str(int(ta))]
            elif cent==0 and ta>99.9:
                Lo[7][0]=listealpha["0"]
                Lo[6][0]=listealpha["0"]
                Lo.append([listealpha["1"],[750,0]])
                cent=1
            elif cent==1 and ta>99.9:
                Lo[8][0]=listealpha[str(int(ta))[0]]
                Lo[7][0]=listealpha[str(int(ta))[2]]
                Lo[6][0]=listealpha[str(int(ta))[1]]    
            else :
                Lo[7][0]=listealpha[str(int(ta))[1]]
                Lo[6][0]=listealpha[str(int(ta))[0]]
            t1=time()
        if time()-ti>slow:
            tuyin()
            Lo[0][1][0]-=1
            Lo[1][1][0]-=1
            for a in [tactu1,tactu2,tactd1,tactd2]:
                for i in a :
                    i[0]-=1
                    
            ti=time()
            if Lo[0][1][0]<-3000:
                Lo[0][1][0]=3000
                for a in [tactu1,tactd1]:
                    for i in a :
                        i[0]+=6000
            if Lo[1][1][0]<-3000:
                Lo[1][1][0]=3000
                for a in [tactu2,tactd2]:
                    for i in a :
                        i[0]+=6000
        if time()-tc>0.01:
            
            if j==1:
                tc=time()
                
                Lo[2][1][1]=300*(time()-tc2)**2-300*(time()-tc2)+yi
                if Lo[2][1][1]>358:
                    Lo[2][1][1]=358
                    j=0
                    
        for e in pygame.event.get():
            if e.type==KEYDOWN:
                if e.key==K_SPACE:
                    yi=Lo[2][1][1]
                    j=1
                    tc2=time()
            if slowpossible==1:
                if e.type==KEYDOWN:
                    if e.key==K_s:
                        slow=0.008
                        slowon=1
                        timer=time()
                        Lo[4][0]=pygame.image.load("shade.png").convert_alpha()
                        Lo[2][0]=hm
                        Lo[0][0]=bg2
                        Lo[1][0]=bg2
                        Lo[2][0]=hmb
                if e.type==KEYUP:
                    if e.key==K_s:
                        slowon=0
                        slow=0.0008
                        Lo[4][0]=pygame.image.load("shade0.png").convert_alpha()
                        Lo[0][0]=bg
                        Lo[1][0]=bg
                        Lo[2][0]=hm
            if e.type==MOUSEBUTTONUP:
                if e.pos[0]>950 and e.pos[1]<50:
                    continuer=0
            if e.type==QUIT :continuer=0                    
    pygame.quit()



#Execution______
ini()
