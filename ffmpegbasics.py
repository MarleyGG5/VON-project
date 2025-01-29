import subprocess

subprocess.run(['ffmpeg', '-i', 'sample1.mp4', '-vf', 'scale=640:480', 'output.mp4']) # changes the resolution

subprocess.run(['ffmpeg', '-i', 'output.mp4', '-vf', 'format = gray', 'output.mp4']) # changes the colours to gray

subprocess.run(['ffplay', 'output2.mp4']) # replays the video

