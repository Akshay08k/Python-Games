from pytube import Playlist
import os

def download_youtube_playlist(playlist_url, download_path):
    playlist = Playlist(playlist_url)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    print(f'Downloading playlist: {playlist.title}')
    print(f'Total videos: {len(playlist.video_urls)}')
    
    for video in playlist.videos:
        try:
            print(f'Downloading {video.title}...')
            video.streams.get_highest_resolution().download(output_path=download_path)
            print(f'{video.title} downloaded successfully.')
        except Exception as e:
            print(f'Failed to download {video.title}. Error: {e}')
    
    print('All downloads complete!')

if __name__ == "__main__":
    playlist_url = ''
    # Enter the link of playlist that you want to download
    download_path = './downloads'
    
    download_youtube_playlist(playlist_url, download_path)
