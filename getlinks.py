import requests as re

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, identity",
    "Accept-Language": "en-GB,en;q=0.5",
    "Connection": "keep-alive",
    "Host": "www.reddit.com",
    "Origin": "https://www.reddit.com",
    "Referer": "https://www.reddit.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
    "x-reddit-loid": "0000000007mt11b57x.2.1679479692000.Z0FBQUFBQmtHdE9NU0dLSWk4STlwQnVKLVBJYVlfaE5Dcm9IZlNKVEpMb0kwNmkxVW1tUWt3bzhaSkRrVFpGRk1JZktVajF0Vl9pY09Zdm9zNzBMdVZoYloyMkpnSnVGMjZJXzN0WjlJOGE2bzlrMkxsUmpqR2JfYl83OXZoN0JuRVZNd2gxanhKT3Q",
    "x-reddit-session": "oaXz2vCyZyBtd4B6kD.0.1680112926681.Z0FBQUFBQmtKSDBlQXpTQnEwaWJCeXVGSkdvWmUwWkVfNFAxcGlsSEVnbFBpeVZoYld0clBSTldVNWN4OE5VMU8xYlBkZnNoSnpWMmdBZGtqOGtOczN3a1BRdWFVY09TQkJScF9XbnUwcTdGYkVOTUR4REh5WjFETHhyaTBnSFNTeU5UNkkwSG5ka1c"
}


def fetch_links(sub):
    links = []
    base = f'https://www.reddit.com/r/{sub}/top.json'
    res = re.get(base, headers=headers).json()
    for post in res['data']['children']:
        try:
                print (post['data']['over_18']== True )

                if post['data']['over_18'] == True:
                    print('not selected')
                    pass
                else :
                    links.append(post['data']['url'])

        except Exception as e:
            print(e)
            pass
    return links
