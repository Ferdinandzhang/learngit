def find_p(A,i,NROW):
	maxest=0
	n=len(A[0])-1
	for j in range(i,n+1,1):
		temp=NROW[j]
		if maxest<abs(A[temp-1][i-1]):
			maxest=abs(A[temp-1][i-1])
	for p in range(i,n+1,1):
		temp1=NROW[p]
		if abs(A[temp1-1][i-1])==maxest:
			break
	return p
def sum_of(i,A,X,NROW):
	total_sum=0
	n=len(A[0])-1
	for j in range(i+1,n+1,1):
		total_sum=total_sum+A[NROW[i]-1][j-1]*X[j-1]
	return total_sum		
def Gaussian_Elimination_with_Partial_pivoting(A):
	n=len(A[0])-1
	NROW=[]
	for i in range(0,n+1,1):
		NROW.append(i)
	for i in range(1,n,1):
		p=find_p(A,i,NROW)
		temp=NROW[p]
		if A[temp-1][i-1]==0:
			print('no unique solution exist')
		if NROW[i]!=NROW[p]:
			NROWtemp=NROW[i]
			NROW[i]=NROW[p]
			NROW[p]=NROWtemp
		for j in range(i+1,n+1,1):
			temp=A[NROW[j]-1][i-1]/A[NROW[i]-1][i-1]
			for mm in range(len(A[0])):
				A[NROW[i]-1][mm]=A[NROW[i]-1][mm]-temp*A[NROW[i]-1][mm]
	if A[NROW[n]-1][n-1]==0:
		print('no unique solution exist')
	X=[0]*n
	X[n-1]=A[NROW[n]-1][n]/A[NROW[n]-1][n-1]
	for i in range(n-1,0,-1):
		X[i-1]=(A[NROW[i]-1][n]-sum_of(i,A,X,NROW))/A[NROW[i]-1][i-1]
	return X
A=[[0.003,59.14,59.17],[5.291,-6.13,46.78]]
print(Gaussian_Elimination_with_Partial_pivoting(A))
	
