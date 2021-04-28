from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

count = 30

tiktoks = api.byHashtag("nuggs", count=10)

for tiktok in tiktoks:
    print(tiktok['stats'])