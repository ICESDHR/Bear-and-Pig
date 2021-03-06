class xiaomiInterview(object):
    def groove(self, lists):
        if len(lists) <= 2:
            return 0
        maxHeight = max(lists)
        if maxHeight < 1:
            return 0
        maxIndex = lists.index(maxHeight)
        left = []
        right = []
        self.leftGroove(lists[:maxIndex], left)
        self.rightGroove(lists[maxIndex + 1:], right)
        return sum(left) + sum(right)

    def leftGroove(self, lists, water):
        if len(lists) < 2:
            return
        maxHeight = max(lists)
        if maxHeight < 1:
            return
        maxIndex = lists.index(maxHeight)
        water.append(sum([maxHeight - h for h in lists[maxIndex + 1:]]))
        self.leftGroove(lists[:maxIndex], water)

    def rightGroove(self, lists, water):
        if len(lists) < 2:
            return
        maxHeight = max(lists)
        if maxHeight < 1:
            return
        maxIndex = lists.index(maxHeight)
        water.append(sum([maxHeight - h for h in lists[:maxIndex]]))
        self.rightGroove(lists[maxIndex + 1:], water)


if __name__ == "__main__":
    soulution = xiaomiInterview()
    print(soulution.groove([5, 1, 2, 4, 3, 1, 3, 2, 1, 1]))
