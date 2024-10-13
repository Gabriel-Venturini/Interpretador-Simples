def archiveReader(path=str):
    try:
        with open(path, 'r') as archive:
            return list(archive)
    except FileNotFoundError:
        return 'File not found!\nTry checking the path you wrote.'
    except Exception as e:
        return f'Unexpected error: {e}'
    
if __name__ == '__main__':
    s = archiveReader('test/files/helloworld.txt')
    print(s)