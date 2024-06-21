
#guess game
secret_number=18
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess= int(input('please enter your guess number : '))
    guess_count += 1
    if guess== secret_number:
        print('you won!!')
        break
    else:
        if guess_count !=3:
            print('Try again')
else:
      print('sorry you failed')