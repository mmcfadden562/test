# Activity 1


def get_test():
    a_file = open("g:\\harper\cis 106 programming\ch 14\scores.txt", "r")

    lists = []
    lines = a_file.readlines()[1:]
    for line in lines:
        stripped_line = line.strip()
        line_list = stripped_line.split(",")
        lists.append(line_list)

    a_file.close()

    return lists


def get_min(score):
    minimum = score[0]
    for i in range(0, len(score), 1):
        if minimum > score[i]:
            minimum = score[i]
    return minimum


def get_max(score):
    maximum = score[0]
    for i in range(0, len(score), 1):
        if maximum < score[i]:
            maximum = score[i]
    return maximum


def get_avg(score):
    total = sum(score)
    average = total / (len(score))
    return average


def show_results(minimum, maximum, average, lists):
    print(lists, end='\n\n')
    print("low ", minimum)
    print("high ", maximum)
    print("average {:0.2f} ".format(average))


def get_scores(lists):
    score = []

    for i in range(len(lists)):
        test = int(lists[i][1])
        print(lists[i][1])

        score.append(test)
        print(score)

    return score


def main():
    lists = get_test()
    score = get_scores(lists)
    minimum = get_min(score)
    maximum = get_max(score)
    average = get_avg(score)
    print()
    show_results(minimum, maximum, average, lists)


main()
