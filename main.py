import youtube_dl
##Youtube_dli pip vasitesi ile endiririk.
video_url = input("Mahninin linki:")

video_bilgisi = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)

faylAdi= f"{video_bilgisi['title']}.mp3"

##Settings/Ayarlar
ayarlar ={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':faylAdi,
}

with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])

print(f"endirme tamamlandi...{faylAdi}")