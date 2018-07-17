#! /usr/bin/env python3

################################################################################
########################### Class for Peak Problems ############################
################################################################################

class PeakProblem(object):
    """
    A class representing an instance of a peak-finding problem.
    """

    def __init__(self, array, bounds):
        """
        A method for initializing an instance of the PeakProblem class.
        Takes an array and an argument indicating which rows to include.
        RUNTIME: O(1)
        """

        (startRow, startCol, numRow, numCol) = bounds

        self.array = array
        self.bounds = bounds
        self.startRow = startRow
        self.startCol = startCol
        self.numRow = numRow
        self.numCol = numCol

    def get(self, location):
        """
        Returns the value of the array at the given location, offset by
        the coordinates (startRow, startCol).
        RUNTIME: O(1)
        """

        (r, c) = location
        if not (0 <= r and r < self.numRow):
            return 0
        if not (0 <= c and c < self.numCol):
            return 0
        return self.array[self.startRow + r][self.startCol + c]

    def getBetterNeighbor(self, location):
        """
        If (r, c) has a better neighbor, return the neighbor.  Otherwise,
        return the location (r, c).
        RUNTIME: O(1)
        """

        (r, c) = location
        best = location

        if r - 1 >= 0 and self.get((r - 1, c)) > self.get(best):
            best = (r - 1, c)
        if c - 1 >= 0 and self.get((r, c - 1)) > self.get(best):
            best = (r, c - 1)
        if r + 1 < self.numRow and self.get((r + 1, c)) > self.get(best):
            best = (r + 1, c)
        if c + 1 < self.numCol and self.get((r, c + 1)) > self.get(best):
            best = (r, c + 1)

        return best
    
    def getMaximum(self, locations):
        """
        Finds the location in the current problem with the greatest value.
        RUNTIME: O(len(locations))
        """
   
        (bestLoc, bestVal) = (None, 0)

        for loc in locations:
            if bestLoc is None or self.get(loc) > bestVal:
                (bestLoc, bestVal) = (loc, self.get(loc))

        return bestLoc

    def isPeak(self, location):
        """
        Returns true if the given location is a peak in the current subproblem.
        RUNTIME: O(1)
        """

        return (self.getBetterNeighbor(location) == location)

    def getSubproblem(self, bounds):
        """
        Returns a subproblem with the given bounds.  The bounds is a quadruple
        of numbers: (starting row, starting column, # of rows, # of columns).
        RUNTIME: O(1)
        """

        (sRow, sCol, nRow, nCol) = bounds
        newBounds = (self.startRow + sRow, self.startCol + sCol, nRow, nCol)
        return PeakProblem(self.array, newBounds)

    def getSubproblemContaining(self, boundList, location):
        """
        Returns the subproblem containing the given location.  Picks the first
        of the subproblems in the list which satisfies that constraint, and
        then constructs the subproblem using getSubproblem().
        RUNTIME: O(len(boundList))
        """

        (row, col) = location
        for (sRow, sCol, nRow, nCol) in boundList:
            if sRow <= row and row < sRow + nRow:
                if sCol <= col and col < sCol + nCol:
                    return self.getSubproblem((sRow, sCol, nRow, nCol))

        # shouldn't reach here
        return self

    def getLocationInSelf(self, problem, location):
        """
        Remaps the location in the given problem to the same location in
        the problem that this function is being called from.
        RUNTIME: O(1)
        """

        (row, col) = location
        newRow = row + problem.startRow - self.startRow
        newCol = col + problem.startCol - self.startCol
        return (newRow, newCol)

################################################################################
################################## Algorithms ##################################
################################################################################

def algorithm1(problem):
    """
    RUNTIME: O(NlogN)
    """
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    # the recursive subproblem will involve half the number of columns
    mid = problem.numCol // 2

    # information about the two subproblems
    (subStartR, subNumR) = (0, problem.numRow)
    (subStartC1, subNumC1) = (0, mid)
    (subStartC2, subNumC2) = (mid + 1, problem.numCol - (mid + 1))

    subproblems = []
    subproblems.append((subStartR, subStartC1, subNumR, subNumC1))
    subproblems.append((subStartR, subStartC2, subNumR, subNumC2))

    # get a list of all locations in the dividing column
    divider = crossProduct(range(problem.numRow), [mid])

    # find the maximum in the dividing column
    bestLoc = problem.getMaximum(divider)

    # see if the maximum value we found on the dividing line has a better
    # neighbor (which cannot be on the dividing line, because we know that
    # this location is the best on the dividing line)
    neighbor = problem.getBetterNeighbor(bestLoc)

    # this is a peak, so return it
    if neighbor == bestLoc:
        return bestLoc
   
    # otherwise, figure out which subproblem contains the neighbor, and
    # recurse in that half
    sub = problem.getSubproblemContaining(subproblems, neighbor)

    result = algorithm1(sub)
    return problem.getLocationInSelf(sub, result)

def algorithm2(problem, location = (0, 0)):
    """
    RUNTIME: O(N^2)
    """
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    nextLocation = problem.getBetterNeighbor(location)

    if nextLocation == location:
        # there is no better neighbor, so return this peak
        return location
    else:
        # there is a better neighbor, so move to the neighbor and recurse
        return algorithm2(problem, nextLocation)

def algorithm3(problem, bestSeen = None, rowSplit = True):
    """
    RUNTIME: O(N)
    """
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    subproblems = []
    divider = []

    if rowSplit:
        # the recursive subproblem will involve half the number of rows
        mid = problem.numRow // 2

        # information about the two subproblems
        (subStartR1, subNumR1) = (0, mid)
        (subStartR2, subNumR2) = (mid + 1, problem.numRow - (mid + 1))
        (subStartC, subNumC) = (0, problem.numCol)

        subproblems.append((subStartR1, subStartC, subNumR1, subNumC))
        subproblems.append((subStartR2, subStartC, subNumR2, subNumC))

        # get a list of all locations in the dividing column
        divider = crossProduct([mid], range(problem.numCol))
    else:
        # the recursive subproblem will involve half the number of columns
        mid = problem.numCol // 2

        # information about the two subproblems
        (subStartR, subNumR) = (0, problem.numRow)
        (subStartC1, subNumC1) = (0, mid)
        (subStartC2, subNumC2) = (mid + 1, problem.numCol - (mid + 1))

        subproblems.append((subStartR, subStartC1, subNumR, subNumC1))
        subproblems.append((subStartR, subStartC2, subNumR, subNumC2))

        # get a list of all locations in the dividing column
        divider = crossProduct(range(problem.numRow), [mid])

    # find the maximum in the dividing row or column
    bestLoc = problem.getMaximum(divider)
    neighbor = problem.getBetterNeighbor(bestLoc)

    # update the best we've seen so far based on this new maximum
    if bestSeen is None or problem.get(neighbor) > problem.get(bestSeen):
        bestSeen = neighbor

    # return when we know we've found a peak
    if neighbor == bestLoc and problem.get(bestLoc) >= problem.get(bestSeen):
        return bestLoc

    # figure out which subproblem contains the largest number we've seen so
    # far, and recurse, alternating between splitting on rows and splitting
    # on columns
    sub = problem.getSubproblemContaining(subproblems, bestSeen)
    newBest = sub.getLocationInSelf(problem, bestSeen)
    result = algorithm3(sub, newBest, not rowSplit)
    return problem.getLocationInSelf(sub, result)


################################################################################
################################ Helper Methods ################################
################################################################################


def crossProduct(list1, list2):
    """
    Returns all pairs with one item from the first list and one item from 
    the second list.  (Cartesian product of the two lists.)
    The code is equivalent to the following list comprehension:
        return [(a, b) for a in list1 for b in list2]
    but for easier reading and analysis, we have included more explicit code.
    """

    answer = []
    for a in list1:
        for b in list2:
            answer.append ((a, b))
    return answer

def getDimensions(array):
    """
    Gets the dimensions for a two-dimensional array.  The first dimension
    is simply the number of items in the list; the second dimension is the
    length of the shortest row.  This ensures that any location (row, col)
    that is less than the resulting bounds will in fact map to a valid
    location in the array.
    RUNTIME: O(len(array))
    """

    rows = len(array)
    cols = 0
    
    for row in array:
        if len(row) > cols:
            cols = len(row)
    
    return (rows, cols)

def createProblem(array):
    """
    Constructs an instance of the PeakProblem object for the given array,
    using bounds derived from the array using the getDimensions function.
   
    RUNTIME: O(len(array))
    """

    (rows, cols) = getDimensions(array)
    return PeakProblem(array, (0, 0, rows, cols))


def generate(size, peak = None):

    if size < 1:
        print('Size must be > 0')
        return -1

    problemMatrix = [[0 for _ in range(size)] for __ in range(size)]

    if not peak:
        peak_r, peak_c = size // 2, size // 2
    else:
        peak_r, peak_c = peak
        if peak_r >= size or peak_c >= size:
            print('Peak location must be between 0 and', size)
            return -1

    mx = size + 1
    

    problemMatrix[peak_r][peak_c] = mx

    # def pr(pm):
    #     for p in pm:
    #         print(p) 

    # pr(problemMatrix)

    mn = mx - peak_r - peak_c
    for r in range(len(problemMatrix)):
        # print('------------------------------------------')
        
        val = mn
        for c in range(len(problemMatrix)):
            problemMatrix[r][c] = val
            if c < peak_c:
                val += 1
            else:
                val -= 1

        if r < peak_r:
            mn += 1
        else:
            mn -= 1
        val = mn
        # pr(problemMatrix)


    return problemMatrix, (peak_r, peak_c)





if __name__ == '__main__':

    import time

    def time_ms():
        return time.time() * 1000

    # problemMatrix = [
    # [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
    # [ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
    # [ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
    # [ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
    # [ 8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
    # [ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
    # [ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
    # [ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
    # [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
    # [ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
    # [ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
    # ]

    size = 10
    peak = (size // 2 + 1, size // 2 - 1)
    problemMatrix, exp_peak = generate(size, peak)


    algorithms = ['algorithm1', 'algorithm2', 'algorithm3']

    print('Problem size', size, 'Peak at', exp_peak)

    for algorithm in algorithms:
        if algorithm in globals():
            problem = createProblem(problemMatrix)
            start = time_ms()
            try:
                ans = globals()[algorithm](problem)
            except RecursionError:
                print(algorithm, ': RecursionError')
                continue
            
            warn = ''
            if ans != exp_peak:
                warn = '!'

            print(algorithm, ':', ans, time_ms() - start, '(ms)', warn)
        else:
            print('Couldnt find:', algorithm)

# Algorithms comparison

# Problem size 10 Peak at (6, 4)
# algorithm1 : (6, 4) 0.14111328125 (ms) 
# algorithm2 : (6, 4) 0.099365234375 (ms) 
# algorithm3 : (6, 4) 0.1484375 (ms)

# Problem size 100 Peak at (60, 40)
# algorithm1 : (60, 40) 1.058349609375 (ms)
# algorithm2 : (60, 40) 2.707275390625 (ms)
# algorithm3 : (60, 40) 0.547119140625 (ms)

# Problem size 1000 Peak at (600, 400)
# algorithm1 : (600, 400) 24.24267578125 (ms)
# algorithm2 : RecursionError
# algorithm3 : (600, 400) 4.545166015625 (ms)

# Problem size 10000 Peak at (5100, 4900) 
# algorithm1 : (5100, 4900) 136642.79614257812 (ms) 
# algorithm2 : RecursionError
# algorithm3 : (5100, 4900) 69.58447265625 (ms) 

