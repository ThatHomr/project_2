import requests
import datetime

def get_access_token(client_id, client_secret):
    url = f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    response = requests.post(url)
    data = response.json()
    access_token = data["access_token"]
    return access_token

# Twitch API 인증 정보
client_id = 'ropc6qmombtag8l64vjssuz474l2v9'
client_secret = '3bapaxa5dunbd0rnc4yje8hdljk2x9'

access_token = get_access_token(client_id, client_secret)
username = '548480905'

# Twitch API 엔드포인트
follows_url = f'https://api.twitch.tv/helix/users/follows?from_id={username}'
streams_url = 'https://api.twitch.tv/helix/streams'
idol_url = 'https://api.twitch.tv/helix/channels?broadcaster_id='

# Twitch API를 통해 사용자가 팔로우한 채널 ID 목록 가져오기
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(follows_url, headers=headers)
data = response.json()
print("data = ")
print(data)

followed_channels = [follow['to_id'] for follow in data['data']]

# 팔로우한 채널의 총 시청 시간 계산
total_watch_time = 0
ine_time = 0
lilpa_time = 0
vichan_time = 0
gosegu_time = 0
jing_time = 0
jururu_time = 0

idol_list = ['ine', 'jingburger', 'lilpa', 'jururu', 'gosegu', 'vichan']
idol_id = {
    'ine' : 702754423,
    'lilpa' : 169700336,
    'vichan' : 195641865,
    'gosegu' : 707328484,
    'jingburger' : 237570548,
    'jururu' : 75453891,
    'roent' : 137881582,
    'wak' : 49045679
}

for channel_id in followed_channels:
    response = requests.get(f'{streams_url}?user_id={channel_id}', headers=headers)
    stream_data = response.json()
    print("스트림 데이터 : ")
    print(stream_data)
    
    # for idol_id in idol_list:
    #     if len(stream_data['data']) > 0:
    #     stream_start_time = stream_data['data'][0]['started_at']
    #     stream_start_time = stream_start_time.replace('T', ' ').replace('Z', '')
    #     stream_start_time = datetime.datetime.strptime(stream_start_time, '%Y-%m-%d %H:%M:%S')
        
    #     current_time = datetime.datetime.now()
        
    #     watch_time = current_time - stream_start_time
    #     total_watch_time += watch_time.total_seconds()
    
    
    if len(stream_data['data']) > 0:
        stream_start_time = stream_data['data'][0]['started_at']
        stream_start_time = stream_start_time.replace('T', ' ').replace('Z', '')
        stream_start_time = datetime.datetime.strptime(stream_start_time, '%Y-%m-%d %H:%M:%S')
        
        current_time = datetime.datetime.now()
        
        watch_time = current_time - stream_start_time
        total_watch_time += watch_time.total_seconds()
        
    # print("스트림 : ")
    # print(stream_data)

# 시청 시간 출력
total_watch_time_minutes = total_watch_time / 60
print(f'팔로우한 채널의 총 시청 시간: {total_watch_time_minutes:.2f} 분')
