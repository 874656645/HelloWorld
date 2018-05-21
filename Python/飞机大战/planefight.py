import sys

import pygame

from settings import Settings

from plane import Plane

import gamefunctions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    # 初始化参数设置类实例
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_name)

    # 创建一艘飞船
    plane = Plane(screen)

    #开始游戏主循环
    while True:

        # 监控键盘和鼠标事件
        gf.check_events()

        gf.update_screen(game_settings, screen, plane)

run_game()