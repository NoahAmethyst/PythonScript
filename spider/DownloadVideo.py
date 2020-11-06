import os
import requests


def do_load_media(url, path):
    try:
        res = requests.get(url)

        with open(path, 'wb') as file:
            file.write(res.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    videoList = []
    #Todo
    #add your video name

    originalUrl = 'your video url'

    downloadPath = '/Users/amethyst/Downloads/auth_video/'


    for video in videoList:
        #optional
        tempUrl = originalUrl.replace('xxx.mp4', video)

        do_load_media(tempUrl, downloadPath + video)

    exit()
    # main()
