# commands
def hw():
    print('hello world')

def msg(param=str):
    print(param)

def wait():
    # when storing a command we need to wait
    # till we can read the value so this function
    # is really important
    pass

def command_not_found():
    print('Command not found! Are you sure you wrote the right command?\n')

# command map
# to add another command, just write the function and put into the dict
command_map = {
    'HEY': hw,
    'MSG': msg,
    '': wait
}

