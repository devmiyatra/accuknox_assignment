import requests
import matplotlib.pyplot as plt

# Mock API
url = "https://fakerapi.it/api/v1/persons?_quantity=5"
response = requests.get(url)
students = response.json()["data"]

names = []
average_scores = []

for student in students:
    scores = [70, 75, 80]  # assumed test scores
    avg = sum(scores) / len(scores)

    names.append(student["firstname"])
    average_scores.append(avg)

# Plot bar chart
plt.bar(names, average_scores)
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Average Student Scores")
plt.show()
