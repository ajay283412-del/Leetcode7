class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # convert string to list
        l = 0
        r = len(s) - 1
        vowels = set('aeiouAEIOU')
        
        while l < r:
            # move l right until a vowel is found
            while l < r and s[l] not in vowels:
                l += 1
            # move r left until a vowel is found
            while l < r and s[r] not in vowels:
                r -= 1
            
            # now both s[l] and s[r] are vowels (if l<r), swap them
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
        # join back to string and return
        return "".join(s)

