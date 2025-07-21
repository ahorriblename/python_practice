def convert_guess_to_int(guess):
    guess = set(map(int, guess))
    return guess

# get n, range of number
num = int(input())
possible_answers = set(range(1, num + 1))
guess = set()

while True:
    # keep track of guessed numbers
    # get response
    response = input().split()

    if response[0] == "HELP":
        break
    else:
        # convert guess into set of numbers
        guess = convert_guess_to_int(response)

    response = input()
    # if response is yes, at least one number in the set is correct, keep track of these
    # guesses
    if response == "YES":
        possible_answers &= guess
    elif response == "NO":
        possible_answers -= guess

possible_answers = list(possible_answers)
possible_answers.sort()
for num in possible_answers:
    print(num, end = " ")