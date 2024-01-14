import shelve
from datetime import date

import matplotlib.pyplot as plt
import pytube


def load_yt_stats(yt_url):
    warehouse = shelve.open('channel_stats')
    yt = pytube.Channel(yt_url)
    videos_data = []
    print(yt.channel_name, len(list(yt.videos)))
    for video in list(yt.videos):
        """
        ['responseContext', 'contents', 'currentVideoEndpoint', 
        'trackingParams', 'playerOverlays', 'overlay', 
        'onResponseReceivedEndpoints', 'engagementPanels', 'topbar', 
        'frameworkUpdates']
        
        ['contents']['twoColumnWatchNextResults']['results']['results']
        ['contents'][0]['videoPrimaryInfoRenderer'] - >
        
        ['title', 'viewCount', 'videoActions', 'trackingParams', 'dateText']
        """
        d = {}

        title = video.title
    
        date, _ = str(video.publish_date).split()
        y, m, n = date.split('-')
        date = (int(y), int(m), int(n))

        views = video.views
    
        try:
            likes = video.initial_data['contents']\
                ['twoColumnWatchNextResults']['results']['results']\
                ['contents'][0]['videoPrimaryInfoRenderer']\
                ['videoActions']['menuRenderer']['topLevelButtons'][0]\
                ['toggleButtonRenderer']['defaultText']['simpleText']
        except (KeyError, IndexError):
            likes = '0'

        if 'K' in likes:
            if '.' in likes:
                likes = likes[:-1].replace('.', '') + '00'
            else:
                likes = likes[:-1] + '000'
        elif 'M' in likes:
            if '.' in likes:
                likes = likes[:-1].replace('.', '') + '00000'
            else:
                likes = likes[:-1] + '000000'
        likes = int(likes) if likes != 'Like' else 0

        try:
            comments = video.initial_data['contents']\
                ['twoColumnWatchNextResults']['results']['results']\
                ['contents'][2]['itemSectionRenderer']['contents'][0]\
                ['commentsEntryPointHeaderRenderer']['commentCount']\
                ['simpleText']
        except (KeyError, IndexError):
            comments = '0'

        if 'K' in comments:
            if '.' in comments:
                comments = comments[:-1].replace('.', '') + '00'
            else:
                comments = comments[:-1] + '000'
        elif 'M' in comments:
            if '.' in comments:
                comments = comments[:-1].replace('.', '') + '00000'
            else:
                comments = comments[:-1] + '000000'
        comments = int(comments)
    
        d = dict(title=title, date=date, views=views, likes=likes,
                 comments=comments)
        videos_data.append(d)
        print(date, title, views, likes, comments)

    videos_data = sorted(videos_data, key=lambda x: x['date'])

    WH = warehouse['names']
    if yt.channel_name not in WH:
        WH.append(yt.channel_name)
    
    warehouse['names'] = WH
    warehouse[yt.channel_name] = videos_data
    warehouse.close()


def create_yt_graphics(i: int):
    warehouse = shelve.open('channel_stats')
    WH = warehouse['names']

    data = warehouse[WH[i]]
    data = sorted(data, key=lambda x: x['date'])

    """
    PDP = warehouse['PewDiePie']
    PDP = sorted(PDP, key=lambda x: x['date'])
    with open('PewDP.txt', encoding='utf-8') as f:
        t = f.readlines()[:0:-1]
        for d in t:
            try:
                y, m, n, *tt, vw, lk, cm = d.split()
            except ValueError:
                continue
            title = ' '.join(tt)
            date = eval(' '.join((y, m, n)))
            views = int(vw)
            likes = int(lk)
            comments = int(cm)

            nd = dict(date=date, title=title, views=views, likes=likes,
                      comments=comments)
            PDP.append(nd)

    PDP = sorted(PDP, key=lambda x: x['date'])
    warehouse['PewDiePie'] = PDP
    """

    ax = plt.subplot()
    # x = [d['date'][0]*10000 + d['date'][1]*100 + d['date'][2]
    # for d in data]
    # print(date(*data[0]['date']))
    x = [date(*d['date']) for d in data]
    # print(x[:50])

    views = [d['views'] for d in data]
    likes = [d['likes'] for d in data]
    comments = [d['comments'] for d in data]
    print(views[:10], list(map(len, (views, likes, comments))))

    ax = plt.subplot()
    ax.plot(x, views)
    plt.xlabel('date')
    plt.ylabel('views')
    plt.title(WH[i] + '\'s views')
    plt.savefig(WH[i] + '_views.png')
    plt.close()

    ax = plt.subplot()
    ax.plot(x, likes)
    plt.xlabel('date')
    plt.ylabel('likes')
    plt.title(WH[i] + '\'s likes')
    plt.savefig(WH[i] + '_likes.png')
    plt.close()

    ax = plt.subplot()
    ax.plot(x, comments)
    plt.xlabel('date')
    plt.ylabel('comments')
    plt.title(WH[i] + '\'s comments')
    plt.savefig(WH[i] + '_comments.png')
    plt.close()

    warehouse.close()


load_yt_stats('https://www.youtube.com/c/Akwin')
create_yt_graphics(9)
