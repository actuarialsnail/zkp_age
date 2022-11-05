import hashlib;
import sys;

age_actual = 20
age_to_prove = 18
seed = b"000abc"

print ("Alice proof")

# todo: build in boundary condition checks to avoid potential exploit

proof = hashlib.md5(seed)
print(proof.hexdigest())

encrypted_age = hashlib.md5(seed)

for i in range(1, 1+age_actual-age_to_prove):
	proof = hashlib.md5(proof.digest())
	print(proof.hexdigest())

print ("Encypted age")

for i in range(1,age_actual+1):
	encrypted_age = hashlib.md5(encrypted_age.digest())
	print(encrypted_age.hexdigest())

verified_age=proof

print ("Verifying age")

for i in range(0,age_to_prove):
	verified_age = hashlib.md5(verified_age.digest())
	print(verified_age.hexdigest())

# print ("Peggy's Age:\t\t",age_actual)
# print ("Age to prove:\t\t",age_to_prove)

print ("....")


print ("Proof:\t\t",proof.hexdigest())
print ("Encr Age:\t",encrypted_age.hexdigest())
print ("Verified Age:\t",verified_age.hexdigest())

if (encrypted_age.hexdigest()==verified_age.hexdigest()):
	print ("You have proven your age ... please come in")
else:
	print ("You have not proven you age!")