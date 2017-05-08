#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	struct NumsWithIndex{
		int number;
		int index;
	};
	static bool comparison(NumsWithIndex a, NumsWithIndex b) {
		return a.number<b.number;
	}
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<NumsWithIndex> nums_with_index;
		NumsWithIndex tmp;
		for (int i = 0; i < nums.size(); i++)
		{
			tmp.index = i;
			tmp.number = nums[i];
			nums_with_index.push_back(tmp);
		}
		// 对结果进行排序
		sort(nums_with_index.begin(), nums_with_index.end(), comparison);

		vector<int> result;
		int begin = 0;
		int end = nums_with_index.size() - 1;
		while (begin <= end)
		{
			if (nums_with_index[begin].number + nums_with_index[end].number == target)
			{
				result.push_back(nums_with_index[begin].index);
				result.push_back(nums_with_index[end].index);
				return result;
			}
			if (nums_with_index[begin].number + nums_with_index[end].number>target)
			{
				end -= 1;
			}
			else{
				begin += 1;
			}
		}
		return result;
	}
};









int main() {
	int  v1[] = {2,7,11,15 };
	int len = (sizeof(v1) / sizeof(v1[0]));
	vector<int> nums;
	for (int i = 0; i<len; i++)
	{
		nums.push_back(v1[i]);//增加一个元素
	}
	int target = 9;
	Solution test;
	vector<int> a;
	a = test.twoSum(nums, target);
	cout << a[0] << "  " << a[1];
}