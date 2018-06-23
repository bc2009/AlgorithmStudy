# from __future__ import print_function

''' complexity O(N)
'''

def max_sub_seq(ar):
    if not ar:
        return []
    arr = [0]+ ar
    start = 0
    end = 0
    S = None
    max_s = None
    min_s=None
    current_record=None
    for idx, v in enumerate(arr):
        # print(idx, v)
        if S is None:
            S = v
            min_s=max_s = v
            end = idx
            
            start=0
            current_record = (v, 0, end)
        else:
            S += v
            if (S >= max_s):
                # end = idx
                max_s = S
                # if (start==-1 and max_s >= current_record[0]):
                #     end=idx
                #     current_record = (max_s, start, end)
                # if (start>=0 and max_s - min_s >= current_record[0]):
                    
                if max_s - min_s >= current_record[0]:
                    end=idx
                    current_record = (max_s - min_s, start, end)


            if end<=start:
                if S-min_s >= current_record[0]:
                    # print('before: ', current_record)
                    end=idx
                    current_record = (S-min_s, start, idx)
                    # print('after: ', current_record)
                # print(arr[start+1: end+1])

                    max_s=S
            
            if S < min_s:
                min_s=S
                start=idx
                # current_record = (max_s - min_s, start, end)
                
            # print('end:', end, ', S: ', S)

    # print('intermediate: ', arr[start+1:end+1])

    # print('result: ', current_record)
    start, end = current_record[1:]
    # if start==0 and arr[0]>=0:
    #     return arr[start+1:end+1]
    # else:
    return arr[start+1:end+1]

def max_sub_seq_simp(arr):
    import sys
    S =  sys.float_info.min
    st = None
    ed = None
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            cur_s = sum(arr[i:j])
            if S <= cur_s:
                st = i
                ed = j
                S = cur_s

    return arr[st:ed] or []

# def mytest(arr):
#     print(max_sub_seq(arr))
#     print(max_sub_seq_simp(arr), '--', sum(max_sub_seq_simp(arr)))
#     print('###############')

def mytest(arr):
    print('checking ', arr)
    o = max_sub_seq(arr)
    print('output: ', o)
    o2 = max_sub_seq_simp(arr)
    assert sum(o) == sum(o2), 'Failed on {}!={}'.format(o, o2)
    print('Passed ==> ', o)

if __name__ == '__main__':
    mytest([1,1,   -2, 3])
    mytest([-2,1,-3, -4,-1,2,1,-5,4])
    mytest([-2,1,-3, 4,-1,2,1,-5,4])
    mytest([-2,-3,1,-3, -4,-1,2,1,-5,4])
    mytest([4,1,1,-2,3])
    mytest([-1, -9, 6, -7, 4, -5, -2, 2, -3, -10])
    mytest([4, -3, 6, 2, 9, 2, -10, 9, 9, 3])
    mytest([-6, 9, -9, -10, -4, -6, -4, -9, -2, -1])
    import numpy as np
    for k in range(10000):
        tr = np.random.randint(-10, high=10, size=10)
        if (np.all(tr<=0)):
            continue
        tr=tr.tolist()
        mytest(tr)
    pass
