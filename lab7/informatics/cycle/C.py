print(' '.join(map(str,(lambda a, b:  [i for i in range(a,b+1) if i**0.5 == int(i **0.5)])(int(input()), int(input())))))