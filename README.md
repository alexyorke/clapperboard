# clapperboard

Automatically fix audio sync for your videos. Should work on any linux system, as long as `ffmpeg` is version `N-78176-gb340bd8` or newer, the `ffmpeg` extensions are installed, and `ffprobe` is installed. This will only work with raw video footage (i.e directly from the camera/source, no post-processing whatsoever.)


## Usage

`clapperboard.sh (--dry-run) /path/to/video /path/to/fixed/video` (`--dry-run` will only show you the audio offset, and not correct it)

## This is magic! How does it work?

Well, here's the secret. A lot of cameras, apps, and audio recording devices will embed the audio offset (in a really weird format) inside of the video. Even VLC doesn't seem to read the audio offset. `clapperboard` uses `ffprobe` to extract this offset, parse it correctly, and then corrects it. This is why it doesn't work with non-raw footage: the converting software ignores the offset and encodes the video, discarding it.
