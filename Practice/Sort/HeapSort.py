# -*- coding:utf-8 -*-
<<<<<<< HEAD
# 本代码为建立大根堆
=======
# 本代码为建立小根堆
>>>>>>> b213038ddb736381f05b86a5cde68800622ca9ec

def HeapAdjust(heap,length,i):
    min = i
    if 2*i+1 < length and heap[2*i+1] > heap[min]:
        min = 2*i+1
    if 2*i+2 < length and heap[2*i+2] > heap[min]:
        min = 2*i+2
    if min != i:
        heap[i],heap[min] = heap[min],heap[i]
        HeapAdjust(heap,length,min)


def HeapSort(heap):
<<<<<<< HEAD
    # 构建大根堆
=======
    # 构建小根堆
>>>>>>> b213038ddb736381f05b86a5cde68800622ca9ec
    for i in range(len(heap)//2-1,-1,-1):
        HeapAdjust(heap,len(heap),i)
    # 将根节点取出与最后一位做对调，对前面剩余节点继续进行对调整
    for i in range(len(heap)-1,0,-1):
        heap[0],heap[i] = heap[i],heap[0]
        HeapAdjust(heap,i,0)
    return heap

if __name__ == '__main__':
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    HeapSort(a)
    print(a)

