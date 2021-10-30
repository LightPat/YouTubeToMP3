from pytube import YouTube
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

def convertMP4ToMP3():
    # TODO
    pass


if __name__ == '__main__':
    # My desktop path
    save_path = r"C:\Users\patse\Desktop"

    # Japanese goblin https://www.youtube.com/watch?v=_bhxZD3Ravo
    # Felt https://www.youtube.com/watch?v=NLzWl57IdDI

    file_extension, file_name = downloadSource("https://www.youtube.com/watch?v=NLzWl57IdDI", save_path)
    file_path = os.path.join(save_path, file_name) + file_extension

    # TODO Convert video download into audio file