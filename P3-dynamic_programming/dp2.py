# from parser import pas

class Job:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


def job_search(job, start_index):
    j = 0
    i = start_index - 1

    while j <= i:
        if Jobs[j].end <= Jobs[i].start:
            if Jobs[j+1].end <= Jobs[i].start:
                j += 1
            else:
                return j
        else:
            i -= 1
    return -1


def job_schedule(job):

    job = sorted(job, key=lambda j: j.end)

    n = len(job)
    net_profit = [0 for i in range(n)]

    net_profit[0] = job[0].weight

    for i in range(1, n):

        job_profit = job[i].weight
        l = job_search(job, i)
        if l != -1:
            job_profit += net_profit[l]

        net_profit[i] = max(job_profit, net_profit[i-1])

    return net_profit[n-1]


with open("input1.txt", "r") as f:
    input = f.read()
    f.close()

Jobs = []
input_list = input.split('\n')
for item in input_list:
    vals = item.split(' ')
    # print(len(vals))
    if len(vals) > 1:
        job = Job(vals[0], vals[1], vals[2])
        Jobs.append(job)

#Jobs = [Job(1, 2, 50), Job(3, 5, 20),  Job(6, 19, 100), Job(2, 100, 200)]

print("Profit:")
print(job_schedule(Jobs))


