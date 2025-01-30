Video Processing and Streaming Tool

This Python script provides a command-line interface for performing various video processing tasks and streaming video over UDP. It uses ffmpeg and ffplay for video manipulation and streaming.
Features

    Convert Video Resolution: Resize a video to a specified resolution.

    Change Video Format: Convert a video to a different format (e.g., grayscale).

    Change File Type: Convert a video file to another file type (e.g., .mp4 to .mp3).

    Stream Video via UDP: Stream a video file over UDP with optional resolution scaling and encryption.

    Stream Webcam via UDP: Stream live video from a webcam to another device over UDP.

    Receive UDP Stream: Receive and play an encrypted UDP video stream.

Prerequisites

Before using this tool, ensure you have the following installed:

    Python 3.x: The script is written in Python 3.

    FFmpeg: Required for video processing and streaming. Download and install it from https://ffmpeg.org/.

    FFplay: Comes bundled with FFmpeg and is used for video playback.

Installation

    Clone this repository or download the script:
    bash
    Copy

    git clone https://github.com/your-username/video-processing-tool.git
    cd video-processing-tool

    Install the required Python packages (if any):
    bash
    Copy

    pip install -r requirements.txt

    Ensure ffmpeg and ffplay are installed and added to your system's PATH.

Usage

Run the script using Python:
bash
Copy

python video_tool.py

Menu Options

    Convert to Different Resolution:

        Input the file name, desired resolution (e.g., 1920:1080), and output file name.

        The script will resize the video and preview it.

    Change Format:

        Input the file name, desired format (e.g., gray for grayscale), and output file name.

        The script will convert the video format and preview it.

    Change File Type:

        Input the file name and the desired output file type (e.g., output.mp3).

        The script will convert the file and preview it.

    Stream Video via UDP:

        Input the file name, target IP address, port, and encryption key.

        The script will check the video resolution, scale it to 720p if necessary, and stream it over UDP.

    Stream from Webcam via UDP:

        Input the webcam device name, target IP address, and port.

        The script will stream live video from the webcam over UDP.

    Receive a Stream:

        Input the UDP IP address, port, and encryption key.

        The script will receive and play the encrypted UDP stream.

    Exit the Program:

        Type Q to exit the program.

Examples
Convert Video Resolution
plaintext
Copy

What would you like to do:
 1) Convert to different resolution
 2) Change format
 3) Change the file type
 4) Stream video via UDP
 5) Stream from webcam to another device via UDP
 6) Receive a stream
 Q) Exit the programme
1
What file would you like to edit: input.mp4
What would you like to change the resolution to (e.g 1920:1080): 1280:720
What would you like to call your file: output.mp4

Stream Video via UDP
plaintext
Copy

What would you like to do:
 1) Convert to different resolution
 2) Change format
 3) Change the file type
 4) Stream video via UDP
 5) Stream from webcam to another device via UDP
 6) Receive a stream
 Q) Exit the programme
4
What file would you like to stream: input.mp4
Enter the UDP IP address (e.g., 127.0.0.1): 127.0.0.1
Enter the UDP port (e.g., 1234): 1234
Enter the encryption key (a long string for encryption): mysecretkey

Stream Webcam via UDP
plaintext
Copy

What would you like to do:
 1) Convert to different resolution
 2) Change format
 3) Change the file type
 4) Stream video via UDP
 5) Stream from webcam to another device via UDP
 6) Receive a stream
 Q) Exit the programme
5
Enter the webcam device name (e.g., video="Your Webcam Name"): Integrated Camera
Enter the UDP IP address (e.g., 127.0.0.1): 127.0.0.1
Enter the UDP port (e.g., 1234): 1234
