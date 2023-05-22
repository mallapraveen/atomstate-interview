from transformers import pipeline


def qa(question: str, context: str) -> str:
    question_answerer = pipeline(
        "question-answering", model="distilbert-base-cased-distilled-squad"
    )

    result = question_answerer(question=question, context=context)

    return result["answer"]


if __name__ == "__main__":
    context = r"""
    In a stunning crossover event, Spider-Man swung through the bustling streets of New York City, only to find himself facing a formidable foe. Just as he was about to be overwhelmed, a streak of blue and red blurred past him, and there stood the legendary Superman. The two heroes joined forces, their powers complementing each other perfectly. Together, they fought side by side, vanquishing the villain with unwavering determination. As the battle concluded, Spider-Man extended his hand to Superman, a newfound respect between Marvel and DC forming. Their encounter served as a testament to the unbreakable bond heroes share, transcending universes and inspiring hope for all.
    """
    question = "What city is Spiderman located in?"

    print(qa(question, context))
