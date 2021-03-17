# Read only

def read_only():
    '''a method that only reads the fill'''
    file1 = open('data.txt')
    text = file1.read()
    print(text)
    file1.close()  # the reason for closing


if __name__ == '__main__':
    read_only()
