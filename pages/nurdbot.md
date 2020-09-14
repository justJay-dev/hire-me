title: Nurdbot - Interactive Chatbot for Twitch, Discord and Minecraft
published: 2020-3-8
tags: [Python, SQLAlchemy, TwitchIO, Discord.py, MCPy]
descr: A cross platform interactive chat bot, providing a healthy mix of useful and silly commands.


This is a pretty dense project that has been constantly evolving over several live-streamed coding sessions, so I will break it up by platform.

####Twitch.tv Chat Bot
_Technology Stack_  

* Python  
* TwitchIO (Asyncio Based)  
* AIOHTTP  
* SQLAlchemy  
* PostgreSQL  

On Twitch, Nurdbot currently connects to chat for 12 different creators. It parses and logs every chat message, and if the message contains a command it will process the command.  
It also has a permissions paradigm within each chat, certain identified twitch usernames are called "Operators" operators have access to commands that may effect Nurdbot's performance, including adding custom commands, adjusting the chance of random outcomes/replies and even muting the bot itself.

Specifics of each command can be found [here](https://gist.github.com/justJay-dev/5a2b3af0122a95c117f969f37139f09a)

####Discord Chat Bot
_Technology Stack_  

* Python
* Discord.py (Asyncio Based)
* AIOHTTP
* SQLAlchemy
* PostgreSQL

This is still an early feature, but within Discord Nurdbot currently connects to 1 server we use for testing, it can parse and log every chat message, and because it uses the same backend as the Twitch bot, members of that discord community can access the same functionality as if they were in twitch chat.  
This is particularly useful for managing communitys in between broadcasts.  
Nurdbot has a !tether command that can correlate Twitch.tv usernames and Discord's "Snowflake ID" system.

####Minecraft Chat Bot
_Technology_  

* Python  
* MCPI  
* SQLAlchemy  
* PostgreSQL  
* Spigot + RespberrJuice  


This feature is more of a proof of concept than a regularly used part of the bot. Using the "Spigot" loader for a vanilla minecraft server, we can run a plugin that opens an additional websocket called RespberryJuice.  
MCPI gives us a python interface across this websocket to affect the game, Nurdbot listens on this and logs / parses all of the in game chat behavior. Using this it can respond to any stored command in the database similar to how it does in Twitch or Discord.
