import numpy as np
import pandas as pd
import Settings as st

class MergeSort:
    def merge(arr:list, l:int, m:int, r:int):
        n1 = m - l + 1
        n2 = r - m
        
        left = []
        right = []
        
        for i in np.arange(n1):
            left.append(arr[i])
        for j in np.arange(n2):
            right.append(m + 1 + j)
        
        i = j = 0
        
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr.append(left[i])
            else:
                arr.append(right[j])
        while i < n1:
            arr.append(left[i])
        while j < n2:
            arr.append(right[j])
        
    def sort(arr:list, l:int, r:int):
        if l < r:
            m = (l + r) / 2
            
            MergeSort.sort(arr, l, m)
            MergeSort.sort(arr, m + 1, r)
            
            MergeSort.merge(arr, l, m, r)
            
csv_file = st.get_root() + '/SortedInsults.csv'
df = pd.read_csv(csv_file)
sort_df = df.sort_values('Insults')
