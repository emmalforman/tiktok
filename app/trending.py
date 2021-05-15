from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)

results = 10

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=1, custom_verifyFp="")
'''
for tiktok in trending:
    # Prints the hashtag info of trending tiktoks
    for d in tiktok["textExtra"]:
        hashtags.append(d["hashtagName"])
    print(hashtags)
'''
for tiktok in trending:
    # Prints the text of the tiktok
    print(type(tiktok))
    tag = False
    print(tiktok)
    for d in tiktok:  
       # print(d)
        '''
        info = list(d.keys())
        if "textExtra" in info:
            tag = True
    if tag == True:
        print(tiktok[9]['hashtagName'])
    else:
        print("no hashtag")
        '''

print(len(trending))