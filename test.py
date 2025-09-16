def horaire_sup(name:str , salary_hour:float , hours_worked:int) -> float :
    if hours_worked > 40:
        salary = (40 * salary_hour) + ((hours_worked - 40) * salary_hour * 1.5)
    else:
        salary = hours_worked * salary_hour

    return salary


print(horaire_sup("Hafid" , 10 , 10))