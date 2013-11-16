import json, urllib2, os

from gif.models import Gif

def gif_get():
    hdr = { 'User-Agent' : 'Gif Grabber by /u/fizzzzzzzzzzzy' }
    req = urllib2.Request("http://www.reddit.com/r/gifs/top.json?t=day", headers=hdr)
    reddit_json = json.load(urllib2.urlopen(req))
    rank = Gif.objects.count()
    for post in reddit_json['data']['children']:
        if post['data']['score'] > 1500:
            url = post['data']['url'].replace('gallery/','')
            if (url[-4:] != '.gif') & (url[-4:] != '.jpg'):
                url += ".gif"
            name = url[url.rfind('/')+1:]
            os.system('wget -O /var/www/media/gifs/%s %s' % (name, url))
            gif = Gif(image = "gifs/" + name)
            gif.save()
            rank += 1

def gif_clean():
    gifs = Gif.objects.all()
    for gif in gifs:
        if gif.rank > 99:
            gif.delete()
