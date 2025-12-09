while True:
    mountains = []
    for i in range(8):
        mountainH = int(input())
        mountains.append(mountainH)

    max_height = max(mountains)
    target_index = mountains.index(max_height)

    print(target_index)
