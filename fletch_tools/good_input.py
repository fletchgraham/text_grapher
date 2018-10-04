"""Tools for making life easier when getting user input."""

from os import path as p

def get_input(prompt="Type something", expected_type="String"):
    """Get authenticated, well formated input with error handling."""
    prompt += '\n>>> '
    answer = ''

    try:
        while True:
            # Get some input to work with.
            answer = str(input(prompt))

            # Handle different expected types.
            if expected_type.lower() in ['enter', 'return']:
                break

            elif answer == '':
                print("You didn't type anything.")

            elif expected_type.lower() in ['str', 'string']:
                break

            elif expected_type.lower() in ['int', 'integer']:
                try:
                    answer = int(answer)
                    break
                except:
                    print("that wasn't an Integer.")

            elif expected_type.lower() in ['val', 'value', 'float']:
                try:
                    answer = float(answer)
                    break
                except:
                    print("that wasn't a Float.")

            elif expected_type.lower() in ['bool', 'boolean', 'tf', 'yn']:
                answer = str(answer)
                if answer.lower() in ['y', 'yes', 'true', 't', '1']:
                    answer = True
                    break

                elif answer.lower() in ['n', 'no', 'false', 'f', '0']:
                    answer = False
                    break

                else:
                    print("Couldn't use that as a boolean.")

            elif expected_type.lower() in ['path', 'file', 'dir', 'directory']:
                if p.exists(answer.replace('"', '')):
                    break
                else:
                    print("That isn't an existing path.")

            else:
                print("Try Again.")

        return answer

    except KeyboardInterrupt:
        # Print a new line (for mac terminal) then exit.
        print()
        exit()

if __name__ == "__main__":
    print(get_input('Type a folderpath or filepath', 'path'))
