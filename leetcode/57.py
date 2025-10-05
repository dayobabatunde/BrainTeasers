# Given array of non-overlapping intervals srted in asceding rder
# intervals[i] = [starti, endi]
# Given array of length 2, newInterval
# Start of interval is always less than end

# Insert newInterval int intervals maintaining the correct order

def insertInterval(intervals, newInterval):

    newIntervals = []
    added = False
    start = newInterval[0]
    end = newInterval[1]

    # newinterval can be its own interval
    # it can start in another interval and/or end in another interval

    for interval in intervals:
        if not added:
            # interval to add is before current
            if start < interval[0] and end < interval[0]:
                newIntervals.append([start, end])
                newIntervals.append(interval)
                added = True
            # interval to add is in current
            elif start >= interval[0] and end <= interval[1]:
                newIntervals.append(interval)
                added = True
            # interval to add includes current
            elif start < interval[0] and end > interval[1]:
                continue
            # interval to add ends within current
            elif start < interval[0] and interval[0] <= end <= interval[1]:
                end = interval[1]
            # interval to add starts within current 
            elif interval[0] <= start <= interval[1] and end > interval[1]:
                start = interval[0]
            else:
                newIntervals.append(interval)
        else:
            newIntervals.append(interval)
    
    if not added:
        newIntervals.append([start, end])

    intervals = newIntervals
    return intervals

def test():
    assert insertInterval([[3,5]], [1,2]) == [[1,2], [3,5]]
    assert insertInterval([[3,5], [7,8], [10,12]], [4,7]) == [[3,8],[10,12]]
    assert insertInterval([[3,5], [7,8]], [1,10]) == [[1,10]]
    assert insertInterval([[3,5], [7,10]], [8,9]) == [[3,5], [7,10]]
    assert insertInterval([[3,5], [7,10]], [1,3]) == [[1,5], [7,10]]
    
    print("All tests passed")

test()