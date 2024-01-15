import time
import os
import json
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL

from youtube_dl.utils import (DownloadError, ContentTooShortError,

                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)

from telethon import types
from telethon.tl import functions
from Cutiepii_Robot.cutiepii import Cutiepii_Robot
from youtubesearchpython import SearchVideos
from tswift import Song


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    return None

JULIASONG = "@MissJuliaRobotMP3"
JULIAVSONG = "@MissJuliaRobotMP4"


@Cutiepii_Robot(pattern="^/lyrics ?(.*)")
async def download_lyrics(v_url):
    if v_url.is_group:
        if (await is_register_admin(v_url.input_chat, v_url.message.sender_id)):
            pass
        elif v_url.chat_id != iid or v_url.sender_id != userss:
            return
    query = v_url.pattern_match.group(1)
    if not query:
        await v_url.reply("You haven't specified which song to look for!")
        return
    if song := Song.find_song(query):
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song!"
    else:
        reply = "Song not found!"
    if len(reply) > 4090:
        with open("lyrics.txt", "w") as f:
            f.write(f"{reply}")
        with open("lyrics.txt", "rb") as f:
            await v_url.client.send_file(
                v_url.chat_id,
                file=f,
                caption="Message length exceeded max limit! Sending as a text file.")
    else:
        await v_url.reply(reply)

global __help__
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /song <songname artist(optional)>: uploads the song in it's best quality available
 - /video <songname artist(optional)>: uploads the video song in it's best quality available
 - /lyrics <songname artist(optional)>: sends the complete lyrics of the song provided as input
 
"""
__mod_name__ = "Music"
