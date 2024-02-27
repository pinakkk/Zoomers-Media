from pyrogram import Client, filters
import requests
import random

PEXELS_API_KEY = 'uScsXBmUhUSb9clnKgleIYRWdbLS0Rm15Gbn2OPy37FuEc5w8O3fz0DV'
YOUR_API_ID = '21758893'
YOUR_API_HASH ='4884f995dee937367a0a1cc6e2d41e68'
YOUR_TELEGRAM_BOT_TOKEN ='7090672339:AAFP_t3V_KMBg5VK8pHcANnB4Bnd-wFHuZI'

app = Client(
    "Zoomers-Media_bot",
    api_id=YOUR_API_ID,
    api_hash=YOUR_API_HASH,
    bot_token=YOUR_TELEGRAM_BOT_TOKEN
)

def search_pexels_images(query):
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=3'
    headers = {'Authorization': PEXELS_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return [photo['src']['original'] for photo in data['photos']]
        else:
            return []
    else:
        return []

def search_pexels_videos(query):
    url = f'https://api.pexels.com/videos/search?query={query}&per_page=3'
    headers = {'Authorization': PEXELS_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['videos']:
            return [video['video_files'][0]['link'] for video in data['videos']]
        else:
            return []
    else:
        return []

@app.on_message(filters.command("generate") & filters.private)
async def handle_generate_command(client, message):
    command_parts = message.text.split(' ')
    if len(command_parts) < 3:
        await message.reply_text('Please specify a search term and whether you want images or videos. Example: /generate nature images')
        return

    search_term = command_parts[1]
    media_type = command_parts[2].lower()

    if media_type not in ['images', 'videos']:
        await message.reply_text('Invalid media type. Please specify "images" or "videos".')
        return

    await message.reply_text('Working on it...')

    if media_type == 'images':
        results = search_pexels_images(search_term)
        if results:
            for result in results[:5]:
                await client.send_photo(message.chat.id, result)
        else:
            await message.reply_text(f'Sorry, could not find any images related to "{search_term}".')
    else:
        results = search_pexels_videos(search_term)
        if results:
            for result in results[:5]:
                await client.send_video(message.chat.id, result)
        else:
            await message.reply_text(f'Sorry, could not find any videos related to "{search_term}".')

app.run()