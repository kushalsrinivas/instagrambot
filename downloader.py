import requests as re
def downloader(links=['']):
    for i,link in enumerate(links):
        data = re.get(link).content
        with open(f'images/{i}.jpg', 'wb') as file:
            file.write(data)
        print(f'{i+1} images downloaded')