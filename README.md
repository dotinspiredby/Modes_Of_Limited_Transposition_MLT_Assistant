# Modes_Of_Limited_Transposition_MLT_Assistant

Hello! This is .inspiredby and here I would like to represent my very first small program on Python3. 

This is Modes Of Limited Transposition (MLT) Assistant, which helps to identify the notes from input in particular modes of limited transposition (O. Messiaen system) and their transposition examples. About O. Messiaen's MLT system you can read here in the Chapter XVI: https://monoskop.org/images/5/50/Messiaen_Olivier_The_Technique_of_My_Musical_Language.pdf

The tool will help with the harmony analysis for musical material (mostly from the 20th century) in terms of mode identification and will make the process of music theory learning easier and faster. 

How to use? There are three files to run (choose one for your personal taste) - "MLT Keyboard" (with virtual piano keys), "MLT Console" and the "light" version without notation option with piano keys.

The code uses numbers from 0(note 'c') to 11(note 'h'). After entering your note request, the program does the following: picks the generator from "library" and constructs the mode consequence (from 0 - note c), then makes possible transpositions until it starts repeating the original - finally the program gathers all the scales of the mode together and validates the set of requested notes by the user with the mode so-called database and prints the result. Then it steps forward to the next generator in "library" and the cycle repeats.

The printed verdict is possible to print in notes - for this function I used 'music21' library. For piano keyboard I used Tkinter library.

Just because I started learning Python two months ago I admit that the code requires improvements, however it is my first project, which moreover for its initial purpose works great, so I would be happy if you let me know, what would be refactored. 

Meanwhile, if someone finds my tool helpful for music theory purposes I would be happy;) so that is why I posted it here...
