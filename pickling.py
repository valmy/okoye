from telethon import TelegramClient, events
from datetime import datetime
import pickle

with open('test.pickle', 'rb') as msgf:
    messages = pickle.load(msgf)
    print(len(messages))
    print(messages)

with open('test.pickle', 'w+b') as msgf:
    messages.append({ 'a': 1, 'b': 2 })
    messages.append({ 'a': 3, 'b': 4 })
    print(len(messages))
    pickle.dump(messages, msgf)
    