from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import imageio
import cv2
import random

class VideoProcessingError(Exception):
    """Base class for other exceptions in this module."""
    pass

class FPSNotFoundError(VideoProcessingError):
    """Raised when the FPS value is 0."""
    pass

class InvalidTimeFormatError(VideoProcessingError):
    """Raised when the time format is invalid."""
    pass

class InvalidTimeError(VideoProcessingError):
    """Raised when the time is greater than the video length."""
    pass

def create_subclip(input_file, output_file, start_time, end_time):
    """
    Cut a video clip from start_time to end_time
    :param input_file: path to the input video file
    :param output_file: path to the output video file
    :param start_time: start time in seconds
    :param end_time: end time in seconds
    :return: None
    """
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

def create_gif(video_path, gif_outputpath):
    """
    Create a gif from a video
    :param video_path: path to the video file
    :param gif_path: path to the gif file
    :return: None
    """
    video = imageio.get_reader(video_path)
    gif_writer = imageio.get_writer(gif_outputpath, mode='I')
    for frame in video:
        gif_writer.append_data(frame)
    gif_writer.close()

def calculate_frame(video_path, time):
    """
    Calculate the frame number from a given time

    Args
    :param video_path: path to the video file
    :param time: time in the format 'hh:mm:ss'
    :return: frame number, time in seconds
    """

    # Open the video file
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    if fps == 0:
        raise FPSNotFoundError("Error: FPS is 0. The video file might be corrupted or not supported.")
    
    # Get the time in seconds
    try:
        hours, minutes, seconds = map(float, time.split(':'))
    except ValueError:
        raise InvalidTimeFormatError(f"Error: Invalid time format {time}. Expected format is 'hh:mm:ss'.")
    time_int = int(hours*3600 + minutes*60 + seconds)
    
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_length = total_frames / fps
    frame_number = time_int * fps
    if frame_number > total_frames:
        raise InvalidTimeError(f"Error: The time {time_int} is greater than the video length {video_length}.")
    
    video.release()
    return frame_number, time_int

def obtain_frame(video_path, time, output_path):
    """
    Obtain a frame from a video at a given time

    Args
    :param video_path: path to the video file
    :param time: time in the format 'hh:mm:ss'
    :param output_path: path to save the frame
    :return: None
    """
    # Open the video file
    video = cv2.VideoCapture(video_path)
    frame_number, _ = calculate_frame(video_path, time)
    # Set the frame position to the desired frame number
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    # Read the frame
    ret, frame = video.read()
    # Check if the frame was read successfully
    if ret:
        # Save the frame as an image
        cv2.imwrite(output_path, frame)
        print(f"Frame  {frame_number} saved successfully in {output_path}.")
    else:
        print("Failed to obtain frame.")
    video.release()

def get_random_frame(video_path, _):
    """
    Obtain a random frame from a video

    Args
    :param video_path: path to the video file
    :param _: unused parameter
    :return
    """

    # Open the video file
    video = cv2.VideoCapture(video_path)
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # Set the frame position to a random frame number
    video.set(cv2.CAP_PROP_POS_FRAMES, random.randint(0, total_frames-1))
    # Read the frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if ret:
        # Save the frame as an image
       cv2.imencode('.jpg', frame)
    else:
        print("Failed to obtain frame.")
        
    video.release()
    return frame

