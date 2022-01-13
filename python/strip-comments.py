# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string, markers):
    output = []

    lines = string.split("\n")

    idx = 0
    while idx < len(lines):
        lines[idx] = lines[idx].strip()
        idx += 1

    print(lines)

    for line in lines:
        # check which marker is present
        marker = ""
        for i in markers:
            if i in line:
                marker = i
                break
            else:
                marker = ""
        

        if marker != "":
            output.append(line.split(marker)[0] + "\n")
        else:
            output.append(line + "\n")


    for i in range(len(output)):
        if " \n" in output[i]:
            output[i] = output[i].replace(" \n", "\n")
    
    remove_markers(output, markers)
    
    # remove \n from last item
    output[-1] = output[-1].strip()


    return ''.join(output)

def remove_markers(text, markers):
    for i in markers:
        for j in range(len(text)):
            if i in text[j]:
                text[j] = text[j].replace(i, "")
    
    return text


# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result = solution("apples, pears \ngrapes\nbananas \n", ["#", "!"])
result = solution("a #\nc\nd $e f g", ["#", "$"])

print(result)