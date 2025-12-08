import math
import random
import pygame
import os

# ===================== CONSTANTS & SETTINGS =====================

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_DROP_Y = 40
BULLET_SPEED = 10
HIT_DIST = 27

PLAYER_LIVES_START = 3
INVINCIBLE_TIME_FRAMES = 60  # 1 second if FPS = 60
FPS = 60

# LEVEL SETTINGS (EXHIBITION FOCUS: SHORT & TOUGH, MAX ~15 SCORE)
LEVEL = 1
MAX_LEVEL = 3  # only 3 levels

level_settings = [
    # Level 1 – warmup but not too easy
    {"num_enemies": 3, "enemy_speed": 4, "bomb_chance": 0.003,  "bomb_speed": 4},
    # Level 2 – more enemies, faster
    {"num_enemies": 4, "enemy_speed": 5, "bomb_chance": 0.004,  "bomb_speed": 5},
    # Level 3 – final, hardest
    {"num_enemies": 5, "enemy_speed": 6, "bomb_chance": 0.006, "bomb_speed": 6},
]

def generate_level_thresholds():
    # Level 1 -> 5 score, Level 2 -> 10, Level 3 (win) -> 15
    steps = [5, 5, 5]   # total: 5, 10, 15
    thresholds = []
    last = 0
    for step in steps:
        last += step
        thresholds.append(last)
    return thresholds

LEVEL_SCORE_THRESHOLDS = generate_level_thresholds()

# ===================== PYGAME INIT =====================

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders – Exhibition Edition")

def load_image(filename, size=None):
    if not os.path.exists(filename):
        print(f"Error: Image file '{filename}' not found in {os.getcwd()}")
        pygame.quit()
        exit(1)
    img = pygame.image.load(filename)
    if size:
        img = pygame.transform.scale(img, size)
    return img

icon = load_image("ufo.png")
pygame.display.set_icon(icon)

# ===================== SOUND EFFECTS & MUSIC =====================

bullet_sound = pygame.mixer.Sound("bullet.wav")
bomb_sound = pygame.mixer.Sound("bomb.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
lose_life_sound = pygame.mixer.Sound("bomb.wav")
win_sound = pygame.mixer.Sound("hit.wav")

# Volume control for exhibition (soft but audible)
SFX_VOLUME = 0.017  # 0.0 = mute, 1.0 = full
MUSIC_VOLUME = 0.019

for s in [bullet_sound, bomb_sound, gameover_sound, hit_sound, lose_life_sound, win_sound]:
    s.set_volume(SFX_VOLUME)

pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)  # loop

# ===================== IMAGES & SPRITES =====================

# Player
player_img = load_image("player.png")
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0

# Enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

num_of_enemies = 4  # will be overridden by set_level()

# Bullet
bullet_img = load_image("bullet.png")
bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_y_change = BULLET_SPEED
bullet_state = "ready"  # "ready" or "fire"

# Bombs
bomb_img = pygame.transform.scale(load_image("bomb.png"), (64, 64))
bombs = []  # each: [x, y]
bomb_speed = 5
bomb_chance = 0.003

# Lives
heart_img = load_image("heart.png", (24, 24))
lives = PLAYER_LIVES_START
invincible = 0

# Score & Fonts
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)
restart_font = pygame.font.Font("freesansbold.ttf", 32)

game_over = False
win = False

background_img = load_image("background.png")

# ===================== POWER-UP LOGIC =====================

powerup_types = [
    {"name": "Double Bullet", "color": (0, 255, 255), "duration": int(7 * FPS)},
    {"name": "Double Speed",  "color": (255, 255, 0), "duration": int(7 * FPS)},
    {"name": "Slow Aliens",   "color": (0, 255, 0),   "duration": int(10 * FPS)},
    {"name": "Slow Bombs",    "color": (255, 0, 255), "duration": int(10 * FPS)},
    {"name": "Bomb Freeze",   "color": (255, 128, 0), "duration": int(10 * FPS)},
]

powerups = []          # [x, y, type_index]
active_powerups = {}   # type_index: frames_left

def spawn_powerup():
    # Exhibition: only from Level 2+ so Level 1 stays simple
    global LEVEL
    if LEVEL < 2:
        return
    if len(powerups) >= 5:
        return
    if random.random() < 0.003:  # small chance per frame
        px = random.randint(32, SCREEN_WIDTH - 64)
        py = -32
        t = random.randint(0, len(powerup_types) - 1)
        powerups.append([px, py, t])

def draw_powerup(x, y, t):
    color = powerup_types[t]["color"]
    pygame.draw.circle(screen, color, (int(x) + 16, int(y) + 16), 16)
    label = pygame.font.Font("freesansbold.ttf", 18).render(powerup_types[t]["name"][0], True, (0, 0, 0))
    screen.blit(label, (x + 8, y + 6))

def apply_powerup(t):
    active_powerups[t] = powerup_types[t]["duration"]

def tick_powerups():
    expired = []
    for t in list(active_powerups):
        active_powerups[t] -= 1
        if active_powerups[t] <= 0:
            expired.append(t)
    for t in expired:
        del active_powerups[t]

def update_powerup_effects():
    """
    Reset per-level speeds, then modify based on active powerups.
    """
    global bomb_speed, bomb_chance, enemy_x_change

    settings = level_settings[LEVEL - 1]

    # Base values from level
    base_enemy_speed = settings["enemy_speed"]
    base_bomb_speed = settings["bomb_speed"]
    base_bomb_chance = settings["bomb_chance"]

    # Reset enemy speeds per level
    for i in range(num_of_enemies):
        enemy_x_change[i] = base_enemy_speed if enemy_x_change[i] >= 0 else -base_enemy_speed

    bomb_speed = base_bomb_speed
    bomb_chance = base_bomb_chance

    # Apply power-ups
    if 2 in active_powerups:  # Slow Aliens
        for i in range(num_of_enemies):
            speed = base_enemy_speed * 0.5
            enemy_x_change[i] = speed if enemy_x_change[i] >= 0 else -speed

    if 3 in active_powerups:  # Slow Bombs
        bomb_speed = base_bomb_speed * 0.4

    if 4 in active_powerups:  # Bomb Freeze
        bomb_chance = 0

def show_active_powerups():
    y = 60
    for t in active_powerups:
        name = powerup_types[t]["name"]
        time_left = int(active_powerups[t] / FPS) + 1
        surf = pygame.font.Font("freesansbold.ttf", 20).render(
            f"{name}: {time_left}s", True, powerup_types[t]["color"]
        )
        screen.blit(surf, (SCREEN_WIDTH - 260, y))
        y += 28

# ===================== UI / TEXT FUNCTIONS =====================

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_lives(x, y, lives_):
    screen.blit(heart_img, (x, y))
    lives_text = font.render(f"x {lives_}", True, (255, 255, 255))
    screen.blit(lives_text, (x + 30, y - 2))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))
    restart_text = restart_font.render("Press R to Restart", True, (255, 255, 0))
    screen.blit(restart_text, (250, 300))

def win_text():
    win_font = pygame.font.Font("freesansbold.ttf", 64)
    win_text_ = win_font.render("YOU WIN!", True, (0, 255, 0))
    screen.blit(win_text_, (220, 200))
    restart_text = restart_font.render("Press R to Play Again", True, (255, 255, 0))
    screen.blit(restart_text, (220, 300))

def show_level_screen(level_):
    level_font = pygame.font.Font("freesansbold.ttf", 48)
    rule_font = pygame.font.Font("freesansbold.ttf", 28)

    if level_ < MAX_LEVEL:
        next_score = LEVEL_SCORE_THRESHOLDS[level_]
        rule_text = rule_font.render(
            f"Reach {next_score} score to unlock next level!", True, (255, 255, 255)
        )
    else:
        rule_text = rule_font.render("Final level – reach 15 score to win!", True, (255, 255, 255))

    level_text = level_font.render(f"Level {level_}", True, (255, 255, 0))

    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))
    screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, SCREEN_HEIGHT // 2 - 60))
    screen.blit(rule_text, (SCREEN_WIDTH // 2 - rule_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    pygame.display.update()
    pygame.time.delay(1800)  # 1.8 seconds

def show_instructions():
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))
    title_font = pygame.font.Font("freesansbold.ttf", 30)
    text_font = pygame.font.Font("freesansbold.ttf", 24)

    y = 40
    lines = [
        "SPACE INVADERS – EXHIBITION EDITION",
        "",
        "Use LEFT/RIGHT or A/D to move.",
        "Press SPACE to shoot.",
        "",
        "Power-ups (Levels 2 & 3):",
        "Double Bullet, Double Speed, Slow Aliens, Slow Bombs, Bomb Freeze.",
        "",
        "Collect power-ups by touching them with your jet.",
        "",
        "Reach 15 score to win all 3 levels.",
        "",
        "Press SPACE to start."
    ]

    for idx, line in enumerate(lines):
        if line == "":
            y += 12
            continue
        if idx == 0:
            surf = title_font.render(line, True, (255, 255, 0))
        else:
            surf = text_font.render(line, True, (255, 255, 255))
        screen.blit(surf, (SCREEN_WIDTH // 2 - surf.get_width() // 2, y))
        y += surf.get_height() + 6

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# ===================== DRAW HELPERS =====================

def player_draw(x, y, visible=True):
    if visible:
        screen.blit(player_img, (x, y))

def enemy_draw(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bullet_sound.play()
    screen.blit(bullet_img, (x + 16, y + 10))

def fire_double_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bullet_sound.play()
    screen.blit(bullet_img, (x + 6, y + 10))
    screen.blit(bullet_img, (x + 26, y + 10))

def is_collision(x1, y1, x2, y2, dist=HIT_DIST):
    distance = math.hypot(x1 - x2, y1 - y2)
    return distance < dist

# ===================== GAME STATE FUNCTIONS =====================

def set_level(lvl):
    global num_of_enemies, enemy_img, enemy_x, enemy_y, enemy_x_change, enemy_y_change
    global bomb_chance, bomb_speed

    settings = level_settings[lvl - 1]
    num_of_enemies = settings["num_enemies"]
    bomb_chance = settings["bomb_chance"]
    bomb_speed = settings["bomb_speed"]

    enemy_img = []
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []

    for _ in range(num_of_enemies):
        enemy_img.append(load_image("enemy.png"))
        enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
        enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
        enemy_x_change.append(settings["enemy_speed"])
        enemy_y_change.append(ENEMY_DROP_Y)

def reset_game():
    global player_x, player_x_change, bullet_x, bullet_y, bullet_state
    global score_value, lives, game_over, invincible, bombs, LEVEL, LEVEL_SCORE_THRESHOLDS
    global win, active_powerups, powerups

    player_x = PLAYER_START_X
    player_x_change = 0
    bullet_x = 0
    bullet_y = PLAYER_START_Y
    bullet_state = "ready"
    score_value = 0
    lives = PLAYER_LIVES_START
    game_over = False
    invincible = 0
    bombs = []
    LEVEL = 1
    win = False
    LEVEL_SCORE_THRESHOLDS = generate_level_thresholds()
    active_powerups.clear()
    powerups.clear()

    set_level(LEVEL)
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))
    pygame.mixer.music.play(-1)

# ===================== MAIN GAME LOOP =====================

clock = pygame.time.Clock()

show_instructions()
set_level(LEVEL)
show_level_screen(LEVEL)

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and not win:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player_x_change = -5
                    if 1 in active_powerups:  # Double Speed
                        player_x_change *= 2
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player_x_change = 5
                    if 1 in active_powerups:
                        player_x_change *= 2
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_x = player_x
                    if 0 in active_powerups:
                        fire_double_bullet(bullet_x, bullet_y)
                    else:
                        fire_bullet(bullet_x, bullet_y)
            if event.type == pygame.KEYUP and event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                player_x_change = 0
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                show_level_screen(LEVEL)

    if not game_over and not win:
        # ----- Player Movement -----
        move_speed = player_x_change
        if 1 in active_powerups and move_speed != 0:
            move_speed = 10 if move_speed > 0 else -10
        player_x += move_speed
        player_x = max(0, min(player_x, SCREEN_WIDTH - 64))

        # ----- Enemies -----
        for i in range(num_of_enemies):
            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - 64:
                enemy_x_change[i] *= -1
                enemy_y[i] += enemy_y_change[i]

            enemy_draw(enemy_x[i], enemy_y[i], i)

            # Drop bombs
            if random.random() < bomb_chance:
                bombs.append([enemy_x[i] + 32, enemy_y[i] + 64])
                bomb_sound.play()

            # Enemy reaches bottom – lose 2 lives
            if enemy_y[i] > 340:
                lives -= 2
                if lives <= 0:
                    lives = 0
                    game_over = True
                    pygame.mixer.music.stop()
                    hit_sound.stop()
                    bomb_sound.stop()
                    gameover_sound.play()
                    break
                else:
                    lose_life_sound.play()
                    enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
                    enemy_y[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
                    pygame.display.update()
                    pygame.time.delay(600)
                    continue

            # Bullet hits enemy
            if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
                bullet_y = PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1
                hit_sound.play()
                enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemy_y[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        # ----- Level progression -----
        if LEVEL < MAX_LEVEL and score_value >= LEVEL_SCORE_THRESHOLDS[LEVEL]:
            LEVEL += 1
            lives += 2   # small reward
            set_level(LEVEL)
            show_level_screen(LEVEL)

        # Win at final level threshold
        if LEVEL == MAX_LEVEL and score_value >= LEVEL_SCORE_THRESHOLDS[-1]:
            win = True
            pygame.mixer.music.stop()
            win_sound.play()

        # ----- Bomb Movement -----
        for bomb in bombs[:]:
            bomb[1] += bomb_speed
            screen.blit(bomb_img, (bomb[0], bomb[1]))

            if bomb[1] > SCREEN_HEIGHT:
                bombs.remove(bomb)
            elif invincible == 0 and is_collision(bomb[0], bomb[1], player_x + 32, player_y + 32, 32):
                bombs.remove(bomb)
                lives -= 1
                bomb_sound.play()
                invincible = INVINCIBLE_TIME_FRAMES
                if lives <= 0:
                    game_over = True
                    pygame.mixer.music.stop()
                    gameover_sound.play()
                    break

        # ----- Bullet Movement -----
        if bullet_y <= 0:
            bullet_y = PLAYER_START_Y
            bullet_state = "ready"
        elif bullet_state == "fire":
            if 0 in active_powerups:
                fire_double_bullet(bullet_x, bullet_y)
            else:
                fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        # ----- Player touch enemy -----
        if invincible == 0:
            for i in range(num_of_enemies):
                if is_collision(enemy_x[i], enemy_y[i], player_x, player_y, 40):
                    lives -= 1
                    invincible = INVINCIBLE_TIME_FRAMES
                    bomb_sound.play()
                    if lives <= 0:
                        game_over = True
                        pygame.mixer.music.stop()
                        gameover_sound.play()
                        break

        # Invincibility timer
        if invincible > 0:
            invincible -= 1

        # ----- POWER-UPS -----
        spawn_powerup()
        for p in powerups[:]:
            p[1] += 3
            draw_powerup(p[0], p[1], p[2])
            if p[1] > SCREEN_HEIGHT:
                powerups.remove(p)
            elif is_collision(p[0], p[1], player_x + 16, player_y + 16, 32):
                apply_powerup(p[2])
                powerups.remove(p)

        if active_powerups:
            update_powerup_effects()
            tick_powerups()
            show_active_powerups()
        else:
            # ensure base behavior if no powerup active
            update_powerup_effects()

        # Draw Player, Score, Lives
        player_draw(player_x, player_y, visible=(invincible % 10 < 5))
        show_score(textX, textY)
        show_lives(SCREEN_WIDTH - 140, 10, lives)

    elif win:
        win_text()
    else:
        game_over_text()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
