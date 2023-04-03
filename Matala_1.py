# Bar Mizrahi 315042994

# Question 1
# i assumed that sections 2+4 shuuld be saparted. checking individualy if there is any int type 
# and than checking if all of them are float type.

def func_1(X1: float, X2: float, X3: float) -> float:
    
    # Check for any parameter is of type int:
    if type(X1)==int or type(X2)==int or type(X3)==int:
        return("Error: parameters should be float")
        
    # Check if all parameters are of type float   
    if not all(isinstance(x, float) for x in [X1, X2, X3]):
        return None

    # Check if denominator is zero
    denominator = X1 + X2 + X3
    if denominator == 0:
        return("Not a number - denominator equals zero")
    
    # Compute and return the value
    numerator = (X1 + X2 + X3) * (X2 + X3) * X3
    return float(numerator / denominator)


# Question 2 

#   Reading the word from the end to the start and changing to lower case.
def revword (word:str) -> str:
    word=word[::-1].lower()
    return (word)

# As i understood, the file needs to be read from inside the function. However, the user can upload any file.
def countword(file_name: str) -> int:
    # Reading the file
    text = open(file_name,"r")
    counter = 1
    # Going through each line and creating a list that contains all the words in the text.
    for line in text:
        word_list = line.split(" ")
        # Setting the first word in the text as the original for comparison in lower case.
        if len(word_list)==1:
            original_word =word_list[0].lower().strip()
        else:
            # Using the revword function on each word from the list.
            for w2 in word_list:
                word = revword(w2).strip()
                # comparing each word from the list to the original word. If identical add 1 to the counter.
                if word == original_word:
                    counter = counter + 1
    return(counter)
                    
