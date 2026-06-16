def score_collector(score):
    score_value = int(score)
    if score_value <= 50:
        print("Below passing, improve your grade")

    elif 50 < score_value <= 70:
        print("You have a passing grade")

    elif 70 < score_value <= 90:
        print("You have a passing grade")
    
    else:
        print("You are the best in your class")



score_collector(input("Enter your score: "))