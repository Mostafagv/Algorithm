"""

https://leetcode.com/discuss/interview-question/304113/google-interview-question-min-time-to-build-all-blocks


A worker can either split into two worker or build a block then dies. Both decisions cost some time.

Given a list blocks, where blocks[i] = k stands for i-th block's building time is k, and cost -
the time cost of spliting one worker. Output the shortest time needed to build all blocks.

Initially there is only one worker.


Input: blocks = [1], cost = 1
Output: 1
Explanation: The worker should build the block instead of splitting into two workers, the answer is 1

Input: blocks = [1, 2], cost = 5
Output: 7
Explanation: The worker should split into two workers (costs 5 time unit), then build two blocks.
The answer is 5 + max(1, 2) = 7.
If the first step is to build a block, the task won't be finished.

Input: blocks = [1, 2, 3], cost = 1
Output: 4
Explanation: The worker splits into 2 workers, then one worker builds blocks[2], one splits, lastly
we have three workers building blocks simultaneously.
The answer is 1 + 1 + max(1, 2, 3 - 1) = 4
There is a 3 - 1 because one worker starts building blocks[2] = 3 from the second step, which lasts
1 time unit (i.e. the splitting time cost).

"""
import numpy as np


def min_build(blocks, cost):
    """
    step
    max_build
    count_split
    count_workers
    """
    # ==================
    # initial
    # ==================
    step = 0
    max_build = 0
    count_split = 0
    count_workers = 1
    end_build = [None for i in range(len(blocks))]
    # ==================
    # step 1
    # ==================
    t = 0
    c1 = helper(count_workers, blocks, 0, cost)
    print('-' * 10, 'result')
    # initial build
    print(c1)
    return c1


def helper(count_workers_, blocks_, time_, cost_):
    print('-' * 10 + '\n', "worker: {}, block: {}, time: {}, cost:{}".format(count_workers_, blocks_, time_, cost_))
    if len(blocks_) == 0:
        print('condition 1',time_)
        return time_
    if count_workers_ >= len(blocks_):
        print('condition 2',time_ + blocks_[-1])
        return time_ + blocks_[-1]
    if count_workers_ == 0 and len(blocks_) > 0:
        print('condition 3', 'inf')
        return float('inf')

    cost = float('inf')

    for _split_ in range(count_workers_ + 1):
        if count_workers_ != _split_:
            cost = max(min(cost, helper(_split_ * 2,
                                        blocks_[:-count_workers_ + _split_],
                                        time_+cost_,
                                        cost_
                                        )
                           )
                       , time_+blocks_[-1]
                       )
        else:
            cost = min(cost, helper(_split_ * 2,
                                        blocks_,
                                        time_+ cost_,
                                        cost_
                                        )
                           )
    print(cost)
    return cost


if __name__ == "__main__":
    # print('test 1: ', min_build([1], 1) == 1)
    # print('test 2: ', min_build([1, 2], 5) == 7)
    # print('test 3: ', min_build([1, 2, 3], 1) == 4)
    print('test 3: ', min_build([1, 2, 3], 5) == 12)
