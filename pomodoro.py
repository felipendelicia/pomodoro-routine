from modules import bars, sounds, time
    

def run_pomodoro():

    pomodoro = 1

    minutesOfStudy = int(input('Input study time (minutes): '))
    secondsOfStudy = time.passMinutestoSeconds(minutesOfStudy)

    minutesOfRelax = int(input('Input relax time (minutes): '))
    secondsOfRelax = time.passMinutestoSeconds(minutesOfRelax)

    input('Press any key to start your training')

    while True:

        sounds.playSound('start.mp3')

        print('Starting', pomodoro, 'pomodoro of study')
        bars.LoadBar(secondsOfStudy, 'Studying...')

        sounds.playSound('stop.mp3')

        print('Starting', pomodoro, 'pomodoro of relax')
        bars.LoadBar(
            time.setPomodoroSecondsOfRelax(pomodoro, 50, 4, secondsOfRelax),
            'Relaxing...'
        )

        sounds.playSound('achievement.mp3')

        input('Press any key to continue to the next round')

        print()

        pomodoro += 1

run_pomodoro()