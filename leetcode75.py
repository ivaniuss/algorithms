class Solution(object):
    def mergeAlternately(self, word1, word2):
        max = word1
        res = ''
        if len(word2) > len(word1):
            max = word2
        for i, _ in enumerate(max):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res
        
def main():
    solution = Solution()
    print(solution.mergeAlternately('ab', 'pqrs'))

if __name__ == '__main__':
    main()