def playSound(file:str):
    import playsound
    from pathlib import Path
    playsound.playsound(str(Path.cwd()) + '/sound/' + file)
