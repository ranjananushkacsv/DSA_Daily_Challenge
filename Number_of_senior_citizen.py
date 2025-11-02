def countSeniors(self, details: List[str]) -> int:
    count = 0
    
    for detail in details:
        age_string = detail[11:13]
        age = int(age_string)
        
        if age > 60:
            count+=1
    return count
    
'''
APPROACH - 

1. Iterate throught the details list and extract 11th and 12th elements, i.e age
2. convert this substring age to int age.
3. compare if age > 60 if yes increase the count by 1
4. return the count
'''