import imageio

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

if __name__ == "__main__":
    video_path = 'I:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/p117-1.mp4'
    gif_outputpath = './Gif/EMU/output4.gif'

    create_gif(video_path, gif_outputpath)