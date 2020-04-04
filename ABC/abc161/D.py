from heapq import heapify, heappop, heappush, heappushpop

def next_int(n):
    nums = {0: [0, 1],
            1: [0, 1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9]}
    return nums[n]


K = int(input())
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heapify(queue)
for _ in range(K-1):
    now = heappop(queue)  # 最小値を取り出す
    for next_i in next_int(int(str(now)[-1])):
        heappush(queue, int(str(now)+str(next_i)))

print(heappop(queue))