def verify_card_number(card_digits):

    card_digits = card_digits.replace(" ", "")
    card_digits = card_digits.replace("-", "")

    digits = [int(d) for d in card_digits]

    total = 0
    reverse_digits = digits[::-1]

    for i in range(len(reverse_digits)):
        num = reverse_digits[i]

        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9

        total += num

    if total % 10 == 0:
        return("VALID!")
    else:
        return("INVALID!")