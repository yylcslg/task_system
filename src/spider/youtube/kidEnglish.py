import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress


def process():

    urls =['https://www.youtube.com/watch?v=7icfo2Pdhr4&list=PL_pla4siITKTruKMtm5lhmVh-soWx4A9b&index=5',
        'https://www.youtube.com/watch?v=iIVXqMNDwDI&list=PL_pla4siITKSoegPCvro0XzseBdNV8u4q&index=11',
        'https://www.youtube.com/watch?v=bCYap9NtE6o&list=PL_pla4siITKSoegPCvro0XzseBdNV8u4q&index=10',
    'https://www.youtube.com/watch?v=Qow3orv23Vk&list=PL_pla4siITKSoegPCvro0XzseBdNV8u4q&index=7']

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
    video_stream = dash_streams.filter(type="video").order_by("resolution").last()
    video_stream.download(filename=title+'.mp4')
    audio_stream = dash_streams.filter(type="audio").first()
    audio_stream.download(filename=title+'.mp3')

    cmd = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental ./video/{title}_f.mp4"
    subprocess.run(cmd, shell=True)

    print(title, '  恭喜你，视频合成成功！', '.......................................')
    os.remove(f'{title}.mp3')
    os.remove(f'{title}.mp4')

    pass





if __name__ == '__main__':
    process()

    print('finish.....')
    pass