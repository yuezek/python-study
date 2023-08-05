import pgzrun
import random

# 窗口宽和高
WIDTH = 480 
HEIGHT = 700
REAL_HEIGHT = 852
TITLE = 'Python飞机大战'

# 加载背景图片
background1 = Actor('background') # 导入背景图片
background1.x = WIDTH/2  # 背景1的x坐标
background1.y = REAL_HEIGHT/2  # 背景1的y坐标
background2 = Actor('background')  # 导入背景图片
background2.x = WIDTH/2   # 背景2的x坐标
background2.y = -REAL_HEIGHT/2  # 背景2的y坐标

# 导入玩家飞机
hero = Actor('hero')  
hero.x = WIDTH/2    # 设置玩家飞机的x坐标
hero.y = HEIGHT*2/3     # 设置玩家飞机的y坐标  

# 导入子弹图片
bullet = Actor('bullet')  # 导入子弹图片
bullet.x = WIDTH/2        # 子弹的x坐标
bullet.y = -HEIGHT       # 子弹的y坐标，开始不可见

# 导入敌机图片
enemy = Actor('enemy')  
enemy.x = WIDTH/2       # 设置敌机的x坐标
enemy.y = 0             # 设置敌机的y坐标

# 游戏得分
score = 0     

#1. 绘制模块，每帧重复执行
def draw():
    # 绘制背景
    background1.draw()
    background2.draw()
    # 绘制自己的飞机
    hero.draw()
    # 绘制敌机飞机
    enemy.draw()  
    # 绘制子弹
    bullet.draw()
    # 显示得分
    screen.draw.text("得分: "+str(score), (200, HEIGHT-50), fontsize=30, fontname='s', color='black')

def backgroundChange():
    # 以下代码用于实现背景图片的循环滚动效果
    if background1.y > REAL_HEIGHT/2 + REAL_HEIGHT:
        background1.y = -REAL_HEIGHT/2  # 背景1移动到背景2的正上方
    if background2.y > REAL_HEIGHT/2 + REAL_HEIGHT:
        background2.y = -REAL_HEIGHT/2  # 背景2移动到背景1的正上方
    background1.y += 1  # 背景1向下滚动
    background2.y += 1  # 背景2向下滚动

#3. 更新模块，每帧重复操作
def update():
    global score
    # 图片开始向下移动-自动
    backgroundChange()
    # 子弹自动向上移动
    if bullet.y > -HEIGHT:
        bullet.y = bullet.y - 10 
    # 敌机自动下落
    enemy.y += 3 
    if enemy.y > HEIGHT: # 敌机落到画面底部
        enemy.y = 0 # 敌机从上面重新出现
        enemy.x = random.randint(30, WIDTH-30)  # 敌机水平位置随机  
    # 子弹与敌机发生碰撞后    
    if bullet.colliderect(enemy): 
        enemy.y = 0 # 敌机从上面重新出现
        enemy.x = random.randint(0, WIDTH)  # 敌机水平位置随机
        score = score + 1 # 得分加1
        bullet.y = -HEIGHT  # 隐藏子弹  

#2. 当鼠标移动时执行 飞机跟随鼠标
def on_mouse_move(pos, rel, buttons):
    hero.x = pos[0]
    hero.y = pos[1]

#4. 当鼠标键按下时 - 发射子弹
def on_mouse_down(): # 当鼠标键按下时
    bullet.x = hero.x   # 把子弹位置设为玩家飞机的正上方
    bullet.y = hero.y - 70

pgzrun.go()