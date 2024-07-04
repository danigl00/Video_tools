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

def obtain_frame(video_path, time, output_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    frame_number, second_number = calculate_frame(video_path, time)
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
    # Release the video file
    video.release()

def calculate_frame(video_path, time):
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
    
    # Release the video file
    video.release()
    return frame_number, time_int

def get_random_frame(video_path, output_path):
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
        image = cv2.imencode('.jpg', frame)
    else:
        print("Failed to obtain frame.")
    # Release the video file
    video.release()
    return frame


#### ----------------------------------------------------------------------------------- ###
if __name__ == "__main__":
    get_random_frame('./video.mp4', './image1.jpg')

    try:
        obtain_frame(
            video_path='./video.mp4',
            time = '0:0:2', #Expected format is 'hh:mm:ss'."
            output_path= './image1.jpg')
    except VideoProcessingError as e:
        print(e)
