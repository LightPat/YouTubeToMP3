# YouTubeToMP3
## IMPORTANT ISSUE WITH PYTUBE
See this stack overflow page to fix an issue with the pytube regex cipher used to filter streams: https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w

I made this change when my program stopped working randomly.

## The Goal
I'm building a user interface that allows you to supply it a youtube link and it will download the video in the highest audio quality possible (around 124 kpbs).

It then needs to extract the audio from the video (all downloads off youtube are in mp4 or webm, which are video formats)

The application will also give the user the ability to trim it, as well astrim off any silence at the end of a recording.

The last component of the project is that the program will amplify the audio if it has room (the recording must not clip due to high volume, otherwise it would sound bad).

Considering turning this into a whole video conversion suite that is much simpler than current encoding softwares out there like handbrake. It would be geared more towards users who just want to convert videos/audio on their machine without worrying about a million settings.