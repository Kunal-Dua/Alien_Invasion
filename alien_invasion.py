import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    alein = Alien(ai_settings,screen)
    bullets = Group()
    aleins = Group()
    stats = GameStats(ai_settings)
 
    gf.create_fleet(ai_settings,screen,ship,aleins)

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aleins,bullets)
            gf.update_aliens(ai_settings,stats,ship,screen,aleins,bullets)
        gf.update_screen(ai_settings,screen,ship,aleins,bullets)

run_game()