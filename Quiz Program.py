
quiz={
    "question 1":{ "question":"What is capital of India?",
        "answer":"Lucknow"
    },
    "question 2":{
        "question":"What is capital of Germany?",
        "answer":"Berlin"
    },
    "question 3":{
        "question":"What is capital of Italy?",
        "answer":"Rome"
    },
    "question 4":{
        "question":"What is capital of Spain?",
        "answer":"Madrid"
    },
    "question 5":{
        "question":"What is capital of Portugese?",
        "answer":"Lisbon"
    },
    "question 6":{
        "question":"What is capital of Switzerland?",
        "answer":"Bern"
    }
}

score=0
for key,value in quiz.items():
    print(value['question'])
    answer=input("answer")

    if answer.lower()==value['answer'].lower():
        print('correct')
        score=score+1
        print("your score is:"+str(score))

    else:
        print("wrong")
        print("the answer is:"+value['answer'])
        print("your score is:"+str(score))
        print("")
        print("")

    print("You got"+str(score)+"out of 7 questions")
    print("your percentage is"+str(int(score/7*100))+"%")

   
