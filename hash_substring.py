# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    mode = input()
    if "I" in mode:
        pattern = input()
        text = input()
        #get_occurrences(pattern, text)
    elif "F" in mode:
        filename = input()
        with open ("./tests/" + filename, mode="r") as file:
            pattern = file.readline()
            text = file.readline()
           # get_occurrences(pattern, text)
        
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    B = 13
    Q = 256
    output = []
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    for i in range(pattern_length):
        pattern_hash = (B * pattern_hash +ord(pattern[i])) % Q
        text_hash = (B * text_hash +ord(text[i])) % Q
    k = text_length-pattern_length
    for i in range(k+1):
        if text_hash==pattern_hash:
            output.append(i)
        if i < k:
            h = pow(B,pattern_length-1) % Q
            text_hash= (B * (text_hash-ord(text[i])*h)+ord(text[i+pattern_length]))% Q


    # and return an iterable variable
    return output 


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

