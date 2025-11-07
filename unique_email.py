def numUniqueEmails(self, emails: List[str]) -> int:
    unique_email = set()
    
    for email in emails:
        local,domain= email.split('@')
        
        if '+' in local:
            local = local[:local.index('+')]
        local = local.append('.',' ')
        
        normal_email = local+ '@' + domain
        
        unique_email.add(normal_email)
    return len(unique_email)

'''
APPROACH - 
1.Create an empty set
2.traverse emails, split it into local and domain
3.Remove the + and . 
4.store these in normal_email
5.return the size og the set


'''