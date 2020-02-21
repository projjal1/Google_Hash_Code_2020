B,L,D=[int(i) for i in input().split()]
S=[int(i) for i in input().split()] # scores of each book

L_index=[]

N=[] # no of books in each library
T=[] # total sign up days for each library
M=[] # max books each library can scan each day
LB=[] # book ids of each library
for i in range(L):
	L_index.append(i)
	for j in N,T,M:
		j.append(None)
	N[i],T[i],M[i]=[int(i) for i in input().split()]
	LB.append([])
	LB[i]=[int(i) for i in input().split()]


# sorting libraries in ascending order of signup time
for i in range(L):
	min_i=i
	for j in range(i+1,L):
		if T[j]<T[min_i]:
			min_i=j
	L_index[i],L_index[min_i]=L_index[min_i],L_index[i]
	N[i],N[min_i]=N[min_i],N[i]
	T[i],T[min_i]=T[min_i],T[i]
	M[i],M[min_i]=M[min_i],M[i]
	LB[i],LB[min_i]=LB[min_i],LB[i]


#sorting books in each library in descending order of their scores
for i in range(L):
	for j in range(N[i]):
		max_j=j
		for k in range(j+1,N[i]):
			if S[LB[i][k]]>S[LB[i][max_j]]:
				max_j=k
		LB[i][j],LB[i][max_j]=LB[i][max_j],LB[i][j]


# calculating...
books_dict={}
LB_out=[] #books ids to set to scan for each library
days=0
for i in range(L):
	days+=T[i]
	if D-days-1<=0:
		break
	LB_out.append([])
	for j in range((D-days-1)*M[i]):
		if j==len(LB[i]):
			break
		if LB[i][j] not in books_dict:
			books_dict[LB[i][j]]=None
			LB_out[-1].append(LB[i][j])
	if len(LB_out[-1])==0:
		LB_out[-1].append(LB[i][0])
	
# printing...
print(len(LB_out))
for i in range(len(LB_out)):
	print(L_index[i],len(LB_out[i]))
	for j in range(len(LB_out[i])):
		print(LB_out[i][j],end=" ")
	print()


	
	

