# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    """
    Restate: Find the indexes of adjacent numbers that add up to the target in a list, where the first one is smaller than the next.
    Example: nums = [1, 2, 3, 5, 7, 8] --> two_sum(nums, 12)

    Assuming that all elements in the list are some form of a number type value.

    Loop through each index of i from 0 to the length of the lists.

    And for every i, add and check j which would add each element of the list one at a time
    to see if it equals to the target.

    Return the first solution found
    """
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    if len(nums) == 0:
        return 0

    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # This is the easiest way, but the longest for bigger lists as it checks each element and uses a nested loop


def max_profit(prices):
    # Outline:
    """
    Restate: Create a function that would take a list that would buy at an earlier index and sell at a later index to earn the greatest profit.
    Return 0 if no profit.

    Example: [6, 8, 1, 3, 0] --> Returns 2 (Buy at 6, sell at 8)
    """
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    # max_profit([7, 1, 5, 3, 6, 4])   # returns 5   (buy at 1, sell at 6)
    # max_profit([7, 6, 4, 3, 1])      # returns 0   (prices only fall)

    if len(prices) == 0:
        return 0

    lowest_price = prices[0]
    highest_profit = 0

    for price in prices:
        profit = price - lowest_price

        # If we calculated a new higher profit, update the variable
        if profit > highest_profit:
            highest_profit = profit

        # If the current price is lower than the recorded lowest price update the variable
        if price < lowest_price:
            lowest_price = price

    return highest_profit
    """
    The obvious brute force way here is to compare each and every profit made using nested for loops similar to the two_sum function
    It would be much faster this way -- Looping through the list once and keeping track of the highest  profit made.
    """


def max_subarray(nums):
    # Outline:
    #   ...
    """
    Restate: Find the subarray that gives the highest sum of consecutive numbers in a given list

    Example: max_subarray([1,2,3,-1,2,-3]) --> Returns 7 from [1,2,3,-1,2]

    We can use a nested for loop or a recursion case where it takes the whole list first and take the last element out each time
    Saving it if the group renders a high sum.
    """
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.

    if len(nums) == 0:
        return 0

    max_sum = nums[0]
    startIndex = 0
    endIndex = 0

    for i in range(len(nums)):  # The beggining of the block of numbers
        current_sum = 0
        for j in range(i, len(nums)):  # The end of the block of numbers  --  Range(start(included), end(excluded))
            current_sum += nums[j]  # Takes the value of i on the outside loop and adds it too
            if current_sum > max_sum:
                max_sum = current_sum
                startIndex = i
                endIndex = j
    #print(nums[startIndex:endIndex + 1])
    return max_sum





def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
