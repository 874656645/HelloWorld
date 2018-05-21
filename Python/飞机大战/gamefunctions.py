import sys
import pygame

def check_events():
    
    # 监控键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()


def update_screen(game_settings, screen, plane):
    """更新屏幕上的图像，并切换到新屏幕""" 

    # 每次循环时都重绘屏幕
    screen.fill(game_settings.bg_color)
    plane.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
