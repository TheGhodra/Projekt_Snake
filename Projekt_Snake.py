import pygame, sys, random, shelve
from pygame.math import Vector2
from button import Button
pygame.init()


programIcon = pygame.image.load("Bilddateien\Körper_Schlange\Snake_Symbol.PNG")  #Icon in der linken oberen Ecke der GUI
pygame.display.set_icon(programIcon)

pygame.display.set_caption("Projekt: Snake")


class Schlange:
    def __init__(self):
        self.body = [Vector2(5,9),Vector2(4,9),Vector2(3,9)] #Kreiert Schlangenkörper
        self.Richtung = Vector2(0,0)
        self.Verlängerung = False
        
        self.Kopf_links = pygame.image.load('Bilddateien\Körper_Schlange\Kopf_links.png').convert_alpha()        #kreiert die Kopfanimation
        self.Kopf_rechts = pygame.image.load('Bilddateien\Körper_Schlange\Kopf_rechts.png').convert_alpha()
        self.Kopf_oben = pygame.image.load('Bilddateien\Körper_Schlange\Kopf_unten.png').convert_alpha()
        self.Kopf_unten = pygame.image.load('Bilddateien\Körper_Schlange\Kopf_oben.png').convert_alpha()

        self.Körper_LO = pygame.image.load('Bilddateien\Körper_Schlange\LO.png').convert_alpha()                 # kreiert die Körperanimation
        self.Körper_RO = pygame.image.load('Bilddateien\Körper_Schlange\RO.png').convert_alpha()
        self.Körper_LU = pygame.image.load('Bilddateien\Körper_Schlange\LU.png').convert_alpha()
        self.Körper_RU = pygame.image.load('Bilddateien\Körper_Schlange\RU.png').convert_alpha()

        self.Schwanz_rechts = pygame.image.load('Bilddateien\Körper_Schlange\Schwanz_links.png').convert_alpha()  # kreiert die Schwanzanimation
        self.Schwanz_links = pygame.image.load('Bilddateien\Körper_Schlange\Schwanz_rechts.png').convert_alpha()
        self.Schwanz_unten = pygame.image.load('Bilddateien\Körper_Schlange\Schwanz_unten.png').convert_alpha()
        self.Schwanz_oben = pygame.image.load('Bilddateien\Körper_Schlange\Schwanz_oben.png').convert_alpha()

        self.Körper_links = pygame.image.load('Bilddateien\Körper_Schlange\Korper_links.png').convert_alpha()    # kreiert die Körperanimation
        self.Körper_rechts = pygame.image.load('Bilddateien\Körper_Schlange\Korper_rechts.png').convert_alpha()
        self.Körper_unten = pygame.image.load('Bilddateien\Körper_Schlange\Korper_unten.png').convert_alpha()
        self.Körper_oben = pygame.image.load('Bilddateien\Körper_Schlange\Korper_oben.png').convert_alpha()

        self.Blau_Kopf_links = pygame.image.load('Bilddateien\Körper_Schlange\head_left.png').convert_alpha()        #kreiert die Kopfanimation
        self.Blau_Kopf_rechts = pygame.image.load('Bilddateien\Körper_Schlange\head_right.png').convert_alpha()
        self.Blau_Kopf_oben = pygame.image.load('Bilddateien\Körper_Schlange\head_down.png').convert_alpha()
        self.Blau_Kopf_unten = pygame.image.load('Bilddateien\Körper_Schlange\head_up.png').convert_alpha()

        self.Blau_Körper_LO = pygame.image.load('Bilddateien\Körper_Schlange\\body_bottomright.png').convert_alpha()   # kreiert die Körperanimation
        self.Blau_Körper_RO = pygame.image.load('Bilddateien\Körper_Schlange\\body_bottomleft.png').convert_alpha()
        self.Blau_Körper_LU = pygame.image.load('Bilddateien\Körper_Schlange\\body_topright.png').convert_alpha()
        self.Blau_Körper_RU = pygame.image.load('Bilddateien\Körper_Schlange\\body_topleft.png').convert_alpha()

        self.Blau_Schwanz_rechts = pygame.image.load('Bilddateien\Körper_Schlange\\tail_right.png').convert_alpha()  # kreiert die Schwanzanimation
        self.Blau_Schwanz_links = pygame.image.load('Bilddateien\Körper_Schlange\\tail_left.png').convert_alpha()
        self.Blau_Schwanz_unten = pygame.image.load('Bilddateien\Körper_Schlange\\tail_up.png').convert_alpha()
        self.Blau_Schwanz_oben = pygame.image.load('Bilddateien\Körper_Schlange\\tail_down.png').convert_alpha()

        self.Blau_Körper_links = pygame.image.load('Bilddateien\Körper_Schlange\\body_horizontal.png').convert_alpha()    # kreiert die Körperanimation
        self.Blau_Körper_rechts = pygame.image.load('Bilddateien\Körper_Schlange\\body_horizontal.png').convert_alpha()
        self.Blau_Körper_unten = pygame.image.load('Bilddateien\Körper_Schlange\\body_vertical.png').convert_alpha()
        self.Blau_Körper_oben = pygame.image.load('Bilddateien\Körper_Schlange\\body_vertical.png').convert_alpha()

        self.oneup = pygame.mixer.Sound('Sounds/1UP.mp3')
        self.oneup.set_volume(0.3)

 
    def Schlange_bewegen(self):
        if self.Verlängerung == True:
            Körper_copy = self.body[:] #Kopiert alle Körperteile
            Körper_copy.insert(0, Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            self.Verlängerung = False
            
        else:
            Körper_copy = self.body[:-1] #Kopiert alle außer den letzten Wert
            Körper_copy.insert(0, Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            

    def Schlange_malen(self):
        self.update_Kopf_Grafiken()
        self.update_Schwanz_Grafiken()

        for index, Körperteil in enumerate(self.body):
            x_pos = int(Körperteil.x) * Zellengroesse #Positionierung x-Achse Schlange
            y_pos = int(Körperteil.y) * Zellengroesse #Positionierung y-Achse Schlange
            Körperteil_rect = pygame.Rect(x_pos, y_pos, Zellengroesse, Zellengroesse) #Erschafft eine Oberfläche für jedes Körperteil

            if index == 0:
                screen.blit(self.Kopf,Körperteil_rect) #Zeichnet Kopf
            elif index == len(self.body) - 1:
                screen.blit(self.Schwanz,Körperteil_rect) #Zeichnet Körper
            else:
                vorgänger = self.body[index + 1] - Körperteil
                folgender = self.body[index - 1] - Körperteil
                
                if Farbe == 'Grün': #Bei Grünem Skin
                    if vorgänger.x == folgender.x:
                        screen.blit(self.Körper_oben,Körperteil_rect) #macht bei hortizontal nur Körper unten
                    elif vorgänger.y == folgender.y:
                        screen.blit(self.Körper_rechts,Körperteil_rect) #macht bei vertikal nur Körper unten
                    else: #Ecken, wie hängen benachbarte Körperteile von dem Aktuellen ab
                        if vorgänger.x == -1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == -1: #Wenn von oben nach unten links oder anderstherum
                            screen.blit(self.Körper_RU, Körperteil_rect) #Zeige die Ecke rechts unten an
                        elif vorgänger.x == -1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == -1: #Rechtsoben
                            screen.blit(self.Körper_RO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == 1: #Linksoben
                            screen.blit(self.Körper_LO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == 1: #Linksunten
                            screen.blit(self.Körper_LU, Körperteil_rect)
                if Farbe == 'Blau': #(siehe "Grün")
                    if vorgänger.x == folgender.x:
                        screen.blit(self.Blau_Körper_oben,Körperteil_rect) 
                    elif vorgänger.y == folgender.y:
                        screen.blit(self.Blau_Körper_rechts,Körperteil_rect) 
                    else: 
                        if vorgänger.x == -1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == -1:
                            screen.blit(self.Blau_Körper_RU, Körperteil_rect)
                        elif vorgänger.x == -1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == -1:
                            screen.blit(self.Blau_Körper_RO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == 1:
                            screen.blit(self.Blau_Körper_LO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == 1:
                            screen.blit(self.Blau_Körper_LU, Körperteil_rect)

        
    def update_Kopf_Grafiken(self):
        Kopf_abhängigkeiten = self.body[1] -self.body[0] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Farbe == 'Grün':
            if Kopf_abhängigkeiten == Vector2(1,0): #Wenn kopf links neber 2. Körperteil
                self.Kopf = self.Kopf_links
            elif Kopf_abhängigkeiten == Vector2(-1,0): #rechts
                self.Kopf = self.Kopf_rechts
            elif Kopf_abhängigkeiten == Vector2(0,-1): #oberhalb
                self.Kopf = self.Kopf_oben
            elif Kopf_abhängigkeiten == Vector2(0,1): #unterhalb
                self.Kopf = self.Kopf_unten
        
        if Farbe == 'Blau': #(siehe "Grün")
            if Kopf_abhängigkeiten == Vector2(1,0):
                self.Kopf = self.Blau_Kopf_links
            elif Kopf_abhängigkeiten == Vector2(-1,0):
                self.Kopf = self.Blau_Kopf_rechts
            elif Kopf_abhängigkeiten == Vector2(0,-1):
                self.Kopf = self.Blau_Kopf_oben
            elif Kopf_abhängigkeiten == Vector2(0,1):
                self.Kopf = self.Blau_Kopf_unten  

    def update_Schwanz_Grafiken(self):
        Schwanz_abhängigkeiten = self.body[-2] -self.body[-1] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Farbe == 'Grün':
            if Schwanz_abhängigkeiten == Vector2(1,0): #Schwanz rechts von 2. letztem Körperteil
                self.Schwanz = self.Schwanz_links
            elif Schwanz_abhängigkeiten == Vector2(-1,0): #links
                self.Schwanz = self.Schwanz_rechts
            elif Schwanz_abhängigkeiten == Vector2(0,-1): #unterhalb
                self.Schwanz = self.Schwanz_oben
            elif Schwanz_abhängigkeiten == Vector2(0,1): #oberhalb
                self.Schwanz = self.Schwanz_unten

        if Farbe == 'Blau': #(siehe "Grün")
            if Schwanz_abhängigkeiten == Vector2(1,0):
                self.Schwanz = self.Blau_Schwanz_links
            elif Schwanz_abhängigkeiten == Vector2(-1,0):
                self.Schwanz = self.Blau_Schwanz_rechts
            elif Schwanz_abhängigkeiten == Vector2(0,-1):
                self.Schwanz = self.Blau_Schwanz_oben
            elif Schwanz_abhängigkeiten == Vector2(0,1):
                self.Schwanz = self.Blau_Schwanz_unten

    def Schlange_verlängern(self): #sorgt dafür, dass die Schlange verlängert wird, wenn schlange in frucht
        self.Verlängerung = True
    
    def play_sound(self): #spielt pilz sound ab, wenn schlange in frucht
        self.oneup.play()

    def reset(self): 
        self.body = [Vector2(5,9),Vector2(4,9),Vector2(3,9)] #Positionierung bei neustart
        self.Richtung = Vector2(0,0) #Keine Richtung, erst wenn  ">" oder "D gedrückt wird"

            
class Frucht: 
    def __init__(self):
        self.Fruchtliste = [Vector2(random.randint(2, Anzahl_Zellen - 1),random.randint(2, Anzahl_Zellen - 1))] #Startet mit einer random Position in Fruchtliste
        self.random_fruit()
        
    def Frucht_malen(self): #Malt die Frucht an der Positionierung der Fruchtliste
        
        frucht_rect = pygame.Rect(int(self.Fruchtliste[-2].x * Zellengroesse), int(self.Fruchtliste[-2].y * Zellengroesse), Zellengroesse, Zellengroesse) 
        screen.blit(Pilz,frucht_rect)

    def random_fruit(self):
            while True:                                            # zufällige x und y Positionierungen im Spielfeld
                self.x = random.randint(2, Anzahl_Zellen - 1)      
                self.y = random.randint(2, Anzahl_Zellen - 1)
                self.vor_fruchtpos = Vector2(self.x,self.y)   
                if self.vor_fruchtpos in Hindernisliste:           # wenn Position der Frucht schon in der Hindernisliste ist, dann neue zufällige Position der Frucht
                    continue
                else: 
                    self.fruchtpos = self.vor_fruchtpos           
                    self.Fruchtliste.append(self.fruchtpos)        # Position wird an die Liste angehängt 
                    return

class Hindernisse:
    def __init__(self):
 

        self.Hindernisliste = []
        self.Hindernis_Sprites = []
        self.schlange = Schlange()
        self.frucht = Frucht()
        self.random_hindernisse() 


    def Hindernisse_malen(self):
        if Level == 2 or Level == 3: #Erscheinen nur in Lvl 2 oder 3
            i = 0 
            for hindernis in self.Hindernisliste: #Malt jedes Hindernis aus der Hindernisliste
                self.Hindernis_Sprites.append(random.choice([Cactus_1, Cactus_2, Cactus_3, Cactus_4])) #Gibt jedem Hindernis einen random Sprite von den 4
                hindernis_rect = pygame.Rect(int(hindernis.x * Zellengroesse), int(hindernis.y * Zellengroesse), Zellengroesse, Zellengroesse)
                screen.blit(self.Hindernis_Sprites[i],hindernis_rect)
                i += 1
        
    
    def random_hindernisse(self):
        if Level == 2 or Level == 3: #Erscheinen nur in Lvl 2 oder 3
            while True:
                self.x = random.randint(2, Anzahl_Zellen - 1) #Random x Position im Feld
                self.y = random.randint(2, Anzahl_Zellen - 1) #Random y Position im Feld
                self.pos = Vector2(self.x,self.y)
                if self.pos in self.schlange.body or self.pos == self.frucht.Fruchtliste[-1] or self.pos in self.Hindernisliste \
                    or self.pos == (self.schlange.body[0] + Vector2(1,0)) or self.pos == (self.schlange.body[0] + Vector2(-1,0)) \
                    or self.pos == (self.schlange.body[0] + Vector2(0,1)) or self.pos == (self.schlange.body[0] + Vector2(0,-1)): 
                    continue #solange wiederholen, bis Hindernis nicht in Frucht, in bestehendem Hindernis, in Schlange und 1 Feld vom Kopf der Schlange entfernt-
                else: 
                    self.securepos = self.pos
                    self.Hindernisliste.append(self.securepos) #Hängt die Position der Hindernisliste an
                    return
    
    def reset(self):
        global Hindernisliste
        if Todesart != 0: #Wenn Tod hindernisliste leer
            self.Hindernisliste = []

class MAIN:
    def __init__(self):
        self.schlange = Schlange()
        self.frucht = Frucht ()
        self.hindernisse = Hindernisse()
        self.silver_trophy = pygame.image.load('Bilddateien\Sprites/silver_trophy.png').convert_alpha()
        self.gold_trophy = pygame.image.load('Bilddateien\Sprites/gold_trophy.png').convert_alpha()
        self.rage_trophy = pygame.image.load('Bilddateien\Sprites/mad_face.png').convert_alpha()

    def Update(self): #Ruft alles auf, was durchgehend kontrolliert wird
        self.schlange.Schlange_bewegen()
        self.Kollisionen()
        self.Tod()
        self.check_fail()
  
    def Malen(self): #Ruft alles auf, das gezeichnet werden soll
        self.Gras_Feld()
        self.Score()
        self.Highscore()
        main_game.frucht.Frucht_malen()
        main_game.hindernisse.Hindernisse_malen()
        main_game.schlange.Schlange_malen()
        
        
    def Kollisionen(self):
        if self.frucht.Fruchtliste[-2] == self.schlange.body[0]: #Wenn aktuelle Frucht in Kopf der Schlange
            self.frucht.random_fruit() #neue Frucht
            self.schlange.Schlange_verlängern() #mach Schlange länger
            self.schlange.play_sound() #spiel den Pilz sound
            self.hindernisse.random_hindernisse() #neues Hindernis
        
        
        for Körperteil in self.schlange.body[1:]: #Wenn Frucht Position in Körper der Schlange, dann erneut random
            if Körperteil == self.frucht.Fruchtliste[-2]: 
                self.frucht.random_fruit()
        
        if Level == 2 or Level == 3:
            for Körperteil in self.schlange.body[1:]:
                if Körperteil == self.hindernisse.securepos: #Wenn neues Hindernis in Schlange
                    del self.hindernisse.Hindernisliste[-1] #Lösche neues  Hindernis aus der Liste
                    self.hindernisse.random_hindernisse() #Neues Hindernis generieren
            
            #Wenn neue frucht neber neuem Hindernnis:
            if (self.frucht.Fruchtliste[-2] in self.hindernisse.Hindernisliste) \
                or self.frucht.Fruchtliste[-2] == (self.hindernisse.securepos + Vector2(1,0)) or self.frucht.Fruchtliste[-2] == (self.hindernisse.securepos + Vector2(-1,0)) \
                or self.frucht.Fruchtliste[-2] == (self.hindernisse.securepos + Vector2(0,1)) or self.frucht.Fruchtliste[-2] == (self.hindernisse.securepos + Vector2(0,-1)):
                self.frucht.random_fruit()      # generiere neue Frucht                      
                
    def check_fail(self): # Schlange trifft sich selbst oder rand, Spiel verloren
        global safe_score1, safe_score2, safe_score3, hindernis, Level, Todesart

        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2: # Wenn Schlange aus Feld speichere Highscores
            if Level == 1:
                safe_score1 = str(len(self.schlange.body) - 3)
            elif Level == 2:                                                                    
                safe_score2 = str(len(self.schlange.body) - 3)
            elif Level == 3:
                safe_score3 = str(len(self.schlange.body) - 3)
            self.hindernisse.reset() #Leere Hindernisliste
            self.schlange.reset() #respawn Schlange am start

        if Level == 2 :
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]: #Wenn Schlange in Hindernis (Kaktus) -> Spiel verloren
                    safe_score2 = str(len(self.schlange.body) - 3) #Speichere Highscore für lvl 2
                    self.hindernisse.reset() #Leere Hindernisliste
                    self.schlange.reset() #respawn Schlange am start
                    
        if Level == 3 : #Wie bei lvl 2
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    safe_score3 = str(len(self.schlange.body) - 3) 
                    self.hindernisse.reset() 
                    self.schlange.reset() 

        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0]: #Wenn schlange in sich selbst -> Speichere Highscore
                if Level == 1:
                    safe_score1 = str(len(self.schlange.body) - 3)
                if Level == 2:
                    safe_score2 = str(len(self.schlange.body) - 3)
                if Level == 3:
                    safe_score3 = str(len(self.schlange.body) - 3)
                self.hindernisse.reset() #Leere Hindernisliste
                self.schlange.reset() #respawn Schlange am start
                 

    def Tod(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global Todesart   
        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2 : #Außerhalb vom Feld
            Todesart = 1 #Todesart 1 zuweisen
        
        for Körperteil in self.schlange.body[1:]: #Schlange in sich selbst und nicht am Startpunkt
            if Körperteil == self.schlange.body[0] and not self.schlange.body[0] == Vector2(5, 9) and not self.schlange.body[1] == Vector2(4, 9) \
                and not self.schlange.body[2] == Vector2(3,9):
                Todesart = 2 #Todesart 2 zuweisen
        
        
        if Level == 2 or Level == 3: 
            for hindernis in self.hindernisse.Hindernisliste: 
                if hindernis == self.schlange.body[0]: #Kopf der Schlange im Kaktus
                    Todesart = 3 #Todesart 3 zuweisen


    def Gras_Feld(self): #erzeugt Schachbrettmuster
    
        GRAS_FARBE = (240,230,140)
        for Zeile in range(Anzahl_Zellen):
            if Zeile % 2 == 0: #in jeder geraden Zeile
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 == 0: #Jede gerade Zelle wird umgefärbt
                        grass_rect = pygame.Rect(Zelle * Zellengroesse + Overlay_bar, Zeile * Zellengroesse + Overlay_bar, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)
            else: #in ungeraden Zeile
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 != 0: #Jede ungerade Zelle wird umgefärbt
                        grass_rect = pygame.Rect(Zelle * Zellengroesse + Overlay_bar, Zeile * Zellengroesse + Overlay_bar, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)

    def Score(self): #Momentaner Score
        global current_score, Level
        current_score = str(len(self.schlange.body) - 3) #score startet nicht bei 3
        if Level == 1 or Level == 2: score_surface = SCHRIFTART.render(current_score, True, (56,74,12)) #Dunkle Schriftart in lvl 1&2
        else: score_surface = SCHRIFTART.render(current_score, True, (255,255,255)) #Weiße Schriftart in lvl 3
        score_x = int(340) #Wo Score Anzeige x
        score_y = int(40) #Wo Score Anzeige y
        score_rect = score_surface.get_rect(center = (score_x,score_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        frucht_rect = Pilz.get_rect(midright = (score_rect.left, score_rect.centery)) #Zeigt frucht links von Score an

        screen.blit(score_surface, score_rect) #Zeichnt Zahl auf Position
        screen.blit(Pilz, frucht_rect) #Zeichnet Frucht links von Zahl
        return current_score

    def Highscore(self):
        global safe_score1, Highscore1, safe_score2, Highscore2, Level, Highscore3, safe_score3

        if Level == 1:

            Highscore = Highscore1 #Zeigt den Highscore von lvl 1 an
            trophy = self.silver_trophy #Weißt silbertrophy zu
            if int(safe_score1) > int(Highscore1) and Todesart != 0: #Speicher nach Tod den Highscore ab, wenn er größer als der vorherige war
                Highscore1 = safe_score1
                d = shelve.open('score.txt')  
                d['Highscore1'] = Highscore1  
                d.close()
                
        if Level == 2:
            trophy = self.gold_trophy #Weißt goldtrophy zu
            Highscore = Highscore2  #Zeigt den Highscore von lvl 2 an
            if int(safe_score2) > int(Highscore2) and Todesart != 0: #Speicher nach Tod den Highscore ab, wenn er größer als der vorherige war
                    Highscore2 = safe_score2
                    d = shelve.open('score.txt')  
                    d['Highscore2'] = Highscore2           
                    d.close()
                    
        if Level == 3:
            trophy = self.rage_trophy #Weißt ragetrophy zu
            Highscore = Highscore3 #Zeigt den Highscore von lvl 3 an
            if int(safe_score3) > int(Highscore3) and Todesart != 0: #Speicher nach Tod den Highscore ab, wenn er größer als der vorherige war
                    Highscore3 = safe_score3
                    d = shelve.open('score.txt')
                    d['Highscore3'] = Highscore3          
                    d.close()


        if Level == 1 or Level == 2: highscore_surface = SCHRIFTART.render(Highscore, True, (56,74,12)) # Wenn Level = 1 oder Level = 2, dann mache Schriftfarbe dunkelgrün
        else: highscore_surface = SCHRIFTART.render(Highscore, True, (255,255,255)) #Sonst: Wenn Level = 3 => Schriftfarbe ist weiß
        highscore_x = int(440) #Wo Score Anzeige
        highscore_y = int(40)

        highscore_rect = highscore_surface.get_rect(center = (highscore_x,highscore_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        trophy_rect = self.silver_trophy.get_rect(midright = (highscore_rect.left, highscore_rect.centery))
        screen.blit(highscore_surface, highscore_rect) #Zeigt Zahl an
        screen.blit(trophy, trophy_rect) #Zeigt tropg an

def get_font(size): #Festlegung unserer Schriftart
    return pygame.font.Font("Fonts/font.ttf", size) #man kann größe festlegen

def play():
    pygame.display.set_caption("Play")
    global Todesart, es_score, countdown
    Todesart = 0 #Zu start ist man nicht tot
    countdown = 600 #Für lvl 3 auf 10s, da 60 fps
    spielen = True
    while spielen: #Game loop
        es_score = str(len(main_game.schlange.body) - 3) #Holt sich den score für den Endscreen
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
                pygame.quit() #Fenster schließen
                sys.exit() #beendet allen Code
            if event.type == SCREEN_UPDATE:
                main_game.Update() #Updated nach jedem Screenupdate die Funktionen aus main
                
            if event.type == pygame.KEYDOWN: #Steuerung der Schlange
                
                if main_game.schlange.Richtung == Vector2(0,0): #beim Spawnpunkt
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #Wenn nach rechts oder D
                        main_game.schlange.Richtung = Vector2(1, 0) #Schlange nach rechts
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_w: #Wenn nach oben oder W
                    if main_game.schlange.Richtung.y != 1: # und schlange nicht nach unten geht
                        main_game.schlange.Richtung = Vector2(0, -1) #Schlange nach oben

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s: #wie bei up
                    if main_game.schlange.Richtung.y != -1:
                        main_game.schlange.Richtung = Vector2(0, 1) #Schlange nach unten

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a: #wie bei up
                    if main_game.schlange.Richtung.x != 1:
                        main_game.schlange.Richtung = Vector2(-1, 0) #Schlange nach links
                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  #wie bei up
                    if main_game.schlange.Richtung.x != -1:
                        main_game.schlange.Richtung = Vector2(1, 0) #Schlange nach rechts
                
        if Level == 1: #ändert den Hintergrund je nach level
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))


        Feldrahmen_rect = pygame.Rect(75,75,610,610) # Malt einen grauen Rahmen um das Feld       
        pygame.draw.rect(screen, (79, 70, 65), Feldrahmen_rect, 0)
        Feld_rect = pygame.Rect(80,80,600,600) #Malt das Feld in einem Farbton aus
        pygame.draw.rect(screen, (205,198,115), Feld_rect, 0)

        if Level == 3: #Zeigt den Countdown für level 3 an
            countdown_text = get_font(40).render(f'{int(countdown/60)}', True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(center = (690, 40))
            screen.blit(countdown_text,countdown_rect)
            countdown -= 1
            if countdown <= 0: #Nach 10s
                play_upside_down() #Wechsel zu play_upside_down()


        main_game.Malen() #Malt alles auf das Brett
        pygame.display.update() #Bildschirm Updatet alle Grafiken nach jedem while loop
        clock.tick(FPS) #updatet 60x pro sekunde
        if Todesart != 0: #Nach jedem Tod
            spielen = False #While loop stoppt
            restart() #Man kommt in den Restart screen
            main_game.Highscore() #Highscore wird abgespeichert


def play_upside_down(): #Das selbe wie play nur mit Umgedrehter Steuerung und man wechselt nach 10s zurück zu play()
    pygame.display.set_caption("Play")
    global Todesart, es_score, countdown
    Todesart = 0
    countdown = 600
    spielen = True
    while spielen: #Game loop
        es_score = str(len(main_game.schlange.body) - 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            if event.type == SCREEN_UPDATE:
                main_game.Update()
                
            if event.type == pygame.KEYDOWN:
                
                if main_game.schlange.Richtung == Vector2(0,0):
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        main_game.schlange.Richtung = Vector2(1, 0)
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_w: 
                    if main_game.schlange.Richtung.y != -1: 
                        main_game.schlange.Richtung = Vector2(0, 1)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if main_game.schlange.Richtung.y != 1:
                        main_game.schlange.Richtung = Vector2(0, -1)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if main_game.schlange.Richtung.x != -1:
                        main_game.schlange.Richtung = Vector2(1, 0)
                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if main_game.schlange.Richtung.x != 1:     
                        main_game.schlange.Richtung = Vector2(-1, 0)
                
        if Level == 1:
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))


        Feldrahmen_rect = pygame.Rect(75,75,610,610)        
        pygame.draw.rect(screen, (79, 70, 65), Feldrahmen_rect, 0)
        Feld_rect = pygame.Rect(80,80,600,600)
        pygame.draw.rect(screen, (205,198,115), Feld_rect, 0)

        if Level == 3:
            countdown_text = get_font(40).render(f'{int(countdown/60)}', True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(center = (690, 40))
            screen.blit(countdown_text,countdown_rect)
            countdown -= 1
            if countdown <= 0:
                play()


        main_game.Malen()
        pygame.display.update()
        clock.tick(FPS) 
        if Todesart != 0:
            spielen = False
            restart()  
            main_game.Highscore()

def laden(): #Alle gespeicherten Daten werden aus datei geladen
    global loading_states, Highscore1, Highscore2, Highscore3, Sterne_lvl_1, Sterne_lvl_2, is_Ton_an
    if loading_states:
            d = shelve.open('score.txt')
            if 'Highscore1' in d:
                Highscore1 = d['Highscore1']
            else: Highscore1 = str(0)
            if 'Highscore2' in d: 
                Highscore2 = d['Highscore2']
            else: Highscore2 = str(0)
            if 'Highscore3' in d:  
                Highscore3 = d['Highscore3']
            else: Highscore3 = str(0)
            if 'Sterne_lvl_1' in d:
                Sterne_lvl_1 = d['Sterne_lvl_1']
            if 'Sterne_lvl_2' in d:  
                Sterne_lvl_2 = d['Sterne_lvl_2']
            if 'is_Ton_an' in d:
                is_Ton_an = d['is_Ton_an']
            d.close()
            loading_states = False

def main_menu():
    pygame.display.set_caption("Main Menu")
    global Todesart, is_unlocked_screen, Level
    
    while True: 
        if Level == 1: #Ändert Hintergrund je nach Levelauswahl
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))

        laden() #Alle gespeicherten Daten werden geladen
        Ton_aendern() #Wenn Ton aus, dann alle sounds auf 0
        if level3_is_unlocked and is_unlocked_screen == False: #Wenn lvl 3 freigeschaltet zeigt den Unlock screen an
            unlock_screen()

        MENU_MOUSE_POS = pygame.mouse.get_pos() #Bekommt die Mausposition auf dem Bildschirm
        if Level == 1 or Level == 2: #Schriftart ist dunkel
            MENU_TEXT = get_font(50).render("SNAKE GAME", True, (56,74,12))
            MENU_RECT = MENU_TEXT.get_rect(center = (380, 100))
            screen.blit(MENU_TEXT, MENU_RECT)
        else:  #Schriftart ist Hell (Weiß)
            MENU_TEXT = get_font(50).render("SNAKE GAME", True, (255,255,255))
            MENU_RECT = MENU_TEXT.get_rect(center = (380, 100))
            screen.blit(MENU_TEXT, MENU_RECT)
        #Buttons felstlegen
        PLAY_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 250), 
                            text_input = "Play", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos=(380, 375), 
                            text_input="Options", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 500), 
                            text_input = "Quit", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]: #Buttons anzeigen
            button.changeColor(MENU_MOUSE_POS) #Farbe verändern wenn hovern
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Schließt das spielt, wenn auf x
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): #Wenn auf Button gedrückt
                    Todesart = 0 #Stellt todesart auf 0, damit man nicht direkt stirbt
                    button_sound.play() #spielt button sound ab
                    main_game.hindernisse.random_hindernisse() #Spawnt ein hindernis in der Hindernisliste
                    play() #Startet play
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): #Wenn auf Button gedrückt
                    button_sound.play()
                    options() #geht in Options screen
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #Wenn auf Button gedrückt -> Schließt spiel
                    button_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def unlock_screen():
    global is_unlocked_screen
    pygame.display.set_caption("Level 3 unlocked")
    is_unlocked_screen = True
    while True:
        screen.blit(Wüste_BG_4, (0,0)) #zeigt Hintergrund von lvl 3
        UNLOCK_MOUSE_POS = pygame.mouse.get_pos() #Mausposition
        UNLOCK_TITLE = get_font(50).render("WARNING", True, (255,255,255)) #generiert Text
        UNLOCK_TITLE_RECT = UNLOCK_TITLE.get_rect(center = (380, 100)) #Macht eine Oberfläche für Text
        screen.blit(UNLOCK_TITLE, UNLOCK_TITLE_RECT) #Zeigt text auf oberfläche an
        #Pygame doesnt support multiline :(
        UNLOCK_TEXT1 = get_font(20).render("Master of the serpent, ", True, (255,255,255))
        UNLOCK_TEXT1_RECT = UNLOCK_TEXT1.get_rect(center = (380, 200))
        screen.blit(UNLOCK_TEXT1, UNLOCK_TEXT1_RECT)
        UNLOCK_TEXT2 = get_font(20).render("you've conquered every challenge,", True, (255,255,255))
        UNLOCK_TEXT2_RECT = UNLOCK_TEXT2.get_rect(center = (380, 225))
        screen.blit(UNLOCK_TEXT2, UNLOCK_TEXT2_RECT)
        UNLOCK_TEXT3 = get_font(20).render("eating pellets with finesse ", True, (255,255,255))
        UNLOCK_TEXT3_RECT = UNLOCK_TEXT3.get_rect(center = (380, 250))
        screen.blit(UNLOCK_TEXT3, UNLOCK_TEXT3_RECT)
        UNLOCK_TEXT4 = get_font(20).render("and navigating mazes with precision.", True, (255,255,255))
        UNLOCK_TEXT4_RECT = UNLOCK_TEXT4.get_rect(center = (380, 275))
        screen.blit(UNLOCK_TEXT4, UNLOCK_TEXT4_RECT)
        UNLOCK_TEXT5 = get_font(20).render("Now, at the peak of your journey,", True, (255,255,255))
        UNLOCK_TEXT5_RECT = UNLOCK_TEXT5.get_rect(center = (380, 300))
        screen.blit(UNLOCK_TEXT5, UNLOCK_TEXT5_RECT)
        UNLOCK_TEXT6 = get_font(20).render("the ultimate trial beckons.", True, (255,255,255))
        UNLOCK_TEXT6_RECT = UNLOCK_TEXT6.get_rect(center = (380, 325))
        screen.blit(UNLOCK_TEXT6, UNLOCK_TEXT6_RECT)

        GO_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/UNLOCK Rect.png"), pos = (380, 500), 
                            text_input = "Ultimate Challenge", font = get_font(28), base_color="#d7fcd4", hovering_color = "Red")
        BACK_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 600), 
                            text_input = "Back", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")

        for button in [GO_BUTTON, BACK_BUTTON]:
            button.changeColor(UNLOCK_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GO_BUTTON.checkForInput(UNLOCK_MOUSE_POS):
                    button_sound.play()
                    level() #Ruft den level screen auf
                if BACK_BUTTON.checkForInput(UNLOCK_MOUSE_POS):
                    button_sound.play()
                    main_menu() #geht zurück ins main menü
        
        pygame.display.update()


def options():
    pygame.display.set_caption("Options")
    global is_Ton_an
    
    while True:
        d = shelve.open('score.txt') 
        d['is_Ton_an'] = is_Ton_an #Speichert die änderung des Tons          
        d.close()

        screen.blit(Wüste_BG_3, (0, 0)) #Zeigt extra Hintergrund an
        Ton_aendern() #gibt den aktuellen Ton wieder
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_TEXT = get_font(50).render("OPTIONS", True, "#b68f40")  
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center = (380, 75))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()        

        LEVEL_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 200), 
                            text_input = "Level", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")        
        SKIN_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 325), 
                            text_input = "Skins", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        RESET_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 450), 
                            text_input = "Reset", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Options Rect.png"), pos = (380, 575), 
                    text_input = "Back", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        if is_Ton_an: #zeigt symbol für ton ist an 
            TON_BUTTON = Button(image = pygame.image.load('Bilddateien\Sprites/Ton_an.png'), pos = (700, 715),
                    text_input = '', font = get_font(50), base_color="#d7fcd4", hovering_color = "White")   
        else:  #zeigt symbol für ton ist aus 
            TON_BUTTON = Button(image = pygame.image.load('Bilddateien\Sprites/Ton_aus.png'), pos = (700, 715),
                    text_input = '', font = get_font(50), base_color="#d7fcd4", hovering_color = "White")


        for button in [MAIN_MENU_BUTTON, LEVEL_BUTTON, SKIN_BUTTON, RESET_BUTTON, TON_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #schließt das spiel
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN: #zurück ins main menü
                if MAIN_MENU_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN: #auf den Skin auswahl screen
                if SKIN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    skins()
            if event.type == pygame.MOUSEBUTTONDOWN: #auf den level auswahl screen
                if LEVEL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    level()
            if event.type == pygame.MOUSEBUTTONDOWN: #setzt alle gespeicherten daten zurück
                if RESET_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    reset_highscore()
            if event.type == pygame.MOUSEBUTTONDOWN: #ändert ton von an zu aus v.v.
                if TON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    if is_Ton_an: is_Ton_an = False
                    else: is_Ton_an = True
                    Ton_aendern()

        pygame.display.update()  

def Ton_aendern():
    global is_Ton_an
    if not is_Ton_an: # Wenn ton aus, dann lautstärke aller sounds auf 0
        button_sound.set_volume(0)
        fail_sound.set_volume(0)
        main_game.schlange.oneup.set_volume(0)
    else: #sonst ton wie normal
        button_sound.set_volume(0.4)
        fail_sound.set_volume(0.8)
        main_game.schlange.oneup.set_volume(0.3)

        
def reset_highscore(): #setzt alle gespeicherten Daten zurück
    global Highscore1, Highscore2, Highscore3, Sterne_lvl_1, Sterne_lvl_2
    Highscore1 = str(0)
    Highscore2 = str(0)
    Highscore3 = str(0)
    Sterne_lvl_1 = 0
    Sterne_lvl_2 = 0
    d = shelve.open('score.txt')
    d.clear()  # shelve verhält sich wie ein dictionary
    d.close()


def skins(): #Skinauswahl screen
    global Farbe
    pygame.display.set_caption("Skins")
    blau_ganze_Schlange =  pygame.image.load('Bilddateien\Sprites/blau_ganze_Schlange.png').convert_alpha() #Bilder der Skins
    grun_ganze_Schlange = pygame.image.load('Bilddateien\Sprites/grun_ganze_Schlange.png').convert_alpha()
    
    while True:  
        screen.blit(Wüste_BG_3, (0, 0)) #Hintergrund von Options screen
        SKIN_MOUSE_POS = pygame.mouse.get_pos()
        SKIN_TEXT = get_font(50).render("SKIN WAHL", True, "#b68f40")
        SKIN_RECT = SKIN_TEXT.get_rect(center = (380, 75))
        SKIN_MOUSE_POS = pygame.mouse.get_pos()

        blaue_Schlange_rect = blau_ganze_Schlange.get_rect(center = (230, 330))
        screen.blit(blau_ganze_Schlange, blaue_Schlange_rect) #Zeigt blaue schlange an 
        if Farbe == 'Blau':
            haekchen_blau_rect = haekchen.get_rect(center = (310, 385))
            screen.blit(haekchen, haekchen_blau_rect) #zeigt häkchen an, wenn blauer skin gewählt

        gruene_ganze_Schlange_rect = grun_ganze_Schlange.get_rect(center = (530, 330))
        screen.blit(grun_ganze_Schlange, gruene_ganze_Schlange_rect) #Zeigt grüne schlange an 
        if Farbe == 'Grün': 
            haekchen_gruen_rect = haekchen.get_rect(center = (610, 385))
            screen.blit(haekchen, haekchen_gruen_rect) #zeigt häkchen an, wenn grüner skin gewählt

        SKIN_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (230, 480), 
                            text_input = "Blau", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        SKIN_BUTTON_2 = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (530, 480), 
                            text_input = "Grün", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (380, 600), 
                            text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")

        screen.blit(SKIN_TEXT, SKIN_RECT)
        for button in [SKIN_BUTTON, SKIN_BUTTON_2, MAIN_MENU_BUTTON]:
            button.changeColor(SKIN_MOUSE_POS)
            button.update(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_BUTTON.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    Farbe = 'Blau' #ändert farbe des ausgewählten skins auf blau
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_BUTTON_2.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    Farbe = 'Grün' #ändert farbe des ausgewählten skins auf grün
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    options()  #geht zurück zum options screen                 
        
        pygame.display.update() 

def unlock_3(): #Schaltet lvl 3 frei, wenn lvl 1&2 auf 3 Sterne
    global Sterne_lvl_1, Sterne_lvl_2, level3_is_unlocked
    if Sterne_lvl_1 == 3 and Sterne_lvl_2 == 3: 
        level3_is_unlocked = True
        return level3_is_unlocked    
    else: 
        level3_is_unlocked = False
        return level3_is_unlocked

def Sternanzeige(): #Zeigt die Sterne im lvl Screen an
    global Sterne_lvl_1, Sterne_lvl_2
    star_50 = pygame.image.load('Bilddateien\Sprites/star_50.png').convert_alpha()
    star_50_grey = pygame.image.load('Bilddateien\Sprites/star_50_grey.png').convert_alpha()
    star_80 = pygame.image.load('Bilddateien\Sprites/star_80.png').convert_alpha()
    star_80_grey = pygame.image.load('Bilddateien\Sprites/star_80_grey.png').convert_alpha()

    #Alle Sterne grau
    Stern1_links_rect = star_50.get_rect(center = (170,215)) #Stern links
    screen.blit(star_50_grey,Stern1_links_rect)
    Stern1_rechts_rect = star_50.get_rect(center = (290,215)) #Stern rechts
    screen.blit(star_50_grey,Stern1_rechts_rect)
    Stern1_mitte_rect = star_80.get_rect(center = (230,200)) #Stern Mitte
    screen.blit(star_80_grey,Stern1_mitte_rect)

    Stern2_links_rect = star_50.get_rect(center = (470,215)) #Stern links
    screen.blit(star_50_grey,Stern2_links_rect)
    Stern2_rechts_rect = star_50.get_rect(center = (590,215)) #Stern rechts
    screen.blit(star_50_grey,Stern2_rechts_rect)
    Stern2_mitte_rect = star_80.get_rect(center = (530,200)) #Stern Mitte
    screen.blit(star_80_grey,Stern2_mitte_rect)

    if Sterne_lvl_1 == 1: #Zeigt je nach Sternenlevel verschiedene Goldene Sterne über die Grauen
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect) #1.
    elif Sterne_lvl_1 == 2:
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect) #1.
        Stern1_rechts_rect = star_50.get_rect(center = (290,215))
        screen.blit(star_50,Stern1_rechts_rect) #2.
    elif Sterne_lvl_1 == 3:
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect) #1.
        Stern1_rechts_rect = star_50.get_rect(center = (290,215))
        screen.blit(star_50,Stern1_rechts_rect) #2.
        Stern1_mitte_rect = star_80.get_rect(center = (230,200))
        screen.blit(star_80,Stern1_mitte_rect) #3.
    #Wie bei Sterne_lvl_1 oben
    if Sterne_lvl_2 == 1:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
    elif Sterne_lvl_2 == 2:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
    elif Sterne_lvl_2 == 3:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200))
            screen.blit(star_80,Stern2_mitte_rect)

def level(): #levelauswahl screen
    global Level, Sterne_lvl_1, Sterne_lvl_2, level3_is_unlocked
    pygame.display.set_caption("Level")
    danger_sign = pygame.image.load('Bilddateien\Sprites/danger.png').convert_alpha() #lädt Ausrufezeichen rein
    level_1 = pygame.image.load('Bilddateien\Sprites/level_1.PNG').convert_alpha() #lädt Ausrufezeichen rein
    level_2 = pygame.image.load('Bilddateien\Sprites/level_2.PNG').convert_alpha() #lädt Ausrufezeichen rein

    while True:  
        screen.blit(Wüste_BG_3, (0, 0)) #Zeigt Hintergrund von options screen an
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_TEXT = get_font(50).render("LEVEL WAHL", True, "#b68f40")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center = (380, 75))
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        unlock_3() #Kontrolliert ob level 3 Freigeschaltet ist
        Sternanzeige() #zeigt die Sterne an, die Freigeschaltet sind
        level1_rect = level_1.get_rect(center = (230, 330))
        screen.blit(level_1, level1_rect) #Zeigt Bild von level 1 an
        if Level == 1:
            haekchen_level1_rect = haekchen.get_rect(center = (340, 410))
            screen.blit(haekchen, haekchen_level1_rect) #bei auswahl von lvl 1 zeigt häkchen an

        level2_rect = level_2.get_rect(center = (530, 330))
        screen.blit(level_2, level2_rect) #Zeigt Bild von level 2 an
        if Level == 2:
            haekchen_level2_rect = haekchen.get_rect(center = (640, 410))
            screen.blit(haekchen, haekchen_level2_rect) #bei auswahl von lvl 2 zeigt häkchen an
        
        if Level == 3: #bei auswahl von level 3 zeigt 2 ausrufezeichen an
            danger1_rect = danger_sign.get_rect(center = (492, 575))
            danger2_rect = danger_sign.get_rect(center = (268, 575))
            screen.blit(danger_sign, danger1_rect)
            screen.blit(danger_sign, danger2_rect)
     
        LEVEL_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (230, 480), 
                            text_input = "Level 1", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        LEVEL_BUTTON_2 = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (530, 480), 
                            text_input = "Level 2", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        if level3_is_unlocked: #Wenn level 3 is unlocked dann zeige den danger button an und schiebe den back button nach unten
            MAIN_MENU_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (380, 670), 
                                text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
            DANGER_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (380, 575), 
                              text_input = "DANGER", font = get_font(20), base_color="#d7fcd4", hovering_color = "Red")
        else:
            MAIN_MENU_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (380, 600), 
                                text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")


        screen.blit(LEVEL_TEXT, LEVEL_RECT)
        if level3_is_unlocked:
            for button in [LEVEL_BUTTON, LEVEL_BUTTON_2, MAIN_MENU_BUTTON, DANGER_BUTTON]:
                button.changeColor(LEVEL_MOUSE_POS)
                button.update(screen) 
        else:
            for button in [LEVEL_BUTTON, LEVEL_BUTTON_2, MAIN_MENU_BUTTON]:
                button.changeColor(LEVEL_MOUSE_POS)
                button.update(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN: #Wurde Linksclick?
                if MAIN_MENU_BUTTON.checkForInput(LEVEL_MOUSE_POS): #Wenn auf button gedrückt?
                    button_sound.play()
                    options() #gehe zurück in Options screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    button_sound.play()
                    Level = 1 #ausgewähltes Level ist 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON_2.checkForInput(LEVEL_MOUSE_POS):
                    button_sound.play()
                    Level = 2 #ausgewähltes level ist 2
            
            if level3_is_unlocked:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if DANGER_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                        button_sound.play()
                        Level = 3 #ausgewähltes level ist 3
                
        pygame.display.update()     

def restart(): #Nach Tod restart screen
    global es_score, Sterne_lvl_1, Sterne_lvl_2, Level
    fail_sound.play()
    pygame.display.set_caption("Exit Menu")
    meme_suicide = pygame.image.load('Bilddateien\Memes\eating ys.jpg').convert_alpha()
    meme_cant_see = pygame.image.load('Bilddateien\Memes\cant see.jpg').convert_alpha()
    meme_cactus = pygame.image.load('Bilddateien\Memes\cactus.jpg').convert_alpha()
    
    while True: #Hintergrund des jeweiligen levels
        if Level == 1: screen.blit(Wüste_BG,(0,0))
        elif Level == 2: screen.blit(Wüste_BG_2,(0,0))
        else: screen.blit(Wüste_BG_4,(0,0))

        if Level == 1 or Level == 2: #in lvl 1&2 dunkle schriftart
            DEATH_TEXT = get_font(50).render("You DIED", True, (56,74,12))
            DEATH_RECT = DEATH_TEXT.get_rect(center = (380, 75))
            screen.blit(DEATH_TEXT, DEATH_RECT)
            STAR_TEXT = get_font(20).render(f'You achieved a score of {es_score}', True, (56,74,12)) #zeigt den errechten Score an
            STAR_TEXT_RECT = STAR_TEXT.get_rect(center = (380, 120))
            screen.blit(STAR_TEXT, STAR_TEXT_RECT) 
        else: #in lvl 3 helle (weiß)
            DEATH_TEXT = get_font(50).render("You DIED", True, (255,255,255))
            DEATH_RECT = DEATH_TEXT.get_rect(center = (380, 75))
            screen.blit(DEATH_TEXT, DEATH_RECT)
            STAR_TEXT = get_font(20).render(f'You achieved a score of {es_score}', True, (255,255,255))
            STAR_TEXT_RECT = STAR_TEXT.get_rect(center = (380, 120))
            screen.blit(STAR_TEXT, STAR_TEXT_RECT) 


        Anzahl_Sterne = int(int(es_score)/10) #Bestimmt, wie viele Sterne man erreicht hat
        bis_1_stern_Text = get_font(17).render(f'You need {10-int(es_score)} points more for 1 star', True, (56,74,12))
        bis_1_stern_rect = bis_1_stern_Text.get_rect(center = (380, 160))
        bis_2_stern_Text = get_font(17).render(f'You need {20-int(es_score)} points more for 2 stars', True, (56,74,12))
        bis_2_stern_rect = bis_2_stern_Text.get_rect(center = (380, 160))
        bis_3_stern_Text = get_font(17).render(f'You need {30-int(es_score)} points more for 3 stars', True, (56,74,12))
        bis_3_stern_rect = bis_3_stern_Text.get_rect(center = (380, 160))                          
        drei_bekommen_Text = get_font(17).render(f'You got your third Star. Congratulations!', True, (56,74,12))
        drei_bekommen_rect = drei_bekommen_Text.get_rect(center = (380, 160))   

        if Level == 1: #Je nachdem wie viele Sterne man erreicht hat variiert der Text
            if Sterne_lvl_1 == 0 and Anzahl_Sterne == 0: screen.blit(bis_1_stern_Text, bis_1_stern_rect)
            elif Sterne_lvl_1 == 1 and Anzahl_Sterne < 2: screen.blit(bis_2_stern_Text, bis_2_stern_rect)
            elif Sterne_lvl_1 == 2 and Anzahl_Sterne < 3: screen.blit(bis_3_stern_Text, bis_3_stern_rect)
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 1: Sterne_lvl_1 = 1
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 2: Sterne_lvl_1 = 2
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 1 and Anzahl_Sterne == 2: Sterne_lvl_1 = 2
            elif Sterne_lvl_1 == 1 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 2 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 3: screen.blit(drei_bekommen_Text,drei_bekommen_rect)
       
        if Level == 2:
            if Sterne_lvl_2 == 0 and Anzahl_Sterne == 0: screen.blit(bis_1_stern_Text, bis_1_stern_rect)
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne <= 1: screen.blit(bis_2_stern_Text, bis_2_stern_rect)
            elif Sterne_lvl_2 == 2 and Anzahl_Sterne <= 2: screen.blit(bis_3_stern_Text, bis_3_stern_rect)
            elif Sterne_lvl_2 == 3: screen.blit(drei_bekommen_rect,drei_bekommen_rect)
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 1: Sterne_lvl_2 = 1
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 2: Sterne_lvl_2 = 2
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne == 2: Sterne_lvl_2 = 2
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
            elif Sterne_lvl_2 == 2 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
                
        d = shelve.open('score.txt')  #Abspeichern der Sternenlevel in datei
        d['Sterne_lvl_1'] = Sterne_lvl_1
        d['Sterne_lvl_2'] = Sterne_lvl_2             
        d.close()
        #Zeigt unterschiedliche Memes nach Todesart
        if Todesart == 1: #cant see
            MEME_RECT = meme_cant_see.get_rect(center = (380, 415))
            screen.blit(meme_cant_see, MEME_RECT)
        if Todesart == 2: #eating yourself
            MEME_RECT = meme_suicide.get_rect(center = (380, 415))
            screen.blit(meme_suicide, MEME_RECT)
        if Todesart == 3: #cactus
            MEME_RECT = meme_cactus.get_rect(center = (380, 415))
            screen.blit(meme_cactus, MEME_RECT)
        
        RESTART_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (175, 700), 
                            text_input = "Restart", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Main Menu.png"), pos = (380, 700), 
                            text_input = "Main Menu", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image = pygame.image.load("Bilddateien\Hintergrund/Restart Rect.png"), pos = (585, 700), 
                            text_input = "Quit", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        
        DEATH_MOUSE_POS = pygame.mouse.get_pos()
        for button in [RESTART_BUTTON, MAIN_MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(DEATH_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Spiel schließen
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:            
                    main_game.hindernisse.random_hindernisse()
                    play() #wenn space neustarten
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    button_sound.play()
                    main_game.hindernisse.random_hindernisse()
                    play() #wenn auf restart button neustarten
                if MAIN_MENU_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    button_sound.play()
                    main_menu() #ins main menü
                if QUIT_BUTTON.checkForInput(DEATH_MOUSE_POS): #Schließen
                    button_sound.play()
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

#Äußere Gegebenheiten
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
Zellengroesse = 40   
Anzahl_Zellen = 15
Overlay_bar = 80
Feldhöhe = Zellengroesse * Anzahl_Zellen + Overlay_bar
screen = pygame.display.set_mode((Zellengroesse*Anzahl_Zellen+2*Overlay_bar,Feldhöhe+Overlay_bar)) #Legt Fenstergröße fest (Breite * Höhe)
clock = pygame.time.Clock()
FPS = 60
Todesart = 0
Highscore1 = str(0)
Highscore2 = str(0)
Highscore3 = str(0)
safe_score1 = str(0)
safe_score2 = str(0)
safe_score3 = str(0)

#Laden von ressourcen
SCHRIFTART = pygame.font.Font('Fonts/font.ttf', 25)

Pilz = pygame.image.load('Bilddateien\Sprites\Pilz.png').convert_alpha() #convert: ändert Bild in besseres Format für python
fail_sound = pygame.mixer.Sound('Sounds\Fail.mp3')       #Festlegung der Sounds
fail_sound.set_volume(0.8)
button_sound = pygame.mixer.Sound('Sounds/button.mp3')    
button_sound.set_volume(0.4)
haekchen = pygame.image.load('Bilddateien\Sprites/häkchen.PNG').convert_alpha()         #Festlegung der Variablen für die Hintergründe und Sprites
Wüste_BG = pygame.image.load('Bilddateien\Hintergrund/desert.jpg').convert_alpha()
Wüste_BG_2 = pygame.image.load('Bilddateien\Hintergrund/desert2.jpg').convert_alpha()
Wüste_BG_3 = pygame.image.load('Bilddateien\Hintergrund/desert3.png').convert_alpha()
Wüste_BG_4 = pygame.image.load('Bilddateien\Hintergrund/desert4.jpg').convert_alpha()
Cactus_1 = pygame.image.load('Bilddateien\Sprites/cactus_1.png').convert_alpha()
Cactus_2 = pygame.image.load('Bilddateien\Sprites/cactus_2.png').convert_alpha()
Cactus_3 = pygame.image.load('Bilddateien\Sprites/cactus_3.png').convert_alpha()
Cactus_4 = pygame.image.load('Bilddateien\Sprites/cactus_4.png').convert_alpha()

#Startoptions
Farbe = 'Blau'
Level = 1 
Sterne_lvl_1 = 0
Sterne_lvl_2 = 0
es_score = 0
level3_is_unlocked = False
is_unlocked_screen = False
is_Ton_an = True

countdown = 600
#Hindernisse
Start_Hindernis = Vector2(random.randint(2, Anzahl_Zellen - 1),random.randint(2, Anzahl_Zellen - 1))
Hindernisliste = []
#Geschwindigkeit Schlange
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#save states
loading_states = True

main_game = MAIN()

main_menu() #Start mit dem Main Menu