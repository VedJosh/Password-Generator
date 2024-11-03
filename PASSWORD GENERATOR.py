# password creator

def password(x=15):
    import random
    nsp = random.randint(2, 4)
    nd = random.randint(2, 4)
    nchr = random.randint(1, 3)
    nchr1 = x - nsp - nd - nchr
    alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                 'n', 'b', 'v', 'c', 'x', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`', '{', '}', '[', ']', '|',
                          ';', ':', ',', '.', '<', '>', '/', '?']
    f = []
    final_password = ''
    for i in range(nsp):
        f.append(random.choice(special_characters))
    for j in range(nd):
        f.append(random.choice(numbers))
    for k in range(nchr):
        f.append(random.choice(alphabets).upper())
    for a in range(nchr1):
        f.append(random.choice(alphabets))
    for z in range(len(f)):
        p = f.pop(random.randrange(0, len(f)))
        final_password += p
    print(f"Your password is {final_password}")
    return final_password

password(int(input('Enter the length of password you want: ')))