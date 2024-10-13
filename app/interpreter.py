from command_divider import returnCommands
from document_reader import archiveReader
import commands

path = 'test/files/commands.txt'
new = archiveReader(path=path)

cmds = returnCommands(new)

store_cmd = ''

for cmd in cmds:

    if store_cmd:
        # executes the command with the parameter
        # format: (<cmd>, <alternative>)(<param>)
        commands.command_map.get(store_cmd, commands.command_not_found)(cmd)
    else:
        # store the cmd into the storage to use with its parameter
        store_cmd = cmd

print('All executed.')