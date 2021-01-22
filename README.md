# roblox-server-scrapper
Uses http requests of the roblox game api to list the currently servers of a game

## Dependencies
```
os
json
requests
```

## Roblox/Place status
I just used the http request on the roblox link and on the possible game page and checked that the status is not `404`


## Servers Pages
So, when using the game API to get the servers, we can change the number of servers per page, with a maximum of 100, so if we want to get many servers, we will need to use the `nextPageCursor` that will be in the response to the request.
You can test and see it by your self here https://games.roblox.com/docs#!/Games/get_v1_games_placeId_servers_serverType

## API Response
```
id
maxPlayers
playing
fps
ping
```
Here above, the server structure in the response.

And i think i should explain the `playing` one, so, before, it was the currently players in the server, with all their user ids, but now, with the massive increase in active roblox players, they have changed that, not only for the amount increase, but also for the stream snipers, that used the api to check every server in a game, and find some user id in the `playing`, now it is just the players amount.
