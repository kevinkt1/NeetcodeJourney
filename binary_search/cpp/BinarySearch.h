#include <iostream>
#include <vector>

bool binarySearch(std::vector<int> array, int target)
{
	int low = 0;
	int high = array.size() - 1;

	while (low <= high)
	{
		int mid = low + (high - low) / 2;

		if (target < array.at(mid))
		{
			high = mid - 1;
		}

		else if (target > array.at(mid))
		{
			low = mid + 1;
		}

		else
		{
			return true;
		}
	}

	return false;
}
