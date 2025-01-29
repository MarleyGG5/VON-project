import subprocess

run = True
while run:

    menu = input('What would you like to do: \n 1) Convert to different resolution \n 2) Change format \n 3) Change the file type \n 4) Stream video \n Q) Exit the programme \n')

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
        ipaddr = input('Enter the destination IP address (e.g., 192.168.2.1): ')
        port = input('Enter the port to stream to (e.g., 5000): ')
        
        # Stream over UDP
        subprocess.run([
            'ffmpeg',
            '-i', filen,                        # Input file
            '-c:v', 'libx264',                  # Video codec
            '-c:a', 'aac',                      # Audio codec
            '-f', 'mpegts',                     # MPEG Transport Stream format
            f'udp://{ipaddr}:{port}'            # Output stream destination
        ])
        
        print(f"Streaming to udp://{ipaddr}:{port}")