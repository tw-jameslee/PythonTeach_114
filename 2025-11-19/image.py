import pygame
import os

def load_images(assets_dir):
  # 定義顏色
  BLACK = (0, 0, 0)

  # 載入圖片
  # image.load 用來載入圖片檔案
  global background_img
  background_img_file = os.path.join(assets_dir, "background.png")
  background_img = pygame.image.load(background_img_file).convert()

  global player_img
  player_img_file = os.path.join(assets_dir, "player.png")
  player_img = pygame.image.load(player_img_file).convert()
  
  global player_mini_img
  player_mini_img = pygame.transform.scale(player_img, (25, 19))
  player_mini_img.set_colorkey(BLACK)
  pygame.display.set_icon(player_mini_img)
