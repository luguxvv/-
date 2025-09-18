def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    pos = m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[pos] = nums1[i]
            i -= 1
        else:
            nums1[pos] = nums2[j]
            j -= 1
        pos -= 1
