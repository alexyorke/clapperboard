import sys
import subprocess

inputFile = sys.argv[1]

# prepare command
output = subprocess.Popen(["ffprobe -v quiet -show_format -show_streams '" +
                           inputFile + "' | grep -F 'start_time' | sort -u" +
                           " | cut -d '=' -f 2"],
                          stdout=subprocess.PIPE, shell=True).communicate()[0]

# get each line seperately
audioChannels = output.split("\n")

# last line is always empty
audioChannels.pop()

# will only work for two or three audio channels
print "Recognized audio channel starting positions: " + str(audioChannels)
if len(audioChannels) == 2:
    offset = str(float(audioChannels[0]) - float(audioChannels[1])) + "s"
    print "Offset: " + offset
elif len(audioChannels) == 3:
    avgTwoAndThree = (float(audioChannels[1]) + float(audioChannels[2]))/2.0
    offset = str(float(audioChannels[0]) - avgTwoAndThree) + "s"
    print "Offset: " + offset
else:
    print "Audio offset could not be determined."
