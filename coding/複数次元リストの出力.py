ans=[['dog','cat','rabbit']]
print(" ".join(*ans))
# dog cat rabbit

# これを利用して
ans=[['dog','cat'],["tiger",'rabbit']]
for i in range(2):
    print(" ".join(ans[i]))

# dog cat
# tiger rabbit
