from userbot.modules.sql_helper.spotifypublished import is_song_published, publish_song
from spotipy import Spotify, util
from telethon.client.telegramclient import TelegramClient
from telethon.sessions.string import StringSession
from userbot import CMD_HELP, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_LIST_CHANNEL_ID, SPOTIFY_QUERY_DELAY, SPOTIFY_USERNAME, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

if (SPOTIFY_USERNAME not in (None, "") and SPOTIFY_CLIENT_ID not in (None, "")
    and SPOTIFY_CLIENT_SECRET not in (None, "") and SPOTIFY_LIST_CHANNEL_ID not in (None, "")):
    token = util.prompt_for_user_token(username=SPOTIFY_USERNAME,
                                        scope="user-read-playback-state",
                                        client_id=SPOTIFY_CLIENT_ID,
                                        client_secret=SPOTIFY_CLIENT_SECRET,
                                        redirect_uri="http://localhost/")
    spotify_client = Spotify(auth=token)
    async def queryNowPlaying():
        results = spotify_client.current_playback()
        if (results != None):
            song = str(results['item']['name'])
            album = str(results['item']['album']['name'])
            artist = str(results['item']['artists'][0]['name'])
            if (not is_song_published(song, album, artist)):
                publish_song(song, album, artist)
                await bot.send_message(SPOTIFY_LIST_CHANNEL_ID, 'Song Name: ' + song +
                                                            '\nAlbum Name: ' + album +
                                                            '\nArtist: ' + artist +
                                                            '\nBrowser Link: ' + str(results['item']['album']['external_urls']['spotify']) +
                                                            '?highlight=' + str(results['item']['uri']) +
                                                            '\nMobile Link: ' + str(results['item']['external_urls']['spotify']))
    scheduler = AsyncIOScheduler()
    scheduler.add_job(queryNowPlaying, 'interval', seconds=SPOTIFY_QUERY_DELAY)
    scheduler.start()

CMD_HELP.update({
"Spotify Publisher":
"Simple background running process to publish the user's currently \
\nplaying track to a channel specified in configuration"
})