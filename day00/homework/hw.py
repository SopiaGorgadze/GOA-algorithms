# მოცემული 3 მთელი a, b, c ̸= 0 რიცხვებისთვის მოძებნეთ a და
# b რიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების
# რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე
# a, b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი.
# მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გა-
# უშვით პროგრამა ციკლის და რეკურსიის (აგრეთვე range) კონ-
# სტრუქციის გამოყენების გარეშე.


def count_multiples(a, b, c):
    if c == 0:
        return 0 
    if a <= b:
        start = a
        end = b
    else:
        start = b
        end = a
    multiples_end = end // c
    multiples_start = (start - 1) // c
    count = multiples_end - multiples_start
    return count

