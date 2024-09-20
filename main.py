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
font = pygame.font.SysFont("roboto", 20)

# Render static texts
text = font.render("Enter the name of the Pokemon you are looking for:", True, [255, 255, 255])
search_text = font.render("Search: ", True, [255, 255, 255])
surch = font.render(" Search: Crabominable ", True, [255, 255, 255])
buuton = font.render("  --->  ", True, [0, 0, 0])
butoon = font.render("  <---  ", True, [0, 0, 0])
button = font.render("  Done  ", True, [0, 0, 0])

# Set up hitboxes and buttons
hitbox = pygame.Rect(
    (screen_width / 2 - surch.get_width() / 2, screen_height / 2 - surch.get_height() / 2),
    (surch.get_width(), surch.get_height())
)

buuton_width = buuton.get_width()
buuton_height = buuton.get_height()

le_buuton = pygame.Rect(
    (screen_width - buuton_width * 1.12, screen_height - buuton_height * 2.3),
    (buuton_width, buuton_height)
)

el_butoon = pygame.Rect(
    (buuton_width * 1.12, screen_height - buuton_height * 2.3),
    (buuton_width, buuton_height)
)

la_button = pygame.Rect(
    (screen_width / 2 - button.get_width() / 2, screen_height - buuton_height * 2.3),
    (button.get_width(), buuton_height)
)

# Text input settings
search = " Search: "
searchTyped = ""
textInputFocused = False
KEYS = {}

# Set up the game clock
clock = pygame.time.Clock()
backspaceTimer = 0


def pageBasic(info):
  National_Number = font.render("National Number: " + str(info["NationalNum"]), True,  [255, 255, 255])
  Type = font.render("Type: " + str(info["Type"]), True,  [255, 255, 255])
  Species = font.render("Species: " + str(info["Species"]), True,  [255, 255, 255])
  Height = font.render("Height: " + str(info["Height"]), True,  [255, 255, 255])
  Weight = font.render("Weight: " + str(info["Weight"]), True,  [255, 255, 255])
  Abilities = font.render("Possible Abilities: " + str(info["Abilities"]), True,  [255, 255, 255])
  Hidden_Ablility = font.render("Hidden Ability: " + str(info["HiddenAbility"]), True,  [255, 255, 255])
  basic_info = [National_Number, Type, Species, Height, Weight, Abilities, Hidden_Ablility]
  return basic_info

def pageTraining(info):
  EV_Yield = font.render("EV Yield: " + str(info["evYield"]), True,  [255, 255, 255])
  Catch_Rate = font.render("Catch Rate: " + str(info["CatchRate"]), True,  [255, 255, 255])
  Base_Frienship = font.render("Base Friendship: " + str(info["BaseFriendship"]), True,  [255, 255, 255])
  Base_Experience = font.render("Base Experience: " + str(info["BaseExp"]), True,  [255, 255, 255])
  training_info = [EV_Yield, Catch_Rate, Base_Frienship, Base_Experience]
  return training_info

def pageBreeding(info):
  Egg_Cycles = font.render("Egg Cycles: " + str(info["EggCycles"]), True,  [255, 255, 255])
  Egg_Groups = font.render("Egg Groups: " + str(info["EggGroups"]), True,  [255, 255, 255])
  Gender_Chance = font.render("Gender Chance: " + str(info["Gender"]), True,  [255, 255, 255])
  breeding_info = [Egg_Cycles, Egg_Groups, Gender_Chance]
  return breeding_info

def pageMinStats(info):
  Min_HP = font.render("Minimum HP: " + str(info["MinStats"][0]), True,  [255, 255, 255])
  Min_Attack = font.render("Minimum Attack: " + str(info["MinStats"][1]), True,  [255, 255, 255])
  Min_Defense = font.render("Minimum Defense: " + str(info["MinStats"][2]), True,  [255, 255, 255])
  Min_Special_Attack = font.render("Minimum Special Attack: " + str(info["MinStats"][3]), True,  [255, 255, 255])
  Min_Special_Defense = font.render("Minimum Special Attack: " + str(info["MinStats"][4]), True,  [255, 255, 255])
  Min_Speed = font.render("Minimum Speed: " + str(info["MinStats"][5]), True,  [255, 255, 255])
  minStats_info = [Min_HP, Min_Attack, Min_Defense, Min_Special_Attack, Min_Special_Defense, Min_Speed]
  return minStats_info

def pageBaseStats(info):
  Base_HP = font.render("Base HP: " + str(info["BaseStats"][0]), True,  [255, 255, 255])
  Base_Attack = font.render("Base Attack: " + str(info["BaseStats"][1]), True,  [255, 255, 255])
  Base_Defense = font.render("Base Defense: " + str(info["BaseStats"][2]), True,  [255, 255, 255])
  Base_Special_Attack = font.render("Base Special Attack: " + str(info["BaseStats"][3]), True,  [255, 255, 255])
  Base_Special_Defense = font.render("Base Special Attack: " + str(info["BaseStats"][4]), True,  [255, 255, 255])
  Base_Speed = font.render("Base Speed: " + str(info["BaseStats"][5]), True,  [255, 255, 255])
  BaseStats_info = [Base_HP, Base_Attack, Base_Defense, Base_Special_Attack, Base_Special_Defense, Base_Speed]
  return BaseStats_info

def pageMaxStats(info):
  Max_HP = font.render("Maximum HP: " + str(info["MaxStats"][0]), True,  [255, 255, 255])
  Max_Attack = font.render("Maximum Attack: " + str(info["MaxStats"][1]), True,  [255, 255, 255])
  Max_Defense = font.render("Maximum Defense: " + str(info["MaxStats"][2]), True,  [255, 255, 255])
  Max_Special_Attack = font.render("Maximum Special Attack: " + str(info["MaxStats"][3]), True,  [255, 255, 255])
  Max_Special_Defense = font.render("Maximum Special Attack: " + str(info["MaxStats"][4]), True,  [255, 255, 255])
  Max_Speed = font.render("Maximum Speed: " + str(info["MaxStats"][5]), True,  [255, 255, 255])
  MaxStats_info = [Max_HP, Max_Attack, Max_Defense, Max_Special_Attack, Max_Special_Defense, Max_Speed]
  return MaxStats_info
  
clock = pygame.time.Clock()
backspaceTimer = 0
while True:
  clock.tick()
  backspaceTimer += clock.get_time()
  q = pygame.event.get(pygame.QUIT)
  if q:
    exit(0)

  keyEvent = pygame.event.get(pygame.KEYDOWN)
  eventKey = pygame.event.get(pygame.KEYUP)

  if textInputFocused and KEYS.get("backspace") == True and backspaceTimer > 150:
    backspaceTimer = 0
    searchTyped = searchTyped[:-1]
  if textInputFocused and keyEvent:
    KEYS[pygame.key.name(keyEvent[0].key)] = True
    if pygame.key.name(keyEvent[0].key) in string.ascii_letters:
      searchTyped += (pygame.key.name(keyEvent[0].key))
    elif pygame.key.name(keyEvent[0].key) == "space":
      searchTyped += " "
    elif keyEvent[0].key == pygame.K_RETURN:
      soop = dex.get_soop(searchTyped)
      info = dex.get_pokemon_info(soop)
      if isinstance(info, dict):
        basicpage = pageBasic(info)
        NationalNum = basicpage[0]
        Type = basicpage[1]
        Species = basicpage[2]
        Height = basicpage[3]
        Weight = basicpage[4]
        Abilities = basicpage[5]
        HiddenAbility = basicpage[6]

        trainingpage = pageTraining(info)
        evYield = trainingpage[0]
        CatchRate = trainingpage[1]
        BaseFriendship = trainingpage[2]
        BaseExp = trainingpage[3]

        breedingpage = pageBreeding(info)
        EggCycles = breedingpage[0]
        EggGroups = breedingpage[1]
        Gender = breedingpage[2]

        minstatspage = pageMinStats(info)
        MinHP = minstatspage[0]
        MinAttack = minstatspage[1]
        MinDefense = minstatspage[2]
        MinSpecialAttack = minstatspage[3]
        MinSpecialDefense = minstatspage[4]
        MinSpeed = minstatspage[5]

        basestatspage = pageBaseStats(info)
        BaseHP = basestatspage[0]
        BaseAttack = basestatspage[1]
        BaseDefense = basestatspage[2]
        BaseSpecialAttack = basestatspage[3]
        BaseSpecialDefense = basestatspage[4]
        BaseSpeed = basestatspage[5]

        maxstatspage = pageMaxStats(info)
        MaxHP = maxstatspage[0]
        MaxAttack = maxstatspage[1]
        MaxDefense = maxstatspage[2]
        MaxSpecialAttack = maxstatspage[3]
        MaxSpecialDefense = maxstatspage[4]
        MaxSpeed = maxstatspage[5]
        

        

        page = 1
        while True:
          if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if le_buuton.collidepoint(pygame.mouse.get_pos()):
              page += 1
            if el_butoon.collidepoint(pygame.mouse.get_pos()):
              page -= 1
            if la_button.collidepoint(pygame.mouse.get_pos()) and page == 6:
              break
          if page > 6:
            page = 6
          if page < 1:
            page = 1
          pygame.draw.rect(window, [0, 0, 0],[0, 0, screen_width, screen_height])
          
          curPos = 3.5*NationalNum.get_height()
          hoit = NationalNum.get_height()
          if page < 1:
            page = 1
          if page == 1:
            window.blit(NationalNum, [((screen_width / 2) - (NationalNum.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Type, [((screen_width / 2) - (Type.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Species, [((screen_width / 2) - (Species.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Height, [((screen_width / 2) -(Height.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Weight, [((screen_width / 2) -(Weight.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Abilities, [((screen_width / 2) -(Abilities.get_width()/2)), curPos])
            curPos += hoit
            window.blit(HiddenAbility, [((screen_width / 2) -(HiddenAbility.get_width()/2)), curPos])
            pygame.draw.rect(window, [255, 255, 255], le_buuton)
            
            window.blit(buuton, [((screen_width) - (buuton.get_width() * 1.12)), ((screen_height) - (buuton.get_height()*2.3))])
            
          if page == 2:
            window.blit(evYield, [((screen_width / 2) - (evYield.get_width()/2)), curPos])
            curPos += hoit
            window.blit(CatchRate, [((screen_width / 2) - (CatchRate.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseFriendship, [((screen_width / 2) - (BaseFriendship.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseExp, [((screen_width / 2) -(Height.get_width()/2)), curPos])
            
            pygame.draw.rect(window, [255, 255, 255], le_buuton)
            window.blit(buuton, [((screen_width) - (buuton.get_width() * 1.12)), ((screen_height) - (buuton.get_height()*2.3))])
            
            pygame.draw.rect(window, [255, 255, 255], el_butoon)
            window.blit(butoon, [((buuton.get_width() * 1.12)), ((screen_height) -(buuton.get_height()*2.3))])
            
          if page == 3:
            window.blit(EggCycles, [((screen_width / 2) - (EggCycles.get_width()/2)), curPos])
            curPos += hoit
            window.blit(EggGroups, [((screen_width / 2) - (EggGroups.get_width()/2)), curPos])
            curPos += hoit
            window.blit(Gender, [((screen_width / 2) - (Gender.get_width()/2)), curPos])
            curPos += hoit
            

            pygame.draw.rect(window, [255, 255, 255], le_buuton)
            window.blit(buuton, [((screen_width) - (buuton.get_width() * 1.12)), ((screen_height) - (buuton.get_height()*2.3))])
            
            pygame.draw.rect(window, [255, 255, 255], el_butoon)
            window.blit(butoon, [((buuton.get_width() * 1.12)), ((screen_height) -(buuton.get_height()*2.3))])
            
          if page == 4:
            window.blit(BaseHP, [((screen_width / 2) - (BaseHP.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseAttack, [((screen_width / 2) - (BaseAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseDefense, [((screen_width / 2) - (BaseDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseSpecialAttack, [((screen_width / 2) -(BaseSpecialAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseSpecialDefense, [((screen_width / 2) -(BaseSpecialDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(BaseSpeed, [((screen_width / 2) -(BaseSpeed.get_width()/2)), curPos])
            
            pygame.draw.rect(window, [255, 255, 255], el_butoon)
            window.blit(butoon, [((buuton.get_width() * 1.12)), ((screen_height) -(buuton.get_height()*2.3))])

            pygame.draw.rect(window, [255, 255, 255], le_buuton)
            window.blit(buuton, [((screen_width) - (buuton.get_width() * 1.12)), ((screen_height) - (buuton.get_height()*2.3))])
            
          if page == 5:
            window.blit(MaxHP, [((screen_width / 2) - (MaxHP.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MaxAttack, [((screen_width / 2) - (MaxAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MaxDefense, [((screen_width / 2) - (MaxDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MaxSpecialAttack, [((screen_width / 2) -(MaxSpecialAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MaxSpecialDefense, [((screen_width / 2) -(MaxSpecialDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MaxSpeed, [((screen_width / 2) -(MaxSpeed.get_width()/2)), curPos])
            
            pygame.draw.rect(window, [255, 255, 255], el_butoon)
            window.blit(butoon, [((buuton.get_width() * 1.12)), ((screen_height) -(buuton.get_height()*2.3))])
            
            pygame.draw.rect(window, [255, 255, 255], le_buuton)
            window.blit(buuton, [((screen_width) - (buuton.get_width() * 1.12)), ((screen_height) - (buuton.get_height()*2.3))])
            
          if page == 6:
            window.blit(MinHP, [((screen_width / 2) - (MinHP.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MinAttack, [((screen_width / 2) - (MinAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MinDefense, [((screen_width / 2) - (MinDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MinSpecialAttack, [((screen_width / 2) -(MinSpecialAttack.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MinSpecialDefense, [((screen_width / 2) -(MinSpecialDefense.get_width()/2)), curPos])
            curPos += hoit
            window.blit(MinSpeed, [((screen_width / 2) -(MinSpeed.get_width()/2)), curPos])
            
            pygame.draw.rect(window, [255, 255, 255], el_butoon)
            window.blit(butoon, [((buuton.get_width() * 1.12)), ((screen_height) -(buuton.get_height()*2.3))])
            
            pygame.draw.rect(window, [255, 255, 255], la_button)
            window.blit(button, [((screen_width / 2) - (buuton.get_width() / 2)), ((screen_height) - (buuton.get_height()*2.3))])
            
          if page > 6:
            page = 6
          
          
          
          pygame.display.update()
      else:
        while True:
          pygame.draw.rect(window, [0, 0, 0],
                           [0, 0, screen_width, screen_height])
          err = font.render("Error, pokemon not found", True, [255, 255, 255])
          window.blit(err,
                      [((screen_width / 2) - (err.get_width() / 2)),
                       ((screen_height / 2) - (err.get_height() / 2))])
          pygame.display.update()
          if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            break
  elif textInputFocused and eventKey:
    KEYS[pygame.key.name(eventKey[0].key)] = False
 
    

  if pygame.event.get(pygame.MOUSEBUTTONDOWN):
    if hitbox.collidepoint(pygame.mouse.get_pos()):
      textInputFocused = True
    else:
      textInputFocused = False

  textsearch = font.render(search + searchTyped + " ", True, [0, 0, 0])

  pygame.draw.rect(window, [0, 0, 0],
                   [0, 0, screen_width, screen_height])

  pygame.draw.rect(window, [255, 255, 255], hitbox)

  window.blit(textsearch, [
      ((screen_width / 2) - (textsearch.get_width() / 2)),
      ((screen_height / 2) - (textsearch.get_height() / 2)) 
  ])

  window.blit(
      text,
      [screen_width / 2 - text.get_width() / 2, screen_height / 4])

  pygame.display.flip()
