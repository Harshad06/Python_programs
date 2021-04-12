# Given a string, find the longest subsequence consisting of a single character.  
# Example: longest("ABAACDDDBBA") should return {'D': 3}.

# Big O(n) in time as we need to move once only in forward direction.



def longest(seq):
    max_count = 0
    max_char = None
    prev_char = None
    
    for current in seq:
        if prev_char == current:
            count +=1
        else:
            count = 1
        
        if count > max_count:
            max_count = count
            max_char = current
        
        prev_char = current
    
    return {max_char:max_count}

if __name__ == "__main__":
    seq = "ABAACDDDBBA"
    print(longest(seq))
