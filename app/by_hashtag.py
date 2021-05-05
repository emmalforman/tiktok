from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

count = 30

tiktoks = api.byHashtag("nuggs", count=10)

#prints the statistics for top 10 videos under #nuggs
for tiktok in tiktoks:
    print(tiktok['stats'])
