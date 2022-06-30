from googleapiclient.discovery import build

api_key = 'AIzaSyAqEKiUoSQ8sR81kpuaZLJNlsEwmBHFAH0'

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
        part="id,snippet",
        type='video',
        q="Spider-Man",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1,
        fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
)

response = request.execute()

print(response)