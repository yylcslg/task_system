
import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress


def process():

    urls =['https://www.youtube.com/watch?v=EEshiMH1cNw']

    num=0
    for url in urls:
        num = num+1
        pytubefix_test(url, str(num))
        pass

    pass




def pytubefix_test(url,num):
    proxies = {"http": "127.0.0.1:8889", "https": "127.0.0.1:8889"}
    yt = YouTube(url, proxies=proxies,on_progress_callback=on_progress)
    dash_streams = yt.streams.filter(is_dash=True)

    title=num +"_"+ yt.title.split(',')[0].strip()
    #title ='那些被動物戲弄的倒霉人類'
    video_stream = dash_streams.filter(type="video").order_by("resolution").last()
    video_stream.download(filename=title+'.mp4')
    audio_stream = dash_streams.filter(type="audio").first()
    audio_stream.download(filename=title+'.mp3')

    cmd = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental ./fun/{title}.mp4"
    subprocess.run(cmd, shell=True)

    print(title, '  恭喜你，视频合成成功！', '.......................................')
    os.remove(f'{title}.mp3')
    os.remove(f'{title}.mp4')

    pass





if __name__ == '__main__':
    process()

    print('finish.....')
    pass