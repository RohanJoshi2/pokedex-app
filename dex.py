import bs4
import requests

def get_soop(pokemon_name):
  pokemon = pokemon_name.replace(" ", "-")
  url = "https://pokemondb.net/pokedex/"+pokemon
  req = requests.get(url)
  page = req.text
  soup = bs4.BeautifulSoup(page, "html.parser")
  return soup


def get_pokemon_info(soup):

    pokedexnum = soup.select("strong:first-child")
    if len(pokedexnum) == 0:
      return "Err"
    nationalnum = pokedexnum[0].text
  
  
    typelements = soup.select("tr td:not(.cell-icon) a[class^=type-]:not([title])")
    types = [element.text for element in typelements]
    if len(types) > 1 :
      typestwo = [types[0],types[1]]
      if typestwo[0] == typestwo[1]:
        typesfour = [typestwo[0]]
    elif len(types) == 1 :
      typesthree = [types[0]]
  
    if len(types) == 1 :
      type = typesthree[0]
    elif len(types) == 0 :
      return "Err"
    elif typestwo[0] == typestwo[1]:
      type = typesfour[0]
    elif len(types) > 1 :
      type = "-".join(typestwo)
    else :
      return "Err"
   
    species_row = soup.select("div.grid-col.span-md-6.span-lg-4 table.vitals-table tbody tr td:-soup-contains('Pokémon')")
    species_text = species_row[0].text

    height_elements = soup.select("div.grid-col.span-md-6.span-lg-4 table.vitals-table tbody tr:nth-child(4) td")
    height_values = [element.text.strip() for element in height_elements]
    height_values_two = [height_values[0]]
    height = " ".join(height_values_two)

  
    weight_elements = soup.select("div.grid-col.span-md-6.span-lg-4 table.vitals-table tbody tr:nth-child(5) td")
    weight_values = [element.text.strip() for element in weight_elements]
    weight_values_two = [weight_values[0]]
    weight = " ".join(weight_values_two)

    abilities_elements = soup.select("div.grid-col.span-md-6.span-lg-4 table.vitals-table tbody tr:nth-child(6) td span.text-muted")
    abilities_values = [element.text.strip() for element in abilities_elements]
    abilities_value = " ".join(abilities_values)
  
    hidden_ability_elements = soup.select("div.grid-col.span-md-6.span-lg-4 table.vitals-table tbody tr:nth-child(6) td small.text-muted")
    hidden_ability_values = [element.text.strip() for element in hidden_ability_elements]
    if len(hidden_ability_values) >= 1 :
      ability_hidden = hidden_ability_values[0].replace(" (hidden ability)", "")
    else :
      return "Hidden Ability: None"
 
  
    ev_yield_elements = soup.select("div.grid-col.span-md-12.span-lg-4 div.grid-row div.grid-col.span-md-6.span-lg-12 table.vitals-table tbody tr:first-child td.text")
    ev_yield_values = [element.text.strip() for element in ev_yield_elements]
    ev_yield = ev_yield_values[0]
 
    catch_rate_elements = soup.select("div.grid-col.span-md-12.span-lg-4 div.grid-row div.grid-col.span-md-6.span-lg-12 table.vitals-table tbody tr:nth-child(2) td")
    catch_rate_values = [element.text.strip() for element in catch_rate_elements]
    catch_rate = catch_rate_values[0]
  
    base_friendship_elements = soup.select("div.grid-col.span-md-12.span-lg-4 div.grid-row div.grid-col.span-md-6.span-lg-12 table.vitals-table tbody tr:nth-child(3) td")
    base_friendship_values = [element.text.strip() for element in base_friendship_elements]
    base_friendship = base_friendship_values[0]
  
    base_experience_elements = soup.select("div.grid-col.span-md-12.span-lg-4 div.grid-row div.grid-col.span-md-6.span-lg-12 table.vitals-table tbody tr:nth-child(4) td")
    base_experience_values = [element.text.strip() for element in base_experience_elements]
    base_xp = base_experience_values[0]
  
    growth_rate_elements = soup.select("div.grid-col.span-md-12.span-lg-4 div.grid-row div.grid-col.span-md-6.span-lg-12 table.vitals-table tbody tr:nth-child(5) td")
    growth_rate_values = [element.text.strip() for element in growth_rate_elements]
    growth_rate = growth_rate_values[0]
  
    egg_groups_elements = soup.select("div.grid-col.span-md-6.span-lg-12:nth-child(2) table.vitals-table tbody tr:first-child td")
    egg_groups_values = [element.text.strip() for element in egg_groups_elements]
    egg_groups = egg_groups_values[0]
  
    gender_chance_elements = soup.select("div.grid-col.span-md-6.span-lg-12:nth-child(2) table.vitals-table tbody tr:nth-child(2) td")
    gender_chance_values = [element.text.strip() for element in gender_chance_elements]
    gender_chance = gender_chance_values[0]
  
    egg_cycles_elements = soup.select("div.grid-col.span-md-6.span-lg-12:nth-child(2) table.vitals-table tbody tr:nth-child(3) td")
    egg_cycles_values = [element.text.strip() for element in egg_cycles_elements]
    egg_cycles = egg_cycles_values[0]
  
    base_hp_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(1) td:nth-child(2)")
    base_hp_values = [element.text.strip() for element in base_hp_elements]
    base_hp = base_hp_values[0]
  
    base_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(2) td:nth-child(2)")
    base_attack_values = [element.text.strip() for element in base_attack_elements]
    base_attack = base_attack_values[0]
  
    base_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(3) td:nth-child(2)")
    base_defense_values = [element.text.strip() for element in base_defense_elements]
    base_defense = base_defense_values[0]
  
    base_special_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(4) td:nth-child(2)")
    base_special_attack_values = [element.text.strip() for element in base_special_attack_elements]
    base_special_attack = base_special_attack_values[0]
  
    base_special_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(5) td:nth-child(2)")
    base_special_defense_values = [element.text.strip() for element in base_special_defense_elements]
    base_special_defense = base_special_defense_values[0]
  
    base_speed_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(6) td:nth-child(2)")
    base_speed_values = [element.text.strip() for element in base_speed_elements]
    base_speed = base_speed_values[0]

    base_stats = [base_hp, base_attack, base_defense, base_special_attack, base_special_defense, base_speed]

    min_hp_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(1) td:nth-child(4)")
    min_hp_values = [element.text.strip() for element in min_hp_elements]
    min_hp = min_hp_values[0]
  
    min_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(2) td:nth-child(4)")
    min_attack_values = [element.text.strip() for element in min_attack_elements]
    min_attack = min_attack_values[0]
  
    min_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(3) td:nth-child(4)")
    min_defense_values = [element.text.strip() for element in min_defense_elements]
    min_defense = min_defense_values[0]
  
    min_special_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(4) td:nth-child(4)")
    min_special_attack_values = [element.text.strip() for element in min_special_attack_elements]
    min_special_attack = min_special_attack_values[0]
  
    min_special_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(5) td:nth-child(4)")
    min_special_defense_values = [element.text.strip() for element in min_special_defense_elements]
    min_special_defense = min_special_defense_values[0]
  
    min_speed_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(6) td:nth-child(4)")
    min_speed_values = [element.text.strip() for element in min_speed_elements]
    min_speed = min_speed_values[0]

    min_stats = [min_hp, min_attack, min_defense, min_special_attack, min_special_defense, min_speed]

  
    max_hp_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(1) td:nth-child(5)")
    max_hp_values = [element.text.strip() for element in max_hp_elements]
    max_hp = max_hp_values[0]
  
    max_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(2) td:nth-child(5)")
    max_attack_values = [element.text.strip() for element in max_attack_elements]
    max_attack = max_attack_values[0]
  
    max_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(3) td:nth-child(5)")
    max_defense_values = [element.text.strip() for element in max_defense_elements]
    max_defense = max_defense_values[0]
  
    max_special_attack_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(4) td:nth-child(5)")
    max_special_attack_values = [element.text.strip() for element in max_special_attack_elements]
    max_special_attack = max_special_attack_values[0]
  
    max_special_defense_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(5) td:nth-child(5)")
    max_special_defense_values = [element.text.strip() for element in max_special_defense_elements]
    max_special_defense = max_special_defense_values[0]
  
    max_speed_elements = soup.select("div:nth-child(2) div.grid-col.span-md-12.span-lg-8 div.resp-scroll table tbody tr:nth-child(6) td:nth-child(5)")
    max_speed_values = [element.text.strip() for element in max_speed_elements]
    max_speed = max_speed_values[0]

    max_stats = [max_hp, max_attack, max_defense, max_special_attack, max_special_defense, max_speed]

    levelup_moves_elements_names = soup.select("div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr > td.cell-name")
    levelup_moves_values = {element.text.strip() for element in levelup_moves_elements_names}

    egg_moves_elements_names = soup.select("div > div:nth-child(1) > div:nth-child(6) > table > tbody > tr > td.cell-name")
    egg_moves_values = {element.text.strip() for element in egg_moves_elements_names}

    tm_tutor_moves_elements_names = soup.select("div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr > td.cell-name")
    tm_tutor_moves_values = {element.text.strip() for element in tm_tutor_moves_elements_names}

    info = {"NationalNum" : nationalnum, "Type" : type, "Species" : species_text, "Height" : height, "Weight" : weight, "Abilities" : abilities_value, "HiddenAbility" : ability_hidden, "evYield" : ev_yield, "CatchRate" : catch_rate, "BaseFriendship" : base_friendship, "BaseExp" : base_xp, "EggCycles" : egg_cycles, "EggGroups" : egg_groups, "Gender" : gender_chance, "BaseStats" : base_stats, "MinStats" : min_stats, "MaxStats" : max_stats, "LevelUpMoves" : levelup_moves_values, "EggMoves": egg_moves_values}

    return info



def get_ability_info(ability_name):    
  urltwo = "https://pokemondb.net/ability/"+ability_name
  reqtwo = requests.get(urltwo)
  pagetwo = reqtwo.text
  souptwo = bs4.BeautifulSoup(pagetwo, "html.parser")
  abilty_description_element = souptwo.select("#main div.grid-row div:nth-child(1) p:nth-child(2)")
  ability_description_values = [element.text.strip() for element in abilty_description_element]
  if len(ability_description_values) > 0:
    ability_description = ability_description_values[0]
    return ability_description
  else: 
    return "Not an ability"



def lvlup_move_get(specific_move, soup):
  levelup_moves_info = soup.select("div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr")
  for tr in levelup_moves_info:
    if specific_move.lower() in tr.text.strip().lower():
      levelearned = tr.select("td.cell-num:nth-child(1)")[0]
      lvl = levelearned.text
      type_elements = tr.select("td.cell-icon")
      type = type_elements[0].text
      Category = tr.select("td.cell-icon.text-center > img")[0]['title']
      cat = str(Category)
      power = tr.select("div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(5)")[0]
      powr = power.text
      accuracy = tr.select("div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(6)")[0]
      acc = accuracy.text
      urlthree = "https://pokemondb.net/move/"+specific_move.replace(" ","-")
      reqthree = requests.get(urlthree)
      pagethree = reqthree.text
      soupthree = bs4.BeautifulSoup(pagethree, "html.parser")
      move_description = soupthree.select("p:nth-child(1)")
      desc = move_description[0].text
      moveinfo = {"Level":lvl, "Type":type, "Catergory":cat, "Power":powr, "Accuracy":acc, "Description":desc}
      return moveinfo
    else:
      return "Error, move not found"



def egg_move_get(specific_move, soup):
  egg_moves_elements_info = soup.select("div > div:nth-child(1) > div:nth-child(6) > table > tbody > tr")
  for tr in egg_moves_elements_info:
    if specific_move.lower() in tr.text.strip().lower():
      types = tr.select("td.cell-icon")
      type = types[0].text
      Category = tr.select("td.cell-icon.text-center > img")[0]['title']
      cat = str(Category)
      power = tr.select("td.cell-num:nth-child(2)")[0]
      powr = power.text
      accuracy = tr.select("td.cell-num:nth-child(3)")[0]
      acc = accuracy.text
      urlthree = "https://pokemondb.net/move/"+specific_move.replace(" ","-")
      reqthree = requests.get(urlthree)
      pagethree = reqthree.text
      soupthree = bs4.BeautifulSoup(pagethree, "html.parser")
      move_description = soupthree.select(".span-md- > p:nth-child(2)")
      desc = move_description[0].text
      moveinfo = {"Type":type, "Catergory":cat, "Power":""+powr, "Accuracy":acc, "Description":desc}
      return moveinfo
    else:
      return "Error, move not found"


    
def tm_tutor_move_get(specific_move, soup):
  tm_tutor_moves_elements_info = soup.select("div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr")
  for tr in tm_tutor_moves_elements_info:
    if specific_move.lower() in tr.text.strip().lower():
      tmnumber = tr.select("td.cell-num:nth-child(1)")[0]
      tm_num = tmnumber.text
      types = tr.select("td.cell-icon")
      type = types[0].text
      Category = tr.select("td.cell-icon.text-center > img")[0]['title']
      cat = str(Category)
      power = tr.select("td.cell-num:nth-child(2)")[0]
      powr = power.text
      accuracy = tr.select("td.cell-num:nth-child(3)")[0]
      acc = accuracy.text
      urlthree = "https://pokemondb.net/move/"+specific_move.replace(" ","-")
      reqthree = requests.get(urlthree)
      pagethree = reqthree.text
      soupthree = bs4.BeautifulSoup(pagethree, "html.parser")
      move_description = soupthree.select(".span-md- > p:nth-child(2)")
      desc = move_description[0].text
      moveinfo = {"TM Number":tm_num, "Type":type, "Catergory":cat, "Power":""+powr, "Accuracy":acc, "Description":desc}
      return moveinfo
    else:
      return "Error, move not found"