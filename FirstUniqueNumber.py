# You have a queue of integers, you need to retrieve the first unique integer in the queue.
#
# Implement the FirstUnique class:
#    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
#    int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if
#        there is no such integer
#    void add(int value) insert value to the queue.
#
# Example 1:
# Input:
# ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
# [[[2, 3, 5]], [], [5], [], [2], [], [3], []]
# Output:
# [null, 2, null, 2, null, 3, null, -1]
#
# Explanation:
#   FirstUnique firstUnique = new FirstUnique([2,3,5]);
#   firstUnique.showFirstUnique(); // return 2
#   firstUnique.add(5);            // the queue is now [2,3,5,5]
#   firstUnique.showFirstUnique(); // return 2
#   firstUnique.add(2);            // the queue is now [2,3,5,5,2]
#   firstUnique.showFirstUnique(); // return 3
#   firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
#   firstUnique.showFirstUnique(); // return -1
#
# Example 2:
# Input:
# ["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
# [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]
# Output:
# [null, -1, null, null, null, null, null, 17]
#
# Explanation:
# FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
# firstUnique.showFirstUnique(); // return -1
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
# firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
# firstUnique.showFirstUnique(); // return 17
#
#
# Example 3:
# Input:
# ["FirstUnique", "showFirstUnique", "add", "showFirstUnique"]
# [[[809]], [], [809], []]
# Output:
# [null, 809, null, -1]
#
# Explanation:
# FirstUnique firstUnique = new FirstUnique([809]);
# firstUnique.showFirstUnique(); // return 809
# firstUnique.add(809);          // the queue is now [809,809]
# firstUnique.showFirstUnique(); // return -1
#
#
# Constraints:
#
#     1 <= nums.length <= 10^5
#     1 <= nums[i] <= 10^8
#     1 <= value <= 10^8
#     At most 50000 calls will be made to showFirstUnique and add.
from collections import Counter


class FirstUnique:
    def __init__(self, nums):
        self.all_ctr = Counter(nums)
        self.unique_ctr = {k: v for k, v in Counter(nums).items() if v == 1}

    def show_first_unique(self):
        return next(iter(self.unique_ctr)) if self.unique_ctr else -1

    def add(self, value):
        if value not in self.all_ctr:
            self.all_ctr[value] = 1
            self.unique_ctr[value] = 1
        else:
            self.all_ctr[value] += 1
            if value in self.unique_ctr:
                del self.unique_ctr[value]


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

#   FirstUnique firstUnique = new FirstUnique([2,3,5]);
#   firstUnique.showFirstUnique(); // return 2
#   firstUnique.add(5);            // the queue is now [2,3,5,5]
#   firstUnique.showFirstUnique(); // return 2
#   firstUnique.add(2);            // the queue is now [2,3,5,5,2]
#   firstUnique.showFirstUnique(); // return 3
#   firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
#   firstUnique.showFirstUnique(); // return -1
f = FirstUnique([2, 3, 5])
print(f.show_first_unique())
f.add(5)
print(f.show_first_unique())
f.add(2)
print(f.show_first_unique())
f.add(3)
print(f.show_first_unique())
