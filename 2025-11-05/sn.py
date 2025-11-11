import pygame
# .....===

# 定義顏色
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

# 設定遊戲視窗大小
WIDTH, HEIGHT = 60, 46
SCALE = 10  # 設定縮放比例

# 初始化pygame
pygame.init()

# 創建遊戲顯示畫布(pygame顯示層)
gameSurface = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
pygame.display.set_caption('我的貪食蛇遊戲')    # 設定視窗抬頭
gameSurface.fill(COLOR_BLACK) # 用黑色填滿畫布

# 建立時鐘物件，遊戲速度控制用
clock = pygame.time.Clock()
FPS = 10  # 設定遊戲每秒幀數

running = True
# 遊戲主迴圈
while running:

    # 逐一檢測pygame的事件佇列(Queue)，看看發生了哪些事件
    for e in pygame.event.get():
    
        if e.type == pygame.QUIT:
            running = False

    # 遊戲邏輯和繪圖代碼放在這裡

    pygame.display.flip()
    clock.tick(FPS)  # 控制遊戲速度為每秒FPS幀