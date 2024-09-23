#include "BinarySearch.h"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{
	std::vector<int> v = {1};
	assert(binarySearch(v, 1));

	v = {1, 2, 3};
	assert(binarySearch(v, 1));
	assert(binarySearch(v, 2));
	assert(binarySearch(v, 3));

	v = {1, 2, 3, 4};
	assert(binarySearch(v, 4));

	v.clear();
	assert(!binarySearch(v, 1));

	v = {2};
	assert(!binarySearch(v, 1));

	v = {1, 2, 4, 6};
	assert(!binarySearch(v, 0));
	assert(!binarySearch(v, 5));
	assert(!binarySearch(v, 3));

	return 0;
}
