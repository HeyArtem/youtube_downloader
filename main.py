'''
работаю с youtube downloader yt-dlp

$ yt-dlp --help
$ yt-dlp https://youtu.be/bnWSucrILVk   -скачать по ссылке "https://youtu.be/bnWSucrILVk" в формате mp4
$ yt-dlp --list-formats https://youtu.be/N7NOcxG0Ekg    -вывести все форматы, доступные к скачиванию
$ yt-dlp -f 'bv*+ba' https://music.youtube.com/watch?v=pmoYP_QvGsM&feature=share -o '%(id)s.%(ext)s'     -видео max кач-во и аудио maxка-во ОТДЕЛЬНО
$ yt-dlp -f '137' https://music.youtube.com/watch?v=pmoYP_QvGsM&feature=share[1] 9598       -скачать 137 id
$ yt-dlp -f '137+140' https://music.youtube.com/watch?v=pmoYP_QvGsM&feature=share[1] 10180      -скачать по id аудио и видео и объединить  
$ yt-dlp -f 'bv*[ext=mp4]+ba*[ext=m4a]' https://music.youtube.com/watch?v=pmoYP_QvGsM&feature=share     -скачать bestVideo mp4 & bestAudio m4a (webm+m4a=mkv)
$ yt-dlp -f 'bv*[ext=mp4]+ba*[ext=m4a]' https://youtu.be/dZ9ycm3BNW8 -o 'my_title'      -скачать bestVideo mp4 & bestAudio m4a + СВОЙ TITLE
$ yt-dlp id https://www.youtube.com/c/ChrisLuno     -выкачать весь канал

$ yt-dlp --proxy '45.23.123.123.123:4488'       -можно качать через proxy

'''
