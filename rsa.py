def pgcd(nombres_):
	nombres=nombres_.copy()
	if not type(nombres) is list:
		return None
	if len(nombres)==0:
		return None
	for i in range(len(nombres)):
		if nombres[i]<0:
			nombres[i]=-nombres[i]
		if nombres[i]==0:
			return None
	min_n=nombres[0]
	for n in nombres:
		if min_n>n:
			min_n=n
	for i in range(int(min_n),0,-1):
		found=True
		for n in nombres:
			if n%i!=0:
				found=False
				break
		if found==True:
			return i
	return None

def producekeys(primenumber1,primenumber2):
	N=primenumber1*primenumber2
	T=(primenumber1-1)*(primenumber2-1)
	e=0
	d=0
	for i in range(T-1,1,-1):
		if pgcd([i,T])==1 and pgcd([i,N])==1:
			e=i
			break
	d=e+T
	return (e,N),(d,N)

def crypt(key,message):
	answer=[]
	for m in message:
		answer.append(chr((ord(m)**key[0])%key[1]))
	return "".join(answer)

def main():
	print("\nŞÜKRÜ ÇİRİŞ 18401785 GSU\nRSA encryption algorithm uses two prime numbers to produce public and private keys\nthat will be used to encrypt and decrypt the messages.")
	print("If you select prime numbers that are too small, decryption may not work correctly.\nThe product of the prime numbers must be greater than the size of the ASCII table at least.\n")
	primenumber1=int(input("Give first prime number: "))
	primenumber2=int(input("Give second prime number: "))
	publickey,privatekey=producekeys(primenumber1,primenumber2)
	print("Public key: "+str(publickey))
	print("Private key: "+str(privatekey))
	while(True):
		print("Enter 1 to encrypt a message.\nEnter 2 to decrypt a message.\nEnter 3 to encrypt a file.\nEnter 4 to decrypt a file.\nEnter 5 to exit.")
		inp=input()
		if inp=="1":
			print(crypt(publickey,input("Message: ")))
		elif inp=="2":
			print(crypt(privatekey,input("Message: ")))
		elif inp=="3":
			f1 = open(input("File path: "), "rb")
			f2=open(input("Save file path: "), "wb")
			f2.write(crypt(publickey,f1.read().decode("UTF-8")).encode("UTF-8"))
			f2.close()
			f1.close()
		elif inp=="4":
			f1 = open(input("File path: "), "rb")
			f2=open(input("Save file path: "), "wb")
			f2.write(crypt(privatekey,f1.read().decode("UTF-8")).encode("UTF-8"))
			f2.close()
			f1.close()
		elif inp=="5":
			break
		else:
			print("Please enter valid input.\n")
	return 0

main()