while True:
    score = input("Enter score: ")
    if score.isdigit():
        score = int(score)
        break
    else: print("Enter valid score.\n")

print("Excellent" if score >= 90 else "Very Good" if score >= 80 else "Good" if score >= 70 else "Needs Improvement")

