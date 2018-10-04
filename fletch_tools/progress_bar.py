"""A simple cli progress bar"""

import sys

def print_progress(iteration, total):
    """Print a progress bar showing a given level of completion."""
    iteration += 1
    prefix = 'Progress'
    suffix = 'Complete'
    length = 50
    fill = u"\u2588"
    fill_alt = '#'

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    bar_alt = fill_alt * filledLength + '-' * (length - filledLength)

    try:
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    except:
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar_alt, percent, suffix))
    sys.stdout.flush()

    # Print New Line on Complete
    if iteration == total:
        print()
