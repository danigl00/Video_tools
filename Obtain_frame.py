import cv2

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
        print(f"Frame number {frame_number} from time {time} (second {second_number}) saved successfully.")
    else:
        print("Failed to obtain frame.")
    # Release the video file
    video.release()

def calculate_frame(video_path, time):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    # Get the time in seconds
    hours, minutes, seconds = map(float, time.split(':'))
    time_int = hours*3600 + minutes*60 + seconds
    # Get the frame rate of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    # Calculate the frame number based on the time
    frame_number = int(time_int * fps)
    # Release the video file
    video.release()
    return frame_number, time_int


calculate_frame(
    video_path='c:/Users/p0121182/Project/Skeleton_Tracking/EMU_videos/p299-1_01.mp4',
    time = '0:03:41',
    output_path = './image1.jpg')