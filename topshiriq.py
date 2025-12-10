from random import randint



def main():
    greeting()
    random_number = get_random_number()
    imkoniyat = 4
    summ = 10000
    print(f"Sizning balansingiz: {summ}")

    
    while True:
        imkoniyat -= 1
        if imkoniyat == 0:
            print("Imkoniyatlaringiz tugadi siz yutqizdingiz!!!")
            print(f"Men o`ylagan son {random_number} edi.")
            summ -= 1000     
            break
        
        input_number = get_number_from_user()
        
        if input_number == 0:
            break
    
        hint = get_hint(random_number, input_number)

        if hint == "siz men o`ylagan songa o`ta yaqinsiz":
            print("siz men o`ylagan songa o`ta yaqinsiz")
            continue
        elif hint == "siz ozgina o`tib ketdingiz..":
            print("siz ozgina o`tib ketdingiz..")
            continue    
        elif hint == "kichik":
            print("Men o'ylagan son kichik siz kiritgan sondan")
            continue
        elif hint == "katta":
            print("Men o'ylagan son katta siz kiritgan sondan")
            continue
        elif hint == "teng":
            print("Tabriklayman siz yutdingiz!")
            print("Yana kutib qolamiz")
            summ += 1000
            break
        

def greeting():
    print("""
    Assalomu alaykum
    Omad o'yiniga xush kelibsiz
    men son o'ylayman siz topasiz!
    son o'yladim men. uni toping
    sizda 3ta imkoniyat bor!!!
    """)


def get_random_number(from_ = 1, _to = 10):
    return randint(from_, _to)


def get_number_from_user():
    print("Son kiriting:>>")
    return int(input())

def get_hint(random_number: int, input_number: int):
    if random_number - input_number == 2 or input_number - input_number == 1:
        return "siz men o`ylagan songa o`ta yaqinsiz"
    if input_number - random_number == 2 or input_number - input_number == 1:
        return "siz ozgina o`tib ketdingiz.."    
    elif random_number > input_number:
        return "katta"
    elif random_number < input_number:
        return "kichik"
    else:
        return "teng"


main()