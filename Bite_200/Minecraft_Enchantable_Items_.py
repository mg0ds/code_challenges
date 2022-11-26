import os
from pathlib import Path
from urllib.request import urlretrieve
from dataclasses import dataclass
from collections import namedtuple

from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
HTML_FILE = TMP / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    
    
    def __init__(self, id_name, name, max_level, description):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = []
    
    def add_items(self, items):
        for item in items:
            self.items.append(item)
    
    def __str__(self):
        return "{} ({}): {}".format(self.name, self.max_level, self.description)
        

class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    
    def __init__(self, name):
        self.name = name.replace("_", " ")
        self.enchantments = []
    
    
    def __str__(self):
        sorted_enchantments = sorted(self.enchantments, key=lambda x: x.id_name)
        ans = [f"{self.name.title()}: "]
        for en in sorted_enchantments:
            ans.append(f"  [{en.max_level}] {en.id_name}")
        return "\n".join(ans)
    

def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """

    roman = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}
    
    a = soup.find_all('td')
 
    elist = []
    edict = {}
    
    to_remove = ["sm", "png", "iron", "enchanted", "rod"]
    item_dict = {}
    ilist = []
    
    i = 0
    j = 0
    
    for b in a:
        if b.get_text() != "" or b.find("img"):
            if b.find("img") in b:
                c = b.find("img")
                iname = c["data-src"].split("/")[-1]
                iname = iname.split(".")
                iname = [x.split("_") for x in iname]
                for d in iname:
                    for e in d:
                        if e not in to_remove:
                            if e == "fishing":
                                ilist.append("fishing_rod")
                            else:
                                ilist.append(e)
                i = 0
                edict[elist[0][1]] = Enchantment(elist[0][1], elist[0][0], elist[1], elist[2])
                edict[elist[0][1]].add_items(ilist)
                elist = []
                ilist = []
            else:
                if i == 0 and len(b.get_text()) > 6:
                    elist.append([b.get_text().split("(")[0], b.get_text().split("(")[1].replace(")", "")])
                    i += 1
                elif i == 1:
                    elist.append(roman[b.get_text()])
                    i += 1
                elif i == 2:
                    elist.append(b.get_text())
    return edict

def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    item_dict = {}
    item_list = []
    
    for poz in data:
        for item in data[poz].items:
            if item not in item_list:
                item_list.append(item)
    
    print(f"item_list: {item_list}")
    for i in item_list:
        item_dict[i] = Item(i.title())
        for j in data:
            if i in data[j].items:
                item_dict[i].enchantments.append(data[j])
    return item_dict

def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not file.is_file():
            urlretrieve(URL, file)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")
    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
