import time
from progress.bar import IncrementalBar

def passMinutesToSeconds(minutes:int):
    return minutes*60

def playSound(file:str):
    import playsound
    from pathlib import Path
    playsound.playsound(str(Path.cwd()) + '/sound/' + file)

def LoadBar(minutes:int, task:str):

    seconds = passMinutesToSeconds(minutes)

    with IncrementalBar(task, max=seconds, suffix='%(percent).1f%% - %(eta)ds') as bar:
        for i in range(seconds):
            time.sleep(1)
            bar.next()

studyRound = 1

minutesOfStudy = int(input('Input study time (minutes): '))

minutesOfRelax = int(input('Input relax time (minutes): '))

input('Press any key to start your training')

while True:

    print('Starting', studyRound, 'round of study')
    LoadBar(minutesOfStudy, 'Studying...')
    playSound('achievement.mp3')

    print('Starting', studyRound, 'round of relax')
    LoadBar(minutesOfRelax, 'Relaxing...')
    playSound('achievement.mp3')

    input('Press any key to continue to the next round')

    studyRound+=1
    