from pytube import YouTube
from ytmusicapi import YTMusic
import os
import json

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

def get_vid_names(path):
    filenames = [f for f in os.listdir(path) if f.endswith('.mp4')]
    vid_names = [f.split(".")[0] for f in filenames]
    return vid_names

if __name__ == "__main__":
    targets = ["STAY - Justin Bieber",
               "Jiggle Jiggle - Jason Derulo x Duke x Louis Theroux x Amelia Dimz",
               "Bad Habits - Ed Sheeran",
               "Born To Do - Steven Cooper",
               "Been Through - EXO",
               "Despacito - Luis Fonsi x Daddy Yankee x Justin Bieber",
               "Bad Guy - Billie Eilish",
               "Still D.R.E. - Dr. Dre x Snoop Dogg",
               "Enemy - Imagine Dragons x J.I.D","Believer - Imagine Dragons",
               "Thunder - Imagine Dragons",
               "Mood - 24kGoldn",
               "Drake - Hotline Bling",
               "A$AP Ferg - Plain Jane REMIX (Official Audio) ft. Nicki Minaj",
               "The Chainsmokers - Don't Let Me Down (Official Video) ft. Daya"
               ]
    output_path = "./vids"

    for target in targets:
        song = get_vid_link(target)
        get_video(song, output_path)
    video_names = get_vid_names(output_path)
    with open(f'./{output_path}/vid_names.json', 'w') as f:
        json.dump(video_names, f)
