# https://www.codewars.com/kata/551f23362ff852e2ab000037

def longest_slide_down(pyramid):

    if len(pyramid) == 1:
        return pyramid[0][0]
    elif len(pyramid) == 2:
        if pyramid[1][0] > pyramid[1][1]:
            return pyramid[1][0] + pyramid[0][0]
        else:
            return pyramid[1][1] + pyramid[0][0]
    
    for i in range(len(pyramid)):
        bottom_pairs = get_bottom_pairs(pyramid)
        row_above = pyramid[len(pyramid) - 2]

        bottom_row_sums = find_larger_sums(bottom_pairs, row_above)
        new_pyramid = form_new_pyramid(pyramid, bottom_row_sums)

        if len(new_pyramid) == 2:
            if new_pyramid[1][0] > new_pyramid[1][1]:
                return new_pyramid[1][0] + new_pyramid[0][0]
            else:
                return new_pyramid[1][1] + new_pyramid[0][0]

def get_bottom_pairs(pyramid):
    idx = len(pyramid) - 1

    bottom_pairs = []
    for i in range(len(pyramid[idx]) - 1):
        pair = [pyramid[idx][i], pyramid[idx][i + 1]]
        bottom_pairs.append(pair)

    return bottom_pairs


def find_larger_sums(bottomPairs, rowAbove):
    sums = []

    for i in range(len(bottomPairs)):
        if bottomPairs[i][0] > bottomPairs[i][1]:
            bottomPairs[i] = bottomPairs[i].pop(0)
        else:
            bottomPairs[i] = bottomPairs[i].pop(1)

    sums = []
    for i in range(len(bottomPairs)):
        sums.append(bottomPairs[i] + rowAbove[i])

    return sums

def form_new_pyramid(oldPyramid, newBottomRow):
    # remove last two rows
    # add newBottomRow
    
    oldPyramid.pop()
    oldPyramid.pop()
    oldPyramid.append(newBottomRow)
    new_pyramid = oldPyramid

    return new_pyramid



ans = longest_slide_down([[3],
                    [7, 4],
                    [2, 4, 6],
                    [8, 5, 9, 3]
])

print(ans)