#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using std::vector;
using std::ifstream;
using std::cout;
using std::endl;

int main(int argc, char **argv) {
	ifstream in(argv[1]);
	vector<int> weight;
	int a;
    while (in >> a) {
        weight.push_back(a);
    }

	in.close();
	size_t maxDepth = (int) (sqrt(8*weight.size() + 1) - 1)/2;

    vector<int> sum(weight.size());
    for(size_t i = 0; i < sum.size(); i++) {
    	sum[i] = -1;
    }
    sum[0] = weight[0];

    size_t i = 0;
    for(size_t depth = 0; depth < maxDepth - 1; depth++) {
    	for (size_t j = 0; j <= depth; j++) {
    		if (sum[i + depth + 1] < sum[i] + weight[i + depth + 1]) { 
    			sum[i + depth + 1] = sum[i] + weight[i + depth + 1];
    		}
    		if (sum[i + depth + 2] < sum[i] + weight[i + depth + 2]) { 
    			sum[i + depth + 2] = sum[i] + weight[i + depth + 2];
    		}
    		i++;
    	}
    }

    int max = -1;
    for (; i < sum.size(); i++) {
    	if (max < sum[i]) {
    		max = sum[i];
    	}
    }

    cout << max << endl;
	return 0;
}
