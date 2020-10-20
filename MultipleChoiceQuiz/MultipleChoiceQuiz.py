from Question import Question


question_prompts = [
        "What colours are Apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
        "What colours are Bannanas?\n(a)Teal\n (b)Magenta\n(c)Yellow\n\n",
        "What colours are Strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"
]  # cos do czego moge sie odwolac - pytania i odpowiedzi

poprawne_odpowiedzi = [
         Question(question_prompts[0], "a"),  
         Question(question_prompts[1], "c"),
         Question(question_prompts[2], "b"),
] # wczytuje poprawne pytania i odpowiedzi do klasy

def run_test(questions):
        score = 0
        for question in questions:
                answer = input(question.prompt) # odwoluje sie do elementow klasy
                if answer == question.answer:
                        score += 1
        print("You got", score,"/", len(poprawne_odpowiedzi), "correct") # przy len nie musze zamieniac na stringa

run_test(poprawne_odpowiedzi)

