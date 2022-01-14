'''
Largest Palindrome Product:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

/*
 *
 * Find the last occurrence of the longest substring without repeating characters.
 * You are asked to implement the functions printOutput() and longestSubstring() as specified below.
 *
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

#define MAX_LENGTH 1000      // the max allowed input string length


struct Result {             // the structure used to store the function output
	int start;              // the start position of the longest substring
	int length;             // the length of the longest substring
};

//-------------------------- functions to be implemented by you

/*
 * Given a c-string str, find the last occurrence of the longest substring without repeating characters.
 *
 * Return a Result object having the start position and the length of the longest substring.
 *
 * Time Complexity Requirement: O(n)
 *
 */

Result longestSubstring(char* str) {

	int start = 0, end = 1;
	int n = strlen(str);
	bool done[256];
	for (int i = 0; i < 256; i++) {
		done[i] = false;
	}
	int ans = 0;
	int idx = n - 1;
	done[str[0]] = true;
	for (int start = 0; start < n; start++) {
		while (end < n && !done[str[end]]) {
			done[str[end]] = true;
			end++;
		}
		if (end - start >= ans) {
			idx = start;
			ans = end - start;
		}
		done[str[start]] = false;
	}
	Result a;
	a.start = idx;
	a.length = ans;
	return a;



}


/*
* A helper function to format and print the output.
*/
void printOutput(int caseNo, char* str, Result result) {

	cout << "Case " << caseNo << endl;
	cout << "The Length is " << result.length<< endl;
	cout << "The substring is ";
		for (int i = result.start; i < result.start + result.length; i++)
		{
			cout << str[i];
		}
		cout << endl;
		cout << endl;

}


//-------------------------- functions prepared for you

/*
 * Driver program
 *
 * Read the test cases from the input file and use them to test
 * your implementation of longestSubstring().
 *
 */
int main(int argc, char** argv) {
	char str[MAX_LENGTH]; // buffer

	ifstream fin("tut02_input.txt");
	if (!fin) {
		cout << "Input file not found.";
		exit(1);
	}

	int testcase = 0;
	fin >> testcase;

	for (int i = 0; i < testcase; i++) {
		fin >> str;
		printOutput(i + 1, str, longestSubstring(str));
	}

	return 0;

}