 #ffmpeg -f image2 -framerate 12 -i img%02d.png  foo.mp4
 ffmpeg -f image2 -framerate 0.5 -i img%02d.png -vcodec libx264 -vf scale=640:-2,format=yuv420p foo.mp4