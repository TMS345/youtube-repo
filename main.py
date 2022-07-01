from googleapiclient.discovery import build

import pandas as pd

import sqlalchemy as db

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

data = request.execute()

data_frame = pd.DataFrame.from_dict (data)

engine = db.create_engine('sqlite:///data_base_name.db')

data_frame.to_sql('table_name', con=engine, if_exists='replace', index=False)

query_result = engine.execute("SELECT * FROM table;").fetchall ()

print(pd.DataFrame(query_result))