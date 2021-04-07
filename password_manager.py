SECURE_CODES = (('A','/|'),('B','8'),('C','('),('d','6'),('E','3'),('F','7'),('g','8'),('H','|-|'),('I','1'),('o','0'),('K','|<'),('a','@'),('s','&'),('p','|*'),('q','*|'),('t','#'),('M','|\/|'),('N','|\|'),('P','?'),('x','*'),('D','|)'),('d','c|'),('m','^^'),('n','^'),('S','$'),('L','|_'),('l','|'))

def passwordSecure(password):
    for a,b in SECURE_CODES:
        password = password.replace(a,b)
    return password

password = input('Please provide your password here: ').strip()
decision = input('Do you want to include UPPER/LOWER case letters?("y for UPPER/n for lower",else will remain unchanged): ').strip()

if decision == 'y':
    password = password.upper()
    print(f"Your new password is {passwordSecure(password)}")

elif decision == 'n':
    password = password.lower()
    print(f"Your new password is {passwordSecure(password)}")
else:
    print(f"Your new password is {passwordSecure(password)}")
