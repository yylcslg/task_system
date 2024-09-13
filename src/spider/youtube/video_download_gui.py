
import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk


#https://www.youtube.com/watch?v=EEshiMH1cNw
def process():
    window = tk.Tk()
    window.title("youtube 视频下载")
    window.geometry('850x300')

    # 创建标签
    label1 = tk.Label(window, text="路径:")

    path_name = tk.StringVar()
    text1 = tk.Entry(window, width=100, textvariable=path_name)

    title_label = tk.Label(window, text="标题:")
    title = tk.StringVar()
    title_text = tk.Entry(window, width=50, textvariable=title)

    label2 = tk.Label(window, text="下载状态:")
    state = tk.StringVar()
    label3 = tk.Label(window, textvariable=state)

    def download(*args):
        try:
            url = path_name.get()
            state.set("下载中.....................")
            t = title.get()
            pytubefix_test(url, str(1),t)
            state.set("下载完成！！！！！！")
            exit(0)
        except ValueError:
            pass
    button1 = tk.Button(window, text='下载', command = download)

    label1.grid(row = 0, column=0)
    text1.grid(row=0, column=1)

    title_label.grid(row=1, column=0)
    title_text.grid(row=1, column=1)


    label2.grid(row=2, column=0)
    label3.grid(row=2, column=1)

    button1.grid(row=3, column=1)
    # 运行窗口主循环
    window.mainloop()


def pytubefix_test(url,num,title:str):
    proxies = {"http": "127.0.0.1:8889", "https": "127.0.0.1:8889"}
    yt = YouTube(url, proxies=proxies,on_progress_callback=on_progress)
    dash_streams = yt.streams.filter(is_dash=True)
    if(title == '' and len(title)==0):
        title=num +"_"+ yt.title.split(',')[0].strip()

    print('title:',title)
    #title ='那些被動物戲弄的倒霉人類'
    video_stream = dash_streams.filter(type="video").order_by("resolution").last()
    #video_stream.download(filename=title+'.mp4')
    audio_stream = dash_streams.filter(type="audio").first()
    #audio_stream.download(filename=title+'.mp3')

    #cmd = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental ./{title}_f.mp4"
    #subprocess.run(cmd, shell=True)

    print(title, '  恭喜你，视频合成成功！', '.......................................')
    #os.remove(f'{title}.mp3')
    #os.remove(f'{title}.mp4')

    pass





if __name__ == '__main__':
    process()

    print('finish.....')
    pass