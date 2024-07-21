import pgzrun

import pgzero.game
import pgzero.keyboard
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.clock import schedule_interval
from pgzero.constants import mouse

keyboard: pgzero.keyboard.keyboard
screen: pgzero.game.screen


WIDTH = 600
HEIGHT = 400

TITLE = "Clicker Heroes"
FPS = 30

# Объекты
fon = Actor('fon')
enemy = Actor('enemy', (400, 230))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))
button_menu = Actor("bonus", (300, 280))
button_game = Actor("bonus", (300, 180))
button_gallery = Actor("bonus", (300, 280))
win = Actor('win')

#Коллекция
button_menu_2 = Actor('bonus', (300, 350))
enemy_gallery = Actor('enemy', (150, 80))
enemy_2 = Actor('enemy_2', (280, 80))
enemy_3 = Actor('enemy_3', (450, 80))
enemy_4 = Actor('enemy_4', (220, 230))
enemy_5 = Actor('enemy_5', (400, 230))

# Переменные
count = 0
damage = 1
hp = 50
price1 = 15
price2 = 200
mode = 'menu'

#Отрисовка
def draw():
    global hp, mode
    if mode == 'game':
        fon.draw()
        enemy.draw()
        screen.draw.text(str(hp), center=(400, 130), color="#DC143C", fontsize = 30, background="#FFE4B5")
        screen.draw.text(str(count), center=(570, 30), color="black", fontsize = 30)
        #Бонусы
        bonus_1.draw()
        screen.draw.text("1 урон каждые 2с", center=(100, 80), color="black", fontsize = 20)
        screen.draw.text(str(price1), center=(100, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("5 очков каждые 2с", center=(100, 180), color="black", fontsize = 20)
        screen.draw.text(str(price2), center=(100, 210), color="black", fontsize = 20)
        #Условия отрисовки 
        if  hp <= 0 and enemy.image == 'enemy':
            hp = 100
            enemy.image = 'enemy_2'
        elif hp <= 0 and enemy.image == 'enemy_2':
            hp = 200
            enemy.image = 'enemy_3'
        elif hp <= 0 and enemy.image == 'enemy_3':
            hp = 350
            enemy.image = 'enemy_4'
        elif hp <= 0 and enemy.image == 'enemy_4':
            hp = 500
            enemy.image = 'enemy_5'
        #Финальное окно
        elif hp <= 0 and enemy.image == 'enemy_5':
            win.draw()
            screen.draw.text("Вы победили всех монстов!", center=(300, 100), color="white", fontsize = 24)
            button_menu.draw()
            screen.draw.text("Вернутся в меню?", center=(300, 270), color="black", fontsize = 20)
    
    elif mode == 'menu':
        win.draw()
        #Кнопки меню
        button_game.draw()
        screen.draw.text("Играть", center=(300, 170), color="black", fontsize = 20)
        button_gallery.draw()
        screen.draw.text("Коллекция", center=(300, 270), color="black", fontsize = 20)
    
    elif mode == 'gallery':
        win.draw()
        #Коллекция монстров
        enemy_gallery.draw()
        enemy_2.draw()
        enemy_3.draw()
        enemy_4.draw()
        enemy_5.draw()
        button_menu_2.draw()
        screen.draw.text('Венуться в меню', center=(300, 340), color="black", fontsize = 20)
#Функции бонусов
def for_bonus_1():
    global hp
    hp -= 1

def for_bonus_2():
    global count
    count += 5


#Обработка кликов
def on_mouse_down(button, pos):
    global count, damage, hp, price1, price2, mode
    if button == mouse.LEFT:
        # Клик по объекту
        if enemy.collidepoint(pos) and mode == 'game':
            count += 1
            hp -= damage
            enemy.y = 200
            animate(enemy, tween='bounce_end', duration=0.5, y=230)
        
        elif bonus_1.collidepoint(pos):
            if count >= price1:
                schedule_interval(for_bonus_1, 2)
                count -= price1
                price1 *= 2
        # Клик по кнопке bonus_2  
        elif bonus_2.collidepoint(pos):
            if count >= price2:
                schedule_interval(for_bonus_2, 2)
                count -= price2
                price2 *= 2 
        
        #Клик по кнопке играть
        elif button_game.collidepoint(pos):
            mode = 'game'
            
        #Клик по кнопке коллекция
        elif button_gallery.collidepoint(pos):
            mode = 'gallery'
        #Клик по кнопке вернутся в меню
        elif button_menu.collidepoint(pos):
            mode = 'menu'
        elif button_menu_2.collidepoint(pos):
            mode = 'menu'
pgzrun.go()
