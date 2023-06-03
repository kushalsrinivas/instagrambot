import instabot
import os
from getlinks import fetch_links
from downloader import downloader
from converter import converter
import time
bot = instabot.Bot()

bot.login(username="the.sidewalk.project", password="iloveyousugar")

# Generate a random caption
hashtags = '\n\n\n\n\n#photography #streetphotography #filmphotography #analogphotography #filmisnotdead #ishootfilm #believeinfilm #shootfilmstaybroke #thefilmcommunity #buyfilmnotmegapixels #analogvibes #filmwave #fujifilm #fujifilm_xseries #fujilove #fujifilm_global #fujifeed #fujixt4 #fujifilm_northamerica #urbanphotography #cityscape #architecturephotography #lightandshadow #moodygrams #visualsoflife #thecreatorclass #artofvisuals #visualambassadors #instagram #wanderlust'
# "cityporn",
# "earthporn",
# "astrophotography",
# "filmphotos",
# "filmphotography",
# "analog",
subreddits = [
"cityporn",
"earthporn",
    "fujifilm",
    "filmphotos",
    "filmphotography",
    "analog",
]
import random
from cleaner import cleaner

for sub in subreddits:
    print(f'scraping  {sub}.... ')
    print('downloading images.....')
    downloader(links=fetch_links(sub))

    print('reformatting....')
    converter()
    print('posting images.....')
    for image in os.listdir('images/reformatted'):
        caption = hashtags
        if image.endswith('.jpg'):
            print('uploading...')
            bot.upload_photo(f'images/reformatted/{image}', caption)
            bot.upload_story_photo(f'images/reformatted/{image}')
    print('deleteing images....')
    cleaner()
bot.logout()



# Print the caption

