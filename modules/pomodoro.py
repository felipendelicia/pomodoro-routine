def pomodoroRound(
    pomodoro:int, 
    secondsOfStudy:int, 
    secondsOfRelax:int, 
    relaxIncrementPercentage:int,
    rangeOfIncreaseRelax:int
    ):
    from modules import sounds, bars, time

    sounds.playSound('start.mp3')

    print('Starting', pomodoro, 'pomodoro of study')
    bars.LoadBar(secondsOfStudy, 'Studying...')

    sounds.playSound('stop.mp3')

    print('Starting', pomodoro, 'pomodoro of relax')
    bars.LoadBar(
        time.setPomodoroSecondsOfRelax(
            pomodoro, 
            relaxIncrementPercentage, 
            rangeOfIncreaseRelax, 
            secondsOfRelax),
        'Relaxing...'
    )

    sounds.playSound('achievement.mp3')

    input('Press any key to continue to the next round')

    print()

def playPomodoro(
    pomodoro:int, 
    secondsOfStudy:int, 
    secondsOfRelax:int, 
    relaxIncrementPercentage:int,
    rangeOfIncreaseRelax:int
    ):
    while True:
        pomodoroRound(
            pomodoro=pomodoro, 
            secondsOfStudy=secondsOfStudy, 
            secondsOfRelax=secondsOfRelax, 
            relaxIncrementPercentage=relaxIncrementPercentage,
            rangeOfIncreaseRelax=rangeOfIncreaseRelax
            )

        pomodoro+=1