#!/usr/bin/env python3

import sys

#Belting songs out at the top of your lungs is the best thing ever.
#Sadly, it's often frowned upon in public spaces.
#This script will belt 'em out for you, just super quietly. on a screen.
#Without making... any noise. At all.

#Is it the same? No. 

#Will it sate that primal urge within you to just go
#all Steven Tyler on the chorus of Dream On? Not even close.

#But, hey, let's face it: at this point you're desperate, and you
#completely and totally lack the courage to tell the others in the computer
#lab to shove it.

#Yours is a sad existence, and this script is a testament to that fact.
#Wow. Even I didn't expect this to end on such a low note.

#I would tell you to 'enjoy,' but we both already know you will, and that
#just might be the saddest thing about it all.

#Enjoy your life.

song = sys.argv[1]

with open(song , 'r') as song_file_object , open('loud_song.txt', 'w') as lsong:

	for line in song_file_object:
		line = line.rstrip()
		print(line.upper())
		lsong.write(f'{line.upper()}\n')	
