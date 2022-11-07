def LoadBar(seconds: int, tag: str):
    import time
    from progress.bar import IncrementalBar

    with IncrementalBar(tag, max=seconds, suffix='%(percent).1f%% - %(eta)ds') as bar:
        for i in range(seconds):
            time.sleep(1)
            bar.next()
