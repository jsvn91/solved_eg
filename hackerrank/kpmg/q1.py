# stemmer

def calculate(xtext):

    words = xtext.split()

    remove_words = ['ly', 'ing', 'ed']

    for n,word in enumerate(words):

        for i in remove_words:

            prospect = word[:-len(i)]

            if len(prospect) >= len(words):

                words[n] = prospect

                continue

        # words[n] = prospect

    return " ".join(words)

if __name__ == '__main__':

    text = "an dog is quickly jumping"

    print("the calculate word is :", calculate(text))