from pytube import YouTube

link = input("Введите ссылку на видео: ")
video = YouTube(link)
quality = input("Выберите качество видео (high/low)")

if quality == "high":
    output = video.streams.get_highest_resolution()
if quality == "low":
    output = video.streams.get_lowest_resolution()

output.download()