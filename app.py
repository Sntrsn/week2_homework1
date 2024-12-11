import requests
import time

URL = "https://hacker-news.firebaseio.com/v0"


def get_top_story_ids(limit=30):
    url = f"{URL}/topstories.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[:limit]
    else:
        print("トップストーリーの取得に失敗しました。")
        return []


def get_story_details(story_id):
    url = f"{URL}/item/{story_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ストーリーID {story_id} の詳細取得に失敗しました。")
        return None


def main():
    top_story_ids = get_top_story_ids()
    for story_id in top_story_ids:
        story = get_story_details(story_id)
        if story and "title" in story:
            title = story["title"]
            link = story.get("url", None)
            if link:
                print({"title": title, "link": link})
        time.sleep(1)


if __name__ == "__main__":
    main()
