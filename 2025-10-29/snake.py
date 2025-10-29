import pygame


pygame.init() # 初始化pygame的模組(一開始固定要寫的)

# 定義頻色變數
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(27, 205, 70, 163)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)

WIDTH = 160    # 遊戲畫面寬
HEIGHT = 100   # 遊戲畫面高
SCALE = 20    # 放大比例 

screen = pygame.display.set_mode( ( WIDTH*SCALE, HEIGHT*SCALE ) )  # 設定遊戲視窗的尺寸(size)

pygame.display.set_caption('我的貪食蛇遊戲') # 遊戲視窗的抬頭

screen.fill(blackColor)   # 塗黑全部背景


# 設定一開始蛇頭的x,y座標
# head_x = WIDTH / 2  
# head_y = HEIGHT /2
# body = [ (head_x, head_y) ]  # 預設身體裡只有一個「頭」
# direction = '右'  # 預設一開始蛇是往右走

running = True  # 控制遊戲迴圈的變數

# 遊戲迴圈 --Begin--------
while running:

  #--事件(event)檢查_Start---------
  for e in pygame.event.get():  #取得所有曾發生的event(事件)來檢查

    # 若事件類型是「視窗右上角x被按下」
    if e.type == pygame.QUIT: # 按視窗右上角x的事件
      running = False   # 離開遊戲迴圈 while running
      break             # 離開 for event 迴圈

    # 檢查其它事件
    # if e.type == pygame.KEYDOWN: # 按鍵被按下的事件
    #   if e.key == pygame.K_RIGHT: # 按下「右」鍵
    #     direction = "右"
    #   elif e.key == pygame.K_LEFT:  # 按下「左」鍵
    #     direction = "左"
    #   elif e.key == pygame.K_UP:  # 按下「上」鍵
    #     direction = "上"
    #   elif e.key == pygame.K_DOWN:  # 按下「下」鍵
    #     direction = "下"

  #--事件(event)檢查_End-----------
  

  # 清空、重繪pygame顯示層
  # screen.fill(blackColor)   # 塗黑全部背景

  # if direction == "右":
  #   head_x = head_x + 1
  # elif direction == "左":
  #   head_x = head_x - 1
  # elif direction == "上":
  #   head_y = head_y - 1
  # elif direction == "下":
  #   head_y = head_y + 1

  # # 定義一個pygame的矩形物件(pygame.Rect())，等一下要用
  # rect = pygame.Rect( head_x*SCALE, head_y*SCALE, SCALE, SCALE)

  # # 使用rect()來畫矩形，需要指定要畫在哪裡(screen)，畫什麼顏色(greenColor)，畫的Rect物件
  # pygame.draw.rect( screen, greenColor, rect )


  # 更新pygame顯示層
  pygame.display.update()

# 遊戲迴圈 --End--

pygame.quit() # 結束 pygame模組(結束固定要寫的)