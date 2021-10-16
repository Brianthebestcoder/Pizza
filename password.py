import time
password = "robertthebuilder1230"
wait_count = 2
print ("enter password")
inp = str(input())
#print (inp)
while inp != password:
    print ("wrong password... Try Again in " + str(wait_count) + " seconds")
    time.sleep(wait_count)
    print ("enter password again:")
    inp = str(input())
    wait_count = wait_count * wait_count
print ("Access granted")
time.sleep(30)



    



