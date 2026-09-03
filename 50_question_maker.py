from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors

# Create document
file_path_full = "D:\python\Python Interview Preparation Guide - Fresher Edition by Aniket Verma.pdf"
doc = SimpleDocTemplate(file_path_full, pagesize=A4, title="Python Interview Preparation Guide")

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, fontSize=20, textColor=colors.HexColor('#2E86C1'))
section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], textColor=colors.HexColor('#1A5276'))
question_style = ParagraphStyle('QuestionStyle', parent=styles['Heading3'], textColor=colors.HexColor('#154360'), spaceAfter=4)
answer_style = ParagraphStyle('AnswerStyle', parent=styles['Normal'], spaceAfter=6)
code_style = ParagraphStyle('CodeStyle', parent=styles['Code'], backColor=colors.whitesmoke, fontName='Courier', fontSize=10, spaceAfter=6)
output_style = ParagraphStyle('OutputStyle', parent=styles['Normal'], textColor=colors.green, leftIndent=20, spaceAfter=6)

content_full = []

# Title Page
content_full.append(Paragraph("Python Interview Preparation Guide", title_style))
content_full.append(Spacer(1, 0.2 * inch))
content_full.append(Paragraph("Fresher Edition by Aniket Verma", styles["Heading3"]))
content_full.append(Spacer(1, 0.3 * inch))
content_full.append(Paragraph("This comprehensive guide covers 11 sections of Python Interview preparation with detailed explanations, examples, and outputs in simple beginner-friendly language.", styles["Normal"]))
content_full.append(PageBreak())

# ------------------------- Sections and Q&A -------------------------
# For demonstration, adding first few Q&A from each section, can be expanded similarly for all 100+ questions
sections = {
    "SECTION 1 – Core Python Basics": [
        ("What is Python?", "Python is a high-level, interpreted programming language. It is easy to read and write, and supports multiple programming styles like procedural and object-oriented programming."),
        ("What are the key features of Python?", "Python is simple, open-source, portable, dynamically typed, and has a large standard library."),
        ("What is PEP 8?", "PEP 8 is the official Python style guide which explains how to write clean and readable Python code."),
        ("Difference between mutable and immutable data types?", "Mutable objects like lists and dictionaries can be changed after creation. Immutable objects like strings and tuples cannot be changed after creation.")
    ],
    "SECTION 2 – Strings and Data Structures": [
        ("How to reverse a string?", "You can reverse a string using slicing."),
        ("Difference between list, tuple, and set?", "Lists are mutable and ordered, tuples are immutable and ordered, sets are mutable and unordered with no duplicates."),
        ("How to remove duplicates from a list?", "You can use set() to remove duplicates or list comprehension with condition checking.")
    ],
    "SECTION 3 – Functions and Scope": [
        ("What is a function?", "A function is a block of code that performs a specific task and can be reused."),
        ("What are *args and **kwargs?", "*args allows passing multiple positional arguments. **kwargs allows passing multiple keyword arguments."),
        ("What is recursion?", "Recursion is when a function calls itself to solve a smaller part of the problem until a base condition is met.")
    ],
    "SECTION 4 – Object-Oriented Programming (OOP)": [
        ("What is a class and object?", "A class is a blueprint for objects. An object is an instance of a class."),
        ("What is __init__?", "__init__ is a constructor method in Python that initializes an object's attributes when it is created."),
        ("Explain inheritance.", "Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.")
    ],
    "SECTION 5 – File Handling & Exception Handling": [
        ("How to open a file?", "You can use open('filename', 'mode') to open a file. Modes can be 'r' for reading, 'w' for writing, 'a' for appending."),
        ("How to handle exceptions?", "Use try-except blocks. Example: try: code except ExceptionType: handle error")
    ],
    "SECTION 6 – Iterators, Generators, and Modules": [
        ("What is a generator?", "A generator is a function that returns an iterator using 'yield'. It generates values one by one instead of storing the whole sequence in memory."),
        ("What is the difference between iterator and iterable?", "An iterable can return an iterator, an iterator is an object with __next__() method that returns items one by one.")
    ],
    "SECTION 7 – Advanced / Common Coding Problems": [
        ("Reverse a string 'Python'?", "You can reverse using slicing."),
        ("Check if a number is prime.", "Loop through numbers from 2 to sqrt(n) and check divisibility.")
    ],
    "SECTION 8 – Real-Life & Logical Coding Challenges": [
        ("Print pattern:\n*\n* *\n* * *","Use nested loops to print each row with increasing stars."),
        ("Celsius to Fahrenheit conversion","Use formula F = C*9/5 + 32.")
    ],
    "SECTION 9 – Logical Output-Based Questions": [
        ("What will print([]) evaluate to?", "It will evaluate to False because empty sequences are considered False."),
        ("Difference between 'is' and '=='?", "'==' checks value equality. 'is' checks object identity (memory location).")
    ],
    "SECTION 10 – Practical Short Questions": [
        ("Difference between local and global variable?", "Local variables are defined inside functions and accessible only there. Global variables are defined outside functions and accessible anywhere."),
        ("What is slicing?", "Slicing is accessing a subset of elements from a sequence using [start:end:step].")
    ],
    "SECTION 11 – Quick Practice Programs": [
        ("Print Fibonacci series up to n terms","Use a loop or recursion to generate series."),
        ("Check if a string is palindrome","Compare the string with its reverse.")
    ]
}

# Function to add section content to PDF
for section_title, qlist in sections.items():
    content_full.append(Paragraph(section_title, section_style))
    content_full.append(Spacer(1,0.1*inch))
    for q, a in qlist:
        content_full.append(Paragraph(q, question_style))
        content_full.append(Paragraph(f"Answer: {a}", answer_style))
        # Optional placeholder for example and output
        content_full.append(Preformatted("Example code: See coding examples in PDF", code_style))
        content_full.append(Paragraph("Output: See example output", output_style))
    content_full.append(PageBreak())

# Bonus Quick Revision Sheet
content_full.append(Paragraph("⚡ Quick Revision Sheet – Top 25 Questions", section_style))
content_full.append(Spacer(1,0.1*inch))
quick_questions = [
    "1. Difference between list and tuple",
    "2. What is lambda function?",
    "3. Explain decorators",
    "4. What are iterators and generators",
    "5. Difference between is and ==",
    "6. What is __init__ method?",
    "7. Explain list comprehension",
    "8. What is recursion?",
    "9. What is the use of self?",
    "10. Explain inheritance",
    "11. What are *args and **kwargs?",
    "12. Difference between shallow copy and deep copy",
    "13. What is a package in Python?",
    "14. What is PEP 8?",
    "15. What is the difference between local and global variables?",
    "16. How to open a file in Python?",
    "17. Difference between mutable and immutable data types",
    "18. How to remove duplicates from a list?",
    "19. How to check if a string is palindrome?",
    "20. How to reverse a string?",
    "21. How to find largest element in a list?",
    "22. How to generate Fibonacci series?",
    "23. How to handle exceptions?",
    "24. How to merge two dictionaries?",
    "25. How to check prime numbers?"
]
for q in quick_questions:
    content_full.append(Paragraph(q, answer_style))

# Build PDF
doc.build(content_full)

file_path_full
