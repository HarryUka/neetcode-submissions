# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        


        def merge_sort(arr,start,end):
            if (end - start + 1) <= 1:
                return arr

            mid = (end + start) // 2

            merge_sort(arr,start,mid)
            merge_sort(arr, mid + 1, end)

            merge(arr,start,mid,end)
            return arr


        def merge(arr,start,mid,end):
            left_half = arr[start:mid + 1]
            right_half = arr[mid + 1:end + 1]



            p = start
            p1 = 0 
            p2 = 0 


            while p1 < len(left_half) and p2 < len(right_half):
                if left_half[p1].key <= right_half[p2].key:
                    arr[p] = left_half[p1]
                    p1 += 1
                else:
                    arr[p] = right_half[p2]
                    p2 += 1
                p += 1
            
            while p1 < len(left_half):
                arr[p] = left_half[p1]
                p1 += 1
                p += 1
            while p2 < len(right_half):
                arr[p] = right_half[p2]
                p2 += 1
                p += 1

        return merge_sort(pairs,0,len(pairs)-1)


                




