from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)



input_file = "i:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/5190414-2.mp4"
output_file = "./video.mp4"
start_time = 0  # Start time in seconds
end_time = 20  # End time in seconds

cut_video(input_file, output_file, start_time, end_time)