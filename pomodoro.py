from modules import bars, sounds, timeConversion

'''
    pomodoro : int = Number of pomodoro rounds.
    percentageOfIncrease : int = Percentage of increase the time of rest.
    rangeOfIncrease : int = Number of pomodoros to increase the rest time.
    inputSeconds : int = user input seconds.

    return : int = Relax time based on pomodoros.
'''

def setPomodoroSecondsOfRelax(pomodoro:int, percentageOfIncrease:int, rangeOfIncrease:int, inputSeconds:int):
    rangePassedTimes = pomodoro // rangeOfIncrease
    increasedTime = rangePassedTimes * ( percentageOfIncrease / 100 ) * inputSeconds
    return int(increasedTime + inputSeconds)
    

def run_pomodoro():

    pomodoro = 1

    minutesOfStudy = int(input('Input study time (minutes): '))
    secondsOfStudy = timeConversion.passMinutestoSeconds(minutesOfStudy)

    minutesOfRelax = int(input('Input relax time (minutes): '))
    secondsOfRelax = timeConversion.passMinutestoSeconds(minutesOfRelax)

    input('Press any key to start your training')

    while True:

        sounds.playSound('start.mp3')

        print('Starting', pomodoro, 'pomodoro of study')
        bars.LoadBar(secondsOfStudy, 'Studying...')

        sounds.playSound('stop.mp3')

        print('Starting', pomodoro, 'pomodoro of relax')
        bars.LoadBar(
            setPomodoroSecondsOfRelax(pomodoro, 50, 4, secondsOfRelax),
            'Relaxing...'
        )

        input('Press any key to continue to the next round')

        pomodoro += 1

run_pomodoro()