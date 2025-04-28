import yaml
import sys

suits = [
    'Relic',
    'Material',
    'Psionic',
    'Fuel',
    'Weapon'
]

fates = [
    "Steward",
    "Founder",
    "Magnate",
    "Advocate",
    "Caretaker",
    "Partisan",
    "Admiral",
    "Believer",
    "Pathfinder",
    "Hegemon",
    "Planet Breaker",
    "Pirate",
    "Blight Speaker",
    "Pacifist",
    "Peacekeeper",
    "Warden",
    "Overlord",
    "Survivalist",
    "Redeemer",
    "Guardian",
    "Naturalist",
    "Gate Wraith",
    "Conspirator",
    "Judge"
]

with open(sys.argv[1]) as stream:
    try:
        cards = yaml.safe_load(stream)
        for card in cards:
            tags = card['tags']
            tags.remove('Blighted Reach')
            fate = None
            suit = ''
            for f in fates:
                if f in tags:
                    fate = f
                    tags.remove(f)
            for s in suits:
                if s in tags:
                    suit = s
                    tags.remove(s)
            if 'Blighted Reach Court' in tags:
                tags.remove('Blighted Reach Court')
            tags = ";".join(tags)
            print(f"{card['id']},{card['name']},{fate},{suit},{tags}")
    except yaml.YAMLError as exc:
        print(exc)
