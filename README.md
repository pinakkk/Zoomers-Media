# Zoomers-Media

# Setup 
To use this bot, you need to follow these steps:

Get Pexels API Key: Obtain your Pexels API key from Pexels.
Get Telegram API Credentials: Obtain your Telegram API ID, API Hash, and Bot Token from Telegram's website.
Install Dependencies: Install the required Python packages using pip:
pip install pyrogram requests

# Usage
1. Clone the repository:
git clone https://github.com/yourusername/stockvideo-bot.git

2. Navigate to the project directory:
cd stockvideo-bot

3. Open main.py and replace the placeholders with your Pexels API key, Telegram API credentials, and bot token:
PEXELS_API_KEY = 'YOUR_PEXELS_API_KEY'
YOUR_API_ID = 'YOUR_TELEGRAM_API_ID'
YOUR_API_HASH ='YOUR_TELEGRAM_API_HASH'
YOUR_TELEGRAM_BOT_TOKEN ='YOUR_TELEGRAM_BOT_TOKEN'

4. Run the bot:
python main.py

# Bot Commands
/generate {search_term} {media_type}: Generate stock images or videos based on the search term.
Example: /generate nature images

# How it Works
The bot communicates with the Pexels API to search for images and videos based on the user's command.
It then sends the top 5 results back to the user.

# Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

# License 
This project is licensed under the MIT License.
