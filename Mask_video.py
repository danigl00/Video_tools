import cv2
import numpy as np

import Masking_fun as mks
import Obtain_frame as ObFr

COORDINATES = []
start_point = None
end_point = None


def Mask_video(video_path, output_path):
    random_frame = ObFr.get_random_frame(video_path, output_path)

    start_point, end_point = mks.obtain_roi(random_frame)
    output_frames = []

    capture = cv2.VideoCapture(video_path)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while True:
        ret, original_image = capture.read()
        if not ret:
            break
        masked_image = mks.mask_roi(original_image, start_point, end_point)

        output_frames.append(masked_image)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame_p in output_frames:
        out.write(frame_p)
    print(f"Output video saved at {output_path}")
    capture.release()
    out.release()

    return output_frames

Mask_video("i:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/p134-78.mp4",#'./video.mp4', 
           'c:/Users/p0121182/Project/Skeleton_Tracking/EMU_videos/masked_video.mp4')