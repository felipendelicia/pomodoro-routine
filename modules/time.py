passMinutestoSeconds = lambda minutes: minutes * 60

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