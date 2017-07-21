def composeRanges(nums):
    start = 0
    group = []
    # you minus one because array index will be inbound
    nums.append("#")

    length = len(nums)

    for index in range(length-1):
        if nums[index] + 1 == nums[index + 1]:
            group.append(str(nums[index]))
        else:
            group.append(str(nums[index]))
            group.append("$")

    rangeGroup = []
    tmp = []
    for i in group:
        if i == "$":
            rangeGroup.append(tmp)
            tmp = []
        else:
            tmp.append(i)

    answerGroup = []
    for innerGroup in rangeGroup:
        if len(innerGroup) == 2:
            string = "->".join(innerGroup)
            answerGroup.append(string)
        else:
            firstElement = innerGroup[0]
            lastElement = innerGroup[len(innerGroup)-1]
            if firstElement == lastElement:
                answerGroup.append(firstElement)
            else:
                string = firstElement + "->" + lastElement
                answerGroup.append(string)
    print("AnswerGroup:", answerGroup)


nums = [-1, 0, 1, 2, 6, 7, 9]
nums1 = [0,1]
nums2 = [0, 1, 3, 4, 5, 6]
nums3 = [7,8]
nums4 = [1,3]
nums5 = [0,8,9]

composeRanges(nums)
composeRanges(nums1)
composeRanges(nums2)
composeRanges(nums3)
composeRanges(nums5)
# print(composeRanges(nums2))
# print(composeRanges(nums3))


