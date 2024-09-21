import pygame
import dex  # Assuming you have a module named dex for your Pokedex logic
import string
import time

# Initialize Pygame
pygame.init()

# Set up initial screen dimensions
screen_width = 1000
screen_height = 500

# Create a resizable window
window = pygame.display.set_mode([screen_width, screen_height], pygame.RESIZABLE)

# Set window title
pygame.display.set_caption("Pokedex Search")

# Initialize font
pygame.font.init()
base_font_size = 20
font = pygame.font.SysFont("roboto", base_font_size)

# Function to update font size based on window dimensions
def update_font_size():
    global font, base_font_size
    font_size = int(min(screen_width, screen_height) / 40)
    if font_size != base_font_size:
        base_font_size = font_size
        font = pygame.font.SysFont("roboto", base_font_size)

# Function to render text
def render_text(text, color=[255, 255, 255]):
    return font.render(text, True, color)

# Function to get relative position
def get_relative_pos(x_percent, y_percent):
    return (int(screen_width * x_percent), int(screen_height * y_percent))

# Function to create button
def create_button(text, x_percent, y_percent, padding=10):
    text_surface = render_text(text, [0, 0, 0])
    button_rect = pygame.Rect(
        get_relative_pos(x_percent, y_percent),
        (text_surface.get_width() + padding * 2, text_surface.get_height() + padding * 2)
    )
    return button_rect, text_surface

# Set up hitboxes and buttons
def update_ui_elements():
    global hitbox, le_buuton, el_butoon, la_button
    search_text = render_text(" Search: Crabominable ")
    hitbox = pygame.Rect(
        get_relative_pos(0.5 - search_text.get_width() / (2 * screen_width), 0.5 - search_text.get_height() / (2 * screen_height)),
        (search_text.get_width(), search_text.get_height())
    )
    le_buuton, _ = create_button("  --->  ", 0.9, 0.9)
    el_butoon, _ = create_button("  <---  ", 0.1, 0.9)
    la_button, _ = create_button("  Done  ", 0.5, 0.9)

update_ui_elements()

# Text input settings
search = " Search: "
searchTyped = ""
textInputFocused = False
KEYS = {}

# Set up the game clock
clock = pygame.time.Clock()
backspaceTimer = 0

# Original helper functions (preserved from your code)
def pageBasic(info):
    return [
        render_text(f"National Number: {info['NationalNum']}"),
        render_text(f"Type: {info['Type']}"),
        render_text(f"Species: {info['Species']}"),
        render_text(f"Height: {info['Height']}"),
        render_text(f"Weight: {info['Weight']}"),
        render_text(f"Possible Abilities: {info['Abilities']}"),
        render_text(f"Hidden Ability: {info['HiddenAbility']}")
    ]

def pageTraining(info):
    return [
        render_text(f"EV Yield: {info['evYield']}"),
        render_text(f"Catch Rate: {info['CatchRate']}"),
        render_text(f"Base Friendship: {info['BaseFriendship']}"),
        render_text(f"Base Experience: {info['BaseExp']}")
    ]

def pageBreeding(info):
    return [
        render_text(f"Egg Cycles: {info['EggCycles']}"),
        render_text(f"Egg Groups: {info['EggGroups']}"),
        render_text(f"Gender Chance: {info['Gender']}")
    ]

def pageMinStats(info):
    return [
        render_text(f"Minimum HP: {info['MinStats'][0]}"),
        render_text(f"Minimum Attack: {info['MinStats'][1]}"),
        render_text(f"Minimum Defense: {info['MinStats'][2]}"),
        render_text(f"Minimum Special Attack: {info['MinStats'][3]}"),
        render_text(f"Minimum Special Defense: {info['MinStats'][4]}"),
        render_text(f"Minimum Speed: {info['MinStats'][5]}")
    ]

def pageBaseStats(info):
    return [
        render_text(f"Base HP: {info['BaseStats'][0]}"),
        render_text(f"Base Attack: {info['BaseStats'][1]}"),
        render_text(f"Base Defense: {info['BaseStats'][2]}"),
        render_text(f"Base Special Attack: {info['BaseStats'][3]}"),
        render_text(f"Base Special Defense: {info['BaseStats'][4]}"),
        render_text(f"Base Speed: {info['BaseStats'][5]}")
    ]

def pageMaxStats(info):
    return [
        render_text(f"Maximum HP: {info['MaxStats'][0]}"),
        render_text(f"Maximum Attack: {info['MaxStats'][1]}"),
        render_text(f"Maximum Defense: {info['MaxStats'][2]}"),
        render_text(f"Maximum Special Attack: {info['MaxStats'][3]}"),
        render_text(f"Maximum Special Defense: {info['MaxStats'][4]}"),
        render_text(f"Maximum Speed: {info['MaxStats'][5]}")
    ]

# Main game loop
while True:
    clock.tick(60)
    backspaceTimer += clock.get_time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            window = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            update_font_size()
            update_ui_elements()
        elif event.type == pygame.KEYDOWN:
            KEYS[pygame.key.name(event.key)] = True
            if textInputFocused:
                if event.key == pygame.K_BACKSPACE:
                    searchTyped = searchTyped[:-1]
                elif event.key == pygame.K_RETURN:
                    soop = dex.get_soop(searchTyped)
                    info = dex.get_pokemon_info(soop)
                    if isinstance(info, dict):
                        page = 1
                        while True:
                            for sub_event in pygame.event.get():
                                if sub_event.type == pygame.QUIT:
                                    exit(0)
                                elif sub_event.type == pygame.VIDEORESIZE:
                                    screen_width, screen_height = sub_event.size
                                    window = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                                    update_font_size()
                                    update_ui_elements()
                                elif sub_event.type == pygame.MOUSEBUTTONDOWN:
                                    if le_buuton.collidepoint(sub_event.pos) and page < 6:
                                        page += 1
                                    if el_butoon.collidepoint(sub_event.pos) and page > 1:
                                        page -= 1
                                    if la_button.collidepoint(sub_event.pos) and page == 6:
                                        break
                            
                            if page > 6:
                                page = 6
                            if page < 1:
                                page = 1
                            
                            window.fill((0, 0, 0))
                            
                            curPos = 3.5 * render_text("").get_height()
                            hoit = render_text("").get_height()
                            
                            if page == 1:
                                for line in pageBasic(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            elif page == 2:
                                for line in pageTraining(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            elif page == 3:
                                for line in pageBreeding(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            elif page == 4:
                                for line in pageBaseStats(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            elif page == 5:
                                for line in pageMaxStats(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            elif page == 6:
                                for line in pageMinStats(info):
                                    window.blit(line, get_relative_pos(0.5 - line.get_width() / (2 * screen_width), curPos / screen_height))
                                    curPos += hoit
                            
                            if page < 6:
                                pygame.draw.rect(window, [255, 255, 255], le_buuton)
                                window.blit(render_text("  --->  ", [0, 0, 0]), le_buuton.topleft)
                            
                            if page > 1:
                                pygame.draw.rect(window, [255, 255, 255], el_butoon)
                                window.blit(render_text("  <---  ", [0, 0, 0]), el_butoon.topleft)
                            
                            if page == 6:
                                pygame.draw.rect(window, [255, 255, 255], la_button)
                                window.blit(render_text("  Done  ", [0, 0, 0]), la_button.topleft)
                            
                            pygame.display.update()

                            if sub_event.type == pygame.MOUSEBUTTONDOWN and la_button.collidepoint(sub_event.pos) and page == 6:
                                break

                        searchTyped = ""
                    else:
                        error_text = render_text("Error, pokemon not found", [255, 0, 0])
                        window.blit(error_text, get_relative_pos(0.5 - error_text.get_width() / (2 * screen_width), 0.7))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                elif event.unicode.isprintable():
                    searchTyped += event.unicode
        elif event.type == pygame.KEYUP:
            KEYS[pygame.key.name(event.key)] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hitbox.collidepoint(event.pos):
                textInputFocused = True
            else:
                textInputFocused = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw search box
    pygame.draw.rect(window, [255, 255, 255], hitbox)
    textsearch = render_text(search + searchTyped + " ", [0, 0, 0])
    window.blit(textsearch, hitbox.topleft)

    # Draw instructions
    text = render_text("Enter the name of the Pokemon you are looking for:")
    window.blit(text, get_relative_pos(0.5 - text.get_width() / (2 * screen_width), 0.25))

    pygame.display.flip()