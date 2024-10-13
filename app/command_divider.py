def returnCommands(document=list):
    # return the commands in a list format one by one

    # empty list to store the new values
    commandList = []

    # iterate over each item in the list
    for cmd in document:
        # remove the \n and divide the strings into words
        commandList.extend(cmd.strip().split())

    return commandList # list format like ['MSG', 'ADD', 'NEW']

if __name__ == '__main__':
    s = returnCommands(['MSG\n', 'HEY'])
    print(s)