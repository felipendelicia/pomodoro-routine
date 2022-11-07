from modules import bars, sounds, timeConversion

def run_pomodoro():

    studyRound = 1

    minutesOfStudy = int(input('Input study time (minutes): '))
    secondsOfStudy = timeConversion.passMinutestoSeconds(minutesOfStudy)

    minutesOfRelax = int(input('Input relax time (minutes): '))
    secondsOfRelax = timeConversion.passMinutestoSeconds(minutesOfRelax)

    input('Press any key to start your training')

    while True:
        sounds.playSound('start.mp3')

        print('Starting', studyRound, 'round of study')
        bars.LoadBar(secondsOfStudy, 'Studying...')

        sounds.playSound('stop.mp3')

        print('Starting', studyRound, 'round of relax')
        bars.LoadBar(secondsOfRelax, 'Relaxing...')

        input('Press any key to continue to the next round')

        studyRound += 1

run_pomodoro()