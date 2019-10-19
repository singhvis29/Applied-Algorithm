### CSCI B-505 Applied Algorithms - Assignment - 2
### Submitted by - Vishal

import numpy as np
import timeit
import statistics
from matplotlib import pyplot as plt
import random
import math
import copy
import sys
sys.setrecursionlimit(30000)


class SortingAlgos:

    def __init__(self):

        self.list_lengths = np.arange(5000, 30001, 5000)

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
        A[i + 1], A[r] = A[r], A[i + 1]
        q = i + 1
        # print(q, A)
        return q

    def quick_sort(self, A, p, r):
        A_copy = copy.deepcopy(A)
        start_time = timeit.default_timer()
        if p < r:
            q = self.partition(A_copy, p, r)
            self.quick_sort(A_copy, p, q - 1)
            self.quick_sort(A_copy, q + 1, r)
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
        mid = math.floor(n / 2)
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
            for j in range(i + 1, len(A)):
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
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
        time_elapsed = timeit.default_timer() - start_time
        return A, time_elapsed

    def plot_graph(self, suffix, is_array=None, ss_array=None, ms_array=None, qs_array=None):
        if is_array is not None:
            plt.plot(self.list_lengths, is_array, label='Insertion Sort',
                     marker='o')
        if ss_array is not None:
            plt.plot(self.list_lengths, ss_array, label='Selection Sort',
                     marker='o')
        if ms_array is not None:
            plt.plot(self.list_lengths, ms_array, label='Merge Sort',
                     marker='o')
        if qs_array is not None:
            plt.plot(self.list_lengths, qs_array, label='Quick Sort',
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

    def generate_runtimes(self, sort=False, rvs=False, avg=False, swap=False, s_srt=False, q_srt=True):
        if avg == True:
            print("Averaging ...")
        if swap == True:
            print("Swapping...")
        is_runtimes, ss_runtimes, ms_runtimes, qs_runtimes = [], [], [], []
        for n in self.list_lengths:
            print(n)
            gen_arr1 = sorting_algos.gen_array(n)
            gen_arr2 = copy.deepcopy(gen_arr1)
            gen_arr3 = copy.deepcopy(gen_arr2)
            gen_arr4 = copy.deepcopy(gen_arr3)
            qs_r = n - 1
            if sort:
                gen_arr1 = sorted(gen_arr1, reverse=rvs)
                gen_arr2 = sorted(gen_arr2, reverse=rvs)
                gen_arr3 = sorted(gen_arr3, reverse=rvs)
                gen_arr4 = sorted(gen_arr4, reverse=rvs)
            if swap:
                for s in range(50):
                    self.swap_random(gen_arr1)
                    self.swap_random(gen_arr2)
                    self.swap_random(gen_arr3)
                    self.swap_random(gen_arr4)
            if avg:
                is_time_avg, ss_time_avg, ms_time_avg, qs_time_avg = [], [], [], []
                for i in range(3):
                    is_arr_sub, is_time_sub = self.insertion_sort(gen_arr1)
                    if s_srt:
                        ss_arr_sub, ss_time_sub = self.selection_sort(gen_arr2)
                    ms_arr_sub, ms_time_sub = self.merge_sort(gen_arr3)
                    if q_srt:
                        qs_arr_sub, qs_time_sub = self.quick_sort(gen_arr4, 0, qs_r)
                    is_time_avg.append(is_time_sub)
                    if s_srt:
                        ss_time_avg.append(ss_time_sub)
                    ms_time_avg.append(ms_time_sub)
                    if q_srt:
                        qs_time_avg.append(qs_time_sub)
                is_time = statistics.mean(is_time_avg)
                if s_srt:
                    ss_time = statistics.mean(ss_time_avg)
                ms_time = statistics.mean(ms_time_avg)
                if q_srt:
                    qs_time = statistics.mean(qs_time_avg)
            else:
                is_arr, is_time = self.insertion_sort(gen_arr1)
                if s_srt:
                    ss_arr, ss_time = self.selection_sort(gen_arr2)
                ms_arr, ms_time = self.merge_sort(gen_arr3)
                if q_srt:
                    qs_arr, qs_time = self.quick_sort(gen_arr4, 0, qs_r)
            is_runtimes.append(is_time)
            if s_srt:
                ss_runtimes.append(ss_time)
            ms_runtimes.append(ms_time)
            if q_srt:
                qs_runtimes.append(qs_time)
        print("Insertion sort running times:",
              [round(t, 5) for t in is_runtimes])
        if s_srt:
            print("Selection sort running times:",
                  [round(t, 5) for t in ss_runtimes])
        print("Merge sort running times:",
              [round(t, 5) for t in ms_runtimes])
        if q_srt:
            print("Quick sort running times:",
                  [round(t, 5) for t in qs_runtimes])
        return is_runtimes, ss_runtimes, ms_runtimes, qs_runtimes

    def generate_runtimes_i5(self):
        is_runtime_i5 = 0
        ss_runtime_i5 = 0
        ms_runtime_i5 = 0
        qs_runtime_i5 = 0
        for i in range(100000):
            gen_arr_i5_1 = sorting_algos.gen_array(50)
            gen_arr_i5_2 = copy.deepcopy(gen_arr_i5_1)
            gen_arr_i5_3 = copy.deepcopy(gen_arr_i5_1)
            gen_arr_i5_4 = copy.deepcopy(gen_arr_i5_1)
            #            print(gen_arr_i5)
            is_arr_i5, is_time_i5 = self.insertion_sort(gen_arr_i5_1)
            ss_arr_i5, ss_time_i5 = self.selection_sort(gen_arr_i5_2)
            ms_arr_i5, ms_time_i5 = self.merge_sort(gen_arr_i5_3)
            qs_arr_i5, qs_time_i5 = self.quick_sort(gen_arr_i5_4, 0, 49)
            print(qs_time_i5)
            is_runtime_i5 += is_time_i5
            ss_runtime_i5 += ss_time_i5
            ms_runtime_i5 += ms_time_i5
            qs_runtime_i5 += qs_time_i5
        return is_runtime_i5, ss_runtime_i5, ms_runtime_i5, qs_runtime_i5


if __name__ == "__main__":
    sorting_algos = SortingAlgos()

    #Generating runtimes
    print("Input 1")
    is_runtimes_p1, ss_runtimes_p1, ms_runtimes_p1, qs_runtimes_p1 = sorting_algos.generate_runtimes(
            sort=False, avg=True)
    print("Input 2")
    is_runtimes_p2, ss_runtimes_p2, ms_runtimes_p2, qs_runtimes_p2 = sorting_algos.generate_runtimes(
            sort=True, rvs=False, q_srt=False)
    print("Input 3")
    is_runtimes_p3, ss_runtimes_p3, ms_runtimes_p3, qs_runtimes_p3 = sorting_algos.generate_runtimes(
            sort=True, rvs=True, q_srt=False)
    print("Input 4")
    is_runtimes_p4, ss_runtimes_p4, ms_runtimes_p4, qs_runtimes_p4 = sorting_algos.generate_runtimes(
            sort=True, rvs=False, swap=True, avg=True, q_srt=False)
    print("Input 5")
    is_runtimes_p5, ss_runtimes_p5, ms_runtime_p5, qs_runtime_p5 = sorting_algos.generate_runtimes_i5()
    print(is_runtimes_p5, ss_runtimes_p5, ms_runtime_p5, qs_runtime_p5)

    ##Plotting
    sorting_algos.plot_graph(is_runtimes_p1, ss_runtimes_p1, ms_runtimes_p1, qs_runtimes_p1, "input 1")
    sorting_algos.plot_graph("input 2", is_array=is_runtimes_p2, ms_array=ms_runtimes_p2)
    sorting_algos.plot_graph("input 3", is_array=is_runtimes_p3, ms_array=ms_runtimes_p3)
    sorting_algos.plot_graph("input 4", is_array=is_runtimes_p4, ms_array=ms_runtimes_p4)
    print("Total insertion sort running time for input 5:",
          round(is_runtimes_p5, 5))
    print("Total selection sort running time for input 5:",
          round(ss_runtimes_p5, 5))
    print("Total merge sort running time for input 5:",
          round(ms_runtime_p5, 5))
    print("Total quick sort running time for input 5:",
          round(qs_runtime_p5, 5))
