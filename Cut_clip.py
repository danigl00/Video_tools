from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

# Example usage
input_file = "C:/Users/p0121182/Project/Skeleton_Tracking/EMU_videos/p229-1_01.mp4"
output_file = "C:/Users/p0121182/Project/Skeleton_Tracking/EMU_videos/Cut_p229-1_01.mp4"
start_time = 100  # Start time in seconds
end_time = 101  # End time in seconds

cut_video(input_file, output_file, start_time, end_time)