from typing import Any
from googleapiclient.discovery import build
import os
import psycopg2

channel_ids = [
    'UC-OVMPlMA3-YCIeg4z5z23A',
    'UCwHL6WHUarjGfUM_586me8w'
]
api_key = os.getenv('API_KEY')

def get_youtube_data(api_key: str, channel_ids: list[str]):

    youtube = build('youtube', 'v3', developerKey=api_key)
    data = []
    videos_data = []
    next_page_token = None
    for channel_id in channel_ids:
        channel_data = youtube.channels().list(part='snippet, statistics', id=channel_id).execute()


        #while True:
            #response = youtube.search().list(part='id,snippet', channelId=channel_id, type='video',
                                             #order='date', maxResults=50, pageToken=next_page_token).execute()
            #videos_data.extend(response['items'])
            #next_page_token = response.get('nextPageToken')
            #if not next_page_token:
                #break

        data.append({
            'channel': channel_data['items'][0],
            #'videos': videos_data
        })

        return data

def create_database(database_name: str, params: dict) -> None:
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE channels (
                channel_id SERIAL PRIMARY KEY,
                title varchar(255) NOT null,
                views int,
                subscribers int,
                videos int
        
        )""")
    conn.commit()
    conn.close



def save_data_to_database(data, database_name: str, params: dict) -> None:
    pass
