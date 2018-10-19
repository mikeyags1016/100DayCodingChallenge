import time


def stage(section):
    stages = {
        1: 'Seed',
        2: 'Sapling',
        3: 'Child',
        4: 'Young adult',
        5: 'Grown evergreen',
        6: 'Grandfather tree'
    }
    if section > 6:
        raise AssertionError('Invalid Input')
    return stages[section]


def timer(max_time, sections):
    start = time.time()
    time.clock()
    seconds = 0
    section = 0

    while seconds < max_time:
        seconds = time.time() - start
        section += 1
        print("Stage of tree: %s, seconds count: %02d" % (stage(section), seconds))
        time.sleep(sections)


def tree_counter(max_time):
    section_times = max_time // 5
    timer(max_time, section_times)
    print("Congratulations, you have completed your time")


tree_counter(60)