A,B, C = [int(i) for i in input().split()]
if C == 0:
   if A > B:
       print("Takahashi")
   else:
       print("Aoki")
else:
    if B > A:
        print("Aoki")
    else:
        print("Takahashi")

