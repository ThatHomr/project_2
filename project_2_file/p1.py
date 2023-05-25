import requests
import time
# my_id = 'ropc6qmombtag8l64vjssuz474l2v9'
# my_secrect = '3bapaxa5dunbd0rnc4yje8hdljk2x9'
# req = requests.post(
#     f'https://id.twitch.tv/oauth2/token?client_id={my_id}&client_secret={my_secrect}&grant_type=client_credentials')
# print(req.text)


def get_channel_watch_time(channel_id):
    my_id = 'ropc6qmombtag8l64vjssuz474l2v9'
    my_secrect = '3bapaxa5dunbd0rnc4yje8hdljk2x9'
    req = requests.post(
        f'https://id.twitch.tv/oauth2/token?client_id={my_id}&client_secret={my_secrect}&grant_type=client_credentials')
    print(req.text)
    print(req.json()['access_token'])
    access_token = req.json()['access_token']

    time.sleep(1)
    url = f"https://api.twitch.tv/helix/users?login={channel_id}'"
    headers = {
        "Client-ID": 'ropc6qmombtag8l64vjssuz474l2v9',
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    print(response.text)


get_channel_watch_time("vo_ine")
