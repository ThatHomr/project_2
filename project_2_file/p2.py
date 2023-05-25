import requests

def get_access_token(client_id, client_secret):
    url = f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    response = requests.post(url)
    data = response.json()
    access_token = data["access_token"]
    return access_token

def get_subscribed_channels(user_id, access_token):
    subscribed_channels = []
    url = f"https://api.twitch.tv/helix/users/follows?from_id={user_id}"
    headers = {
        "Client-ID": 'ropc6qmombtag8l64vjssuz474l2v9',
        "Authorization": f"Bearer {access_token}"
    }

    while True:
        response = requests.get(url, headers=headers)
        data = response.json()

        for follow in data.get("data", []):
            subscribed_channels.append(follow["to_id"])

        pagination = data.get("pagination", {})
        cursor = pagination.get("cursor")
        if not cursor:
            break

        url = f"https://api.twitch.tv/helix/users/follows?from_id={user_id}&after={cursor}"

    return subscribed_channels

# 클라이언트 ID와 클라이언트 시크릿을 입력하세요
client_id = 'ropc6qmombtag8l64vjssuz474l2v9'
client_secret = '3bapaxa5dunbd0rnc4yje8hdljk2x9'

# 사용자 ID를 입력하세요
user_id = 'psjgopsj'

# 액세스 토큰을 얻습니다
access_token = get_access_token(client_id, client_secret)
print(access_token)

# 액세스 토큰을 사용하여 구독 중인 채널 ID를 가져옵니다
subscribed_channels = get_subscribed_channels(user_id, access_token)

print(subscribed_channels)