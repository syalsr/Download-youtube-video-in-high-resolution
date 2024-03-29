import os
from pytube import YouTube
import ffmpeg

path = './'
count = 1

def combine(video, audio, name):
    video_stream = ffmpeg.input(video)
    audio_stream = ffmpeg.input(audio)
    
    ff = ffmpeg.output(audio_stream, video_stream, path + name + '.mp4').run()

def download_video(link):
    yt = YouTube(link)
    video = yt.streams.filter(file_extension='mp4').order_by('resolution').last()
    video_name = 'video ' + video.title + '.mp4'
    result_name = video.title
    print('RESULT NAME: ', result_name)
    video.download(path, video_name)
    if not video.is_progressive:
        audio = yt.streams.get_audio_only()
        audio_name = 'audio' + audio.title + 'mp4'
        audio.download(path, audio_name)
        combine(path + video_name, path + audio_name, video.title)
    os.remove(audio_name)
    os.remove(video_name)

def download_audio(link):
    yt = YouTube(link)
    audio = yt.streams.get_audio_only()
    audio_name = 'audio ' + audio.title + '.mp3'
    audio.download(path, audio_name)

def parse_links():
    list_links = list()
    while True:
        inp = input("Enter link or exit to start downloading: ")
        if inp.lower() == "exit":
            break
        list_links.append(inp)
    return list_links

def run_download_video(links):
    for link in links:
        download_video(link)

def run_download_audio(links):
    for link in links:
        download_audio(link)

if __name__ == '__main__':
    anwser = input('Would you download video or audio: ')
    links = parse_links()
    if anwser.lower() == 'video':
        run_download_video(links)
    elif anwser.lower() == 'audio':
        run_download_audio(links)

    #os.system(f'ffmpeg -i new.mp4 -ac 2 -f wav new.wav')

