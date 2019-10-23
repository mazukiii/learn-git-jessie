class Solution(object):
    def reverse(self, x):
        inputed_number = input()
        reversed_number = ''
        if inputed_number[0:1] == '-':
            reversed_number += '-'
            inputed_number = inputed_number[1:]

        for i in range(len(inputed_number)):
            reversed_number += inputed_number[len(inputed_number)-i-1:len(inputed_number)-i]
        reversed_number = int(reversed_number)
        print(reversed_number)


        
        return None
