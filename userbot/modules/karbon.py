import os
import time
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from time import sleep
from html import unescape
from re import findall
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from urbandict import define
from requests import get
from search_engine_parser import GoogleSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN, bot
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
from userbot.modules.upload_download import progress, humanbytes, time_formatter
from userbot.google_images_download import googleimagesdownload
import subprocess
from datetime import datetime


CARBONLANG = "auto"
TTS_LANG = "en"
TRT_LANG = "en"
TEMP_DOWNLOAD_DIRECTORY = "/root/userbot/.bin"

@register(outgoing=True, pattern="^.crblang (.*)")
async def setlang(prog):
    global CARBONLANG
    CARBONLANG = prog.pattern_match.group(1)
    await prog.edit(f"Language for carbon.now.sh set to {CARBONLANG}")

@register(outgoing=True, pattern="^.karbon1")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Processing..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
    

@register(outgoing=True, pattern="^.karbon2")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Processing..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
    

@register(outgoing=True, pattern="^.karbon3")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(74%2C144%2C226%2C1)&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Processing..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
    
    
@register(outgoing=True, pattern="^.karbon4")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(29%2C40%2C104%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Processing..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
    

@register(outgoing=True, pattern="^.karbon5")
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = 'https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    await e.edit("`Processing..\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': '/root/userbot/.bin'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    driver.get(url)
    await e.edit("`Processing..\n50%`")
    download_path = '/root/userbot/.bin'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    while not os.path.isfile("/root/userbot/.bin/carbon.png"):
        await sleep(0.5)
    await e.edit("`Processing..\n100%`")
    file = '/root/userbot/.bin/carbon.png'
    await e.edit("`Uploading..`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Made using [Carbon](https://carbon.now.sh/about/),\
        \na project by [Dawn Labs](https://dawnlabs.io/)",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('/root/userbot/.bin/carbon.png')
    driver.quit()
    # Removing carbon.png after uploading
    await e.delete()  # Deleting msg
    

@register(outgoing=True, pattern="^.karbonRGB")
async def carbon_api(e):
 RED = random.randint(0,256)
 GREEN = random.randint(0,256)
 BLUE = random.randint(0,256)
 THEME= [         "3024-night",
                  "a11y-dark",
                  "blackboard",
                  "base16-dark",
                  "base16-light",
                  "cobalt",
                  "dracula",
                  "duotone-dark",
                  "hopscotch",
                  "lucario",
                  "material",
                  "monokai",
                  "night-owl",
                  "nord",
                  "oceanic-next",
                  "one-light",
                  "one-dark",
                  "panda-syntax",
                  "paraiso-dark",
                  "seti",
                  "shades-of-purple",
                  "solarized",
                  "solarized%20light",
                  "synthwave-84",
                  "twilight",
                  "verminal",
                  "vscode",
                  "yeti",
                  "zenburn",
]

 CUNTHE = random.randint(0, len(THEME) - 1)
 The = THEME[CUNTHE]


 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
   """ A Wrapper for carbon.now.sh """
   await e.edit("⬜⬜⬜⬜⬜")
   CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
   CARBONLANG = "en"
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[8:]:
         pcode = str(pcode[8:])
   elif textx:
         pcode = str(textx.message) # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded
   url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, T=The, lang=CARBONLANG)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.binary_location = GOOGLE_CHROME_BIN
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument('--disable-gpu')
   prefs = {'download.default_directory' : './'}
   chrome_options.add_experimental_option('prefs', prefs)
   await e.edit("⬛⬛⬜⬜⬜")

   driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
   driver.get(url)
   download_path = './'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   sleep(5) # this might take a bit.
   #driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   await e.edit("⬛⬛⬛⬜⬜")
   #driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   #sleep(5) #Waiting for downloading

   await e.edit("⬛⬛⬛⬛⬛")
   file = './carbon.png'
   await e.edit("✅RGB Karbon Completed, Uploading Karbon✅")
   await e.client.send_file(
         e.chat_id,
         file,
         caption="RGB Karbon by [@PhycoNinja13b](https://github.com/Phyco-Ninja/UniNinja)",
         force_document=True,
         reply_to=e.message.reply_to_msg_id,
         )

   os.remove('./carbon.png')
   # Removing carbon.png after uploading
   await e.delete() # Deleting msg    
    
    
@register(outgoing=True, pattern="^.karbonRGB2")
async def carbon_api(e):   
 RED = random.randint(0,256)
 GREEN = random.randint(0,256)
 BLUE = random.randint(0,256)
 OPC = random.random()
 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
   """ A Wrapper for carbon.now.sh """
   await e.edit("⬜⬜⬜⬜⬜")
   CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C{O})&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
   CARBONLANG = "en"
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[8:]:
         pcode = str(pcode[8:])
   elif textx:
         pcode = str(textx.message) # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded
   url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, O=OPC, lang=CARBONLANG)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.binary_location = GOOGLE_CHROME_BIN
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument('--disable-gpu')
   prefs = {'download.default_directory' : './'}
   chrome_options.add_experimental_option('prefs', prefs)
   await e.edit("⬛⬛⬜⬜⬜")

   driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
   driver.get(url)
   download_path = './'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   sleep(5) # this might take a bit.
   #driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   await e.edit("⬛⬛⬛⬜⬜")
   #driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   #sleep(5) #Waiting for downloading

   await e.edit("⬛⬛⬛⬛⬛")
   file = './carbon.png'
   await e.edit("✅RGB Karbon 2.0 Completed, Uploading Karbon✅")
   await e.client.send_file(
         e.chat_id,
         file,
         caption="RGB Karbon 2.0 by [@PhycoNinja13b](https://github.com/Phyco-Ninja/UniNinja)",
         force_document=False,
         reply_to=e.message.reply_to_msg_id,
         )

   os.remove('./carbon.png')
   # Removing carbon.png after uploading
   await e.delete() # Deleting msg
    
    
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})

    
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})

    
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
