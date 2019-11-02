from optparse import OptionParser

class Job:
    """
    Class to define a job with attributes start, end and weight
    """
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


def job_search(job, start_index):
    """
    this function uses binary search to return the job with the highest start time which does not overlap with the
     passed job
    :param job: a particular job
    :param start_index: start index of the job
    :return: start index of the job which does not overlap with the given job
    """
    j = 0
    i = start_index - 1

    #Binary search
    while j <= i:
        mid = (i + j) // 2
        if Jobs[mid].end <= Jobs[start_index].start:
            if Jobs[mid+1].end <= Jobs[start_index].start:
                j = mid + 1
            else:
                return mid
        else:
            i = mid - 1
    return -1


def job_schedule(job):
    """
    Function which uses memoization to store the highest weights for a given set of job
    :param job: Set of jobs
    :return: highest weights
    """
    job = sorted(job, key=lambda j: j.end)

    n = len(job)
    net_profit = [0 for i in range(n)]

    # table which stores the maximum weight for given set of jobs
    net_profit[0] = job[0].weight

    for i in range(1, n):
        job_profit = job[i].weight
        l = job_search(job, i)
        if l != -1:
            job_profit += net_profit[l]
        net_profit[i] = max(job_profit, net_profit[i-1])
    return net_profit[n-1]


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--filename", dest="filename")
    (options, args) = parser.parse_args()
    with open(options.filename, "r") as f:
        input = f.read()
        f.close()

    Jobs = []
    input_list = input.split('\n')
    for item in input_list:
        vals = item.split(' ')
        # print(len(vals))
        if len(vals) > 1:
            job = Job(int(vals[0]), int(vals[1]), int(vals[2]))
            Jobs.append(job)

    print("Profit:")
    print(job_schedule(Jobs))


