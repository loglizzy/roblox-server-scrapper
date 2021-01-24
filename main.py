import os
import json
import requests as req

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def main():
    listed_servers = 0
    listed_players = 0
    cursor = ''

    while listed_servers < max_servers :
        link = f'https://games.roblox.com/v1/games/{place_id}/servers/Public?sortOrder=Asc&limit=100{cursor}'
        response = req.get(link)

        servers = response.json()
        servers = json.dumps(servers)
        servers = json.loads(servers)

        data = servers['data']
        for server in data:
            if listed_servers < max_servers:
                listed_servers += 1
                listed_players += server['playing']

        cls()
        print(f'{listed_servers}...')
        if servers['nextPageCursor']:
            cursor = f'&cursor={servers["nextPageCursor"]}'
        else:
            break
    print(f'Finished with {listed_servers} servers and {listed_players} players')

place_id = input('Game place id: ')
max_servers = int(input('Max servers: '))
cls()

print('Checking roblox state...')
response = req.get('https://roblox.com'); cls()
cls()

if response.status_code == 200:
    print('Checking place...')
    response = req.get(f'https://roblox.com/games/{place_id}')
    cls()

    if response.status_code == 200:
        main()
    else:
        print("That place don't exist")
else:
    print('Roblox is currently down, try again later')
