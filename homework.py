import requests
import time

# トップストーリーのIDリストを取得
top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()

# 30件のニュースを取得
for i in range(30):
    time.sleep(1)  # 1秒間隔を空ける
    story_id = top_stories[i]
    story_data = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json').json()
    title = story_data.get('title', 'タイトルなし')
    link = story_data.get('url', None)
    print({'title': title, 'link': link})
