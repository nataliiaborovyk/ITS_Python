'''
Rotoli dei Giudici
Segnala problema

Valuti la purezza dei cristalli. Applica `grade(score)` con le soglie: 
`A` (>=90), `B` (>=80), `C` (>=70), `D` (>=60), altrimenti `F`. 
Mantieni la firma e titola i test.
'''


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"