#include <iostream>
#include <stdio.h>
#include <vector>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;
//6. ZigZag Conversion


class Solution {
public:
	string convert(string s, int numRows) {
		vector<string> zigRow;
		string result = "";
		int k = 2 * numRows - 2;
		//三行
		for (int i = 0; i < numRows; i++)
		{
			zigRow.push_back("");
		}
		for (int i = 0; i < s.size(); i++)
		{
			int row = i%k;
			if (row >= numRows)
			{
				row = k - row;
			}
			zigRow[row] += s[i];
		}
		for (int i = 0; i < numRows; i++)
		{
			result += zigRow[i];
		}
		return result;
	}
};


int main()
{
	Solution test;
	string s1 = "PAYPALISHIRING";
	string s = "";
	string result = test.convert(s1, 100);
	cout << result << endl;
	return 0;
}