# Project

A modular Telegram userbot running on Python 3.8+ with an sqlalchemy database. Based on RaphielGang's [Paperplane](https://github.com/RaphielGang/Telegram-UserBot") Telegram userbot along with few picked and self written extras.

## Unique Feature

1. Publish spotify played unique songs history to a User/Channel/Group of your choice. Refer [Spotify to Telegram Publisher](https://github.com/d3athwarrior/spotifytotelegrampublisher) for more details on how the module works and how to obtain a session file. Thanks [Pranav](https://github.com/deltaonealpha) & [Jeel](https://github.com/JeelPatel231) for the help to write this feature.
Copy the session file from that location to the root directory of the userbot deployment and your spotify history module should work fine.

## Untested

1. The spotify web api may rate limit your developer account if too many requests are made.
~~2. The spotify session is usually for 1 hour. It is yet to be tested as to what will happen when the session expires.~~ Fixed to auto-renew the session if expired

## How To Host

Option 1: Deploy it locally on Raspberry Pi or Termux or anything else that you like  
Option 2: You can try to deploy it using Heroku or the likes but I don't guarantee whether or not it will work.

## Credits
Huge thanks to [everyone](https://github.com/d3athwarrior/userbot/graphs/contributors) who have helped make this userbot awesome!

## Updates and Support

Contact [Me](https://t.me/d3athwarrior) on Telegram for support. I may not know answers to all your questions but I will help.

## License
[Raphielscape Public License](https://github.com/d3athwarrior/userbot/blob/sql-extended/LICENSE) - Version 1.c, June 2019
