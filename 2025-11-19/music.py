"""
載入音樂、音效的模組
"""
import pygame
import os

# 載入音樂、音效
def load_sounds(assets_dir):  

  # mixer.Sound 用來載入音效檔案，可以同時播放多個音效，用來播放遊戲中的音效
  # mixer.music 一次只能播放一首音樂(但是可以控制播放的功能比較多)，所以用來播放背景音樂

  # 載入吃到食物音效
  global eat_sound
  eat_sound_file = os.path.join(assets_dir, "eat.mp3")
  eat_sound = pygame.mixer.Sound(eat_sound_file)
  
  # 載入死掉音效
  global die_sound
  die_sound_file = os.path.join(assets_dir, "dead.wav")
  die_sound = pygame.mixer.Sound(die_sound_file)

  # 載入背景音樂
  bgm_music_file = os.path.join(assets_dir, "bgm.wav")
  pygame.mixer.music.load(bgm_music_file)
  pygame.mixer.music.set_volume(1.0)  # 設定背景音樂音量0.1~1.0
  # pygame.mixer.music.play(-1)  # -1代表無限迴圈