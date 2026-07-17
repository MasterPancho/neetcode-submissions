class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        #Get the size of each element, and append them together with the word, separating it with "#"
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        
        #Join all the words together
        return("".join(encoded))

    def decode(self, s: str) -> List[str]:
        decoded = []

        while(s is not ""):
            
            a = (s.split('#', 1))
            lenSize = len(a[0])
            size = int(a[0])
            totalSize = lenSize + size + 1

            decoded.append(a[1][:size])   

            s = s[totalSize:]

        return decoded
       