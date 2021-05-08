#FatemehZarinjouee
#981813106
from datetime import datetime

def LCG(a, c, m, seed):     
    while True:
        seed = (a * seed + c) % m
        yield seed

def rand(max):
    seed = datetime.now().microsecond
    m=2 ** 31
    res= LCG(1103515245, 12345, m , seed)
    sample=int(next(res)*max/m)
    return sample+1


#-------------------------------------
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a , a)
#-------------------------------------

# It returns (x^y) % p
def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):# yani y fard bashe
        if (y & 1):
            res = (res * x) % p
        y = y//2
        x = (x * x) % p

    return res

def miller(d, n):
    a = 2 + rand(n - 4)

    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True

    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    return False


def is_Prime(n, k):
    if (n <= 1 or n == 4):
        return False

    if (n <= 3):
        return True


    d = n - 1
    while (d % 2 == 0):
        d //= 2

    for i in range(k):
        if (miller(d, n) == False):
            return False

    return True

#-------------------------------------------

def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)


        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

#--------------------------------------------------
#to in algoritm gcd(e,Qn) , zarib e , zarib Qn mohasebe mishe
#vali chon gcd(e,Qn)=1 va be zarib Qn niaz nadarim azashon sarf nazar kardam
#va faghat zarib e ro hesab mikone
    
def xgcd(e, Qn):
    x, old_x = 0, 1
    s=Qn

    while (Qn != 0):
        quotient = e // Qn
        e, Qn = Qn, e - quotient * Qn
        old_x, x = x, old_x - quotient * x
        
    if old_x<0:
        old_x=old_x+s
        
    return old_x
#-----------------------------------------------
def chineseremaindertheorem(d, p , q, c):
    dq=power(d,1,q-1)
    dp=power(d,1,p-1)
    m1 = power(c, dp, p) 
    m2 = power(c, dq, q) 
      
    qinv = xgcd(q, p) 
    h = (qinv * (m1 - m2)) % p 
    m = m2 + h * q 
    return m


#-----------------------------------------
def key_maker():
    p=0
    q=0
    n,m,c=False , False,False
    while p==q:
        s=0
        while n==False:
            p=rand(2**512)
            if p!=s:
                if is_Prime(p,30)==True:
                    n=True
                s=p
                
        while m==False:
            q=rand(2**512)
            if q!=s:
                if is_Prime(q,30)==True:
                    m=True
                s=q
                
        if len(str(p))-len(str(q))>3:
            p=q

    n=karat(p,q)
    Qn=karat(p-1,q-1)
    #entekhab e 
    while c==False:
        e=rand(Qn)
        if gcd(e,Qn)==1:
            c=True

    d=xgcd(e,Qn)
    public=(e,n)
    private=(d,n)
    with open('public_key','w') as file:
        file.write(f'{public}')
    with open('private_key' , 'w') as file2:
        file2.write(f"{private}" + '\n')
        file2.write(f'{(p,q)}' + '\n')


#------------------------------------------
def encrypt(message,file='public_key',block_size=32):
    try:
        with open(file , 'r') as fi:
            e,n = eval(fi.readline())
            
    except FileNotFoundError:
        print('That file is not found.')

    else:
        encrypted_blocks = []
        ciphertext = -1
        
        if (len(message) > 0):
            ciphertext = ord(message[0])

        for i in range(1, len(message)):

            if (i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            ciphertext = ciphertext * 55292 + ord(message[i])

        encrypted_blocks.append(ciphertext)

        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str(power(encrypted_blocks[i],e, n))

        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message

    
def Ascci_encrypt(message,file='public_key',block_size=32):
    try:
        with open(file , 'r') as fi:
            e,n = eval(fi.readline())
            
    except FileNotFoundError:
        print('That file is not found.')

    else:
        encrypted_blocks = []
        ciphertext = -1
        
        if (len(message) > 0):
            ciphertext = ord(message[0])

        for i in range(1, len(message)):

            if (i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            ciphertext = ciphertext * 256 + ord(message[i])

        encrypted_blocks.append(ciphertext)

        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str(power(encrypted_blocks[i],e, n))

        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message


#----------------------------------------------
def decrypt(code,block_size=32):
    with open('private_key','r') as file:
        d,n=eval(file.readline())
        p,q=eval(file.readline())
        
    list1=list(map(int,code.split()))
    message=''

    for i in range(len(list1)):
        list1[i]= chineseremaindertheorem(d, p , q, list1[i])

        text=''

        for j in range(block_size):
            text=chr(list1[i] % 55292) + text
            list1[i]=list1[i]//55292
            
        message+=text
        
    return message


def Assci_decrypt(code,block_size=32):
    with open('private_key','r') as file:
        d,n=eval(file.readline())
        p,q=eval(file.readline())
        
    list1=list(map(int,code.split()))
    message=''

    for i in range(len(list1)):
        list1[i]= chineseremaindertheorem(d, p , q, list1[i])

        text=''

        for j in range(block_size):
            text=chr(list1[i] % 256) + text
            list1[i]=list1[i]//256
            
        message+=text
        
    return message
#------------------------------------------------


def main():

    choose_again = input('Do you want to generate new public and private keys? (YEs or NO)\t')
    if (choose_again.lower() == 'yes'):
        print('please be patient...')
        key_maker()

    instruction = input('Would you like to encrypt or decrypt? (Enter E or D):\t')
    length=int(input('how longe is the block size!?\t'))
    if (instruction.lower() == 'e'):
        lan=input('do you want to use Ascci(1)or another(2) languages!?(Enter 1 or 2)\t')
        message = input('What would you like to encrypt?\n')
        option = input('Do you want to encrypt using your own public key? (YES or NO) \t')
        if (option.lower() == 'yes'):
            if lan.lower()=='2':
                print('Encrypting...')
                print(encrypt(message,'public_key',length))
            if lan.lower() == '1':
               print('Encrypting...')
               print(Ascci_encrypt(message,'public_key',length))
               
                   
        else:
            file_option = input('Enter the file name that stores the public key:\t ')
            print('Encrypting...')
            print(Ascci_encrypt(message, file_option,length))

    elif (instruction.lower() == 'd'):
        lang=input('do you want to use Ascci(1) or another(2) languages!?(Enter 1 or 2)\t')
        message = input('What would you like to decrypt?\n')
        if lang.lower()=='2':
            print('Decryption...')
            print(decrypt(message,length))
        if lang.lower() == '1':
            print('Decryption...')
            print(Assci_decrypt(message,length))

    else:
        print('That is not a proper instruction.')

if __name__=='__main__':
    main()



















