import random

# read list of random times and numbers (sourced from the internet)
RandomDateTimes = open("./RandomDateTimes.txt")
dateTimes = RandomDateTimes.readlines()

# numbers that call regularly
regularNumbers = (
    "07649524464",
    "07824920650",
    "07859651251",
    "07629986333",
    "07849203593"
)

# numbers that call occasionally
occasionalNumbers = (
    "07825989689",
    "07852078379",
    "07515242452",
    "07735573099"
)

oneoffs = {
    "[1]": "07825940402 -> 07825695442 1000GMT 20190213\n",
    "[2]": "07825940402 -> 07825695442 1200GMT 20190225\n",
    "[3]": "07825940402 -> 07825695442 0900GMT 20190320\n",
    "[4]": "07825940402 -> 07825695442 1400GMT 20190409\n",
    "[5]": "07825940402 -> 07825695442 1230GMT 20190528\n"
}

doWrite = True # used to prevent writing of unreasonable calls

# create time portion
def createTimePortion(timeFromFile):
    dateComponents = timeFromFile.split(":")
    hours = int(dateComponents[0])
    global doWrite

    # create a bias to prevent unusually early calls to occur frequently
    if hours < 6:
        if random.randint(0,10) != 0:
            doWrite = False

    # create a bias to prevent unusually late calls to occur frequently
    if hours >= 22:
        if random.randint(0,10) != 0:
            doWrite = False

    time = dateComponents[0] + dateComponents[1] + "GMT"
    return time

def createRandomNumber():
    number = "07"
    for x in range(9):
        number += str(random.randint(0,9))
    return number


# create an array of random unknown numbers
randomUnknownNumbers = list()
for x in range(20):
    randomUnknownNumbers.append(createRandomNumber())

# create randomised phonelog
output = ""
for line in dateTimes:

    # select a direction
    dirIndicator = "->" if random.randint(0,1) == 0 else "<-"

    lineNoRtrn = line.rstrip("\n\r")
    if lineNoRtrn in oneoffs:
        output += oneoffs[lineNoRtrn]
    else:
        # seperate time components [0] = YYYY-MM-DD date, [1] = HH:MM:SS time
        spaceSeperated = line.split()

        # select a number to use for this particular record
        number = ""
        if random.randint(0,120) == 0:
            number = randomUnknownNumbers[random.randint(0,19)]
            dirIndicator = "->" if random.randint(0,5) == 0 else "<-" # <<< people tend to recieve more calls from random numbers
        else:
            if random.randint(0,15) == 0:
                number = occasionalNumbers[random.randint(0, len(occasionalNumbers) - 1)]
            else:
                number = regularNumbers[random.randint(0, len(regularNumbers) - 1)]

        # format time
        time = createTimePortion(spaceSeperated[1])

        # format date
        spaceSeperated[0] = spaceSeperated[0].split("-")

        # merge all
        if doWrite:
            output += "07825940402 " + dirIndicator + " " + number + " " + time + " " + spaceSeperated[0][0] + spaceSeperated[0][1] + spaceSeperated[0][2] + "\n"

        doWrite = True

outfile = open("./PhoneLog.log", "w+")
outfile.write(output)
