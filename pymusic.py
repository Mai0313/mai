from pytube import YouTube
from ytmusicapi import YTMusic
import os

def get_video(url: str, outpath: str):
    os.makedirs(outpath, exist_ok=True)
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download(outpath)

def get_vid_link(video_names: str, filter_type: str = "videos"):
    ytmusic = YTMusic()
    __search_result = ytmusic.search(query = video_names, filter = filter_type, limit = 1)
    vid = __search_result[0].get("videoId")
    result = f"https://www.youtube.com/watch?v={vid}"
    return result

if __name__ == "__main__":
    song = get_vid_link("we dont talk anymore")
    get_video(song, './vvv')
