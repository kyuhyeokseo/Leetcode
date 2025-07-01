class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        dictionary = sorted(dictionary, key=lambda x:len(x))
        sentence_list = list(sentence.split(' '))

        for i, item in enumerate(sentence_list):
            for key in dictionary:
                if key == item[:len(key)]:
                    sentence_list[i] = key
                    break
        
        return ' '.join(sentence_list)