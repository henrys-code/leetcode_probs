"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """       
        list = [0] * n
        for i in range(0,n):
            list[i] = str(i+1)     
            if (i+1) % 3 == 0:
                list[i] = 'Fizz'
            if (i+1) % 5 == 0:
                list[i] = 'Buzz'
            if (i+1) % 15 == 0:
                list[i] = 'FizzBuzz'
        return list
