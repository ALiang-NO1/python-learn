L=[1,2,3,4,5,7,8]
def delete_list(L,i):
	L_lenght = len(L)
	if i<1 or i>L_lenght:
		return false
	if i<L_lenght:
		del L[i]
		for k in range(i+1,L_lenght-1)[::1]:
			L[k]= L[k+1]
	print(L)

delete_list(L,5)