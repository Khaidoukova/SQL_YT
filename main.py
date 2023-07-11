import os
from utils import get_youtube_data, create_database, save_data_to_database
from config import config


def main():
    api_key = 'AIzaSyCBh9oaWXIhnkxRLjw9Imla_EcFqSpecyU'
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A']
    params = config()

    #data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    #save_data_to_database(data, 'youtube', params)




if __name__ == '__main__':
    main()

