import pygame as pg

import random

pg.init()

# def recog():
    

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 0.5
#         r.energy_threshold=300
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")       
#         query = r.recognize_google(audio, language='en-in') 
#         print(f"User said: {query}\n") 
#     except Exception :
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query


def game_loop():
    x = 30
    y = 101
    fps = 90
    grav_acc = 5
    score=0
    
    screen = pg.display.set_mode((500, 500))
    pg.display.set_caption('Flappy_ball')
    g_o=False

    game_over = False
    isfly = False
   
    pipes_cor=[]
    pipes = []
    pipe_frequency = 1500  
    last_pipe = pg.time.get_ticks()
  
    with open ('D:/projets/flappy_ball/score.txt','r') as f:
        hiscore=f.read()

    while not game_over:
        pg.time.Clock().tick(fps)

        if y > 480 or y < 20 or g_o:
            with open ('D:/Flappy ball/maain/score.txt','w') as f:
                f.write(str(hiscore))
           
       
            r1 = random.randint(1, 50)
            r2 = random.randint(1, 50)
            p1 = random.randint(0, 500)
            p2 = random.randint(0, 500)
            p3 = random.randint(0, 500)
            c1 = random.randint(0, 250)
            c2 = random.randint(0, 250)
            s1 = random.randint(50, 51)

            pg.draw.circle(screen, (225, 0, 0), (p1, p2), r1)
            pg.draw.circle(screen, (225, 0, 180), (p2, p1), r2)

            screen.blit(pg.font.SysFont(None, s1).render('^& G A M E  O V E R !@ ', True, 'black'), [50, 220])
     
            if score==int(hiscore):
                screen.blit(pg.font.SysFont(None, 70).render( str(hiscore) , True, 'blue'), [p1, p3])
                screen.blit(pg.font.SysFont(None, 70).render(str(hiscore), True, 'blue'), [p3, p2])
                screen.blit(pg.font.SysFont(None, 200).render(str(score), True, 'yellow'), [200, 290])
            else:
                screen.blit(pg.font.SysFont(None, 70).render(' 1 ', True, 'darkgreen'), [p1, p3])
                screen.blit(pg.font.SysFont(None, 70).render(' 0 ', True, 'darkgreen'), [p3, p2])
                screen.blit(pg.font.SysFont(None, 200).render(str(score), True, 'white'), [200, 290])
                screen.blit(pg.font.SysFont(None, 100).render(str(hiscore), True, 'blue'), [200, 110])
        else:

            y += grav_acc
            k_event = pg.key.get_pressed()

            if k_event[pg.K_SPACE] or k_event[pg.K_UP] or pg.mouse.get_pressed()[0]==1 :
                isfly = True

            if isfly:
                grav_acc += -0.75
                if grav_acc <= -10:
                    while True:  
                        grav_acc += 2
                        if grav_acc >= 5:
                            grav_acc = 5
                            break
                    isfly = False


            if pg.time.get_ticks() - last_pipe > pipe_frequency:
                pipe_height = random.randint(200, 300)
                pipes.append((500, pipe_height))  
                last_pipe = pg.time.get_ticks()

            
            for i, (pipe_x, pipe_height) in enumerate(pipes):
                pipe_x -= 2
                pipes_cor.append(pipe_x)
                pipes[i] = (pipe_x, pipe_height)  
           

           
                if (x + 15 > pipe_x and x - 15 < pipe_x + 50) and (y < pipe_height or y > pipe_height + 150):
                     g_o= True

           
            
            for i in pipes:
                if i[0]<-10:
                    pipes.remove(i)
                    score+=1
                    
            if int(hiscore)<score:
                hiscore=score
            
            
            screen.fill((0, 0, 0))
            if y>=380 or y<=100:
                x1=random.randint(150,165)
                screen.blit(pg.font.SysFont(None, x1).render('NO !!!' ,True,'red'),[100,200])

                xo=random.randint(70,80)
                p1=random.randint(0, 500)
                p2=random.randint(0,500)
                p3=random.randint(0, 500)
                screen.blit(pg.font.SysFont(None, xo).render('no' ,True,'red'),[p1,p2])
                screen.blit(pg.font.SysFont(None, xo).render('no' ,True,'green'),[p2,p1])
                screen.blit(pg.font.SysFont(None, xo).render('No' ,True,'blue'),[p3,p2])
                screen.blit(pg.font.SysFont(None, xo).render('No' ,True,'white'),[p1,p3])
                screen.blit(pg.font.SysFont(None, xo).render('No' ,True,'red'),[p3,p1])
                screen.blit(pg.font.SysFont(None, xo).render('No' ,True,'blue'),[p2,p3])
                screen.blit(pg.font.SysFont(None, xo).render('no' ,True,'red'),[p2,p2])
                screen.blit(pg.font.SysFont(None, xo).render('no' ,True,'blue'),[p3,p3])
            else:
                p1=random.randint(0, 500)
                p2=random.randint(0,500)
                p3=random.randint(0, 500)
                screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'darkgreen'),[p1,p2])
                screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'darkgreen'),[p2,p1])
                screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'darkgreen'),[p1,p3])
                screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'darkgreen'),[p2,p3])
                screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'darkgreen'),[p3,p2])
                screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'darkgreen'),[p3,p1])
                
            c1=random.randint(0, 225)
            c2=random.randint(0,225)
            pg.draw.circle(screen, (c1, 225, c2), (x, y), 15)

            for pipe_x, pipe_height in pipes:
                r=random.randint(0, 225)
                g=random.randint(0, 225)
                b=random.randint(0, 225)
                pg.draw.rect(screen, (r, g, b), (pipe_x, 0, 50, pipe_height))
                pg.draw.rect(screen, (r, g, b), (pipe_x, pipe_height + 150, 50, 500 - (pipe_height + 150)))  # Bottom pipe
                
           
            x01 = random.randint(40, 41)
            screen.blit(pg.font.SysFont(None, x01).render('Score : '+str(score), True, 'red'), [350, 10])
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
                

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN :
                    game_loop()

        pg.display.update()

    pg.quit()

game_loop()