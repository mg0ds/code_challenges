import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = {}
    with open(BATTLE_DATA, mode="r") as csv_file:
        bd_reader = csv.DictReader(csv_file)
        for row in bd_reader:
            bije = []
            for x, y in row.items():
                if y == "win":
                    bije.append(x)
            defeat_mapping[row["Attacker"]] = bije
    return defeat_mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if defeat_mapping.get(player1) == None or defeat_mapping.get(player2) == None:
        raise ValueError
    else:
        if player1 == player2:
            return "Tie"
        elif player1 in defeat_mapping[player2]:
            return player2
        else:
            return player1
