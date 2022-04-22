import textwrap

def wrap(string, max_width):
    li = {}
    li = textwrap.wrap(string, width = max_width)   #this will create a list containing where the string divided by width
    s = '\n'.join(li)   #this will make a new line for each division
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
