import markovify

class CityNameText(markovify.NewlineText):

    def word_split(self, city):
        chunks, chunk_size = len(city), 2
        tokens =  [city[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        return tokens
                
    def word_join(self, words):
        return "".join(words) 