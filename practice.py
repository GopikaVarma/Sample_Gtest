


def modify_division(function):
    def inner(a,b):
        if(b==0):
            print("Division by zero is not possible")
            return
        return(function(a,b))
    return inner

def modify_division2(function):
    def inner(a,b):
        if(a<b):
            a,b = b,a

        return(function(a,b))
    return inner

@modify_division2
@modify_division
def division(a,b):
    print(a/b)


division(2,80)



