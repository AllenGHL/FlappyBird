#从迭代器库中调用cycle方法
from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *

def main():
	pygame.init()
	#设置游戏对话框尺寸
	screen = pygame.display.set_mode((288, 512))
	#取背景图,抠掉边缘转换
	background_day = pygame.image.load('assets/sprites/background-day.png').convert_alpha(),
	# 贴图, 0, 0坐标开始
	screen.blit(background_day, (0, 0))
	# 图片刷新
	pygame.display.update()


if __name__ == "__main__":
	main()

