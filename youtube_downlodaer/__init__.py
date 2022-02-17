from .video_downloader import audio_download,video_download,twitch_vod_download,change_working_dir

# if __name__ == "__main__":
#     format = input("Which file do you want to download video/audio/twitch_vod?:")
#     if format == "video":
#         link = input("Enter Download link: ")
#         res = input("Enter the resolution(at present only 720p and best are availabe): ")
#         path = input("Enter the path:")
#         video_download(path, link, res)
#     elif format == "audio":
#         link = input("Enter Download link: ")
#         path = input("Enter the path:")
#         audio_download(path, link)
#     elif format == "twitch_vod":
#         link = input("Enter Download link: ")
#         res = input("Enter the resolution(at present only 720p and best are availabe): ")
#         path = input("Enter the path:")
#         file_name = input("Enter output file name: ")
#         start_time = input("Enter time in format HH:MM:SS.MS: ")
#         end_time = input("Enter time in format HH:MM:SS.MS: ")
#         twitch_vod_download(path, link, file_name, start_time, end_time)