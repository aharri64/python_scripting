# Read only

def read_only():
    '''a method that only reads the fill'''
    try:
        file1 = open('data.txt')
        text = file1.read()
        print(text)
        file1.close()  # the reason for closing
    except FileNotFoundError:
        text = None
        print(text)


def write_only():
    '''A method that writes to a file'''
    # if file exists it will be overwritten
    # if file doesn't exist it will be created
    file2 = open('more_data.txt', 'w')
    file2.write('tomatoes')
    file2.close()


if __name__ == '__main__':
    # read_only()
    write_only()
