# roblox-server-scrapper
Uses http requests of the roblox game api to list the currently servers of a game
Just for learn, you can modify it to make what you want

## Dependencies
```
os
json
requests
```

## Roblox/Place status
I just used the http request on the roblox link and on the possible game page and checked that the status isn´t `404`


## Servers Pages
So, when using the game API to get the servers, we can change the number of servers per page, with a maximum of 100, so if we want to get many servers, we will need to use the `nextPageCursor` that will be in the response to the request.
You can test and see it by your self here https://games.roblox.com/docs#!/Games/get_v1_games_placeId_servers_serverType

## API Response
Here bellow, the server structure that is gived in the response
```
id
maxPlayers
playing
fps
ping
```

And I think I should explain the `playing`, so, before it was only the currently players in the server, with all their user IDs, but now, with the massive increase in the fame/players of the roblox, they changed it to patch the stream snipers, which they was using the api to search in each server of a game, a specific id in the `playing`, and then join in that server, then now it´s just the number of players.
