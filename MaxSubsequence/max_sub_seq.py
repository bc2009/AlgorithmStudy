# from __future__ import print_function
def max_sub_seq(arr):
    if not arr:
        return []
    start = 0
    end = 0
    S = None
    max_s = None
    min_s=None
    for idx, v in enumerate(arr):
        # print(idx, v)
        if S is None:
            S = v
            min_s=max_s = v
            end = idx
        else:
            S += v
            if (S >= max_s):
                end = idx
                max_s = S
                
            if S < min_s:
                if end<idx:
                    # print(arr[start+1: end+1])
                    end=idx
                    max_s=S
                min_s=S
                start=idx
                
            # print('end:', end, ', S: ', S)

    # print('intermediate: ', arr[start+1:end+1])

    # print(start, end)
    if start==0 and arr[0]>=0:
        return arr[start:end+1]
    else:
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

def mytest(arr):
    print(max_sub_seq(arr))
    print(max_sub_seq_simp(arr))
    print('###############')

if __name__ == '__main__':
    mytest([1,1,   -2, 3])
    mytest([-2,1,-3, -4,-1,2,1,-5,4])
    mytest([-2,1,-3, 4,-1,2,1,-5,4])
    mytest([-2,-3,1,-3, -4,-1,2,1,-5,4])
    mytest([4,1,1,-2,3])
    pass
