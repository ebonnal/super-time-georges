import pygame
from pygame.locals import *
from time import *
from random import *
pygame.mixer.pre_init(100000,-16,2,2048)
pygame.init()
pygame.key.set_repeat(10000000,3)
fenetre = pygame.display.set_mode((1024,512))
pygame.display.set_caption("Super Time George")
def ini():
    global timmortal,vies,Lt,save
    
    rang=0
    tnuage=time()
    timmortal,tb,t0,t1,ti,tc,tc2,tanim,tr=time(),time(),time(),time(),time(),time(),time(),time(),time()
    tanimtrue=t0
    tjauge=time()
    listealpha={}
    for l in ["0","1","2","3","4","5","6","7","8","9","p1","p2","p3","p4","p5","p6","p7","p8","p9","p0"]:
        listealpha[l]=pygame.transform.scale(pygame.image.load("Alpha/"+l+".png").convert_alpha(), (60, 60))
    bg = pygame.image.load("f1.png").convert()
    bg2 = pygame.image.load("f2.png").convert()
    bgbg=pygame.image.load("ff.png").convert()
    tu = pygame.image.load("tubehc.png").convert_alpha()
    nuage = pygame.image.load("cloud.png").convert_alpha()
    td = pygame.image.load("tubeb3.png").convert_alpha()
    ts = pygame.image.load("tubehcs.png").convert_alpha()
    te = pygame.image.load("tubehce.png").convert_alpha()
    k=pygame.transform.scale(pygame.image.load("keur.png").convert_alpha(), (40, 40))
    
    
    hm = pygame.transform.scale(pygame.image.load("hm2.png").convert_alpha() , (62, 50))
    hmb = pygame.transform.scale(pygame.image.load("hm2b.png").convert_alpha() , (62, 50))
    hma = pygame.transform.scale(pygame.image.load("hm2a.png").convert_alpha() , (62, 50))
    q = pygame.transform.scale(pygame.image.load("quit.png").convert_alpha() , (70, 70))
    jauge=pygame.image.load("slowred.png").convert()
    
    go=pygame.image.load("go.png").convert_alpha()
    s=pygame.image.load("shade0.png").convert_alpha()
    jauge1=pygame.image.load("slowred1.png").convert_alpha()
    jauge2=pygame.image.load("slowred2.png").convert_alpha()
    jauge3=pygame.image.load("slowred3.png").convert_alpha()
    jauge4=pygame.image.load("slowred4.png").convert_alpha()
    jauge5=pygame.image.load("slowred5.png").convert_alpha()
    jauge6=pygame.image.load("slowred6.png").convert_alpha()
    jauge7=pygame.image.load("slowred7.png").convert_alpha()
    jauge8=pygame.image.load("slowred8.png").convert_alpha()
    jauge9=pygame.image.load("slowred9.png").convert_alpha()
    jauge10=pygame.image.load("slowred10.png").convert_alpha()
    jauge11=pygame.image.load("slowred11.png").convert_alpha()
    jauge12=pygame.image.load("slowred12.png").convert_alpha()
    jauge13=pygame.image.load("slowred13.png").convert_alpha()
    jauge14=pygame.image.load("slowred14.png").convert_alpha()
    jauge15=pygame.image.load("slowred15.png").convert_alpha()
    jauge16=pygame.image.load("slowred16.png").convert_alpha()
    jauge17=pygame.image.load("slowred17.png").convert_alpha()
    
    jauge18=pygame.image.load("slowred18.png").convert_alpha()
   
    Lj=[jauge,jauge1,jauge2,jauge3,jauge4,jauge5,jauge6,jauge7,jauge8,jauge9,jauge10,jauge11,jauge12,jauge13,jauge14,jauge15,jauge16,jauge17,jauge18]
    
    fenetre.blit(bg, [0,0])
    pygame.display.flip()
    continuer = 1
    #objets 1697
    n=[nuage,[600,5]]
    bgs=[[bg,[0,0]],[bg2,[1697,0]]]
    superh=[hm,[10,250]]
    quitbutton=[q,[960,-5]]
    shade=[s,[0,0]]
    jaugeact=[jauge,[824,442]]
    Lt=[[tu,[1200,0]],[td,[1200,450]]]
    Lchrono=[[listealpha["p0"],[780,0]],[listealpha["p0"],[840,0]],[listealpha["p0"],[900,0]]]
    
    
    #__________                            
    j=0
    vies=3
    used=0
    randLt=[td,tu]
    uod=0
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
                    if 468>e.pos[1]>382 and 270<e.pos[0]<614:
                        c=0
                    if e.pos[0]>968 and e.pos[1]<60:
                        start()
                if e.type==KEYDOWN:
                    if e.key not in [K_SPACE,K_s]:
                        c=0
                if e.type==QUIT :pygame.quit()
        ini()
    def tuyin():
        global timmortal,vies,Lt,save
        
        if time()-timmortal>0.2+2.8*slowon:
            idel=-1
            i=0
            while i<len(Lt):
                if Lt[i][0]==tu:
                    if -18<Lt[i][1][0]<50:
                        if 185+Lt[i][1][1]<superh[1][1]<254+Lt[i][1][1]:
                            vies-=1
                            timmortal=time()
                            if vies==-1:
                                end()
                elif Lt[i][0]==td:
                    
                    if -45<Lt[i][1][0]<68:
                        if superh[1][1]+35>Lt[i][1][1]:
                            
                            timmortal=time()
                            vies-=1
                            if vies==-1:
                                end()
                elif Lt[i][0]==te:
                    if -18<Lt[i][1][0]<50:
                        if 175+Lt[i][1][1]<superh[1][1]<254+Lt[i][1][1]:
                            if slowpossible==1:save+=1
                            Lt=[]
                            
                            
                            
                else:
                    if -18<Lt[i][1][0]<50:
                        if 175+Lt[i][1][1]<superh[1][1]<254+Lt[i][1][1]:
                            if vies !=3:
                                vies+=1
                            if save!=0 and slowpossible==1:save-=1
                            idel=i
                i+=1
            if idel!=-1: del Lt[idel]
            
            
                            
                        
      
    while continuer:
        if slowpossible==0:
            slow=0.0008
            slowpossible=2
        if slowon==1:
            used=time()-timer
        if slowon==0 :
            save+=used
            used=0
        if time()-tjauge>0.001:
            tjauge=time()
            if used+save<17.5 and slowpossible==1:
                jaugeact[0]=Lj[int(save+used)]
            elif slowpossible==1:
                
                jaugeact[0]=Lj[18]
                slowpossible=0
                slowon=0
                slow=0.0008
                
                shade[0]=pygame.image.load("shade0.png").convert_alpha()
                
                superh[0]=hm
        if time()-tanimtrue>0.2 and slowon==0:
            if superh[0]==hm:superh[0]=hma
            else :superh[0]=hm
            tanimtrue=time()
        if time()-tb>slow*2:
            tb=time()
            
            
            if bgs[0][1][0]<-1697:bgs[0][1][0]=1697
            if bgs[1][1][0]<-1697:bgs[1][1][0]=1697
            bgs[0][1][0]-=1
            bgs[1][1][0]-=1
        if time()-tnuage>slow*4:
            tnuage=time()
            n[1][0]-=1
            if n[1][0]<-2000:
                n[1][0]=1024
        if time()-t0>slow:
            t0=time()
            tuyin()
            if Lt!=[]:
                for a in Lt:
                    a[1][0]-=1
                    if a[1][0]<-90:del a
            
                
            
            
            fenetre.blit(bgbg,[0,0])
            fenetre.blit(bgs[0][0],bgs[0][1])
            fenetre.blit(bgs[1][0],bgs[1][1])
            fenetre.blit(n[0],n[1])
            if Lt!=[[]]:
                for a in Lt:
                    fenetre.blit(a[0],a[1])
                
            for a in [superh]+[shade]+Lchrono+[quitbutton]+[jaugeact]:
                fenetre.blit(a[0],a[1])
            for i in range(vies):
                fenetre.blit(k,[10+i*50,10])
            pygame.display.flip()
            
            #______
        if time()-t1>0.3:
            
            if uod==1:uod=0
            else:uod=randint(0,1)
            randpos=[randint(1024,1090),randint(222-472*uod,500-500*uod)]
            if randint(0,5)==1 and uod==1 :Lt.append([te,randpos])
            elif randint(0,15)==1 and uod==1 :Lt.append([ts,randpos])
            else:Lt.append([randLt[uod],randpos])
            if randint(0,1)==1:
                if 326<randpos[1] or randpos[1]<-65:
                    uod=abs(uod-1)
                    Lt.append([randLt[uod],[randpos[0],256-randpos[1]]])            
            ta=time()-tr
            if ta<10:
                Lchrono[2][0]=listealpha["p"+str(int(ta))]
            
            elif int(ta)>99:
                Lchrono[0][0]=listealpha["p"+str(int(ta))[0]]
                Lchrono[1][0]=listealpha["p"+str(int(ta))[1]]
                Lchrono[2][0]=listealpha["p"+str(int(ta))[2]]
            else :
                Lchrono[2][0]=listealpha["p"+str(int(ta))[1]]
                Lchrono[1][0]=listealpha["p"+str(int(ta))[0]]
            t1=time()

            
        if time()-tc>0.01:
            
            if j==1:
                tc=time()
                
                superh[1][1]=500*(time()-tc2)**2-300*(time()-tc2)+yi
                if -42>superh[1][1] or superh[1][1]>562:
                    end()
                    
        for e in pygame.event.get():
            if e.type==KEYDOWN:
                if e.key==K_SPACE:
                    yi=superh[1][1]
                    j=1
                    tc2=time()              
            if slowpossible==1:
                if e.type==KEYDOWN:
                    if e.key==K_s:
                        slow=0.008
                        slowon=1
                        timer=time()
                        shade[0]=pygame.image.load("shade.png").convert_alpha()
                        superh[0]=hmb
                if e.type==KEYUP:
                    if e.key==K_s:
                        slowon=0
                        slow=0.0008
                        shade[0]=pygame.image.load("shade0.png").convert_alpha()
                        
                        superh[0]=hm
            if e.type==MOUSEBUTTONUP:
                if e.pos[0]>968 and e.pos[1]<70:
                    start()
            if e.type==QUIT :continuer=0                    
    pygame.quit()


def start():
    s1 = pygame.image.load("start1.png").convert()
    s2 = pygame.image.load("start2.png").convert()
    s3 = pygame.image.load("start3.png").convert()
    s4 = pygame.image.load("start4.png").convert()
    Ls=[s1,s2,s3,s4]
    continuer=1
    fenetre.blit(s1, [0,0])
    pygame.display.flip()
    statut=1
    while continuer==1:
        for e in pygame.event.get():
            if e.type==KEYDOWN or e.type==MOUSEBUTTONUP:
                if statut==4:ini()
                else:
                    fenetre.blit(Ls[statut], [0,0])
                    pygame.display.flip()
                    statut+=1
            
            if e.type==QUIT :pygame.quit()                    
        
        
        
    
#Execution______
start()
