import pygame
pygame.init()

all_fonts = pygame.font.get_fonts()

# macOS 中文字體
mac_fonts = ['pingfang', 'heiti', 'songti', 'stkaiti', 'pingfangsc', 'pingfangtc']
print("macOS 中文字體:")
for f in mac_fonts:
    if f in all_fonts:
        print(f"  ✓ {f}")

# Windows 中文字體
win_fonts = ['microsoftyahei', 'microsoftjhenghei', 'simhei', 'simsun', 'mingliu']
print("\nWindows 中文字體:")
for f in win_fonts:
    if f in all_fonts:
        print(f"  ✓ {f}")