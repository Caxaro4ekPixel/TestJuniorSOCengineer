from decouple import config
import logging
from pyrogram import Client


api_id = config('api_id')
api_hash = config('api_hash')
username = config('username')

client_tg = Client(username, api_id, api_hash)

urls_list = config('chats').split(',')

logging.basicConfig(filename='logging project.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level='INFO')