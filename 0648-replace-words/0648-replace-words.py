class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.trie = {}
        for pre in dictionary:
            t = self.trie
            for c in pre:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['/'] = 1
        out = []
        st = sentence.split()
        for word in st:
            t = self.trie
            found = False
            for i in range(len(word)):
                c = word[i]
                if c in t:
                    t = t[c]
                    if t.get('/', -1) != -1:
                        out.append(word[:(i+1)])
                        found = True
                        break
                else:
                    break
            if not found:
                out.append(word)
        return " ".join(out)
        