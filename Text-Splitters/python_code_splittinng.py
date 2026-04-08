from langchain_text_splitters import RecursiveCharacterTextSplitter ,Language
text = """
# Student marks splitter program

data = input("Enter student name and marks separated by comma: ")

# Example input: Rahul,78,85,90

parts = data.split(",")

name = parts[0]
mark1 = int(parts[1])
mark2 = int(parts[2])
mark3 = int(parts[3])

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent Report")
print("Name:", name)
print("Marks 1:", mark1)
print("Marks 2:", mark2)
print("Marks 3:", mark3)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300 ,
    chunk_overlap = 0
)

chunk = splitter.split_text(text)
print(chunk)