### CSCI B-505 Applied Algorithms - Assignment - 1
### Submitted by - Vishal

import numpy as np
import timeit
import statistics
from matplotlib import pyplot as plt
import random
import math


class SortingAlgos:

    def __init__(self):

        self.list_lengths = np.arange(5000, 10001, 5000)

    def gen_array(self, n):
        gen_arr = np.random.randint(n, size=n)
        return gen_arr

    def partition(self, A, p, r):
        # print(p, r)
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        q = i + 1
        # print(q, A)
        return q

    def quick_sort(self, A, p, r):
        start_time = timeit.default_timer()
        if p < r:
            q = self.partition(A, p, r)
            self.quick_sort(A, p, q - 1)
            self.quick_sort(A, q + 1, r)
        time_elapsed = timeit.default_timer() - start_time
        return A, time_elapsed

    def merge(self, l_arr, r_arr, arr):
        nl = len(l_arr)
        nr = len(r_arr)
        i = j = k = 0
        while i < nl and j < nr:
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = r_arr[j]
                k += 1
                j += 1
        while i < nl:
            arr[k] = l_arr[i]
            i += 1
            k += 1
        while j < nr:
            arr[k] = r_arr[j]
            j += 1
            k += 1

    def merge_sort(self, arr):
        start_time = timeit.default_timer()
        n = len(arr)
        if n < 2:
            return arr
        mid = math.floor(n/2)
        left = [arr[i] for i in range(0, mid)]
        right = [arr[i] for i in range(mid, n)]
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(left, right, arr)
        time_elapsed = timeit.default_timer() - start_time
        return arr, time_elapsed

    def selection_sort(self, A):
        start_time = timeit.default_timer()
        for i in range(len(A)):
            min_idx = i
            for j in range(i+1, len(A)):
                if A[j] < A[min_idx]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        time_elapsed = timeit.default_timer() - start_time
        return A, time_elapsed

    def insertion_sort(self, A):

        start_time = timeit.default_timer()
        for i in range(1, len(A)):
            key = A[i]
            j = i - 1
            while j > 0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j + 1] = key
        time_elapsed = timeit.default_timer() - start_time
        return A, time_elapsed

    def plot_graph(self, is_array, ss_array, suffix):
        plt.plot(self.list_lengths, is_array, label='Insertion Sort',
                 marker='o')
        plt.plot(self.list_lengths, ss_array, label='Selection Sort',
                 marker='o')
        plt.xlabel('array lengths')
        plt.ylabel('sorting times')
        plt.title('Comparison of running times for sorting algorithms for ' + 
                  suffix)
        plt.legend()
        plt.xticks(self.list_lengths)
        plt.show()
        
    def swap_random(self, arr):
        idx = range(len(arr))
        i1, i2 = random.sample(idx, 2)
        arr[i1], arr[i2] = arr[i2], arr[i1]
    
    def generate_runtimes(self, sort=False, rvs=False, avg=False, swap=False, i_srt=False, s_srt=False, m_srt=False,
                          q_srt=False):
        if avg == True:
            print("Averaging ...")
        if swap == True:
            print("Swapping...")
        is_runtimes, ss_runtimes, ms_runtimes, qs_runtimes = [], [], [], []
        for n in self.list_lengths:
            print(n)
            gen_arr = sorting_algos.gen_array(n)
            qs_r = n - 1
            if sort==True:
                gen_arr = sorted(gen_arr, reverse = rvs)
            if swap == True:
                for s in range(50):
                    self.swap_random(gen_arr)
            if avg == True:
                is_time_avg, ss_time_avg, ms_time_avg, qs_time_avg = [], [], [], []
                for i in range(3):
                    is_arr_sub, is_time_sub = self.insertion_sort(gen_arr)
                    ss_arr_sub, ss_time_sub = self.selection_sort(gen_arr)
                    ms_arr_sub, ms_time_sub = self.merge_sort(gen_arr)
                    qs_arr_sub, qs_time_sub = self.quick_sort(gen_arr, 0, qs_r)

                    is_time_avg.append(is_time_sub)
                    ss_time_avg.append(ss_time_sub)
                    ms_time_avg.append(ms_time_sub)
                    qs_time_avg.append(qs_time_sub)
                is_time = statistics.mean(is_time_avg)
                ss_time = statistics.mean(ss_time_avg)
                ms_time = statistics.mean(ms_time_avg)
                qs_time = statistics.mean(qs_time_avg)
            else:
                is_arr, is_time = self.insertion_sort(gen_arr)
                ss_arr, ss_time = self.selection_sort(gen_arr)
                ms_arr, ms_time = self.merge_sort(gen_arr)
                qs_arr, qs_time = self.quick_sort(gen_arr, 0, qs_r)
            is_runtimes.append(is_time)
            ss_runtimes.append(ss_time)
            ms_runtimes.append(ms_time)
            qs_runtimes.append(qs_time)
        print("Insertion sort running times:",
              [round(t, 5) for t in is_runtimes])
        print("Selection sort running times:",
              [round(t, 5) for t in ss_runtimes])
        print("Merge sort running times:",
              [round(t, 5) for t in ms_runtimes])
        print("Quick sort running times:",
              [round(t, 5) for t in qs_runtimes])
        return is_runtimes, ss_runtimes, ms_runtimes, qs_runtimes
    
    def generate_runtimes_i5(self):
        is_runtime_i5 = 0
        ss_runtime_i5 = 0
        ms_runtime_i5 = 0
        qs_runtime_i5 = 0
        for i in range(100000):
            gen_arr_i5 = sorting_algos.gen_array(50)
#            print(gen_arr_i5)
            is_arr_i5, is_time_i5 = self.insertion_sort(gen_arr_i5)
            ss_arr_i5, ss_time_i5 = self.selection_sort(gen_arr_i5)
            ms_arr_i5, ms_time_i5 = self.merge_sort(gen_arr_i5)
            qs_arr_i5, qs_time_i5 = self.quick_sort(gen_arr_i5, 0, 49)
            is_runtime_i5 += is_time_i5
            ss_runtime_i5 += ss_time_i5
            ms_runtime_i5 += ms_time_i5
            qs_runtime_i5 += qs_time_i5
            if i % 1000 == 0:
                print(ms_runtime_i5)
        return is_runtime_i5, ss_runtime_i5, ms_runtime_i5, qs_runtime_i5


if __name__ == "__main__":

    sorting_algos = SortingAlgos()
    # tt = 0
    # for n in range(100000):
    #     A = sorting_algos.gen_array(50)
    #     # print(A)
    #     r = len(A)-1
    #     # print(r)
    #     A, te = sorting_algos.quick_sort(A, 0, 49)
    #     # A, te = sorting_algos.merge_sort(A)
    #     # print(A)
    #     # print(te)
    #     tt += te
    # print(tt)

    # ##Generating runtimes
    # print("Input 1")
    # is_runtimes_p1, ss_runtimes_p1, ms_runtimes_p1, qs_runtimes_p1 = sorting_algos.generate_runtimes(
    #         sort=False, avg=True)
    # print("Input 2")
    # is_runtimes_p2, ss_runtimes_p2 = sorting_algos.generate_runtimes(
    #         sort=True, rvs=False)
    # print("Input 3")
    # is_runtimes_p3, ss_runtimes_p3 = sorting_algos.generate_runtimes(
    #         sort=True, rvs=True)
    # print("Input 4")
    # is_runtimes_p4, ss_runtimes_p4 = sorting_algos.generate_runtimes(
    #         sort=True, rvs=False, swap=True, avg=True)
    print("Input 5")
    is_runtimes_p5, ss_runtimes_p5, ms_runtime_p5, qs_runtime_p5 = sorting_algos.generate_runtimes_i5()
    print(is_runtimes_p5, ss_runtimes_p5, ms_runtime_p5, qs_runtime_p5)
    #
    # ##Plotting
    # sorting_algos.plot_graph(is_runtimes_p1, ss_runtimes_p1, "input 1")
    # sorting_algos.plot_graph(is_runtimes_p2, ss_runtimes_p2, "input 2")
    # sorting_algos.plot_graph(is_runtimes_p3, ss_runtimes_p3, "input 3")
    # sorting_algos.plot_graph(is_runtimes_p4, ss_runtimes_p4, "input 4")
    # print("Total insertion sort running time for input 5:",
    #       round(is_runtimes_p5, 5))
    # print("Total selection sort running time for input 5:",
    #       round(ss_runtimes_p5, 5))

