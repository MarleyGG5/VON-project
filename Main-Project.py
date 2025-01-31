import subprocess  # Import the subprocess module to run external commands like ffmpeg

run = True  # Initialize a flag to control the main loop
while run:
    # Presenting the user with a menu of options
    menu = input('What would you like to do: \n 1) Convert to different resolution \n 2) Change format \n 3) Change the file type \n 4) Stream video via UDP \n 5) Stream from webcam to another device via UDP \n 6) Receive a stream \nQ) Exit the programme \n')

    if menu == 'Q':  # Check if the user wants to quit
        confirm = input('Are you sure you would like to quit the programme [Y/N] ')
        if confirm == 'Y':  # Confirm if user wants to quit
            run = False  # Set the flag to False, exiting the loop
        else:
            continue  # If not confirmed, continue the loop

    if menu == '1':  # Option 1: Change resolution of a video file
        filen = input('What file would you like to edit: ')  # Get the file name
        res = input('What would you like to change the resolution to (e.g 1920:1080): ')  # Get new resolution
        filenew = input('What would you like to call your file: ')  # Get the new file name
        
        # Use ffmpeg to scale (resize) the video to the desired resolution and save it to a new file
        subprocess.run(['ffmpeg', '-i', filen, '-vf', f'scale={res}', filenew])
        
        # Use ffplay to preview the newly scaled video
        subprocess.run(['ffplay', filenew])

    if menu == '2':  # Option 2: Change the format of the video
        filen = input('What file would you like to edit: ')  # Get the file name
        form = input('How would you like to format it (e.g gray): ')  # Get the new format
        filenew = input('What would you like to call your file: ')  # Get the new file name
        
        # Use ffmpeg to convert the video to the specified format
        subprocess.run(['ffmpeg', '-i', filen, '-vf', f'format={form}', filenew])
        
        # Use ffplay to preview the newly formatted video
        subprocess.run(['ffplay', filenew])

    if menu == '3':  # Option 3: Change the file type/extension of the video
        filen = input('What file would you like to edit: ')  # Get the file name
        newtype = input(f'What would you like to change {filen} to e.g (your-file-name.mp3): ')  # Get the new file type
        
        # Use ffmpeg to change the file type/extension
        subprocess.run(['ffmpeg', '-i', f'{filen}', newtype])
        
        # Use ffplay to preview the newly converted file
        subprocess.run(['ffplay', newtype])
    

    if menu == '4':  # Option 4: Stream a video file via UDP (Improved packet loss handling)
        filen = input('What file would you like to stream: ')  # Get the file name to stream

        # Get the current resolution of the video using ffprobe
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=s=x:p=0', filen],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        resolution = result.stdout.decode('utf-8').strip()  # Extract resolution in 'widthxheight' format (e.g., 1920x1080)
        print(f"Current resolution: {resolution}")

        # Check if the resolution is not 720p (1280x720)
        if resolution != '1280x720':
            print("The video resolution will be changed to 720p before streaming.")
            res = '1280:720'  # Set the resolution to 720p
        else:
            print("The video is already 720p, no scaling required.")
            res = resolution  # Keep the original resolution

        udp_ip = input('Enter the UDP IP address (e.g., 127.0.0.1): ')  # Get the target IP address for streaming
        udp_port = input('Enter the UDP port (e.g., 1234): ')  # Get the target port for streaming
        encryption_key = input('Enter the encryption key (a long string for encryption): ')  # Get the encryption key

        # Use ffmpeg to stream the video over UDP with improved parameters
        subprocess.run([
            'ffmpeg',
            '-i', filen,                             # Input file
            '-vf', f'scale={res}',                   # Scale to 720p (or original resolution if already 720p)
            '-c:v', 'libx264',                       # Video codec: libx264
            '-c:a', 'aac',                           # Audio codec: aac
            '-f', 'mpegts',                          # Output format: MPEG-TS
            '-max_delay', '0',                       # Minimize delay in streaming
            '-b:v', '2000k',                         # Set video bitrate
            '-b:a', '128k',                          # Set audio bitrate
            '-g', '50',                              # Keyframe interval for video
            '-r', '30',                              # Frame rate
            '-pkt_size', '1316',                     # Set packet size to reduce packet loss
            '-flush_packets', '1',                   # Flush packets immediately
            '-buffer_size', '1024000',               # Increase buffer size to prevent packet loss
            '-metadata', f'key={encryption_key}',    # Add the encryption key as metadata
            f'udp://{udp_ip}:{udp_port}'             # UDP destination URL
        ])


    if menu == '5':  # Option 5: Stream video from a webcam to another device via UDP
        webcam_device = input('Enter the webcam device name (e.g., video="Your Webcam Name"): ')  # Get the webcam device name (Windows example)
        udp_ip = input('Enter the UDP IP address (e.g., 127.0.0.1): ')  # Get the target IP address for streaming
        udp_port = input('Enter the UDP port (e.g., 1234): ')  # Get the target port for streaming
        
        # Use ffmpeg to stream the webcam feed to a target IP and port over UDP
        subprocess.run([
            'ffmpeg',
            '-f', 'dshow',                            # Use DirectShow for webcam input (Windows-specific)
            '-i', f'video={webcam_device}',            # Specify the webcam device
            '-c:v', 'libx264',                        # Video codec: libx264
            '-c:a', 'aac',                            # Audio codec: aac
            '-f', 'mpegts',                           # Output format: MPEG-TS
            '-max_delay', '0',                        # Minimize delay
            '-b:v', '2000k',                          # Set video bitrate
            '-g', '50',                               # Keyframe interval for video
            '-r', '30',                               # Frame rate
            '-pkt_size', '1316',                      # Set packet size to reduce packet loss
            '-flush_packets', '1',                    # Flush packets immediately
            f'udp://{udp_ip}:{udp_port}'              # UDP destination URL
        ])
    
    
    if menu == '6':  # Option 6: Receive Encrypted UDP Stream and Decrypt Locally
        udp_ip = input('Enter the UDP IP address (e.g., 127.0.0.1): ')  # Get the target IP address for streaming
        udp_port = input('Enter the UDP port (e.g., 1234): ')  # Get the target port for streaming
        encryption_key = input('Enter the encryption key (the same key used for encryption): ')  # Get the encryption key

        # Use ffplay to play the encrypted UDP stream
        subprocess.run([
            'ffplay', f'udp://{udp_ip}:{udp_port}?key={encryption_key}'])
