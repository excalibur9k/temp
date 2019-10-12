n=int(input())

board=[[]*n]*n
string=''

for i in range(n):
	string=list(input())
	board[i]=string

for i in range(n):
	print(board[i][1])
print(board)
