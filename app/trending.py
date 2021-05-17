from TikTokApi import TikTokApi
import os
import trending.py from app

api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)

results = 1

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=1, custom_verifyFp="")

def get_trending():
    for tiktok in trending:
        # Prints the hashtag info of trending tiktoks
        for d in tiktok["textExtra"]:
            print(d['hashtagName'])

output = get_trending()