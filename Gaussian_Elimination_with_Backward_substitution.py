def find_p(A,i):
	flag=0
	for p in range(i,len(A[0]),1):
		if A[p-1][i-1]!=0:
			flag=1
			break
	if flag==1:
		return p
	else:
		return -1
def sum_of(X,A,i):
	n=len(A[0])-1
	total_sum=0
	for j in range(i+1,n+1,1):	
		total_sum=total_sum+A[i-1][j-1]*X[j-1]
	return total_sum
def Gaussian_Elimination_with_Backward_substitution(A):
	n=len(A[0])-1	
	X=[0]*n		
	for i in range(1,len(A[0]),1):
		p=find_p(A,i)
		if p==-1:
			print('no unique solution exist!')
		if p!=i:
			temp=A[p-1]
			for j in range(len(A[0])):
				A[p-1].insert(A[i-1][j],j)
				A[i-1].insert(temp[j],j)
		for j in range(i+1,n+1,1):
			m=A[j-1][i-1]/A[i-1][i-1]
			for k in range(len(A[0])):			
				A[j-1][k]=A[j-1][k]-m*A[i-1][k]
	if A[n-1][n-1]==0:
		print('no unique solution exist!')
	X[n-1]=A[n-1][n]/A[n-1][n-1]
	for i in range(n-1,0,-1):
		X[i-1]=(A[i-1][n]-sum_of(X,A,i))/A[i-1][i-1]
	return X
A=[[1,1,0,3,4],[2,1,-1,1,1],[3,-1,-1,2,-3],[-1,2,3,-1,4]]
print(Gaussian_Elimination_with_Backward_substitution(A))	
	
