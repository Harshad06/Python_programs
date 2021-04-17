
def decor_result(result_func):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print(f"Passed with Distinction")
        result_func(marks)
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m > 33:
            pass
        else:
            print(f"FAIL")
            break
    else:
        print(f"PASS")    


result([50,60,70,80,90])