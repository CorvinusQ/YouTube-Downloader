from pytube import YouTube

def download_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(output_path=output_path)
        print("Видео успешно загружено!")
    except Exception as e:
        print("Произошла ошибка при загрузке видео:", str(e))

if __name__ == "__main__":
    video_url = input("Введите URL видео на YouTube: ")
    download_video(video_url)
