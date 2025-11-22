import pygame
import os, sys, random
import music

# 遊戲常數設定
WIDTH = 32      # 0~31 共32格
HEIGHT = 24     # 0~23 共24格
CELL_SIZE = 20  # 每格大小: 20像素
FPS = 7         # 遊戲更新頻率(每秒幀數)
# 顏色定義(RGB)
BACKGROUND_COLOR = pygame.Color(175, 215, 70)   # R=175,G=215,B=70 綠色
GRASS_COLOR = pygame.Color(167, 209, 61)  # R=167,G=209,B=61 草地色
HEAD_COLOR = pygame.Color(51, 51, 255)    # R=51,G=51,B=255 藍色
BODY_COLOR = pygame.Color(91, 123, 249)   # R=91,G=123,B=249 藍色
FRUIT_COLOR = pygame.Color(255, 0, 0)     # R=255,G=0,B=0 紅色

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

# 暫停遊戲
def pause_game():
    paused = True
    while paused:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 如果按「X」關閉視窗
          pygame.quit(); sys.exit()
        
        # 如果有按鍵被按下 而且 按下的是 ESC鍵
        elif event.type == pygame.KEYDOWN and \
             event.key == pygame.K_ESCAPE:
          paused = False
          break

# 繪製背景圖案函式
def draw_background():
  # 使用純色填滿背景(綠色)
  screen.fill(BACKGROUND_COLOR)
  
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

# 取得新的果實位置，且不與蛇身重疊
def get_new_fruit_pos():
  while True:
    pos = {   # 果實位置(隨機產生)
      'x': random.randint(0, WIDTH-1), 
      'y': random.randint(0, HEIGHT-1)
    }
    if pos not in snake_body: # 如果新位置不在蛇身上，則回傳該位置
      return pos

# 繪製果實
def draw_fruit():
  fruit_rect = (fruit_pos['x']*CELL_SIZE, fruit_pos['y']*CELL_SIZE, CELL_SIZE, CELL_SIZE)
  pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)
  # screen.blit(image.fruit_img, fruit_rect)

# 繪製蛇身
def draw_snake():
  # 繪製蛇頭
  head_rect = (snake_body[0]['x']*CELL_SIZE, snake_body[0]['y']*CELL_SIZE, CELL_SIZE, CELL_SIZE)
  pygame.draw.rect(screen, HEAD_COLOR, head_rect)

  # 繪製蛇身(不含蛇頭)
  for seg in snake_body[1:]: 
    seg_rect = (seg['x']*CELL_SIZE, seg['y']*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BODY_COLOR, seg_rect)

# 顯示分數
def draw_score():
  font = pygame.font.SysFont('microsoftjhenghei,pingfang', 36)  # 使用系統字型，字型大小36
  score_surf = font.render(f"分數: {score}", True, (0, 100, 0))  # 黑色文字
  screen.blit(score_surf, (10, 10))  # 繪製在左上角(10,10)位置

# 遊戲結束處理函式
def game_over():
  pygame.mixer.music.stop()  # 停止背景音樂
  music.die_sound.play()  # 播放遊戲結束音效
  print(f"遊戲結束！你的得分是: {score}")
  pygame.time.delay(2000)  # 暫停2秒鐘讓玩家聽完音效
  pygame.quit(); sys.exit()

# 初始化遊戲變數
score = 0        # 初始分數
direction = '右'  # 蛇的移動方向
x, y = WIDTH // 2, HEIGHT // 2      # 蛇頭初始位置(從畫面中央開始)
snake_body = [  {'x': x, 'y': y} ]  # 蛇身位置
fruit_pos = get_new_fruit_pos()     # 取得初始果實位置
# ate_food = False                    # 是否吃到果實的旗標

# 主遊戲迴圈
while True:
  
  # 處理使用者事件
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit(); sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and direction != '左':
        direction = '右'
      elif event.key == pygame.K_LEFT and direction != '右':
        direction = '左'
      elif event.key == pygame.K_DOWN and direction != '上':
        direction = '下'
      elif event.key == pygame.K_UP and direction != '下':
        direction = '上'
      elif event.key == pygame.K_ESCAPE:
        pause_game()  # 暫停遊戲

  # 取得蛇頭目前位置
  head_x = snake_body[0]['x']
  head_y = snake_body[0]['y']
  # 取得新蛇頭位置
  if direction == '右':
    head_x += 1
  elif direction == '左':
    head_x -= 1
  elif direction == '下':
    head_y += 1
  elif direction == '上':
    head_y -= 1
  # 在蛇頭前加入新位置
  snake_body.insert(0, {'x': head_x, 'y': head_y})

  # 處理遊戲邏輯

  # 判斷是否吃到果實
  ate_food = (head_x == fruit_pos['x'] and 
              head_y == fruit_pos['y'])
  if ate_food:  # 吃到果實
    music.eat_sound.play()  # 播放吃到果實音效
    score += 1  # 增加分數並取得新果實位置
    fruit_pos = get_new_fruit_pos()
  else: # 沒有吃到果實，移除蛇尾    
    snake_body.pop()
    
  # 是否撞牆或撞到自己身體
  if head_x < 0 or head_x >= WIDTH or \
      head_y < 0 or head_y >= HEIGHT or \
      {'x': head_x, 'y': head_y} in snake_body[1:]:
    game_over() # 播放遊戲結束音效並結束遊戲
    break

  # 繪製背景圖
  draw_background()
  # 繪製果實
  draw_fruit()
  # 繪製蛇身
  draw_snake()
  # 顯示分數
  draw_score()
  # 更新畫面顯示
  pygame.display.flip()    
  # 控制遊戲速度為每秒FPS幀
  clock.tick(FPS) 