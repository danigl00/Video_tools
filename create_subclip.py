from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_file, output_file, start_time, end_time):
    """
    Cut a video clip from start_time to end_time
    :param input_file: path to the input video file
    :param output_file: path to the output video file
    :param start_time: start time in seconds
    :param end_time: end time in seconds
    :return: None
    """
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)


if __name__ == "__main__":
    input_file = "i:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/5190414-2.mp4"
    output_file = "./video.mp4"
    start_time = 0  # Start time in seconds
    end_time = 20  # End time in seconds

    cut_video(input_file, output_file, start_time, end_time)