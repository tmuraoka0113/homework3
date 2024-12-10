import requests
import time

# トップストーリーのIDリストを取得
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(top_stories_url)
top_stories = response.json()

# 30件のニュースを取得
for story_id in top_stories[:30]:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_response = requests.get(story_url)
    story_data = story_response.json()

    # タイトルを取得
    title = story_data.get("title", "タイトルなし")

    # リンクを取得（存在しない場合はNone）
    link = story_data.get("url", None)

    # データを表示
    print(f"タイトル: {title}")
    print(f"リンク: {link}\n")

    # APIへの連続アクセスを避けるため1秒間隔を空ける
    time.sleep(1)
