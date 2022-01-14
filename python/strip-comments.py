# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string, markers):
    output = []

    lines = string.split("\n")

    for i in range(len(lines)):
        marker_idx = -1
        for letter_idx in range(len(lines[i])):
            if lines[i][letter_idx] in markers:
                marker_idx = letter_idx
                break
            else:
                marker_idx = -1
        
        slice_point = slice(marker_idx)

        if marker_idx != -1:
            output.append(lines[i][slice_point] + "\n")
        else:
            output.append(lines[i] + "\n")

    for i in range(len(output)):
        if " \n" in output[i]:
            output[i] = output[i].replace(" \n", "\n")
    
    remove_extra_markers(output, markers)
    
    # remove \n from last item
    output[-1] = output[-1].strip()

    return ''.join(output)

def remove_extra_markers(text, markers):
    for i in markers:
        for j in range(len(text)):
            if i in text[j]:
                text[j] = text[j].replace(i, "")
    
    return text


# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result = solution("apples, pears \ngrapes\nbananas \n", ["#", "!"])
# result = solution("a #\nc\nd $e f g", ["#", "$"])

# result = solution("# avocados bananas bananas\nlemons strawberries apples apples\nstrawberries\noranges ! ? cherries bananas '\nbananas ' oranges bananas watermelons", ["'", "?"])

# print(result)

# print("Should equal to:\n" + r"# avocados bananas bananas\nlemons strawberries apples apples\nstrawberries\noranges !\nbananas")