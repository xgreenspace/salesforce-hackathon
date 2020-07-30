from candidates import *


class Analyze():
    def __init__(self, candidate=-1):
        if candidate == -1:
            raise TypeError('Nothing was passed.')

        key_words = self.get_key_words()

        for word in key_words:
            if word in candidate.summary:
                candidate.merit_points += 1

        if candidate.merit_points >= 30:
            candidate.is_good_hire = True
        else:
            pass
        

    def get_key_words(self):
        key_words = []
        i = 0
        with open('resume-words.text', 'r') as file:
            while True:
                if not file.readline():
                    break
                i += 1
                key_words.append(file.readline())


        
        for i in range(len(key_words)):
            key_words[i] = key_words[i][:key_words[i].find('\n')]

        key_words.pop(-1)
        
        return(key_words)

