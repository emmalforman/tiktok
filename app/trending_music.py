from TikTokApi import TikTokApi
import os

api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)

results = 1

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=1, custom_verifyFp="")

def get_trending_music():
    for tiktok in trending:
        # Prints the hashtag info of trending tiktoks
        for m in tiktok["challenges"]:
            print(m)
print(get_trending_music())