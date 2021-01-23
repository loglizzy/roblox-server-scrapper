# roblox-server-scrapper
Uses http requests of the roblox game api to list the currently servers of a game

Just for you learn how to use that feature of the game api, you can modify it to make what you want

## Dependencies
```
os
json
requests
```

## Important
Just to clarify, there is no point in saying "server" / "server instance", as it is impossible to pay for each "server" in a roblox game, roblox probably uses one server to host like 100 "servers" in a roblox game, or something like that, but here i will keep saying "server" because it's really easier to understand.

## Servers Pages
So, when using the game API to get the servers, we can change the number of servers per page, with a maximum of 100, so if we want to get many servers, we will need to use the `nextPageCursor` that will be in the response to the request, to navigate page per page aplying the parameter `cursor` in the api `php` file link.
You can test and see it by your self here -

https://games.roblox.com/docs#!/Games/get_v1_games_placeId_servers_serverType

## API Response
Here bellow, the server structure that is gived in the response
```
id
maxPlayers
playing
fps
ping
```
`id`: A unique ID for that game instance

`maxPlayers`: Maximum players amount allowed in that server

`playing`: So, Before it was only the currently players in the server, with all their user IDs, but now they changed it to patch the stream snipers, which they was using the api to search in each server of a game, a specific id in the `playing`, and then join in that server, then now it's just the number of players.

`fps`: I don't have sure of it, because, it's a bit strange the server rendering the game, or something like that.

`ping`: Obviously it's the ping...
