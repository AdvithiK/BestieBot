# BestieBot

BestieBot is a customizable Discord bot that provides advice and defines popular Gen Z slang terms. It combines an online advice API with user-generated advice stored in a file, giving it a unique and personal touch.

## Features

- **Random Advice**: Provides random advice using the [Advice Slip API](https://api.adviceslip.com/).
- **User-Generated Advice**: Users can store and retrieve personalized advice from their friends.
- **Gen Z Slang Definitions**: Provides definitions for popular Gen Z slang terms.
  
## Commands

- `!help`: Display the list of available commands and how to use them.
- `hi`: Greet the bot.
- `goodnight`: Say goodnight to the bot.
- `!define [term]`: Get the definition of a Gen Z slang term.
- `!advice`: Get a random piece of advice from the Advice Slip API.
- `!fadvice`: Get a random piece of advice stored by your friends.
- `!addadvice [advice]`: Add a new piece of advice from your friends.

## How to Set Up

1. Clone this repository:
    ```bash
    git clone https://github.com/AdvithiK/BestieBot.git
    cd BestieBot
    ```

2. Install dependencies:
    ```bash
    pip install discord requests
    ```

3. Create a `.env` file and add your Discord Bot token:
    ```bash
    TOKENN=your_discord_token_here
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## Tech Stack

- **Python**: Core programming language.
- **Discord.py**: For interacting with Discord's API.
- **Requests**: For making HTTP requests to the Advice Slip API.
- **JSON**: For storing user-generated advice.

## Future Enhancements

- Add more Gen Z slang terms dynamically from an online source.
- Add features like scheduling messages or interactive games.

## About the Developer

This project was developed by **Advithi Kethidi**, who is passionate about building fun, interactive bots using Python and loves learning new technologies.
