import pygame
import os
import music

# 遊戲常數設定
WIDTH = 32      # 0~31 共32格
HEIGHT = 24     # 0~23 共24格
CELL_SIZE = 20  # 每格大小: 20像素
FPS = 7         # 遊戲更新頻率(每秒幀數)
# 顏色定義(RGB)
GREEN_COLOR = pygame.Color(175, 215, 70)  # R=175,G=215,B=70 綠色
GRASS_COLOR = pygame.Color(167, 209, 61)  # R=167,G=209,B=61 草地色
WHITE_COLOR = pygame.Color(255, 255, 255) # R=255,G=255,B=255 白色
GREEN_COLOR = pygame.Color(0, 255, 0)     # R=0,G=255,B=0 綠色
RED_COLOR = pygame.Color(255, 0, 0)       # R=255,G=0,B=0 紅色
YELLOW_COLOR = pygame.Color(255, 255, 0)  # R=255,G=255,B=0 黃色

# 取得上一層資料夾路徑，以便存取 assets 資料夾中的圖片、音效檔案
pardir = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(pardir, "assets")   # assets資料夾路徑

# 遊戲初始化
pygame.init()

# 創建遊戲視窗
screen = pygame.display.set_mode((WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE))
pygame.display.set_caption("我的貪食蛇遊戲")
clock = pygame.time.Clock()

# 音樂初始化與載入
pygame.mixer.init()
music.load_sounds(assets_dir)   # 傳入assets資料夾路徑，載入音樂、音效
pygame.mixer.music.play(-1)     # 開始播放背景音樂，-1代表無限迴圈

# 載入圖片資源
# image.load_images(assets_dir)   # 傳入assets資料夾路徑，載入圖片資源


# 繪製背景圖案函式
def draw_background():
  # 使用純色填滿背景(綠色)
  screen.fill(GREEN_COLOR)
  
  # 畫上草地(grass)顏色圖案
  for y in range(HEIGHT):   # 0~23(共24列)
    
    if y % 2 == 0:  # 偶數列
      for x in range(WIDTH):  # 0~31(共32行)
        if x % 2 == 0:  # 偶數行
          grass_rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE) # 定義矩形區域
          pygame.draw.rect(screen, GRASS_COLOR, grass_rect) # 繪製矩形
    
    else: # 奇數列
      for x in range(WIDTH):  # 0~31(共32行)
        if x % 2 != 0:  # 奇數行
          grass_rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE) # 定義矩形區域
          pygame.draw.rect(screen, GRASS_COLOR, grass_rect) # 繪製矩形


# 主遊戲迴圈
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit(); exit()
  
  # 1.繪製背景圖
  draw_background()
  
  

  pygame.display.flip()
  clock.tick(FPS)