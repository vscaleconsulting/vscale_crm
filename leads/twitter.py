from .models import Contact
import tweepy

consumer_key = "kPTJKLaiwskJHkTbVtlmKdGjC"
consumer_secret = "phJUgKipmEUcoyDgAx6c2Gd9sWDm45RnmS5hYfNJ0khoLpXznM"
access_token = "928953443921813505-MXlWzuRj1FuZL1z0t28ETtZg9LrRyPg"
access_token_secret = "oR0vs0n9zxFZmfh76lGepI7XTTbswag3jl00jk6hR1Ysc"


def create_list(user):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    list_name = f'user_{user.id}'
    lsts = api.lists_all()
    
    for lst in lsts:
        if lst.name == list_name:
            user_list = lst
            break
    else:
        user_list = api.create_list(list_name)

    return f'https://twitter.com/{auth.get_username()}/lists/{user_list.id}'


def add_to_list(user, contact):
    ret1, ret2 = True, True
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    list_id = int(user.twitter_list.split('/')[-1])
    try:
        api.add_list_member(list_id=list_id, screen_name=contact.twitter_personal)
    except:
        ret1 = False
    try:
        api.add_list_member(list_id=list_id, screen_name=contact.twitter_brand)
    except:
        ret2 = False
    return ret1, ret2

def remove_extra(user, contact=None):
    contacts = Contact.objects.filter(user=user).all()
    handles = []
    for cntct in contacts:
        if contact is not None and cntct.id == contact.id: 
            continue
        if cntct.twitter_personal is not None:
            handles.append(cntct.twitter_personal.lower())
        if cntct.twitter_brand is not None:
            handles.append(cntct.twitter_brand.lower())
            
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    list_id = int(user.twitter_list.split('/')[-1])
    members = api.list_members(list_id = list_id)
    print(handles)
    print([m.screen_name for m in members])
    for member in members:
        if member.screen_name.lower() not in handles:
            print('removing', member.screen_name, member.id)
            api.remove_list_member(list_id = list_id, screen_name = member.screen_name)

