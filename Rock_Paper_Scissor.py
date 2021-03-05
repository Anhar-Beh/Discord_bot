def compare(u1, name1, u2, name2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(name1)
        elif u2 == 'paper':
            return(name2)
        else:
            return("Fail")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(name1)
        elif u2 == 'rock':
            return(name2)
        else:
            return("Fail")
    elif u1 == 'paper':
        if u2 == 'rock':
            return(name1)
        elif u2 == 'scissors':
            return(name2)
        else:
            return("Fail")
    else:
        return("Fail")

