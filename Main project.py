import subprocess

run = True
while run:

    menu = input('What would you like to do: \n 1) Convert to different resolution \n 2) Change format \n 3) Change the file type \n Q) Exit the programme \n')

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
        ipaddr = input('Enter the ip destination e.g (192.168.2.1): ')
        port = input('Enter port to stream to e.g (5004): ')

        subprocess.run(['ffmpeg', '-i', filen, '-f', 
                        'rtp', '-vcodec', 'libx264', '-acodec', 
                        'aac', '-bufsize', '2000k', '-g', '50', f'rtp://{ipaddr}:{port}'
                        ])


        # to stream on reciving end ffplay rtp://<ip_address>:<Port>