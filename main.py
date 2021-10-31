from pytube import YouTube
import PySimpleGUI as sg
import os
import ffmpeg

def downloadSource(link, outputPath):
    try:
        yt = YouTube(link)
        print("Title:", yt.title)
        print("Length:", yt.length, "seconds")
        audioStreamFilter = yt.streams

        bitrates = []

        for stream in audioStreamFilter:
            if stream.abr != None:
                bitrates.append(int(stream.abr[:-4]))

        print("\nBitrates:", bitrates)
        maxBitrate = max(bitrates)
        bitrateString = "{}kbps".format(maxBitrate)
        print("Highest bitrate stream:", bitrateString)

        bitrateStreamFilter = audioStreamFilter.filter(abr=bitrateString)

        for stream in bitrateStreamFilter:
            stream.download(output_path=outputPath)

        splitName = stream.default_filename.rsplit(".", 1)
        file_name = splitName[0]
        file_extension = "." + splitName[1]

        return file_extension, file_name

    except Exception as e:
        print(e)

def extractAudio(input_path, output_path, overwrite=True):
    stream = ffmpeg.input(input_path)
    audio = stream.audio
    stream = ffmpeg.output(audio, output_path)
    ffmpeg.run(stream, overwrite_output=overwrite)


if __name__ == '__main__':
    # GUI layout
    layout = [  [
        sg.Text("YouTube Video URL"),
        sg.In(size=(25,1), enable_events=True, key="-URL-")
    ],
    [
        sg.Text("Output Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],

    [sg.Button('Ok'), sg.Button('Cancel')]
]

    # Initialize window object
    window = sg.Window('Window Title', layout)

    # Take user input and wait for button press before executing download/conversion
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        if event == 'Ok':
            save_path = values['-FOLDER-']
            vidURL = values['-URL-']

            # TODO check link validity
            if os.path.isdir(save_path):
                # Downloads video from the internet
                file_extension, file_name = downloadSource(vidURL, save_path)
                # Path where the video is downloaded to
                file_path = os.path.join(save_path, file_name) + file_extension
                # Extract audio from video
                extractAudio(file_path, os.path.join(save_path, "output.mp3"), overwrite=True)
                # Remove downloaded video so that only audio is leftover
                os.remove(file_path)
                break
            else:
                # TODO Add error message to GUI
                print("Path isn't valid")
                continue

    # EXAMPLE VIDEOS/LINKS
    # Japanese goblin https://www.youtube.com/watch?v=_bhxZD3Ravo
    # Felt https://www.youtube.com/watch?v=NLzWl57IdDI