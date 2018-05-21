import pygame

class Plane():

    def __init__(self, screen):
    
        self.screen = screen

        # 加载飞机图像，获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞机放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞机""" 
        
        # 将背景图画上去，blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。
        self.screen.blit(self.image, self.rect)