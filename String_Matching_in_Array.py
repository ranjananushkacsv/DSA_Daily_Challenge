def stringMatching(self, words: List[str]) -> List[str]:
    n = len(words)
    result = []
    
    for i in range(n):
        for j in range(n):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
        return result 
    
'''
APPROACH - 

1. Create an empty list results and start a for loop with 2 pointers
2. we have to make sure that i i != j as both are starting from 0 and words[i] should eb in words[j]
3. If the above 2 conditions is satisfied then we can append the words[i] in the empty lsit result.
4. return result :)

'''