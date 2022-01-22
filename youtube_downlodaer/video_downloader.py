import os
import subprocess

from datetime import datetime

def change_working_dir(path):
    """ This will change working directory to download directory """
    path_name = os.path.dirname(path)
    os.chdir(path)
    
def video_download(path,link,res):
    """ This function will change the working directory to given location and download the file """
    
    change_working_dir(path)

    # This part will ask for the resolution of video to be downloaded and then download the file
    # if qulaity is valid
    if res == "720p":
        qual = "-f 22"
    elif res == "best":
        qual = "bestvideo+bestaudio -S ext:mp4:m4a"
    else:
        print("Only 720p and best are available at this time")
    
    subprocess.Popen(['yt-dlp',qual,str(link)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
    # This will change working directory to current directory
    os.chdir(os.path.dirname(__file__))
    

def audio_download(path,link):
    """This function will download the audio files to the given path  """

    change_working_dir(path)
    subprocess.Popen(['yt-dlp','bestaudio',str(link),'-S','ext:m4a'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    os.chdir(os.path.dirname(__file__))

def twitch_vod_download(path,link,file_name,start_time,end_time):
    """This function will download the given twitch vods from start time to end time 

        Usage:
            The function will take arguments in the following order
            path - path to directory where you want to download
            link - Link of the VOD
            file_name - name of the file you want to save
            start_time - starting time of download in the formant HH:MM:SS.MS
            end_time - ending time in format HH:MM:SS.MS
                example: 03:10:57.00
    """
    # change_working_dir(path)
    print(os.getcwd())

    ffmpeg_link = "yt-dlp" + " " + "-g" + " " + link
    get_link_data = subprocess.check_output(ffmpeg_link,shell=True).decode('utf-8')
    print(get_link_data)
    print("Got Link data")
    # date_time_format = '%H:%M:%S'
    # start_time = datetime.strptime('00:00:00', date_time_format).time()
    # end_time = datetime.strptime('00:01:00',date_time_format).time()

    st_time='00:00:00'
    ed_time = "00:10:00"
    # subprocess.Popen(['ffmpeg','-ss',st_time,'-i',str(get_link_data),'-t',ed_time,'-c','copy',file_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    subprocess.Popen(['ffmpeg','-ss',st_time,'-i','https://d1m7jfoe9zdc1j.cloudfront.net/b005ccdee9dd88236389_shroud_44968214749_1640901189/chunked/index-dvr.m3u8','-t',ed_time,'-c','copy','new1.mp4'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    # os.chdir(os.path.dirname(__file__))

# if __name__ == "__main__":
#     audio_download(path, link)