# roblox-server-scrapper
Uses http requests of the roblox game api to list the currently servers of a game

## Dependencies
```
os
json
requests
```
down here, there is only information about the process of how i made it, if you just want to use the code, you don't need to read it below
## Checking if place exist
I just used http request on the possible game page and verified if the status isn't `404`
## API Response
### Servers Pages
So, when using the game API to get the servers, we can change the number of servers per page, with a maximum of 100, so if we want to get many servers, we will need to use the `nextPageCursor` that will be in the response to the request.
You can test and see by your self here https://games.roblox.com/docs#!/Games/get_v1_games_placeId_servers_serverType
```
id
maxPlayers
playing
fps
ping
```
