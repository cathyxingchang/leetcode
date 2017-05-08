#include <iostream>
#include <stdio.h>
#include <vector>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;


//11. Container With Most Water

class Solution {
public:
	int maxArea(vector<int>& height) {
		int max_water = 0;
		int currentWater = 0;
		int begin = 0;
		int end = height.size()-1;
		while (begin < end)
		{
			// 水的量是最低的水位*宽度
			currentWater = min(height[begin], height[end])*abs(end-begin);
			if (currentWater > max_water)
			{
				max_water = currentWater;
			}
			else if (height[begin] > height[end])
			{
				end -= 1;
			}
			else
			{
				begin += 1;
			}
		}
		return max_water;
	}
};




int main()
{
	Solution test;
	int a[] = { 1, 2, 3, 5, 6, 2, 1 };
	vector<int> height;
	int len = sizeof(a) / sizeof(a[0]);
	for (int i = 0;i<len;i++)
	{
		height.push_back(a[i]);
	}
	cout<<test.maxArea(height)<<endl;
	return 0;
}