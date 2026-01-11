full_dot = '●'
empty_dot = '○'

def create_character(cname, strength, intel, charisma):
    if not isinstance(cname, str):
        return'The character name should be a string'
    if not cname:
        return 'The character should have a name'
    if len(cname) > 10:
        return 'The character name is too long'
    if " " in cname:
        return 'The character name should not contain spaces'
    
    if not isinstance(strength, int) or not isinstance(intel, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength < 1 or intel < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intel > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intel + charisma != 7:
        return 'The character should start with 7 points'

    return (f"""{cname}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot * intel}{empty_dot * (10 - intel)}\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}""")

