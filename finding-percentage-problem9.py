if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Get the list of scores for the queried student
    marks_for_query_student = student_marks[query_name]

    # Calculate the sum of the marks
    total_marks = sum(marks_for_query_student)

    # Calculate the average
    # The problem statement says "length of marks arrays = 3", so we can divide by 3.0
    # Or more generally, divide by the number of elements in the list.
    average_score = total_marks / len(marks_for_query_student)

    # Print the average formatted to 2 decimal places
    print(f"{average_score:.2f}")
