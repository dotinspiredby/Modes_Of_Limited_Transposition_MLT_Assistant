# Modes_Of_Limited_Transposition_MLT_Assistant

Hello! This is .inspiredby and here I would like to represent my very first small program on Python3. 

This is Modes Of Limited Transposition (MLT) Assistant, which helps to identify the notes from input in particular modes of limited transposition (O. Messiaen system) and their transposition examples. About Messiaen and his MLT system you can read here in the Chapter XVI: https://monoskop.org/images/5/50/Messiaen_Olivier_The_Technique_of_My_Musical_Language.pdf

The tool will help with the harmony analysis for musical material (mostly from the 20th century) in terms of mode identification and makes the process of music theory learning easier and faster. 

The code uses numbers from 0(note 'c') to 11(note 'h'). After entering your note request, the program does the following: picks the generator from "library" and constructs the mode consequence (from 0 - note c), then makes possible transpositions until it starts repeating the original - finally the program gathers all the the scales of the mode together and validates the set of requested notes by the user with the mode so-called database and prints the result. Then it steps forward to the next generator in "library" and the cycle repeats.

The printed verdict is possible to print in notes - for this function I used 'music21' library. 

I wrote several variants for my program - simple one with console (it's necessary to input the notes in integers) and one with the window (by using Tkinter), where it becomes easier to input by pressing the keys on the virtual piano keyboard.

Just because I started learning Python two months ago I admit that the code requires improvements, however it is my first project, which moreover for its initial purpose works great, so I would be happy if you let me know, what would be refactored. 

Meanwhile, if someone finds my tool helpful for music theory purposes I would be happy;) so that is why I posted it here...
