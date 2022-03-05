import pygame, sys
from pygame.locals import *
import math
from time import sleep
from time import strftime
import os

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((602, 700))
pygame.display.set_caption('LỘN XỘN')
Trang=(255,255,255)
Den=(0,0,0)
Xanhla=(0,255,0)
Do=(255,0,0)
Xanhduong=(0,178,191)
xanhps=(0,210,255)
xanhden=(0,39,50)

def app(link):
    os.startfile(link)


def hamchu(chu, mau, ngang, doc, cochu):
    font = pygame.font.SysFont('Calibri', cochu)
    chu_ra = font.render(chu, True, mau)
    window.blit(chu_ra, [ngang, doc])

while True:
    pygame.display.flip()
    clock.tick(10)
    event_list = pygame.event.get()

    for event in event_list:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mouse = pygame.mouse.get_pos() 

    window.fill((67,81,109))

    hamchu("ADOBE", Trang, 20,10,30)

    pygame.draw.rect(window, xanhden, (50, 50, 100, 100))
    pygame.draw.line(window, xanhps, (50, 50), (50,152),5)
    pygame.draw.line(window, xanhps, (48, 50), (150,50),5)
    pygame.draw.line(window, xanhps, (150, 48), (150,150),5)
    pygame.draw.line(window, xanhps, (50, 150), (152,150),5)
    hamchu("PS", xanhps,62,66,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 48 <= mouse[0] <= 152 and 50 <= mouse[1] <= 150:
        	if event.button == 1:
        		app("D:\Edit video\Adobe.Photoshop.CC.2019.20.0.6.27696.Multilingual.Plugins.Portable\App\Ps\Photoshop.exe")
        		pygame.quit()
        		sys.exit()

    pygame.draw.rect(window, (27,1,36), (250, 50, 100, 100))
    pygame.draw.line(window, (223,118,255), (250, 50), (250,152),5)
    pygame.draw.line(window, (223,118,255), (248, 50), (350,50),5)
    pygame.draw.line(window, (223,118,255), (350, 48), (350,150),5)
    pygame.draw.line(window, (223,118,255), (250, 150), (352,150),5)
    hamchu("PR", (223,118,255),260,66,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 248 <= mouse[0] <= 352 and 50 <= mouse[1] <= 150:
        	if event.button == 1:
        		app("D:\Edit video\Premiere.Pro.13\App\Pr\Adobe Premiere Pro.exe")
        		pygame.quit()
        		sys.exit()


    pygame.draw.rect(window, (25,0,62), (450, 50, 100, 100))
    pygame.draw.line(window, (211,146,255), (450, 50), (450,152),5)
    pygame.draw.line(window, (211,146,255), (448, 50), (550,50),5)
    pygame.draw.line(window, (211,146,255), (550, 48), (550,150),5)
    pygame.draw.line(window, (211,146,255), (450, 150), (552,150),5)
    hamchu("AE", (211,146,255),460,66,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 448 <= mouse[0] <= 552 and 50 <= mouse[1] <= 150:
        	if event.button == 1:
        		app("D:\Edit video\After.Effects.16\App\Ae\AfterFX.exe")
        		pygame.quit()
        		sys.exit()

    
    #fsdfsdaf
    hamchu("TĂNG TỐC", Trang, 20,205,30)

    pygame.draw.rect(window, (19,18,18), (50, 250, 100, 100))
    pygame.draw.line(window, (248,38,41), (50, 250), (50,352),5)
    pygame.draw.line(window, (248,38,41), (48, 250), (150,250),5)
    pygame.draw.line(window, (248,38,41), (150, 248), (150,350),5)
    pygame.draw.line(window, (248,38,41), (50, 350), (152,350),5)
    hamchu("db", (248,38,41),59,266,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 48 <= mouse[0] <= 152 and 250 <= mouse[1] <= 350:
        	if event.button == 1:
        		app("C:\Program Files (x86)\IObit\Driver Booster\8.3.0\DriverBooster.exe")
        		pygame.quit()
        		sys.exit()


    pygame.draw.rect(window, (24,26,28), (250, 250, 100, 100))
    pygame.draw.line(window, (0,169,255), (250, 250), (250,352),5)
    pygame.draw.line(window, (0,169,255), (248, 250), (350,250),5)
    pygame.draw.line(window, (0,169,255), (350, 248), (350,350),5)
    pygame.draw.line(window, (0,169,255), (250, 350), (352,350),5)
    hamchu("AS", (0,169,255),260,266,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 248 <= mouse[0] <= 352 and 250 <= mouse[1] <= 350:
        	if event.button == 1:
        		app("C:\Program Files (x86)\IObit\Advanced SystemCare\ASC.exe")
        		pygame.quit()
        		sys.exit()


    pygame.draw.rect(window, (32,34,34), (450, 250, 100, 100))
    pygame.draw.line(window, (255,9,9), (450, 250), (450,352),5)
    pygame.draw.line(window, (255,9,9), (448, 250), (550,250),5)
    pygame.draw.line(window, (255,9,9), (550, 248), (550,350),5)
    pygame.draw.line(window, (255,9,9), (450, 350), (552,350),5)
    hamchu("SG", (255,9,9),460,266,80)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 448 <= mouse[0] <= 552 and 250 <= mouse[1] <= 350:
        	if event.button == 1:
        		app("C:\Program Files (x86)\PCGameBoost\Smart Game Booster\SgbMain.exe")
        		pygame.quit()
        		sys.exit()

    #fsadfsdfsa
    hamchu("LẶT VẶT", Trang, 20,405,30)

    pygame.draw.rect(window, (235,176,0), (50, 450, 100, 100))
    pygame.draw.rect(window, (67,81,109), (90,490,20,20))
    pygame.draw.rect(window, (67,81,109), (120,460,20,80))
    pygame.draw.rect(window, (67,81,109), (60,460,20,80))
    pygame.draw.rect(window, (67,81,109), (60,460,80,20))
    pygame.draw.rect(window, (67,81,109), (60,520,80,20))

    pygame.draw.rect(window, (67,81,109), (90,450,20,10))
    pygame.draw.rect(window, (67,81,109), (90,540,20,20))
    pygame.draw.rect(window, (67,81,109), (50,490,20,20))
    pygame.draw.rect(window, (67,81,109), (140,490,20,20))

    pygame.draw.rect(window, (67,81,109), (95,480,10,10))
    pygame.draw.rect(window, (67,81,109), (95,510,10,10))
    pygame.draw.rect(window, (67,81,109), (80,495,10,10))
    pygame.draw.rect(window, (67,81,109), (110,495,10,10))

    pygame.draw.polygon(window, (235,176,0),((60,450),(90,480),(80,490),(50,460)))
    pygame.draw.polygon(window, (235,176,0),((140,450),(149,460),(120,490),(110,480)))
    pygame.draw.polygon(window, (235,176,0),((140,549),(149,540),(120,510),(110,520)))
    pygame.draw.polygon(window, (235,176,0),((60,549),(50,540),(80,510),(90,520)))



    if event.type == pygame.MOUSEBUTTONDOWN:
        if 50 <= mouse[0] <= 150 and 450 <= mouse[1] <= 550:
        	if event.button == 1:
        		app(r"C:\Program Files (x86)\VMware\VMware Player\vmplayer.exe")
        		pygame.quit()
        		sys.exit()


    pygame.draw.rect(window, (13,139,230), (250, 450, 100, 100))
    pygame.draw.circle(window, (255,255,255), (300,500),45)
    pygame.draw.rect(window, (13,139,230), (280, 495, 40, 10))
    pygame.draw.polygon(window, (13,139,230),((270,500),(285,510),(280,500),(285,490)))
    pygame.draw.polygon(window, (13,139,230),((320,500),(315,490),(330,500),(315,510)))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if 250 <= mouse[0] <= 350 and 450 <= mouse[1] <= 550:
        	if event.button == 1:
        		app("C:\Program Files (x86)\TeamViewer\TeamViewer.exe")
        		pygame.quit()
        		sys.exit()


    pygame.draw.rect(window, (42,123,207), (450, 450, 100, 100))
    pygame.draw.line(window, (255,255,255), (450, 450), (450,552),5)
    pygame.draw.line(window, (255,255,255), (448, 450), (550,450),5)
    pygame.draw.line(window, (255,255,255), (550, 448), (550,550),5)
    pygame.draw.line(window, (255,255,255), (450, 550), (552,550),5)
    pygame.draw.rect(window, (255,255,255), (474,474,52,40))
    pygame.draw.rect(window, (255,255,255), (487,510,26,15))
    pygame.draw.rect(window, (255,255,255), (474,520,52,5))
    pygame.draw.rect(window, (42,123,207), (479,479,42,30))
    pygame.draw.polygon(window, (255,255,255),((481,481),(481,507),(519,481)))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if 448 <= mouse[0] <= 552 and 450 <= mouse[1] <= 550:
        	if event.button == 1:
        		app(r"C:\Program Files (x86)\UltraViewer\UltraViewer_Desktop.exe")
        		pygame.quit()
        		sys.exit()

    pygame.draw.rect(window, (12,161,166), (250, 585, 100, 100))
    pygame.draw.circle(window, (255,255,255), (280,635),23,4)
    pygame.draw.circle(window, (255,255,255), (320,635),23,4)
    pygame.draw.rect(window, (255,255,255), (270,630,20,10))
    pygame.draw.rect(window, (255,255,255), (310,630,20,10))
    pygame.draw.rect(window, (255,255,255), (315,625,10,20))


    if event.type == pygame.MOUSEBUTTONDOWN:
        if 250 <= mouse[0] <= 350 and 585 <= mouse[1] <= 685:
        	if event.button == 1:
        		app(R"C:\Program Files (x86)\Arduino\arduino.exe")
        		pygame.quit()
        		sys.exit()



    pygame.display.update()
pygame.quit()
exit()