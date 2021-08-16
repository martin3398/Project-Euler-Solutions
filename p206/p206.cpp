#include <iostream>
#include <regex>

using std::endl;
using std::cout;
using std::regex;

int main(void) {
	unsigned long long n = 1010101010;
	unsigned long long x = n*n;

	regex reg("1.2.3.4.5.6.7.8.9.0");

	bool found = false;

	while(!found) {
		x += 20*n + 100;
		n += 10;
		found = regex_match(std::to_string(x), reg);
	}

	cout << n << endl;
}