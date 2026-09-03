kbc_questions = [
    ["Which famous scientist developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking", 2],
    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 2],
    ["Which planet is known as the 'Red Planet'?", "Jupiter", "Mars", "Venus", "Saturn", 1],
    ["Who is the author of 'The God of Small Things'?", "Salman Rushdie", "Arundhati Roy", "Vikram Seth", "Chetan Bhagat", 1],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 3],
    ["Which of the following is not a programming language?", "Python", "HTML", "Java", "C++", 2],
    ["In which country would you find the Great Barrier Reef?", "Brazil", "Australia", "Mexico", "Thailand", 1],
    ["Who painted the 'Mona Lisa'?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 2],
    ["What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Pb", 0],
    ["What is the name of the largest moon of Saturn?", "Titan", "Europa", "Ganymede", "Triton", 0]
]

# for question in kbc_questions:
#     print(f"Questions:{question[0]}")
#     print(f"1.{question[1]}\n2.{question[2]}\n3.{question[3]}\n4.{question[4]}")
#     print(f"For answer press 1 for option 1, 2 for option 2, 3 for option 3,4 for option 4:")
#     a=int(input("Enter the answer:\n"))
#     if question[5] == a:
#         print(f"Correct Answer Congraluation!!!")
#     else:
#         print(f"Incorrect Answer the correct answer is {question[5]}")
#         break
    
for question in kbc_questions:
    print(f"Question:{question[0]}")
    print(f"Option 1:{question[1]}\nOption 2:{question[2]}\nOption 3:{question[3]}\nOption 4:{question[4]}")
    print(f"For answer press 1 for option 1, 2 for option 2, 3 for option 3,4 for option 4:")
    a=int(input("Enter the Answer:"))
    if question[5] == a:
        print("Correct Answer Congraluation!!!")
    else:
        print(f"This is not a correct Answer and the correct answer is {question[5]}")
        break
