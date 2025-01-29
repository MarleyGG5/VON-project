import subprocess

run = True
while run:
    menu = input('What would you like to do: \n 1) Convert to different resolution \n 2) Change format \n 3) Change the file type \n 4) Stream video via UDP \n Q) Exit the programme \n')

    if menu == 'Q':
        confirm = input('Are you sure you would like to quit the programme [Y/N] ')
        if confirm == 'Y':
            run = False
        else:
            continue

    if menu == '1':
        filen = input('What file would you like to edit: ')
        res = input('What would you like to change the resolution to (e.g 1920:1080): ')
        filenew = input('What would you like to call your file: ')
        
        subprocess.run(['ffmpeg', '-i', filen, '-vf', f'scale={res}', filenew])
        subprocess.run(['ffplay', filenew])
    
    if menu == '2':
        filen = input('What file would you like to edit: ')
        form = input('How would you like to format it (e.g gray): ')
        filenew = input('What would you like to call your file: ')
        
        subprocess.run(['ffmpeg', '-i', filen, '-vf', f'format={form}', filenew])
        subprocess.run(['ffplay', filenew])

    if menu == '3':
        filen = input('What file would you like to edit: ')
        newtype = input(f'What would you like to change {filen} to e.g (your-file-name.mp3): ')

        subprocess.run(['ffmpeg', '-i', f'{filen}', newtype])
        subprocess.run(['ffplay', newtype])
    
    if menu == '4':
        filen = input('What file would you like to stream: ')
        udp_ip = input('Enter the UDP IP address (e.g., 127.0.0.1): ')
        udp_port = input('Enter the UDP port (e.g., 1234): ')
        
        # Streaming over UDP with optimized settings
        subprocess.run([
            'ffmpeg',
            '-i', filen,                             # Input file
            '-c:v', 'libx264',                       # Video codec (H.264)
            '-c:a', 'aac',                           # Audio codec (AAC)
            '-f', 'mpegts',                          # Use MPEG-TS container format
            '-max_delay', '0',                       # Minimize delay
            '-b:v', '2000k',                         # Video bitrate (adjust based on bandwidth)
            '-b:a', '128k',                          # Audio bitrate
            '-g', '50',                              # Keyframe interval (for smoother streaming)
            '-r', '30',                              # Frame rate
            '-pkt_size', '1316',                     # Packet size to help reduce packet loss
            '-flush_packets', '1',                   # Flush packets for better real-time streaming
            '-f', 'mpegts',                          # Specify output format
            f'udp://{udp_ip}:{udp_port}'             # Output UDP stream destination
        ])
        
        print(f"Streaming to UDP://{udp_ip}:{udp_port}")

