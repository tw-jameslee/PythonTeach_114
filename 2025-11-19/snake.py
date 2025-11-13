import pygame
import os
import music

# 遊戲常數設定
FPS = 60 
WIDTH = 640
HEIGHT = 480

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)

# 取得上一層資料夾路徑，以便存取 assets 資料夾中的圖片、音效檔案
pardir = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(pardir, "assets")   # assets資料夾路徑

# 遊戲初始化
pygame.init()

# 創建遊戲視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的貪食蛇遊戲")
clock = pygame.time.Clock()

# 音樂初始化與載入
pygame.mixer.init()
music.load_sounds(assets_dir)  # 載入音樂、音效
pygame.mixer.music.play(-1)  # 開始播放背景音樂，-1代表無限迴圈

# 主遊戲迴圈
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit(); exit()