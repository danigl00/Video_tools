# To convert to mp4, type in terminal:
## change the path and the output
ffmpeg -i '.\filename.m2t' -vcodec copy -c:a aac -f mp4 filename.mp4 