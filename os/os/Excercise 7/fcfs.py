st, li = "Process\t\tWaiting time\t\tTrun Around time\n", [0]
for i in range(int(input('Number of process:'))):
    li.append(li[-1]+int(input(f'P{i+1} = ')))
    st += f"P{i+1}\t\t{li[-2]}\t\t\t{li[-1]}\n"
print('\n'+st+f'Avg Waiting time = {round(sum(li[:-1])/len(li[:-1]), 2)}\nAvg Turn Around time = {round(sum(li[1:])/len(li[1:]), 2)}')
print(li[1])