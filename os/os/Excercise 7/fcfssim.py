lis = [0]
for i in range(int(input('No of process : '))):
    lis.append(lis[-1]+int(input(f'P{i+1} = ')))
print(lis)
print(f'Waiting time : {sum(lis[:-1])/len(lis[:-1])}')
print(f'Turn Around time : {sum(lis[1:])/len(lis[1:])}')