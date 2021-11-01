The contents of this folder are comprised as described below:

WEX Coding Exercise
|-Answers/
  |-CodingExercise_ANSWERS.txt
  |-PhoneLog.log
  |-PhoneLogReader_FIXED_Python2.py
  |-PhoneLogReader_FIXED_Python3.py
  |-RuthBennett.contacts
|-PhoneLog_Python2/
  |-PhoneLog.log
  |-PhoneLogReader_BROKEN.py
  |-RuthBennett.contacts
|-PhoneLog_Python3/
  |-PhoneLog.log
  |-PhoneLogReader_BROKEN.py
  |-RuthBennett.contacts
|-PhoneLogDev/
  |-PhoneLogDev.py
  |-RandomDateTimes.txt
  |-PhoneLog.log

=== PhoneLog ===
The PhoneLog_Python[1/2] directories contain the files pertaining to the exercise that will be provided to the students on the day. Python2 is now considered legacy, but a compatible version shall sit alongside a Python3-based exercise (for interest, the only change is a single line of code on line 131 - Python3 uses an alternate function to garner raw user input).

The phone log reader tool is comprised of three main files:

• PhoneLog.log - contains the raw call data for Ruth Bennett
• RuthBennett.contacts - a dictionary of phone numbers and their respective name designations
• PhoneLogReader_BROKEN.py - a command-line tool that eases assimilation of Ruth Bennett's communication data, but it's broken and needs fixing during the exercise

Central to this collection of files is PhoneLogReader.py. This is a Python script that amalgamates the data contained in the PhoneLog.log and RuthBennett.contacts files and relays the information in a more readable format and generates overview statistics in a CLI. If Python is installed, the program can be run via the command line using: python PhoneLogReader.py OR python3 PhoneLogReader.py (depending on which version is being used).

Upon fixing and running the phone log reader, the user is presented with a CLI containing five options:

0: Quit (or 'quit') - Used to exit the phone log reader CLI
1: Raw Phone Log - Prints the raw disgusting phone log that is read from the PhoneLog.log file
2: Readable Phone Log - Prints a more readable version of the phone log after combining with contact information
3: Outgoing Call Summary - Prints a summary of activity relating to each of the outbound call recipients
4: Incoming Call Summary - Prints a summary of activity relating to each of the inbound callers

=== Answers ===
The answers directory contains fixed Python2 and Python3 versions of the phone log reader. A text file detailing the individual steps required to get the phone log reader fully operation is also provided for reference.

=== Phone Log Dev ===
The PhoneLogDev directory contains a script that uses a list of random dates and times in order to generate the raw phone log that is used in the exercise. The script is stochastic in nature, but it introduces biases to emphasise that Ruth calls some people more than others. Numbers contained in square brackets in the RandomDateTimes file are used to insert specific events into the phone log at certain points. These events are hard-coded and are as below:

[1]: 07825940402 -> 07825695442 1000GMT 20190213
[2]: 07825940402 -> 07825695442 1200GMT 20190225
[3]: 07825940402 -> 07825695442 0900GMT 20190320
[4]: 07825940402 -> 07825695442 1400GMT 20190409
[5]: 07825940402 -> 07825695442 1230GMT 20190528
