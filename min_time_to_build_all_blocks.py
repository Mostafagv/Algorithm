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
    step = 0
    c1 = helper(count_workers + 1, blocks, step + 1)
    c2 = helper(count_workers - 1, blocks[:-1], step + 1) + blocks[-1]
    # print('-' * 10, 'result')
    # print(c1, c2)
    critical_path = min(c1, c2)
    extra_split = max(critical_path - len(blocks), 0)
    critical_path = critical_path - extra_split + extra_split * cost

    return critical_path


def helper(count_workers_, blocks_, step_):
    # print('-' * 10 + '\n', count_workers_, blocks_, step_)
    if len(blocks_) == 0:
        # print(0)
        return 0 + step_ - 1
    if count_workers_ >= len(blocks_):
        # print(step_ + blocks_[-1])
        return step_ + blocks_[-1]
    if count_workers_ == 0 and len(blocks_) > 0:
        # print('inf')
        return float('inf')

    cost = float('inf')

    for _split_ in range(count_workers_ + 1):
        if -count_workers_ + _split_ < 0:
            cost = max(min(cost, helper(_split_ * 2,
                                        blocks_[:-count_workers_ + _split_],
                                        step_ + 1
                                        )
                           ),
                       step_ + blocks_[-1]
                       )
        else:
            cost = max(min(cost, helper(_split_ * 2,
                                        [],
                                        step_ + 1
                                        )
                           ),
                       step_ + blocks_[-1]
                       )
    # print(cost)
    return cost


if __name__ == "__main__":
    print('test 1: ', min_build([1], 1) == 1)
    print('test 2: ', min_build([1, 2], 5) == 7)
    print('test 3: ', min_build([1, 2, 3], 1) == 4)
