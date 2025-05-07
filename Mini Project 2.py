#Mini Project 2
print("Employee Performance Evaluation Expert System\n")
print("Rate the following (1 to 5):")
punctuality = int(input("1. Punctuality: "))
task_completion = int(input("2. Task Completion: "))
teamwork = int(input("3. Teamwork: "))
communication = int(input("4. Communication Skills: "))
initiative = int(input("5. Initiative: "))
total = punctuality + task_completion + teamwork + communication + initiative
avg = total / 5
print("\nEvaluation Result")
if avg >= 4.5:
    print("Performance: Excellent ")
    print("Recommendation: Eligible for promotion or bonus.")
elif avg >= 3.5:
    print("Performance: Good ")
    print("Recommendation: Keep up the good work.")
elif avg >= 2.5:
    print("Performance: Average ")
    print("Recommendation: Provide training or mentorship.")
else:
    print("Performance: Needs Improvement ")
    print("Recommendation: Schedule a performance review meeting.")
