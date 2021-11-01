# read phone log data
logData = open("./PhoneLog.log")
logs = logData.readlines()

# load subscribers data
subscribersFile = {}
def populateSubscribers():
    with open("RuthBennett.contacts") as file:
        for line in file:
           (key, val) = line.split(":")
           subscribersFile[key] = val[:-1]
populateSubscribers()

# declare months for readable phone log
months = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
)

# get longest name contained in array
def getLongestNameLength(nameList):
    longestLength = 0
    if len(nameList) > 0:
        longestLength = len(nameList[0])
        for name in nameList:
            if len(name) > longestLength:
                longestLength = len(name)
    return longestLength

# get contact name from telephone number
def getNameFromNumber(number):
    name = ""
    if number in subscribersFile:
        name = subscribersFile[number]
    else:
        name = "Unknown (" + number + ")"
    return name

# get list of all contact names
def getListOfContactNames():
    names = list()
    for line in logs:
        spaceSeperated = line.split()
        number = spaceSeperated[2]
        name = getNameFromNumber(number)
        if name not in names:
            names.append(name)
    return names

# store longest contact name length for ideal column size when formatting output
longestNameLength = getLongestNameLength(getListOfContactNames())

# get standard time for readable phone log
def convertToStandardTime(time):
    ampm = "AM"
    hours = int(time[:2])
    if hours >= 12:
        if hours > 12:
            hours -= 12
        ampm = "PM"
    hoursStr = " " + str(hours) if hours < 10 else str(hours)
    return hoursStr + ":" + time[2:4] + " " + ampm

# get explicit communications direction for readable phone log
def explicitCommsDirection(dirIndicator):
    if dirIndicator == "->":
        return "[OUTGOING]"
    else:
        return "[INCOMING]"

# get formatted date for readable phone log
def formatDate(date):
    day = date[-2:]
    month = months[int(date[-4:-2]) - 1]
    year = date[:4]
    return day + " " + month + " " + year

# print raw log
def printRawLog():
    print("\nRAW PHONE LOG")
    for line in logs:
        print(line[:-1])

# print readable log
def printReadableLog():
    print("\nREADABLE PHONE LOG")
    for line in logs:
        spaceSeperated = line.split()
        out = ["" for x in range(5)]
        out[0] = getNameFromNumber(spaceSeperated[0])
        out[1] = explicitCommsDirection(spaceSeperated[1])
        out[2] = getNameFromNumber(spaceSeperated[2])
        out[3] = convertToStandardTime(spaceSeperated[3])
        out[4] = formatDate(spaceSeperated[4])
        print(("%s %s %-" + str(longestNameLength) + "s  %s  %s") %(out[0], out[1], out[2], out[4], out[3]))

# call summary (outgoing and incoming toggled by argument)
def callSummary(direction):
    dirIndicator = "->" if direction == "outgoing" else "<-"
    summaryData = dict()
    for line in logs:
        spaceSeperated = line.split()
        if spaceSeperated[1] == dirIndicator:
            contact = spaceSeperated[2]
            date = spaceSeperated[4]
            if contact in summaryData.keys():
                summaryData[contact][0] += 1
                summaryData[contact][2] = date
            else:
                summaryData[contact] = [1, date, date]
    if (direction == "outgoing"):
        print("\nOUTGOING CALL SUMMARY (FROM: RUTH BENNETT)")
    else:
        print("\nINCOMING CALL SUMMARY (TO: RUTH BENNETT)")
    for key in summaryData:
        print(("%-" + str(longestNameLength) + "s  Number of Calls: %-3s  First Call: %s  Last Call: %s") %(getNameFromNumber(key), str(summaryData[key][0]), formatDate(summaryData[key][1]), formatDate(summaryData[key][2])))

# read input code from user
optionCode = ""
while optionCode != "quit" and optionCode != "0":
    optionCode = raw_input("\nENTER AN OPTION CODE\n0: Quit (or 'quit')\n1: Raw Phone Log\n2: Readable Phone Log\n3: Outgoing Call Summary\n4: Incoming Call Summary\n> ")
    if optionCode == "1":
        printRawLog()
    elif optionCode == "2":
        printReadableLog()
    elif optionCode == "3":
        callSummary("outgoing")
    elif optionCode == "4":
        callSummary("incoming")
    elif optionCode == "quit" or optionCode == "0":
        print("quitting...")
    else:
        print("ERROR: invalid option.")
