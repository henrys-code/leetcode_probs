/*
 * The Hamming distance between two integers is the number of positions 
 * at which the   corresponding bits are different.
 *
 * Given two integers x and y, calculate the Hamming distance.
 */

class Solution {
public:
    int hammingDistance(int x, int y) {
        int count = 0;
        int index = 0;
        int result = x^y;
        while (index < 32) {
            if ((result >> index) & 0x1 == 1) count++;
            index++;
        }
        return count;
    }
};
