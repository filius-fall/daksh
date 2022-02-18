import subprocess
def remote(link,res):
    if res.lower() == '720p':
        res = '-f 22'
    elif res.lower() == "best":
        res = "-f 'bestvideo+bestaudio'"
    else:
        res = ""
    download_link = "yt-dlp" + " " + res + " " + link
    process = subprocess.Popen(['ansible','Indra','-m','shell','-a',download_link],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)


link = "https://www.youtube.com/watch?v=C70GJYVoZ4Y"
res = '720p'
remote(link,res)
