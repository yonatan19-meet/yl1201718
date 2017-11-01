a = [1,2,3,4,5,6, "app", "bring"]
def MakeListsShorter (a):
	b = []
	b.append(a[0])
	b.append(a[-1])
	return b


result=MakeListsShorter(a)
print(result)