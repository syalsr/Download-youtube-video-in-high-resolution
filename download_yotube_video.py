import os
from pytube import YouTube
import ffmpeg

path = './'
count = 1
result_name = ''

def combine(video, audio):
    video_stream = ffmpeg.input(video)
    audio_stream = ffmpeg.input(audio)
    ff = ffmpeg.output(audio_stream, video_stream, path + "result_name.mp4").run()

def download_video(link):
    yt = YouTube(link)
    video = yt.streams.filter(file_extension='mp4').order_by('resolution').last()
    video_name = 'video' + video.title + '.mp4'
    result_name = video.title
    video.download(path, video_name)
    if not video.is_progressive:
        audio = yt.streams.get_audio_only()
        audio_name = 'audio' + audio.title + 'mp4'
        audio.download(path, audio_name)
        combine(path + video_name, path + audio_name)
    os.remove(audio_name)
    os.remove(video_name)

def parse_links():
    list_links = list()
    while True:
        inp = input("Enter link or exit for: ")
        if inp == "exit":
            break
        list_links.append(inp)
    return list_links

def run_download_video(links):
    for link in links:
        download_video(link)

if __name__ == '__main__':
    links = parse_links()
    run_download_video(links)


    #os.system(f'ffmpeg -i new.mp4 -ac 2 -f wav new.wav')

