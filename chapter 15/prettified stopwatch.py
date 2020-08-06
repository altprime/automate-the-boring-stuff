'''
prettified stopwatch

rjust() and ljust() functions to prettify the output


'''

import time
import pyperclip

# display instructions
print('Press ENTER to begin. Then press ENTER to "click" the stopwatch. hit Ctrl-c to quit.')

input()
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1

# start tracking lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        # print('Lap # %s:%s(%s)'%(lapNum,totalTime,lapTime))
        print('Lap #' + str(lapNum).rjust(3) + str(totalTime).rjust(8) + ' (' + str(lapTime).rjust(6) + ')')
        outPutTxt = 'Lap # ' + str(lapNum).rjust(3) + str(totalTime).rjust(8) + ' (' + str(lapTime).rjust(6) + ')'
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # handle Ctrl-c exception to keep error message from displaying.

