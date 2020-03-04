add_library('sound')
def setup():
    fullScreen()
    frameRate(40)
    background(10)
    noStroke()
    defH()
    defJ()
    defL()
    defM()
    defO()
    defR()
    defV()
    defQ()
    defC()
    defP()
 
def draw():
    F()
    N()
    P()
    M()
    Q()
    R()
    D()
    L()
    G()
    A()
    B()
    C()
    E()
    H()
    I()
    J()
    K()    
    O()
    S()
    T()
    U()
    V()
    W()
    X()
    Y()
    Z()
    

        
 
def keyPressed():
    global flagA,flagB,flagC,flagD,flagE,flagF,flagG,flagH,flagI,flagJ,flagK,flagL,flagM,flagN,flagO,flagP,flagQ,flagR,flagS,flagT,flagU,flagV,flagW,flagX,flagY,flagZ
    if ((key == 'a')or(key=='A'))and(flagA==0):
        soundA=SoundFile(this,'piston-2.mp3')
        soundA.play()
        flagA=1
    if ((key=='b')or(key=='B'))and (flagB==0):
        flagB=1
        soundB=SoundFile(this,'flash-3.mp3')
        soundB.play()
    if ((key=='c')or(key=='C'))and(flagC==0):
        flagC=1
        soundC=SoundFile(this,'flash-1.mp3')
        soundC.play()
    if ((key=='d')or(key=='D'))and(flagD==0):
        flagD=1
        soundD=SoundFile(this,'moon.mp3')
        soundD.play()
    if ((key=='e')or(key=='E'))and(flagE==0):
        flagE=1
        soundE=SoundFile(this,'confetti.mp3')
        soundE.play()
    if((key=='f')or(key=='F'))and(flagF==0):
        flagF=1
        soundF=SoundFile(this,'corona.mp3')
        soundF.play()
    if((key=='g')or(key=='G'))and(flagG==0):
        flagG=1
        soundG=SoundFile(this,'flash-2.mp3')
        soundG.play()        
    if((key=='h')or(key=='H'))and(flagH==0):
        flagH=1
        soundH=SoundFile(this,'wipe.mp3')
        soundH.play()
    if((key=='i')or(key=='I'))and(flagI==0):
        flagI=1
        soundI=SoundFile(this,'glimmer.mp3')
        soundI.play()
    if((key=='j')or(key=='J'))and(flagJ==0):
        flagJ=1
        soundJ=SoundFile(this,'strike.mp3')
        soundJ.play()
    if((key=='k')or(key=='K'))and(flagK==0):
        flagK=1
        soundK=SoundFile(this,'pinwheel.mp3')
        soundK.play()
    if((key=='l')or(key=='L'))and(flagL==0):
        flagL=1
        soundL=SoundFile(this,'ufo.mp3')
        soundL.play()
    if((key=='m')or(key=='M'))and(flagM==0):
        flagM=1
        soundM=SoundFile(this,'splits.mp3')
        soundM.play()
    if((key=='n')or(key=='N'))and(flagN==0):
        flagN=1
        soundN=SoundFile(this,'prism-1.mp3')
        soundN.play()
    if((key=='o')or(key=='O'))and(flagO==0):
        flagO=1
        soundO=SoundFile(this,'squiggle.mp3')
        soundO.play()
    if((key=='p')or(key=='P'))and(flagP==0):
        flagP=1
        soundP=SoundFile(this,'zig-zag.mp3')
        soundP.play()
    if((key=='q')or(key=='Q'))and(flagQ==0):
        flagQ=1
        soundQ=SoundFile(this,'dotted-spiral.mp3')
        soundQ.play()
    if((key=='r')or(key=='R'))and(flagR==0):
        flagR=1
        soundR=SoundFile(this,'bubbles.mp3')
        soundR.play()
    if((key=='s')or(key=='S'))and(flagS==0):
        flagS=1
        soundS=SoundFile(this,'prism-2.mp3')
        soundS.play()
    if((key=='t')or(key=='T'))and(flagT==0):
        flagT=1
        soundT=SoundFile(this,'prism-3.mp3')
        soundT.play()
    if((key=='u')or(key=='U'))and(flagU==0):
        flagU=1
        soundU=SoundFile(this,'piston-3.mp3')
        soundU.play()
    if((key=='v')or(key=='V'))and(flagV==0):
        flagV=1
        soundV=SoundFile(this,'timer.mp3')
        soundV.play()
    if((key=='w')or(key=='W'))and(flagW==0):
        flagW=1
        soundW=SoundFile(this,'veil.mp3')
        soundW.play()
    if((key=='x')or(key=='X'))and(flagX==0):
        flagX=1
        soundX=SoundFile(this,'suspension.mp3')
        soundX.play()
    if((key=='y')or(key=='Y'))and(flagY==0):
        flagY=1
        soundY=SoundFile(this,'clay.mp3')
        soundY.play()
    if((key=='z')or(key=='Z'))and(flagZ==0):
        flagZ=1
        soundZ=SoundFile(this,'piston-1.mp3')
        soundZ.play()
        
        
                        
flagA=0
rA1=40
def A():
    global flagA,rA1
    if(flagA==1):
        fill(255)
        rect(width/6,height/6,200,200)
        fill(255,0,0)
        circle((width/6)+200,(height/6)+200,rA1)
        rA1inc()

        
def rA1inc():
    global rA1,flagA
    rA1+=10
    if(rA1>160):
        stroke(125)
        line((50*width)/60,0,(45*width)/60,height)
        line((48*width)/60,0,(43*width)/60,height)
        line((46*width)/60,0,(41*width)/60,height)
    if(rA1>240):
        flagA=0
        rA1=40
        background(10)
  
flagB=0
xB=0
xcB=50
countB=0    
def B():
    global flagB,xB,countB,xcB
    if(flagB==1):
        frameRate(30)
        fill(205,0,60)
        circle((436*width)/600,(300*height)/600,xcB)
        fill(205,50,160)
        triangle(((200*width)/600)+xB,(250*height)/600-50,((200*width)/600)+xB,(250*height/600)+50,((200*width)/600)+86+xB,(250*height)/600)
        countB+=1
        xB+=50
        xcB+=50
        if(countB>=5):
            flagB=0
            xB=0
            countB=0
            xcB=50
            background(10)

flagC=0
def defC():
    global xC,yC,aC,zC,cC
    xC=200
    yC=200
    aC=10
    zC=0
    cC=40
    
def C():
    global xC,yC,aC,zC,cC,flagC
    if(flagC==1):
        arcC()
        fill(125,125,255)
        rect(width/2+aC,height/2+zC,20,20)
        fill(240,120,0)
        circle((width/2)+(2*aC),(height/2)+(2*zC),20)
#        fill(240,120,0)
#        circle(xC+9,yC+9,40+cC)
        cC=cC+10
        if(cC>160):
            flagC=0
            cC=40
            aC=10
            zC=0
            cC=40
            bC=0
            background(10)
    
bC=0
def arcC():
    global aC,bC,zC
    ras=radians(bC)
    aC=140*sin(ras)
    zC=140*cos(ras)
    bC=bC+30
    
flagD=0
cxD=200
cyD=200

def D():
    global cxD,cyD,flagD
    if(flagD==1):
#        background(10)
        fill(255)
        circle(300,300,400)
        fill(255,125,125)
        circle(cxD,200,30)
        fill(125,255,125)
        circle(cxD,200 + 50,30)        
        fill(125,125,255)
        circle(cxD,200 + 100,30)
        cxD+=5    
        fill(255,125,125)
        circle(200+50,cyD,30)
        fill(125,255,125)
        circle(200+100,cyD,30)        
        fill(125,125,255)
        circle(200+150,cyD,30)
        cxD+=5
        cyD+=5
        if(cxD>420):
            cxD=200
            cyD=200
            flagD=0
            background(10)
            
flagE=0
countE=1
crE=100
def E():
    global flagE,countE,crE
    if(flagE==1):
        if(countE%5==0):
            fill(255,125,155)
            rect(0,0,width,height)
        if(countE%5==3):
            fill(55,125,255)
            rect(0,0,width,height)
        fill(15,150,40)
        circle(width/2,height/2,crE)
        countE+=1
        crE+=10
        if(crE>275):
            flagE=0
            crE=100
            background(10)
            
flagF=0
ryF=-500
incF=22
def F():
    global flagF,ryF,incF
    if(flagF==1):
        background(10)
        fill(275,245,115)
        rect(0,ryF,width,height)
        ryF+=incF
        if(ryF>600):
            flagF=0
            ryF=-200
            background(10)
 
flagG=0
xG=150
yG=200
wG=40
def G():
    global flagG,xG,yG,wG
    if(flagG==1):
        fill(0,255,255)
        rect((width/4)+xG,(height/4)+yG,wG,40)
        rect((width/4)+xG,(height/4)+yG+50,wG,40)
        rect((width/4)+xG,(height/4)+yG+100,wG,40)
        rect((width/4)+xG,(height/4)+yG+150,wG,40)
        wG+=20
        if(wG>300):
            flagG=0
            wG=40
            background(10)  
            
flagH=0
def defH():
    global xH,yH
    xH=width/2
    yH=height/2
    
bH=0
mH=50
def H():
    global bH,xH,yH,flagH,mH
    if(flagH==1):
        ras=radians(bH)
        aH=mH*sin(ras)
        zH =mH*cos(ras)
        bH=bH+30
        mH+=10
        fill(255,50,255)
        circle(xH+aH,yH+zH,15)
        if(bH>600):
            flagH=0
            bH=0
            mH=50
            background(10)
            
flagI=0
rI=50
def I():
    global flagI,rI
    if(flagI==1):
        fill(255,0,0)
        circle(width/3,height/3,rI)
        fill(255,255,0)
        circle((15*width)/60,(45*height)/60,rI)
        fill(255,0,255)
        circle((5*width)/6,(3*height)/6,rI)
        rI+=10
        if(rI>200):
            rI=50
            flagI=0
            background(10)    
            
flagJ=0
def defJ():
    global xJ,yJ
    xJ=(28*width)/60
    yJ=(28*height)/60
    
angJ=90
def J():
    global flagJ,xJ,yJ,angJ
    if(flagJ==1):
        noStroke()
        fill(255,150,100)
        radJ=radians(angJ)
        x1J=xJ+(120*sin(radJ))
        y1J=yJ+(120*cos(radJ))
        rect(x1J,y1J,40,40,125,125,125,125)
        fill(125,125,220)
        x2J=xJ+(80*sin(radJ))
        y2J=yJ+(80*cos(radJ))
        rect(x2J,y2J,40,40,125,125,125,125)
        fill(100,225,100)
        x3J=xJ+(40*sin(radJ))
        y3J=yJ+(40*cos(radJ))
        rect(x3J,y3J,40,40,125,125,125,125)
        fill(255,150,100)
        rad1J=radians(angJ+180)
        x4J=xJ+(120*sin(rad1J))
        y4J=yJ+(120*cos(rad1J))
        rect(x4J,y4J,40,40,125,125,125,125)
        fill(125,125,220)
        x5J=xJ+(80*sin(rad1J))
        y5J=yJ+(80*cos(rad1J))
        rect(x5J,y5J,40,40,125,125,125,125)
        fill(100,225,100)
        x6J=xJ+(40*sin(rad1J))
        y6J=yJ+(40*cos(rad1J))
        rect(x6J,y6J,40,40,125,125,125,125)
        angJ+=5
        if(angJ==180):
            flagJ=0
            angJ=90
            background(10)
        
        
    
flagK=0
yK=-225
def K():
    global flagK,yK
    if(flagK==1):
        fill(0)
        noStroke()
        fill(10)
        circle((2*width/3),yK,300)
        fill(100,225,100)
        circle((2*width/3),yK,250)
        fill(125,125,220)
        circle((2*width)/3,yK,200)
        fill(255,150,100)
        circle((2*width/3),yK,150)
        yK+=19
        if(yK>height/2):
            yK=-225
            flagK=0
            background(10)
        
    
flagL=0
def defL():
    global x1L,y2L,x3L,y4L
    x1L=(2*width)/60
    y2L=(2*height)/60
    x3L=width
    y4L=height
    
def L():
    global flagL,x1L,y2L,x3L,y4L
    if(flagL==1):
        noStroke()
        fill(125,255,255)
        rect(0,(29*height)/60,x1L,20,125,125,125,125)
        rect((29.5*width)/60,0,20,y2L,125,125,125,125)
        rect(x3L,height/2,x1L,20,125,125,125,125)
        rect(width/2,y4L,20,y2L,125,125,125,125)
        x1L+=(2*width)/60
        y2L+=(2*height)/60
        x3L-=(2*width)/60
        y4L-=(2*height)/60
        if(x1L>width):
            flagL=0
            x1L=(2*width)/60
            y2L=(2*height)/60
            x3L=width
            y4L=height
            background(10)
            
        
        

flagM=0
def defM():
    global x1M,x2M,y3M,y4M
    x1M=width/2
    x2M=width/2
    y3M=height/2
    y4M=height/2
    
def M():
    global flagM,x1M,x2M,y3M,y4M
    if(flagM==1):
        background(10)
        fill(125,125,255)
        circle(x1M,height/2,60)
        circle(x2M,height/2,60)
        circle(width/2,y3M,60)
        circle(width/2,y4M,60)
        fill(240,120,0)
        circle(x1M,y3M,40)
        circle(x1M,y4M,40)
        circle(x2M,y3M,40)
        circle(x2M,y4M,40)
        x1M+=(2*width)/60
        x2M-=(2*width)/60
        y3M+=(2*height)/60
        y4M-=(2*height)/60
        if(x1M>width):
            x1M=width/2
            x2M=width/2
            y3M=height/2
            y4M=height/2
            flagM=0
            background(10)


flagN=0
flag2N=0
countN=0
def N():
    global flagN,countN,flag2N
    if(flagN==1)and(flag2N==0):
        fill(255,132,205,195)
        rect(0,0,width,height)
        flag2N=1
    if(flagN==1)and(flag2N==1):
        countN+=1
        if(countN>30):
            background(10)
            countN=0
            flagN=0
            flag2N=0
    
flagO=0
def defO():
    global xO,yO
    xO=width/2
    yO=height/2
    
angO=0
mO=300
def O():
    global flagO,xO,yO,angO,mO
    if(flagO==1):
        ras=radians(angO)
        x=mO*sin(ras)
        y=mO*cos(ras)
        mO-=10
        angO+=30
        fill(255,125,125)
        rect(xO+x,yO+y,20,20,125,125,125,125)
        if(angO>700):
            flagO=0
            xO=width/2
            yO=height/2
            angO=0
            mO=300
            background(10)
            
        
    
flagP=0
def defP():
    global x1P,y1P,x2P,y2P,x3P,y3P,x4P,y4P
    x1P=20*width/600
    y1P=300*height/600
    x2P=320*width/600
    y2P=580*height/600
    x3P=580*width/600
    y3P=260*height/600
    x4P=260*width/600
    y4P=20*height/600
    
def P():
    global flagP,x1P,y1P,x2P,y2P,x3P,y3P,x4P,y4P
    if(flagP==1):
        noStroke()
        fill(126,25,123)
        quad(0,280*height/600,x1P,y1P,x1P,y1P+20,0,300*height/600)
        quad(width/2,height,320*width/600,height,x2P+20,y2P,x2P,y2P)
        quad(width,height,width,280*height/600,x3P,y3P,x3P,y3P+20)
        quad(width/2,0,280*width/600,0,x4P,y4P,x4P+20,y4P)
        fill(123,145,23)
        quad(20,280,x1P+20,y1P,x1P+20,y1P+20,20,300)
        quad(300,580,320,580,x2P+20,y2P-20,x2P,y2P-20)
        quad(580,300,580,280,x3P-20,y3P,x3P-20,y3P+20)
        quad(300,20,280,20,x4P,y4P+20,x4P+20,y4P+20)
        fill(126,25,123)
        quad(40,280,x1P+40,y1P,x1P+40,y1P+20,40,300)
        quad(300,560,320,560,x2P+20,y2P-40,x2P,y2P-40)
        quad(560,300,560,280,x3P-40,y3P,x3P-40,y3P+20)
        quad(300,40,280,40,x4P,y4P+40,x4P+20,y4P+40)
        x1P+=20
        y1P+=20
        x2P+=20
        y2P-=20
        x3P-=20
        y3P-=20
        x4P-=20
        y4P+=20
        if(x1P>340):
            flagP=0
            x1P=20
            y1P=300
            x2P=320
            y2P=580
            x3P=580
            y3P=260
            x4P=260
            y4P=20
            background(10)
                
                
                
                
flagQ=0
def defQ():
    global y1Q,y2Q,x3Q,x4Q
    y1Q=height/2
    y2Q=height/2
    x3Q=width/2
    x4Q=width/2
    
    
def Q():
    global x1Q,x2Q,x3Q,x4Q,y1Q,y2Q,y3Q,y4Q,flagQ
    if(flagQ==1):
        fill(255,125,125,125)
        triangle(width/2,height/2,0,height/2,0,y1Q)
        triangle(width/2,height/2,width,height/2,width,y2Q)
        triangle(width/2,height/2,width/2,0,x3Q,0)
        triangle(width/2,height/2,width/2,height,x4Q,height)
        y1Q-=10
        y2Q+=10
        x3Q+=10
        x4Q-=10
        if(y2Q>1000):
            y1Q=height/2
            y2Q=height/2
            x3Q=width/2
            x4Q=width/2
            background(10)
            flagQ=0
            
        
         
        
    
flagR=0
def defR():
    global xqR,yqR,xtR,ytR
    xqR=(125*width)/600
    yqR=(125*height)/600
    xtR=(550*width)/600
    ytR=(550*height)/600
    
def R():
    global flagR,xqR,yqR,ytR,xtR
    if(flagR==1):
        fill(0,125,255)
        quad(0,height/6,width/6,0,xqR,0,0,yqR)
        fill(255,125,0)
        triangle(width,height,width,ytR,xtR,height)
        xqR+=width/60
        yqR+=height/60
        xtR-=width/60
        ytR-=height/60
        if(xqR>(55*width)/60):
            xqR=(125*width)/600
            yqR=(125*height)/600
            xtR=(550*width)/600
            ytR=(550*height)/600
            background(10)
            flagR=0
        
flagS=0
rS=500
def S():
    global flagS,rS
    if(flagS==1):
        crS=random(0,255)
        cgS=random(0,255)
        cbS=random(0,255)
        fill(crS,cgS,cbS)
        circle(width/2,height/2,rS)
        rS-=30
        if(rS<30):
            rS=500
            flagS=0
            background(10)
            
        
    
flagT=0
angT=0
mT=20
x1T=200
y1T=100
x2T=200
y2T=400
x3T=500
y3T=300
def T():
    global flagT,angT,mT,x1T,y1T,x2T,y2T,x3T,y3T
    if(flagT==1):
        fill(198,123,36)
        rad=radians(angT)
        x=mT*sin(rad)
        y=mT*cos(rad)
        mT+=3
        angT+=20
        circle((width/2)+x1T+x,(height/4)+y1T+y,10)
        circle((width/4)+x2T+x,(height/3)+y2T+y,10)
        circle((width/3)+x3T+x,(height/2)+y3T+y,10)
        if(angT>400):
            flagT=0
            angT=0
            mT=20
            x1T=100
            y1T=100
            background(10)
        
        
    
flagU=0
x1U=400
x2U=20
def U():
    global flagU,x1U,x2U
    if(flagU==1):
        fill(512,356,122)
        rect((width/4)+x1U,(height/4)+180,x2U,30)
        rect((width/4)+x1U,(height/4)+220,x2U,30)
        rect((width/4)+x1U,(height/4)+260,x2U,30)
        rect((width/4)+x1U,(height/4)+300,x2U,30)
        rect((width/4)+x1U,(height/4)+340,x2U,30)
        rect((width/4)+x1U,(height/4)+380,x2U,30)
        x1U-=20
        x2U+=20
        if(x2U>300):
            x1U=400
            x2U=20
            background(10)
            flagU=0
    
flagV=0
def defV():
    global x1V,x2V,y1V,y2V
    x1V=0
    x2V=width
    y1V=0
    y2V=height
def V():
    global x1V,y1V,x2V,y2V,flagV
    if(flagV==1):
        r=random(0,256)
        g=random(0,256)
        b=random(0,256)
        fill(r,g,b)
        triangle(0,0,x1V,0,0,y1V)
        triangle(0,height,x1V,height,0,y2V)
        triangle(width,0,x2V,0,width,y1V)
        triangle(width,height,x2V,height,width,y2V)
        x1V+=(20*width)/600
        y1V+=(20*height)/600
        x2V-=(20*width)/600
        y2V-=(20*height)/600
        if(x1V>width/2):
            x1V=0
            x2V=width
            y1V=0
            y2V=height
            background(10)
            flagV=0
    
flagW=0
x1W=300
y1W=300
x2W=300
y2W=300
flag1W=0
def W():
    global x1W,x2W,y1W,y2W,flagW,flag1W
    if(flagW==1):
      background(10)
      fill(123,124,145)
      arc(x1W+400,y1W+200, 300, 300, QUARTER_PI, PI+QUARTER_PI)
      arc(x2W+400,y2W+200, 300, 300, PI+QUARTER_PI, PI+PI+QUARTER_PI)  
      x1W-=10
      x2W+=10
      y1W+=10
      y2W-=10
      if(x1W<250):
          x1W=300
          x2W=300
          y1W=300
          y2W=300
          flagW=0
          flag1W=0
          background(10)
          
    
flagX=0
x1X=300
y1X=300
x2X=300
y2X=300
x3X=300
y3X=300
x4X=300
y4X=300
def X():
    global flagX,x1X,y1X,x2X,y2X,x3X,y3X,x4X,y4X
    if(flagX==1):
        fill(213,125,11)
        arc(x1X,y1X,200,200,PI,PI+HALF_PI)
        arc(x2X,y2X,200,200,PI+HALF_PI,PI+PI)
        arc(x3X,y3X,200,200,0,HALF_PI)
        arc(x4X,y4X,200,200,HALF_PI,PI)
        fill(123,215,61)
        arc(x1X,y1X,200,200,QUARTER_PI+PI,QUARTER_PI+PI+HALF_PI)
        arc(x2X,y2X,200,200,QUARTER_PI+PI+HALF_PI,QUARTER_PI+PI+PI)
        arc(x3X,y3X,200,200,QUARTER_PI,QUARTER_PI+HALF_PI)
        arc(x4X,y4X,200,200,QUARTER_PI+HALF_PI,QUARTER_PI+PI)
        x1X-=10
        y1X-=10
        x2X+=10
        y2X-=10
        x3X+=10
        y3X+=10
        x4X-=10
        y4X+=10
        if(x1X<100):
            x1X=300
            y1X=300
            x2X=300
            y2X=300
            x3X=300
            y3X=300
            x4X=300
            y4X=300
            background(10)
            flagX=0
    
flagY=0
angY=10
def Y():
    global flagY, angY
    if(flagY==1):
       angY+=10
       fill(237,171,26)
       rad=radians(angY)
       arc(width/2,height/2,height/2,height/2,0,rad)
       if(angY>410):
            angY=10
            flagY=0
            background(10)
    
    
flagZ=0
aZ=0
def Z():
    global flagZ,aZ
    if(flagZ==1):
        fill(26,232,237)
        stroke(233,167,38)
        triangle((width/2)+200-aZ,(height/2)+200-aZ,(width/2)+400+aZ,(height/2)+200-aZ,(width/2)+300,(height/2)+350+aZ)
        aZ+=5
        if(aZ>100):
            aZ=0
            flagZ=0
            background(10)
            aZ=0
