import requests
import os
import json

CLAN_TAG = "#98C80RGP" #make sure hashtag is elided
CLAN_NAME = "Lethal_Turtles"
CWL_DATE = "26_FEB"

def better_get(url):
    headers = {
        "Authorization": f"Bearer {os.getenv('COC_API')}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None

def fix_tag(tag):
    return tag.replace("#", "")

def populate_wars(clan_tag):
    
    formatted_wars = {}

    url = f"https://api.clashofclans.com/v1/clans/%23{fix_tag(clan_tag)}/currentwar/leaguegroup"
    data = better_get(url)

    all_players = {}
    for clan in data["clans"]:
        for member in clan["members"]:
            all_players[member["tag"]] = member["name"]
            
    rounds = data["rounds"]
    for i, individual_round in enumerate(rounds):
        wars = individual_round["warTags"]
        for war in wars:
            war_data = better_get(f"https://api.clashofclans.com/v1/clanwarleagues/wars/%23{fix_tag(war)}")

            first_clan = war_data["clan"]
            second_clan = war_data["opponent"]

            if not first_clan["tag"] == clan_tag and not second_clan["tag"] == clan_tag:
                print(f"Error: neither clan in war {war} matches the provided clan tag.")
                continue
            print(f"Located {war} as the war for the provided clan tag.")

            attacking_clan = first_clan if first_clan["tag"] == clan_tag else second_clan
            defending_clan = second_clan if attacking_clan == first_clan else first_clan

            formatted_war_data = {}

            players = defending_clan["members"].sort(key=lambda x: x["mapPosition"])

            for j, player in enumerate(defending_clan["members"]):
                player["mapPosition"] = j + 1

                formatted_war_data[player["mapPosition"]] = {
                    "defender": player["name"],
                    "attacker": all_players[player["bestOpponentAttack"]["attackerTag"]]
                }
            formatted_wars[i + 1] = formatted_war_data

    json.dump(formatted_wars, open(f"videos//{CLAN_NAME}//{CWL_DATE}//formatted_wars.json", "w"), indent=4)

def get_attack_info(war_day, attack_number):
    formatted_wars = json.load(open(f"videos//{CLAN_NAME}//{CWL_DATE}//formatted_wars.json", "r"))
    return formatted_wars[str(war_day)][str(attack_number)]

if __name__ == "__main__":
    populate_wars(CLAN_TAG)