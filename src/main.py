import pygame
import sys
from . import settings
from .game import Game
from .utils import load_image

def draw_main_menu(screen, font, panel_image, panel_rect, buttons, bg_image):
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill((30, 30, 30))
    
    title_surface = font.render("venator mali", True, (255, 255, 255))
    screen.blit(title_surface, (settings.WINDOW_WIDTH // 2 - title_surface.get_width() // 2, -30))
    
    if panel_image:
        screen.blit(panel_image, panel_rect)
    else:
        pygame.draw.rect(screen, (50, 50, 50), panel_rect, border_radius=10)
    
    mouse_pos = pygame.mouse.get_pos()
    for btn in buttons:
        if btn["rect"].collidepoint(mouse_pos):
            screen.blit(btn["hover_image"], btn["rect"])
        else:
            screen.blit(btn["image"], btn["rect"])
    
    pygame.display.flip()

def draw_settings_menu(screen, title_font, button_font, panel_image, panel_rect, buttons, bg_image):
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill((30, 30, 30))
        
    title_surface = title_font.render("Settings", True, (255, 255, 255))
    screen.blit(title_surface, (settings.WINDOW_WIDTH // 2 - title_surface.get_width() // 2, -30))
    
    if panel_image:
        screen.blit(panel_image, panel_rect)
    else:
        pygame.draw.rect(screen, (50, 50, 50), panel_rect, border_radius=10)
        
    mouse_pos = pygame.mouse.get_pos()
    for btn in buttons:
        if btn["rect"].collidepoint(mouse_pos):
            screen.blit(btn["hover_image"], btn["rect"])
        else:
            screen.blit(btn["image"], btn["rect"])
        if btn["action"] == "sound":
            txt = "Sound: OFF" if settings.SOUND_OFF else "Sound: ON"
            text_surf = button_font.render(txt, True, (255, 255, 255))
            screen.blit(text_surf, text_surf.get_rect(center=btn["rect"].center))
        elif btn["action"] == "back":
            text_surf = button_font.render("Back", True, (255, 255, 255))
            screen.blit(text_surf, text_surf.get_rect(center=btn["rect"].center))
            
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption("venator mali")
    
    ui_scale = 2.0
    panel_scale = 5.0
    button_scale = 4.0 
    
    try:
        bg_image = load_image("menu_bg.png")
        bg_image = pygame.transform.scale(bg_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    except FileNotFoundError:
        bg_image = None

    font = pygame.font.Font("assets/chiller.ttf", int(75 * ui_scale))
    button_font = pygame.font.Font(None, int(24 * ui_scale))
    
    try:
        panel_image = load_image("menu_border.png")
        new_size = (int(panel_image.get_width() * panel_scale), int(panel_image.get_height() * panel_scale))
        panel_image = pygame.transform.scale(panel_image, new_size)
        panel_rect = panel_image.get_rect(center=(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 + 40))
    except FileNotFoundError:
        panel_image = None
        panel_rect = pygame.Rect(0, 0, int(160 * panel_scale), int(180 * panel_scale))
        panel_rect.center = (settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2 + 40)
        
    button_names = ["play", "settings", "exit"]
    buttons = []
    start_y = panel_rect.top + int(50 * ui_scale)
    spacing = int(50 * ui_scale)
    
    for i, name in enumerate(button_names):
        try:
            img = load_image(f"{name}.png")
            hover_img = load_image(f"{name}_hover.png")
            
            img = pygame.transform.scale(img, (int(img.get_width() * button_scale), int(img.get_height() * button_scale)))
            hover_img = pygame.transform.scale(hover_img, (int(hover_img.get_width() * button_scale), int(hover_img.get_height() * button_scale)))
        except FileNotFoundError:
            img = pygame.Surface((int(120 * button_scale), int(40 * button_scale)))
            img.fill((70, 70, 70))
            hover_img = pygame.Surface((int(120 * button_scale), int(40 * button_scale)))
            hover_img.fill((100, 100, 100))
            
        rect = img.get_rect(center=(panel_rect.centerx, start_y + (i * spacing)))
        
        buttons.append({
            "action": name,
            "image": img,
            "hover_image": hover_img,
            "rect": rect
        })
    
    settings_button_names = ["sound", "back"]
    settings_buttons = []
    for i, name in enumerate(settings_button_names):
        try:
            img = load_image(f"{name}.png")
            hover_img = load_image(f"{name}_hover.png")
            
            img = pygame.transform.scale(img, (int(img.get_width() * button_scale), int(img.get_height() * button_scale)))
            hover_img = pygame.transform.scale(hover_img, (int(hover_img.get_width() * button_scale), int(hover_img.get_height() * button_scale)))
        except FileNotFoundError:
            img = pygame.Surface((int(120 * button_scale), int(40 * button_scale)))
            img.fill((70, 70, 70))
            hover_img = pygame.Surface((int(120 * button_scale), int(40 * button_scale)))
            hover_img.fill((100, 100, 100))
            
        rect = img.get_rect(center=(panel_rect.centerx, start_y + (i * spacing)))
        
        settings_buttons.append({
            "action": name,
            "image": img,
            "hover_image": hover_img,
            "rect": rect
        })
    
    while True:
        running = True
        start_game = False
        current_state = "main_menu"
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if current_state == "main_menu":
                            for btn in buttons:
                                if btn["rect"].collidepoint(event.pos):
                                    if btn["action"] == "play":
                                        running = False
                                        start_game = True
                                    elif btn["action"] == "settings":
                                        current_state = "settings"
                                    elif btn["action"] == "exit":
                                        running = False
                        elif current_state == "settings":
                            for btn in settings_buttons:
                                if btn["rect"].collidepoint(event.pos):
                                    if btn["action"] == "sound":
                                        settings.SOUND_OFF = not settings.SOUND_OFF
                                    elif btn["action"] == "back":
                                        current_state = "main_menu"
                            
            if running:
                if current_state == "main_menu":
                    draw_main_menu(screen, font, panel_image, panel_rect, buttons, bg_image)
                elif current_state == "settings":
                    draw_settings_menu(screen, font, button_font, panel_image, panel_rect, settings_buttons, bg_image)

        if start_game:
            if settings.SOUND_OFF:
                settings.MUSIC_VOLUME = 0.0
                settings.SFX_VOLUME = 0.0
            else:
                settings.MUSIC_VOLUME = 0.25
                settings.SFX_VOLUME = 0.45
                
            game = Game()
            game.run()
        else:
            break
        
    pygame.quit()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
