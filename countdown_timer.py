import time
s=int(input("Enter # seconds : "))
for i in range(s,-1,-1):
	second= i%60
	minute=(i//60)%60
	hour=i//3600
	print(f"\r{hour:02}:{minute:02}:{second:02}",end="")
	time.sleep(1)
print("\nTIME UP!")
