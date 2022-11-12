from modules import pomodoro, time
from data.defaultConf import defaultConfObject as default


def run_pomodoro():

    print('pomodoro routine v1.0.1')

    mode = input(
        'Would you like to use a default routine? (yes / no) ').lower()

    if mode == 'no':

        minutesOfStudy = int(input('Input study time (minutes): '))
        secondsOfStudy = time.passMinutestoSeconds(minutesOfStudy)

        minutesOfRelax = int(input('Input relax time (minutes): '))
        secondsOfRelax = time.passMinutestoSeconds(minutesOfRelax)

        relaxIncrementPercentage = int(input(
            'What percentage of time do you want to increase as you progress through your routine? '))

        rangeOfIncreaseRelax = int(
            input('Every how many pomodoros would you like to extend the break? '))

        pomodoro.playPomodoro(
            pomodoro=1,
            secondsOfStudy=secondsOfStudy,
            secondsOfRelax=secondsOfRelax,
            relaxIncrementPercentage=relaxIncrementPercentage,
            rangeOfIncreaseRelax=rangeOfIncreaseRelax
        )

    elif mode == 'yes':
        pomodoro.playPomodoro(
            pomodoro=1,
            secondsOfStudy=time.passMinutestoSeconds(default['studyMinutes']),
            secondsOfRelax=time.passMinutestoSeconds(default['relaxMinutes']),
            relaxIncrementPercentage=default['relaxIncrementPercentage'],
            rangeOfIncreaseRelax=default['rangeOfIncreaseRelax']
        )

    input('Press any key to start your training')


run_pomodoro()
