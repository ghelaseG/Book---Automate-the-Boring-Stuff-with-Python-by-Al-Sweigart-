# python3! = Expand the stopwatch project from this chapter so that it uses the
# rjust() and ljust() string methods to “prettify” the output

import pyperclip, time

print('Press ENTER to begin and stopwatch. If you want to quit press CTRL-C')
input()
print('Started!')
startTime = time.time() #first lap start time
lastTime = startTime
lapNum = 1

lapTimes = []

try: #start tracking the lap times.
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lap = 'Lap # %s: ' % lapNum
        ttime = str(totalTime).rjust(7)
        ttimeSep = ' ('
        ltime = str(lapTime).rjust(7)
        ltimeSep = ')'
        formatted = lap + ttime + ttimeSep + ltime + ltimeSep

        print(formatted, end='')
        lapNum += 1
        lastTime = time.time()
        lapTimes.append(formatted)

except KeyboardInterrupt:
    print('\nDone')

    pyperclip.copy('\n'.join(lapTimes))
