import discord
from discord import Intents
from discord.ext import commands
#function names are from this library
import os
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True

#create an instance of a client
client = discord.Client(intents=intents)

# Path to the file where friend's advice will be stored
ADVICE_FILE = 'friends_advice.json'

# Function to load advice from the JSON file
def load_advice():
    try:
        with open(ADVICE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save advice to the JSON file
def save_advice(advice_list):
    with open(ADVICE_FILE, 'w') as file:
        json.dump(advice_list, file, indent=4)

# Function to get a random piece of friend's advice
def get_random_friends_advice():
    advice_list = load_advice()
    if advice_list:
        return random.choice(advice_list)
    return None

# Function to add new advice to the JSON file
def add_advice(new_advice):
    advice_list = load_advice()
    advice_list.append(new_advice)
    save_advice(advice_list)

# Function to get a random piece of advice
def get_random_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    if response.status_code == 200:
        data = response.json()
        return data['slip']['advice']
    return None

# Load Gen Z slang terms from JSON file
with open('gen_z_slang.json', 'r') as file:
    gen_z_slang = json.load(file)

#use the client to register an event
@client.event
#this event is going to be called when the bot is ready to start being used 
#0 is going to be replaced by the client, so it's client.user to get the username
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


#creating another event
@client.event
#this event triggers every time a msg is being recieved
async def on_message(message):
  #if msg is from ourselves, ignore
  if message.author == client.user:
    return
  #see if the msg is a command being sent to the bot
  #bot will respond with hello if given command $hello
  if message.content.startswith('$hi'):
    await message.channel.send('Hey Bestie!')

  if message.content.startswith('$goodnight'):
    await message.channel.send('goodnight :)')

  # Check if the message contains the word "cooked" (case-  insensitive)
  if "cooked" in message.content.lower():
    await message.channel.send('keep slaying bestie')

  # Define Gen Z slang term
  if message.content.startswith('$define'):
      term = message.content[len('$define '):].strip().lower()
      # definition = get_definition(term)
      # if definition:
      #     await message.channel.send(f'{term.capitalize()}: {definition}')
      if term in gen_z_slang:
          await message.channel.send(f'{term.capitalize()}: {gen_z_slang[term]}')
      else:
          await message.channel.send(f'Sorry, I don\'t know the definition of "{term}".')
  
  # Provide random advice
  if message.content.startswith('$advice'):
      advice = get_random_advice()
      if advice:
          await message.channel.send(f'Here is a piece of advice: {advice}')
      else:
          await message.channel.send('Sorry, I could not fetch any advice at the moment.')
  
  # Provide random friend's advice
  if message.content.startswith('$fadvice'):
      advice = get_random_friends_advice()
      if advice:
          await message.channel.send(f'Here is a piece of advice from your friends: {advice}')
      else:
          await message.channel.send('Sorry, there is no advice from your friends yet.')
  
  # Add new friend's advice
  if message.content.startswith('$addadvice'):
      new_advice = message.content[len('$addadvice '):].strip()
      if new_advice:
          add_advice(new_advice)
          await message.channel.send(f'New advice added: {new_advice}')
      else:
          await message.channel.send('Please provide some advice to add.')

  # Provide help instructions
  if message.content.startswith('$help'):
      help_message = (
          "Hey Bestie! Here are the commands you can use to talk to me (the bot) <3 :\n"
          "- `$help`: View the commands to use with the bot\n"
          "- `$hi`: Greet the bot\n"
          "- `$goodnight`: Say goodnight to the bot\n"
          "- `$define [term]`: Get the definition of a Gen Z slang term\n"
          "- `$advice`: Get a random piece of advice from the Advice Slip API\n"
          "- `$fadvice`: Get a random piece of advice from your friends or yourself\n"
          "- `$addadvice [advice]`: Add a new piece of advice from your friends or yourself\n"
      )
      await message.channel.send(help_message)
  
  
#line to run the bot
my_secret = os.environ['TOKENN']
client.run(my_secret)

