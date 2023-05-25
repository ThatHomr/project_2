import requests

def get_channel_watch_time(channel_id, access_token):
    url = f"https://api.twitch.tv/helix/users/follows?to_id={channel_id}"
    headers = {
        "Client-ID": 'ropc6qmombtag8l64vjssuz474l2v9',
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        total_watch_time = sum([follow['viewed_at'] - follow['followed_at'] for follow in data['data']])
        return total_watch_time
    else:
        print(response.status_code)
        print("API 요청이 실패했습니다.")
        return None

channel_id = "vo_ine"
access_token = '8f8ppttqu2b40d88ioe0ksvha2dt3n'

watch_time = get_channel_watch_time(channel_id, access_token)

if watch_time is not None:
    print(f"채널 시청 시간: {watch_time} 분")
