import requests

def get_access_token(client_id, client_secret):
    url = f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    response = requests.post(url)
    data = response.json()
    access_token = data["access_token"]
    return access_token

# Twitch API 인증 정보
client_id = 'ropc6qmombtag8l64vjssuz474l2v9'
client_secret = '3bapaxa5dunbd0rnc4yje8hdljk2x9'
oauth_token = get_access_token(client_id, client_secret)
user_login = 'psjgopsj'

# Twitch API 엔드포인트
user_url = f'https://api.twitch.tv/helix/users?login={user_login}'

# Twitch API를 통해 사용자의 user_id 조회
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {oauth_token}'
}

response = requests.get(user_url, headers=headers)
data = response.json()

if len(data['data']) > 0:
    user_id = data['data'][0]['id']
    print(f"사용자 '{user_login}'의 user_id: {user_id}")
else:
    print(f"사용자 '{user_login}'를 찾을 수 없습니다.")
