import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def check_grammar(sentence):
    doc = nlp(sentence)

    print("\nOriginal Sentence:")
    print(sentence)

    errors = []

    for i, token in enumerate(doc):
        word = token.text.lower()

        # He / She / It + have → has
        if word in ["he", "she", "it"]:
            if i + 1 < len(doc) and doc[i + 1].text.lower() == "have":
                errors.append(("have", "has"))

        # He / She / It + go → goes
        if word in ["he", "she", "it"]:
            if i + 1 < len(doc) and doc[i + 1].text.lower() == "go":
                errors.append(("go", "goes"))

        # They / We / You + is → are
        if word in ["they", "we", "you"]:
            if i + 1 < len(doc) and doc[i + 1].text.lower() == "is":
                errors.append(("is", "are"))

        # He / She / It + are → is
        if word in ["he", "she", "it"]:
            if i + 1 < len(doc) and doc[i + 1].text.lower() == "are":
                errors.append(("are", "is"))

    print("\nGrammar Check:")

    if not errors:
        print("✅ No common grammar errors detected.")
        return

    corrected_sentence = sentence

    for incorrect, correct in errors:
        print("\n❌ Grammar Error Detected")
        print("Incorrect:", incorrect)
        print("Suggested:", correct)

        corrected_sentence = corrected_sentence.replace(
            incorrect, correct, 1
        )

    print("\nCorrected Sentence:")
    print(corrected_sentence)


# Get sentence from user
sentence = input("\nEnter an English sentence: ")

check_grammar(sentence)