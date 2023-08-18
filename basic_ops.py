def reverse(input):
    return input[::-1]

def palindromeString(input):
    return (reverse(input) == input)

def reverseNumber(number):
    r = d = 0
    while(number > 0):
        d = number % 10
        r = r * 10 + d
        number = number // 10
    return r

def calculate_sum(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    print(reverseNumber(105))