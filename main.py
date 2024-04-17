import requests

results: list[dict] = requests.get("https://www.reddit.com/r/AmItheAsshole.json").json()['data']['children']
print(results[5]['data']['selftext_html'])
