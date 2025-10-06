from django.core.management.base import BaseCommand
from django.db import IntegrityError
from compiler.models import Problem, TestCase

class Command(BaseCommand):
    help = "Imports predefined coding problems into the database"

    def handle(self, *args, **kwargs):
        problems_data = [
            {
                "title": "Two Sum",
                "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
                "difficulty": "Easy",
                "input": "nums = [2,7,11,15], target = 9",
                "output": "[0,1]",
                "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1].",
                "tags": ["array", "hashmap"],
                "constraints": [
                    "2 <= nums.length <= 10^4",
                    "-10^9 <= nums[i] <= 10^9",
                    "Only one valid answer exists."
                ],
                "test_cases": [
                    ("2 7 11 15\n9", "0 1"),
                    ("3 2 4\n6", "1 2"),
                    ("3 3\n6", "0 1"),
                    ("1 2 3 4 5\n9", "3 4"),
                    ("-1 -2 -3 -4 -5\n-8", "2 4"),
                ]
            },
            {
                "title": "Contains Duplicate",
                "description": "Given an integer array, return true if any value appears at least twice in the array, and false otherwise.",
                "difficulty": "Easy",
                "input": "nums = [1,2,3,1]",
                "output": "true",
                "explanation": "The number 1 appears twice.",
                "tags": ["array", "hashset"],
                "constraints": [
                    "1 <= nums.length <= 10^5",
                    "-10^9 <= nums[i] <= 10^9"
                ],
                "test_cases": [
                    ("1 2 3 4", "False"),
                    ("1 1 2 3", "True"),
                    ("", "False"),
                    ("7 7 7 7", "True"),
                    ("10 20 30", "False"),
                ]
            },
            {
                "title": "Valid Anagram",
                "description": "Given two strings s and t, return true if t is an anagram of s, and false otherwise.",
                "difficulty": "Easy",
                "input": "s = 'anagram', t = 'nagaram'",
                "output": "true",
                "explanation": "The string t is a rearrangement of s.",
                "tags": ["hashmap", "string"],
                "constraints": [
                    "1 <= s.length, t.length <= 5 * 10^4",
                    "s and t consist of lowercase English letters."
                ],
                "test_cases": [
                    ("anagram\nnagaram", "true"),
                    ("rat\ncar", "false"),
                    ("a\na", "true"),
                    ("abc\ncba", "true"),
                    ("hello\nworld", "false"),
                ]
            },
            {
                "title": "Group Anagrams",
                "description": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
                "difficulty": "Medium",
                "input": "strs = ['eat','tea','tan','ate','nat','bat']",
                "output": "[['eat','tea','ate'],['tan','nat'],['bat']]",
                "explanation": "The strings are grouped by their anagram patterns.",
                "tags": ["hashmap", "string"],
                "constraints": [
                    "1 <= strs.length <= 10^4",
                    "0 <= strs[i].length <= 100",
                    "strs[i] consists of lowercase English letters."
                ],
                "test_cases": [
                    ("eat tea tan ate nat bat", "[['eat','tea','ate'],['tan','nat'],['bat']]"),
                    ("", "[[]]"),
                    ("a", "[['a']]"),
                    ("cat act dog god", "[['cat','act'],['dog','god']]"),
                    ("abc bca cab", "[['abc','bca','cab']]"),
                ]
            },
            {
                "title": "Top K Frequent Elements",
                "description": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
                "difficulty": "Medium",
                "input": "nums = [1,1,1,2,2,3], k = 2",
                "output": "[1,2]",
                "explanation": "1 appears 3 times, 2 appears 2 times, so they are the top 2 frequent elements.",
                "tags": ["array", "hashmap", "heap"],
                "constraints": [
                    "1 <= nums.length <= 10^5",
                    "k is in the range [1, the number of unique elements in the array]."
                ],
                "test_cases": [
                    ("1 1 1 2 2 3\n2", "1 2"),
                    ("1\n1", "1"),
                    ("4 4 4 4\n1", "4"),
                    ("1 2 3 4\n2", "1 2"),
                    ("5 5 5 6 6 7\n3", "5 6 7"),
                ]
            },
            {
                "title": "Product of Array Except Self",
                "description": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].",
                "difficulty": "Medium",
                "input": "nums = [1,2,3,4]",
                "output": "[24,12,8,6]",
                "explanation": "The product of all elements except self for each position.",
                "tags": ["array"],
                "constraints": [
                    "2 <= nums.length <= 10^5",
                    "-30 <= nums[i] <= 30",
                    "The product fits in a 32-bit integer."
                ],
                "test_cases": [
                    ("1 2 3 4", "24 12 8 6"),
                    ("1 1 1 1", "1 1 1 1"),
                    ("2 3 4 5", "60 40 30 24"),
                    ("0 0 0 0", "0 0 0 0"),
                    ("1 2", "2 1"),
                ]
            },
            {
                "title": "Valid Sudoku",
                "description": "Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to Sudoku rules.",
                "difficulty": "Medium",
                "input": "board = [['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']]",
                "output": "true",
                "explanation": "The board follows Sudoku rules.",
                "tags": ["array", "hashmap"],
                "constraints": [
                    "board.length == 9",
                    "board[i].length == 9",
                    "board[i][j] is a digit 1-9 or '.'."
                ],
                "test_cases": [
                    ("53..7.... 6..195... .98....6. 8...6...3 4..8.3..1 7...2...6 .6....28. ...419..5 ....8..79", "true"),
                    ("53..7.... 6..195... .98....6. 8...6...3 4..8.3..1 7...2...6 .6....28. ...419..5 ....8..79", "true"),
                    ("53..7.... 6..195... .98....6. 8...6...3 4..8.3..1 7...2...6 .6....28. ...419..5 5...8..79", "false"),
                    ("......... ......... ......... ......... ......... ......... ......... ......... .........", "true"),
                    ("1111..... ......... ......... ......... ......... ......... ......... ......... .........", "false"),
                ]
            },
            {
                "title": "Longest Consecutive Sequence",
                "description": "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.",
                "difficulty": "Medium",
                "input": "nums = [100,4,200,1,3,2]",
                "output": "4",
                "explanation": "The longest consecutive sequence is [1,2,3,4].",
                "tags": ["array", "hashset"],
                "constraints": [
                    "0 <= nums.length <= 10^5",
                    "-10^9 <= nums[i] <= 10^9"
                ],
                "test_cases": [
                    ("100 4 200 1 3 2", "4"),
                    ("0 3 7 2 5 8 4 6 0 1", "9"),
                    ("", "0"),
                    ("1", "1"),
                    ("1 2 3 4 5", "5"),
                ]
            },
            {
                "title": "Reverse Linked List",
                "description": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
                "difficulty": "Easy",
                "input": "head = [1,2,3,4,5]",
                "output": "[5,4,3,2,1]",
                "explanation": "The linked list is reversed.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 5000].",
                    "-5000 <= Node.val <= 5000"
                ],
                "test_cases": [
                    ("1 2 3 4 5", "5 4 3 2 1"),
                    ("1", "1"),
                    ("", ""),
                    ("1 2", "2 1"),
                    ("10 20 30", "30 20 10"),
                ]
            },
            {
                "title": "Merge Two Sorted Lists",
                "description": "Merge two sorted linked lists and return it as a sorted list.",
                "difficulty": "Easy",
                "input": "list1 = [1,2,4], list2 = [1,3,4]",
                "output": "[1,1,2,3,4,4]",
                "explanation": "The lists are merged in sorted order.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in both lists is in the range [0, 50].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 4\n1 3 4", "1 1 2 3 4 4"),
                    ("", ""),
                    ("1", "1"),
                    ("1 3\n2 4", "1 2 3 4"),
                    ("5\n5", "5 5"),
                ]
            },
            {
                "title": "Add Two Numbers",
                "description": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
                "difficulty": "Medium",
                "input": "l1 = [2,4,3], l2 = [5,6,4]",
                "output": "[7,0,8]",
                "explanation": "342 + 465 = 807.",
                "tags": ["linked list", "math"],
                "constraints": [
                    "The number of nodes in each linked list is in the range [1, 100].",
                    "0 <= Node.val <= 9",
                    "It is guaranteed that the list represents a number that does not have leading zeros."
                ],
                "test_cases": [
                    ("2 4 3\n5 6 4", "7 0 8"),
                    ("0\n0", "0"),
                    ("1 2 3\n4 5 6", "5 7 9"),
                    ("9 9 9\n1", "0 0 0 1"),
                    ("1\n9 9", "0 0 1"),
                ]
            },
            {
                "title": "Longest Substring Without Repeating Characters",
                "description": "Given a string s, find the length of the longest substring without repeating characters.",
                "difficulty": "Medium",
                "input": "s = 'abcabcbb'",
                "output": "3",
                "explanation": "The answer is 'abc', with the length of 3.",
                "tags": ["string", "sliding window"],
                "constraints": [
                    "0 <= s.length <= 5 * 10^4",
                    "s consists of English letters, digits, symbols and spaces."
                ],
                "test_cases": [
                    ("abcabcbb", "3"),
                    ("bbbbb", "1"),
                    ("pwwkew", "3"),
                    ("", "0"),
                    ("dvdf", "3"),
                ]
            },
            {
                "title": "Median of Two Sorted Arrays",
                "description": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two arrays merged.",
                "difficulty": "Hard",
                "input": "nums1 = [1,3], nums2 = [2,4]",
                "output": "2.5",
                "explanation": "The merged array is [1,2,3,4] and its median is (2 + 3) / 2 = 2.5.",
                "tags": ["array", "binary search"],
                "constraints": [
                    "nums1.length == m",
                    "nums2.length == n",
                    "0 <= m, n <= 1000",
                    "1 <= m + n <= 2000",
                    "-10^6 <= nums1[i], nums2[i] <= 10^6"
                ],
                "test_cases": [
                    ("1 3\n2 4", "2.5"),
                    ("1 2\n3", "2"),
                    ("1 2 3", "2"),
                    ("1 2 3\n4 5 6", "3.5"),
                    ("1\n2", "1.5"),
                ]
            },
            {
                "title": "Regular Expression Matching",
                "description": "Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.",
                "difficulty": "Hard",
                "input": "s = 'aa', p = 'a*'",
                "output": "true",
                "explanation": "'a*' matches any sequence of 'a' including zero.",
                "tags": ["string", "dynamic programming"],
                "constraints": [
                    "1 <= s.length, p.length <= 20",
                    "s contains only lowercase English letters.",
                    "p contains only lowercase English letters, '.', and '*'."
                ],
                "test_cases": [
                    ("aa\na*", "true"),
                    ("aa\na", "false"),
                    ("ab\na*b", "true"),
                    ("mississippi\nmis*is*p*.", "false"),
                    ("aab\nc*a*b", "true"),
                ]
            },
            {
                "title": "Container With Most Water",
                "description": "Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines that together with the x-axis form a container, such that the container contains the most water.",
                "difficulty": "Medium",
                "input": "height = [1,8,6,2,5,4,8,3,7]",
                "output": "49",
                "explanation": "The container formed by lines at index 1 and 8 holds 49 units of water.",
                "tags": ["array", "two pointers"],
                "constraints": [
                    "n == height.length",
                    "2 <= n <= 10^5",
                    "0 <= height[i] <= 10^4"
                ],
                "test_cases": [
                    ("1 8 6 2 5 4 8 3 7", "49"),
                    ("1 1", "1"),
                    ("2 3 4 5", "6"),
                    ("1 2 1", "2"),
                    ("10 9 8 7 6 5 4 3 2 1", "25"),
                ]
            },
            {
                "title": "3Sum",
                "description": "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.",
                "difficulty": "Medium",
                "input": "nums = [-1,0,1,2,-1,-4]",
                "output": "[[-1,-1,2],[-1,0,1]]",
                "explanation": "The triplets that sum to zero are [-1,-1,2] and [-1,0,1].",
                "tags": ["array", "two pointers"],
                "constraints": [
                    "0 <= nums.length <= 3000",
                    "-10^5 <= nums[i] <= 10^5"
                ],
                "test_cases": [
                    ("-1 0 1 2 -1 -4", "[-1 -1 2] [-1 0 1]"),
                    ("0 0 0", "[0 0 0]"),
                    ("1 2 3", ""),
                    ("-2 0 2 1 -1", "[-2 0 2] [-1 0 1]"),
                    ("", ""),
                ]
            },
            {
                "title": "Remove Nth Node From End of List",
                "description": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
                "difficulty": "Medium",
                "input": "head = [1,2,3,4,5], n = 2",
                "output": "[1,2,3,5]",
                "explanation": "Remove the second node from the end, which is 4.",
                "tags": ["linked list", "two pointers"],
                "constraints": [
                    "The number of nodes in the list is sz.",
                    "1 <= sz <= 30",
                    "0 <= Node.val <= 100",
                    "1 <= n <= sz"
                ],
                "test_cases": [
                    ("1 2 3 4 5\n2", "1 2 3 5"),
                    ("1\n1", ""),
                    ("1 2\n1", "1"),
                    ("1 2 3\n3", "2 3"),
                    ("10 20 30 40\n2", "10 20 40"),
                ]
            },
            {
                "title": "Swap Nodes in Pairs",
                "description": "Given a linked list, swap every two adjacent nodes and return its head.",
                "difficulty": "Medium",
                "input": "head = [1,2,3,4]",
                "output": "[2,1,4,3]",
                "explanation": "Swap nodes in pairs: 1->2 becomes 2->1, 3->4 becomes 4->3.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 100].",
                    "0 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 3 4", "2 1 4 3"),
                    ("1", "1"),
                    ("", ""),
                    ("1 2", "2 1"),
                    ("1 2 3", "2 1 3"),
                ]
            },
            {
                "title": "Rotate List",
                "description": "Given the head of a linked list, rotate the list to the right by k places.",
                "difficulty": "Medium",
                "input": "head = [1,2,3,4,5], k = 2",
                "output": "[4,5,1,2,3]",
                "explanation": "Rotate the list to the right by 2 places.",
                "tags": ["linked list", "two pointers"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 500].",
                    "-100 <= Node.val <= 100",
                    "0 <= k <= 10^9"
                ],
                "test_cases": [
                    ("1 2 3 4 5\n2", "4 5 1 2 3"),
                    ("0 1 2\n4", "2 0 1"),
                    ("1\n1", "1"),
                    ("", ""),
                    ("1 2\n1", "2 1"),
                ]
            },
            {
                "title": "Reverse Words in a String",
                "description": "Given an input string s, reverse the order of the words.",
                "difficulty": "Medium",
                "input": "s = 'the sky is blue'",
                "output": "'blue is sky the'",
                "explanation": "Reverse the order of the words in the string.",
                "tags": ["string", "two pointers"],
                "constraints": [
                    "1 <= s.length <= 10^4",
                    "s contains English letters (upper-case and lower-case), digits, and spaces ' '.",
                    "There is at least one word in s."
                ],
                "test_cases": [
                    ("the sky is blue", "blue is sky the"),
                    ("  hello world  ", "world hello"),
                    ("a", "a"),
                    ("  one   word  ", "word one"),
                    ("hello   world", "world hello"),
                ]
            },
            {
                "title": "Zigzag Conversion",
                "description": "The string 'PAYPALISHIRING' is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) P   A   H   N A P L S I I G Y   I   R And then read line by line: 'PAHNAPLSIIGYIR'. Write the code that will take a string and make this conversion given a number of rows.",
                "difficulty": "Medium",
                "input": "s = 'PAYPALISHIRING', numRows = 3",
                "output": "'PAHNAPLSIIGYIR'",
                "explanation": "The string is written in a zigzag pattern and read line by line.",
                "tags": ["string"],
                "constraints": [
                    "1 <= s.length <= 1000",
                    "s consists of English letters (lower-case and upper-case), ',' and '.'.",
                    "1 <= numRows <= 1000"
                ],
                "test_cases": [
                    ("PAYPALISHIRING\n3", "PAHNAPLSIIGYIR"),
                    ("PAYPALISHIRING\n4", "PINALSIGYAHRPI"),
                    ("A\n1", "A"),
                    ("AB\n2", "AB"),
                    ("ABCDE\n4", "ABCDE"),
                ]
            },
            {
                "title": "String to Integer (atoi)",
                "description": "Implement the myAtoi(string s) function that converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).",
                "difficulty": "Medium",
                "input": "s = '42'",
                "output": "42",
                "explanation": "The string '42' is converted to the integer 42.",
                "tags": ["string"],
                "constraints": [
                    "0 <= s.length <= 200",
                    "s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.",
                    "Output is in range [-2^31, 2^31 - 1]."
                ],
                "test_cases": [
                    ("42", "42"),
                    ("   -42", "-42"),
                    ("4193 with words", "4193"),
                    ("words and 987", "0"),
                    ("-91283472332", "-2147483648"),
                ]
            },
            {
                "title": "Integer to Roman",
                "description": "Given an integer, convert it to a roman numeral.",
                "difficulty": "Medium",
                "input": "num = 3",
                "output": "'III'",
                "explanation": "3 is represented as III in Roman numerals.",
                "tags": ["string", "math"],
                "constraints": [
                    "1 <= num <= 3999"
                ],
                "test_cases": [
                    ("3", "III"),
                    ("4", "IV"),
                    ("9", "IX"),
                    ("58", "LVIII"),
                    ("1994", "MCMXCIV"),
                ]
            },
            {
                "title": "Roman to Integer",
                "description": "Given a roman numeral, convert it to an integer.",
                "difficulty": "Easy",
                "input": "s = 'III'",
                "output": "3",
                "explanation": "III is 3 in Roman numerals.",
                "tags": ["string", "math"],
                "constraints": [
                    "1 <= s.length <= 15",
                    "s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').",
                    "It is guaranteed that s is a valid roman numeral in the range [1, 3999]."
                ],
                "test_cases": [
                    ("III", "3"),
                    ("IV", "4"),
                    ("IX", "9"),
                    ("LVIII", "58"),
                    ("MCMXCIV", "1994"),
                ]
            },
            {
                "title": "Longest Common Prefix",
                "description": "Write a function to find the longest common prefix string amongst an array of strings.",
                "difficulty": "Easy",
                "input": "strs = ['flower','flow','flight']",
                "output": "'fl'",
                "explanation": "'fl' is the longest common prefix among the strings.",
                "tags": ["string"],
                "constraints": [
                    "1 <= strs.length <= 200",
                    "0 <= strs[i].length <= 200",
                    "strs[i] consists of only lower-case English letters."
                ],
                "test_cases": [
                    ("flower flow flight", "fl"),
                    ("dog racecar cat", ""),
                    ("interspecies interstellar", "inters"),
                    ("prefix prefix prefix", "prefix"),
                    ("", ""),
                ]
            },
            {
                "title": "Letter Combinations of a Phone Number",
                "description": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.",
                "difficulty": "Medium",
                "input": "digits = '23'",
                "output": "['ad','ae','af','bd','be','bf','cd','ce','cf']",
                "explanation": "Each digit maps to letters (2 -> 'abc', 3 -> 'def'), and all combinations are listed.",
                "tags": ["string", "backtracking"],
                "constraints": [
                    "0 <= digits.length <= 4",
                    "digits[i] is a digit in the range ['2', '9']."
                ],
                "test_cases": [
                    ("23", "ad ae af bd be bf cd ce cf"),
                    ("", ""),
                    ("2", "a b c"),
                    ("7", "p q r s"),
                    ("234", "adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi"),
                ]
            },
            {
                "title": "4Sum",
                "description": "Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that a + b + c + d = 0.",
                "difficulty": "Medium",
                "input": "nums = [1,0,-1,0,-2,2], target = 0",
                "output": "[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]",
                "explanation": "The quadruplets that sum to zero are listed.",
                "tags": ["array", "two pointers"],
                "constraints": [
                    "1 <= nums.length <= 200",
                    "-10^9 <= nums[i] <= 10^9",
                    "-10^9 <= target <= 10^9"
                ],
                "test_cases": [
                    ("1 0 -1 0 -2 2\n0", "[-2 -1 1 2] [-2 0 0 2] [-1 0 0 1]"),
                    ("2 2 2 2\n8", "[2 2 2 2]"),
                    ("1 2 3 4\n10", "[1 2 3 4]"),
                    ("0 0 0 0\n0", "[0 0 0 0]"),
                    ("", ""),
                ]
            },
            {
                "title": "Generate Parentheses",
                "description": "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
                "difficulty": "Medium",
                "input": "n = 3",
                "output": "['((()))','(()())','(())()','()(())','()()()']",
                "explanation": "All valid combinations of 3 pairs of parentheses are listed.",
                "tags": ["string", "backtracking"],
                "constraints": [
                    "1 <= n <= 8"
                ],
                "test_cases": [
                    ("3", "((())) (()()) (())() ()(()) ()()()"),
                    ("1", "()"),
                    ("2", "(()) ()()"),
                    ("4", "(((()))) ((()())) ((())()) ((()))() (()(())) (()()()) (()())() (())()() ()((())) ()(()()) ()(())() ()()(())) ()()()()"),
                    ("0", ""),
                ]
            },
            {
                "title": "Merge k Sorted Lists",
                "description": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
                "difficulty": "Hard",
                "input": "lists = [[1,4,5],[1,3,4],[2,6]]",
                "output": "[1,1,2,3,4,4,5,6]",
                "explanation": "The linked lists are merged into one sorted list.",
                "tags": ["linked list", "heap"],
                "constraints": [
                    "k == lists.length",
                    "0 <= k <= 10^4",
                    "0 <= lists[i].length <= 500",
                    "-10^4 <= lists[i][j] <= 10^4"
                ],
                "test_cases": [
                    ("1 4 5\n1 3 4\n2 6", "1 1 2 3 4 4 5 6"),
                    ("", ""),
                    ("1\n2\n3", "1 2 3"),
                    ("1 2\n3 4", "1 2 3 4"),
                    ("5\n5", "5 5"),
                ]
            },
            {
                "title": "Valid Parentheses",
                "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
                "difficulty": "Easy",
                "input": "s = '()[]{}'",
                "output": "true",
                "explanation": "The string contains valid pairs of parentheses.",
                "tags": ["string", "stack"],
                "constraints": [
                    "1 <= s.length <= 10^4",
                    "s consists of parentheses only '()[]{}'."
                ],
                "test_cases": [
                    ("()[]{}", "true"),
                    ("([)]", "false"),
                    ("{[}", "false"),
                    ("((()))", "true"),
                    ("", "true"),
                ]
            },
            {
                "title": "Trapping Rain Water",
                "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
                "difficulty": "Hard",
                "input": "height = [0,1,0,2,1,0,1,3,2,1,2,1]",
                "output": "6",
                "explanation": "The elevation map can trap 6 units of water.",
                "tags": ["array", "two pointers", "stack"],
                "constraints": [
                    "0 <= height.length <= 3 * 10^4",
                    "0 <= height[i] <= 10^5"
                ],
                "test_cases": [
                    ("0 1 0 2 1 0 1 3 2 1 2 1", "6"),
                    ("4 2 0 3 2 5", "9"),
                    ("1 2 1", "1"),
                    ("", "0"),
                    ("5 5 5 5", "0"),
                ]
            },
            {
                "title": "Jump Game",
                "description": "Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you can reach the last index.",
                "difficulty": "Medium",
                "input": "nums = [2,3,1,1,4]",
                "output": "true",
                "explanation": "You can reach the last index by jumping from index 0 to 1 to 4.",
                "tags": ["array", "greedy"],
                "constraints": [
                    "1 <= nums.length <= 10^4",
                    "0 <= nums[i] <= 10^5"
                ],
                "test_cases": [
                    ("2 3 1 1 4", "true"),
                    ("3 2 1 0 4", "false"),
                    ("1", "true"),
                    ("0", "true"),
                    ("2 0 0", "true"),
                ]
            },
            {
                "title": "Merge Intervals",
                "description": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
                "difficulty": "Medium",
                "input": "intervals = [[1,3],[2,6],[8,10],[15,18]]",
                "output": "[[1,6],[8,10],[15,18]]",
                "explanation": "Intervals [1,3] and [2,6] overlap and are merged into [1,6].",
                "tags": ["array", "sort"],
                "constraints": [
                    "1 <= intervals.length <= 10^4",
                    "intervals[i].length == 2",
                    "0 <= starti <= endi <= 10^4"
                ],
                "test_cases": [
                    ("1 3\n2 6\n8 10\n15 18", "1 6\n8 10\n15 18"),
                    ("1 4\n4 5", "1 5"),
                    ("1 4", "1 4"),
                    ("2 3\n1 4", "1 4"),
                    ("", ""),
                ]
            },
            {
                "title": "Insert Interval",
                "description": "You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval. Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still contains only non-overlapping intervals by merging if needed.",
                "difficulty": "Medium",
                "input": "intervals = [[1,3],[6,9]], newInterval = [2,5]",
                "output": "[[1,5],[6,9]]",
                "explanation": "The new interval [2,5] overlaps with [1,3], so they are merged into [1,5].",
                "tags": ["array"],
                "constraints": [
                    "0 <= intervals.length <= 10^4",
                    "intervals[i].length == 2",
                    "0 <= intervals[i][0] <= intervals[i][1] <= 10^5",
                    "intervals is sorted by intervals[i][0] in ascending order.",
                    "newInterval.length == 2",
                    "0 <= newInterval[0] <= newInterval[1] <= 10^5"
                ],
                "test_cases": [
                    ("1 3\n6 9\n2 5", "1 5\n6 9"),
                    ("1 2\n3 5\n6 7\n8 10\n12 16\n4 8", "1 2\n3 10\n12 16"),
                    ("2 5", "2 5"),
                    ("1 5\n2 3", "1 5"),
                    ("1 5\n6 8", "1 5\n6 8"),
                ]
            },
            {
                "title": "Minimum Window Substring",
                "description": "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ''.",
                "difficulty": "Hard",
                "input": "s = 'ADOBECODEBANC', t = 'ABC'",
                "output": "'BANC'",
                "explanation": "'BANC' is the smallest substring containing all characters of t.",
                "tags": ["string", "sliding window"],
                "constraints": [
                    "1 <= s.length, t.length <= 10^5",
                    "s and t consist of uppercase and lowercase English letters."
                ],
                "test_cases": [
                    ("ADOBECODEBANC\nABC", "BANC"),
                    ("a\na", "a"),
                    ("a\nb", ""),
                    ("abba\nab", "abba"),
                    ("abc\nbc", "bc"),
                ]
            },
            {
                "title": "Sort List",
                "description": "Given the head of a linked list, return the list after sorting it in ascending order.",
                "difficulty": "Medium",
                "input": "head = [4,2,1,3]",
                "output": "[1,2,3,4]",
                "explanation": "The linked list is sorted in ascending order.",
                "tags": ["linked list", "sort"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 5 * 10^4].",
                    "-10^5 <= Node.val <= 10^5"
                ],
                "test_cases": [
                    ("4 2 1 3", "1 2 3 4"),
                    ("-1 5 3 4 0", "-1 0 3 4 5"),
                    ("", ""),
                    ("1", "1"),
                    ("1 2", "1 2"),
                ]
            },
            {
                "title": "Maximal Rectangle",
                "description": "Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.",
                "difficulty": "Hard",
                "input": "matrix = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]",
                "output": "6",
                "explanation": "The largest rectangle of 1's has an area of 6.",
                "tags": ["array", "stack", "dynamic programming"],
                "constraints": [
                    "rows == matrix.length",
                    "cols == matrix[i].length",
                    "1 <= rows, cols <= 200",
                    "matrix[i][j] is '0' or '1'."
                ],
                "test_cases": [
                    ("1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0", "6"),
                    ("0", "0"),
                    ("1", "1"),
                    ("1 1\n1 1", "4"),
                    ("0 0\n0 0", "0"),
                ]
            },
            {
                "title": "Largest Rectangle in Histogram",
                "description": "Given an array of non-negative integers hist, where each element represents the height of a bar in a histogram with width 1, find the area of the largest rectangle in the histogram.",
                "difficulty": "Hard",
                "input": "heights = [2,1,5,6,2,3]",
                "output": "10",
                "explanation": "The largest rectangle has an area of 10 (height 5 over width 2).",
                "tags": ["array", "stack"],
                "constraints": [
                    "1 <= heights.length <= 10^5",
                    "0 <= heights[i] <= 10^4"
                ],
                "test_cases": [
                    ("2 1 5 6 2 3", "10"),
                    ("2 4", "4"),
                    ("0", "0"),
                    ("1 1 1", "3"),
                    ("5 5 5 5", "20"),
                ]
            },
            {
                "title": "Binary Tree Maximum Path Sum",
                "description": "Given a non-empty binary tree, find the maximum path sum. For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.",
                "difficulty": "Hard",
                "input": "root = [1,2,3]",
                "output": "6",
                "explanation": "The maximum path sum is 2 + 1 + 3 = 6.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [1, 3 * 10^4].",
                    "-1000 <= Node.val <= 1000"
                ],
                "test_cases": [
                    ("1 2 3", "6"),
                    ("-10 9 20 null null 15 7", "42"),
                    ("1", "1"),
                    ("-3", "-3"),
                    ("2 -1", "2"),
                ]
            },
            {
                "title": "Best Time to Buy and Sell Stock",
                "description": "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.",
                "difficulty": "Easy",
                "input": "prices = [7,1,5,3,6,4]",
                "output": "5",
                "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.",
                "tags": ["array", "dynamic programming"],
                "constraints": [
                    "1 <= prices.length <= 10^5",
                    "0 <= prices[i] <= 10^4"
                ],
                "test_cases": [
                    ("7 1 5 3 6 4", "5"),
                    ("7 6 4 3 1", "0"),
                    ("1", "0"),
                    ("1 2", "1"),
                    ("2 1 2 0 1", "1"),
                ]
            },
            {
                "title": "Best Time to Buy and Sell Stock II",
                "description": "You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy and/or sell the stock. You can hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.",
                "difficulty": "Medium",
                "input": "prices = [7,1,5,3,6,4]",
                "output": "7",
                "explanation": "Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3. Total profit = 4 + 3 = 7.",
                "tags": ["array", "greedy"],
                "constraints": [
                    "1 <= prices.length <= 3 * 10^4",
                    "0 <= prices[i] <= 10^4"
                ],
                "test_cases": [
                    ("7 1 5 3 6 4", "7"),
                    ("1 2 3 4 5", "4"),
                    ("7 6 4 3 1", "0"),
                    ("1", "0"),
                    ("1 2", "1"),
                ]
            },
            {
                "title": "Jump Game II",
                "description": "Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.",
                "difficulty": "Medium",
                "input": "nums = [2,3,1,1,4]",
                "output": "2",
                "explanation": "The minimum number of jumps to reach the last index is 2 (jump from index 0 to 1, then to 4).",
                "tags": ["array", "greedy"],
                "constraints": [
                    "1 <= nums.length <= 10^4",
                    "0 <= nums[i] <= 1000"
                ],
                "test_cases": [
                    ("2 3 1 1 4", "2"),
                    ("2 3 0 1 4", "2"),
                    ("1", "0"),
                    ("2 1", "1"),
                    ("3 2 1", "1"),
                ]
            },
            {
                "title": "Unique Paths",
                "description": "A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many unique paths are there to the bottom-right corner?",
                "difficulty": "Medium",
                "input": "m = 3, n = 7",
                "output": "28",
                "explanation": "There are 28 unique paths to reach the bottom-right corner.",
                "tags": ["dynamic programming"],
                "constraints": [
                    "1 <= m, n <= 100",
                    "The answer will be guaranteed to be less than or equal to 2 * 10^9."
                ],
                "test_cases": [
                    ("3\n7", "28"),
                    ("3\n2", "3"),
                    ("1\n1", "1"),
                    ("10\n10", "48620"),
                    ("2\n2", "2"),
                ]
            },
            {
                "title": "Minimum Path Sum",
                "description": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.",
                "difficulty": "Medium",
                "input": "grid = [[1,3,1],[1,5,1],[4,2,1]]",
                "output": "7",
                "explanation": "The path 1->3->1->1->1 has the minimum sum of 7.",
                "tags": ["array", "dynamic programming"],
                "constraints": [
                    "m == grid.length",
                    "n == grid[i].length",
                    "1 <= m, n <= 200",
                    "0 <= grid[i][j] <= 100"
                ],
                "test_cases": [
                    ("1 3 1\n1 5 1\n4 2 1", "7"),
                    ("1 2\n3 4", "7"),
                    ("1", "1"),
                    ("1 2 3", "6"),
                    ("1\n2\n3", "6"),
                ]
            },
            {
                "title": "Climbing Stairs",
                "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
                "difficulty": "Easy",
                "input": "n = 3",
                "output": "3",
                "explanation": "There are 3 ways to climb to the top: [1,1,1], [1,2], [2,1].",
                "tags": ["dynamic programming"],
                "constraints": [
                    "1 <= n <= 45"
                ],
                "test_cases": [
                    ("3", "3"),
                    ("2", "2"),
                    ("1", "1"),
                    ("4", "5"),
                    ("5", "8"),
                ]
            },
            {
                "title": "Coin Change",
                "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.",
                "difficulty": "Medium",
                "input": "coins = [1,2,5], amount = 11",
                "output": "3",
                "explanation": "11 = 5 + 5 + 1, so 3 coins are needed.",
                "tags": ["dynamic programming"],
                "constraints": [
                    "1 <= coins.length <= 12",
                    "1 <= coins[i] <= 2^31 - 1",
                    "0 <= amount <= 10^4"
                ],
                "test_cases": [
                    ("1 2 5\n11", "3"),
                    ("2\n3", "-1"),
                    ("1\n0", "0"),
                    ("1 2\n4", "2"),
                    ("5\n10", "2"),
                ]
            },
            {
                "title": "Longest Increasing Subsequence",
                "description": "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
                "difficulty": "Medium",
                "input": "nums = [10,9,2,5,3,7,101,18]",
                "output": "4",
                "explanation": "The longest increasing subsequence is [2,3,7,101], so the length is 4.",
                "tags": ["array", "dynamic programming", "binary search"],
                "constraints": [
                    "1 <= nums.length <= 2500",
                    "-10^4 <= nums[i] <= 10^4"
                ],
                "test_cases": [
                    ("10 9 2 5 3 7 101 18", "4"),
                    ("0 1 0 3 2 3", "4"),
                    ("7 7 7 7 7", "1"),
                    ("1", "1"),
                    ("", "0"),
                ]
            },
            {
                "title": "Word Break",
                "description": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.",
                "difficulty": "Medium",
                "input": "s = 'leetcode', wordDict = ['leet','code']",
                "output": "true",
                "explanation": "'leetcode' can be segmented as 'leet code'.",
                "tags": ["string", "dynamic programming"],
                "constraints": [
                    "1 <= s.length <= 300",
                    "1 <= wordDict.length <= 1000",
                    "1 <= wordDict[i].length <= 30",
                    "s and wordDict[i] consist of only lowercase English letters."
                ],
                "test_cases": [
                    ("leetcode\nleet code", "true"),
                    ("applepenapple\napple pen", "true"),
                    ("catsandog\ncats dog sand and", "false"),
                    ("a\na", "true"),
                    ("", ""),
                ]
            },
            {
                "title": "Combination Sum",
                "description": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.",
                "difficulty": "Medium",
                "input": "candidates = [2,3,6,7], target = 7",
                "output": "[[2,2,3],[7]]",
                "explanation": "The combinations that sum to 7 are [2,2,3] and [7].",
                "tags": ["array", "backtracking"],
                "constraints": [
                    "1 <= candidates.length <= 30",
                    "1 <= candidates[i] <= 200",
                    "1 <= target <= 500",
                    "All elements of candidates are distinct."
                ],
                "test_cases": [
                    ("2 3 6 7\n7", "2 2 3\n7"),
                    ("2 3 5\n8", "2 3 3\n3 5"),
                    ("2\n1", ""),
                    ("1\n1", "1"),
                    ("2 3\n5", "2 3"),
                ]
            },
            {
                "title": "House Robber",
                "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that you cannot rob two adjacent houses. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
                "difficulty": "Medium",
                "input": "nums = [1,2,3,1]",
                "output": "4",
                "explanation": "Rob house 1 (money = 1) and house 3 (money = 3). Total amount = 1 + 3 = 4.",
                "tags": ["dynamic programming"],
                "constraints": [
                    "0 <= nums.length <= 100",
                    "0 <= nums[i] <= 400"
                ],
                "test_cases": [
                    ("1 2 3 1", "4"),
                    ("2 7 9 3 1", "12"),
                    ("", "0"),
                    ("1", "1"),
                    ("1 2", "2"),
                ]
            },
            {
                "title": "House Robber II",
                "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
                "difficulty": "Medium",
                "input": "nums = [2,3,2]",
                "output": "3",
                "explanation": "You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses. So, rob house 2 (money = 3).",
                "tags": ["dynamic programming"],
                "constraints": [
                    "0 <= nums.length <= 100",
                    "0 <= nums[i] <= 400"
                ],
                "test_cases": [
                    ("2 3 2", "3"),
                    ("1 2 3 1", "4"),
                    ("1 2 3", "3"),
                    ("1", "1"),
                    ("", "0"),
                ]
            },
            {
                "title": "Decode Ways",
                "description": "A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> '1', 'B' -> '2', ..., 'Z' -> '26'. Given a string s containing only digits, return the number of ways to decode it.",
                "difficulty": "Medium",
                "input": "s = '12'",
                "output": "2",
                "explanation": "'12' can be decoded as 'AB' (1 2) or 'L' (12).",
                "tags": ["string", "dynamic programming"],
                "constraints": [
                    "1 <= s.length <= 100",
                    "s contains only digits and may contain leading zero(s)."
                ],
                "test_cases": [
                    ("12", "2"),
                    ("226", "3"),
                    ("0", "0"),
                    ("06", "0"),
                    ("1111", "5"),
                ]
            },
            {
                "title": "Unique Binary Search Trees",
                "description": "Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.",
                "difficulty": "Medium",
                "input": "n = 3",
                "output": "5",
                "explanation": "There are 5 unique BSTs with 3 nodes.",
                "tags": ["dynamic programming", "tree"],
                "constraints": [
                    "1 <= n <= 19"
                ],
                "test_cases": [
                    ("3", "5"),
                    ("1", "1"),
                    ("2", "2"),
                    ("4", "14"),
                    ("5", "42"),
                ]
            },
            {
                "title": "Validate Binary Search Tree",
                "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.",
                "difficulty": "Medium",
                "input": "root = [2,1,3]",
                "output": "true",
                "explanation": "The tree is a valid BST.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [1, 10^4].",
                    "-2^31 <= Node.val <= 2^31 - 1"
                ],
                "test_cases": [
                    ("2 1 3", "true"),
                    ("5 1 4 null null 3 6", "false"),
                    ("1", "true"),
                    ("5 4 null 3", "false"),
                    ("3 1 5 0 2", "true"),
                ]
            },
            {
                "title": "Symmetric Tree",
                "description": "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).",
                "difficulty": "Easy",
                "input": "root = [1,2,2,3,4,4,3]",
                "output": "true",
                "explanation": "The tree is symmetric around its center.",
                "tags": ["tree", "dfs", "bfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [1, 1000].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 2 3 4 4 3", "true"),
                    ("1 2 2 null 3 null 3", "false"),
                    ("1", "true"),
                    ("1 2 3", "false"),
                    ("", "true"),
                ]
            },
            {
                "title": "Binary Tree Level Order Traversal",
                "description": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
                "difficulty": "Medium",
                "input": "root = [3,9,20,null,null,15,7]",
                "output": "[[3],[9,20],[15,7]]",
                "explanation": "The level order traversal gives nodes level by level.",
                "tags": ["tree", "bfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 2000].",
                    "-1000 <= Node.val <= 1000"
                ],
                "test_cases": [
                    ("3 9 20 null null 15 7", "3\n9 20\n15 7"),
                    ("1", "1"),
                    ("", ""),
                    ("1 2 3", "1\n2 3"),
                    ("1 2 null 3", "1\n2\n3"),
                ]
            },
            {
                "title": "Maximum Depth of Binary Tree",
                "description": "Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
                "difficulty": "Easy",
                "input": "root = [3,9,20,null,null,15,7]",
                "output": "3",
                "explanation": "The maximum depth is 3 levels.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 10^4].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("3 9 20 null null 15 7", "3"),
                    ("1 null 2", "2"),
                    ("", "0"),
                    ("1", "1"),
                    ("1 2 3", "2"),
                ]
            },
            {
                "title": "Construct Binary Tree from Preorder and Inorder Traversal",
                "description": "Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.",
                "difficulty": "Medium",
                "input": "preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]",
                "output": "[3,9,20,null,null,15,7]",
                "explanation": "The binary tree is constructed from the given traversals.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "1 <= preorder.length <= 3000",
                    "inorder.length == preorder.length",
                    "-3000 <= preorder[i], inorder[i] <= 3000",
                    "preorder and inorder consist of unique values."
                ],
                "test_cases": [
                    ("3 9 20 15 7\n9 3 15 20 7", "3 9 20 null null 15 7"),
                    ("1\n1", "1"),
                    ("1 2\n2 1", "1 2"),
                    ("3 1 2 4\n1 2 3 4", "3 1 4 null 2"),
                    ("1 2 3\n2 1 3", "1 2 3"),
                ]
            },
            {
                "title": "Lowest Common Ancestor of a Binary Search Tree",
                "description": "Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.",
                "difficulty": "Easy",
                "input": "root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8",
                "output": "6",
                "explanation": "Node 6 is the lowest common ancestor of nodes 2 and 8.",
                "tags": ["tree"],
                "constraints": [
                    "The number of nodes in the tree is in the range [2, 10^5].",
                    "-10^9 <= Node.val <= 10^9",
                    "All Node.val are unique.",
                    "p != q",
                    "p and q will exist in the BST."
                ],
                "test_cases": [
                    ("6 2 8 0 4 7 9 null null 3 5\n2\n8", "6"),
                    ("6 2 8 0 4 7 9 null null 3 5\n2\n4", "2"),
                    ("2 1\n1\n2", "2"),
                    ("3 1 4\n1\n4", "3"),
                    ("5 3 6 2 4\n2\n4", "3"),
                ]
            },
            {
                "title": "Balanced Binary Tree",
                "description": "Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than one.",
                "difficulty": "Easy",
                "input": "root = [3,9,20,null,null,15,7]",
                "output": "true",
                "explanation": "The tree is height-balanced.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 5000].",
                    "-10^4 <= Node.val <= 10^4"
                ],
                "test_cases": [
                    ("3 9 20 null null 15 7", "true"),
                    ("1 2 2 3 3 null null 4 4", "false"),
                    ("", "true"),
                    ("1", "true"),
                    ("1 2 null 3", "false"),
                ]
            },
            {
                "title": "Path Sum",
                "description": "Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.",
                "difficulty": "Easy",
                "input": "root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22",
                "output": "true",
                "explanation": "The path 5->4->11->2 sums to 22.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 5000].",
                    "-1000 <= Node.val <= 1000",
                    "-1000 <= targetSum <= 1000"
                ],
                "test_cases": [
                    ("5 4 8 11 null 13 4 7 2 null null null 1\n22", "true"),
                    ("1 2 3\n5", "false"),
                    ("1\n1", "true"),
                    ("1 2\n3", "true"),
                    ("", "0"),
                ]
            },
            {
                "title": "Path Sum II",
                "description": "Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.",
                "difficulty": "Medium",
                "input": "root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22",
                "output": "[[5,4,11,2],[5,8,4,5]]",
                "explanation": "The paths 5->4->11->2 and 5->8->4->5 sum to 22.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 5000].",
                    "-1000 <= Node.val <= 1000",
                    "-1000 <= targetSum <= 1000"
                ],
                "test_cases": [
                    ("5 4 8 11 null 13 4 7 2 null null 5 1\n22", "5 4 11 2\n5 8 4 5"),
                    ("1 2 3\n5", ""),
                    ("1 2\n3", "1 2"),
                    ("1\n1", "1"),
                    ("", ""),
                ]
            },
            {
                "title": "Binary Tree Inorder Traversal",
                "description": "Given the root of a binary tree, return the inorder traversal of its nodes' values.",
                "difficulty": "Easy",
                "input": "root = [1,null,2,3]",
                "output": "[1,3,2]",
                "explanation": "Inorder traversal: left -> root -> right.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 100].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 null 2 3", "1 3 2"),
                    ("", ""),
                    ("1", "1"),
                    ("1 2 3", "2 1 3"),
                    ("3 1 2", "1 3 2"),
                ]
            },
            {
                "title": "Sum Root to Leaf Numbers",
                "description": "Given a binary tree containing digits from 0-9 only, each root-to-leaf path represents a number. An example is the root-to-leaf path 1->2->3 which represents the number 123. Find the total sum of all root-to-leaf numbers.",
                "difficulty": "Medium",
                "input": "root = [1,2,3]",
                "output": "25",
                "explanation": "The paths are 1->2 (12) and 1->3 (13), so the sum is 12 + 13 = 25.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [1, 1000].",
                    "0 <= Node.val <= 9",
                    "The depth of the tree will not exceed 10."
                ],
                "test_cases": [
                    ("1 2 3", "25"),
                    ("4 9 0 5 1", "1026"),
                    ("1", "1"),
                    ("0", "0"),
                    ("4 9 1", "491"),
                ]
            },
            {
                "title": "Flatten Binary Tree to Linked List",
                "description": "Given the root of a binary tree, flatten the tree into a 'linked list'. The 'linked list' should be in the same order as a pre-order traversal of the binary tree.",
                "difficulty": "Medium",
                "input": "root = [1,2,5,3,4,null,6]",
                "output": "[1,null,2,null,3,null,4,null,5,null,6]",
                "explanation": "The binary tree is flattened into a linked list using pre-order traversal.",
                "tags": ["tree", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 2000].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 5 3 4 null 6", "1 null 2 null 3 null 4 null 5 null 6"),
                    ("", ""),
                    ("1", "1"),
                    ("1 2 null", "1 null 2"),
                    ("1 2 3", "1 null 2 null 3"),
                ]
            },
            {
                "title": "Populating Next Right Pointers in Each Node",
                "description": "You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.",
                "difficulty": "Medium",
                "input": "root = [1,2,3,4,5,6,7]",
                "output": "[1,#,2,3,#,4,5,6,7,#]",
                "explanation": "Each node's next pointer points to the next node on the same level, or NULL if none exists.",
                "tags": ["tree", "bfs", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 2^12 - 1].",
                    "-1000 <= Node.val <= 1000",
                    "Every node has exactly 0 or 2 children."
                ],
                "test_cases": [
                    ("1 2 3 4 5 6 7", "1 # 2 3 # 4 5 6 7 #"),
                    ("1", "1 #"),
                    ("", ""),
                    ("1 2 3", "1 # 2 3 #"),
                    ("1 2 3 4 5", "1 # 2 3 # 4 5 #"),
                ]
            },
            {
                "title": "Populating Next Right Pointers in Each Node II",
                "description": "Populate each next pointer to point                    to its next right node in a binary tree. If there is no next right node, the next pointer should be set to NULL. Unlike the previous problem, the tree is not guaranteed to be perfect.",
                "difficulty": "Medium",
                "input": "root = [1,2,3,4,5,null,7]",
                "output": "[1,#,2,3,#,4,5,7,#]",
                "explanation": "Each node's next pointer points to the next node on the same level, or NULL if none exists.",
                "tags": ["tree", "bfs", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 6000].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 3 4 5 null 7", "1 # 2 3 # 4 5 7 #"),
                    ("1", "1 #"),
                    ("", ""),
                    ("1 2 3", "1 # 2 3 #"),
                    ("1 2 null 3", "1 # 2 # 3 #"),
                ]
            },
            {
                "title": "Binary Tree Right Side View",
                "description": "Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
                "difficulty": "Medium",
                "input": "root = [1,2,3,null,5,null,4]",
                "output": "[1,3,4]",
                "explanation": "From the right side, the visible nodes are 1, 3, and 4.",
                "tags": ["tree", "bfs", "dfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 100].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("1 2 3 null 5 null 4", "1 3 4"),
                    ("1 null 3", "1 3"),
                    ("", ""),
                    ("1", "1"),
                    ("1 2 null 3", "1 2 3"),
                ]
            },
            {
                "title": "Number of Islands",
                "description": "Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
                "difficulty": "Medium",
                "input": "grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]",
                "output": "1",
                "explanation": "There is one island in the grid.",
                "tags": ["dfs", "bfs", "union find"],
                "constraints": [
                    "m == grid.length",
                    "n == grid[i].length",
                    "1 <= m, n <= 300",
                    "grid[i][j] is '0' or '1'."
                ],
                "test_cases": [
                    ("1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0", "1"),
                    ("1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1", "3"),
                    ("1", "1"),
                    ("0", "0"),
                    ("1 0 1\n0 1 0\n1 0 1", "5"),
                ]
            },
            {
                "title": "Rotting Oranges",
                "description": "You are given a m x n grid where each cell can have one of three values: 0 (empty), 1 (fresh orange), or 2 (rotten orange). Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no fresh orange remains. If this is impossible, return -1.",
                "difficulty": "Medium",
                "input": "grid = [[2,1,1],[1,1,0],[0,1,1]]",
                "output": "4",
                "explanation": "It takes 4 minutes for all fresh oranges to rot.",
                "tags": ["bfs"],
                "constraints": [
                    "m == grid.length",
                    "n == grid[i].length",
                    "1 <= m, n <= 10",
                    "grid[i][j] is 0, 1, or 2."
                ],
                "test_cases": [
                    ("2 1 1\n1 1 0\n0 1 1", "4"),
                    ("2 1 1\n0 1 1\n1 0 1", "-1"),
                    ("1", "-1"),
                    ("2", "0"),
                    ("0", "0"),
                ]
            },
            {
                "title": "Search in Rotated Sorted Array",
                "description": "There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-based). Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.",
                "difficulty": "Medium",
                "input": "nums = [4,5,6,7,0,1,2], target = 0",
                "output": "4",
                "explanation": "The target 0 is at index 4 in the rotated array.",
                "tags": ["array", "binary search"],
                "constraints": [
                    "1 <= nums.length <= 5000",
                    "-10^4 <= nums[i] <= 10^4",
                    "All values of nums are unique.",
                    "-10^4 <= target <= 10^4"
                ],
                "test_cases": [
                    ("4 5 6 7 0 1 2\n0", "4"),
                    ("4 5 6 7 0 1 2\n3", "-1"),
                    ("1\n1", "0"),
                    ("1 2 3\n2", "1"),
                    ("3 1\n1", "1"),
                ]
            },
            {
                "title": "Combination Sum II",
                "description": "Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.",
                "difficulty": "Medium",
                "input": "candidates = [10,1,2,7,6,1,5], target = 8",
                "output": "[[1,1,6],[1,2,5],[1,7],[2,6]]",
                "explanation": "The unique combinations that sum to 8 are listed.",
                "tags": ["array", "backtracking"],
                "constraints": [
                    "1 <= candidates.length <= 40",
                    "1 <= candidates[i] <= 100",
                    "1 <= target <= 100"
                ],
                "test_cases": [
                    ("10 1 2 7 6 1 5\n8", "1 1 6\n1 2 5\n1 7\n2 6"),
                    ("2 5 2 1 2\n5", "1 2 2\n5"),
                    ("1\n1", "1"),
                    ("2 3\n6", ""),
                    ("1 1\n2", "1 1"),
                ]
            },
            {
                "title": "Permutations",
                "description": "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
                "difficulty": "Medium",
                "input": "nums = [1,2,3]",
                "output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
                "explanation": "All possible permutations of [1,2,3] are listed.",
                "tags": ["backtracking"],
                "constraints": [
                    "1 <= nums.length <= 6",
                    "-10 <= nums[i] <= 10",
                    "All the integers of nums are unique."
                ],
                "test_cases": [
                    ("1 2 3", "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1"),
                    ("1", "1"),
                    ("1 2", "1 2\n2 1"),
                    ("0 1", "0 1\n1 0"),
                    ("", ""),
                ]
            },
            {
                "title": "Permutations II",
                "description": "Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.",
                "difficulty": "Medium",
                "input": "nums = [1,1,2]",
                "output": "[[1,1,2],[1,2,1],[2,1,1]]",
                "explanation": "All unique permutations of [1,1,2] are listed.",
                "tags": ["backtracking"],
                "constraints": [
                    "1 <= nums.length <= 8",
                    "-10 <= nums[i] <= 10"
                ],
                "test_cases": [
                    ("1 1 2", "1 1 2\n1 2 1\n2 1 1"),
                    ("1 2 3", "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1"),
                    ("1", "1"),
                    ("1 1", "1 1"),
                    ("", ""),
                ]
            },
            {
                "title": "Rotate Image",
                "description": "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.",
                "difficulty": "Medium",
                "input": "matrix = [[1,2,3],[4,5,6],[7,8,9]]",
                "output": "[[7,4,1],[8,5,2],[9,6,3]]",
                "explanation": "The matrix is rotated 90 degrees clockwise.",
                "tags": ["array", "matrix"],
                "constraints": [
                    "matrix.length == n",
                    "matrix[i].length == n",
                    "1 <= n <= 20",
                    "-1000 <= matrix[i][j] <= 1000"
                ],
                "test_cases": [
                    ("1 2 3\n4 5 6\n7 8 9", "7 4 1\n8 5 2\n9 6 3"),
                    ("1", "1"),
                    ("1 2\n3 4", "3 1\n4 2"),
                    ("1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16", "13 9 5 1\n14 10 6 2\n15 11 7 3\n16 12 8 4"),
                    ("", ""),
                ]
            },
            {
                "title": "Group Anagrams",
                "description": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
                "difficulty": "Medium",
                "input": "strs = ['eat','tea','tan','ate','nat','bat']",
                "output": "[['eat','tea','ate'],['tan','nat'],['bat']]",
                "explanation": "The strings are grouped by their anagram patterns.",
                "tags": ["hashmap", "string"],
                "constraints": [
                    "1 <= strs.length <= 10^4",
                    "0 <= strs[i].length <= 100",
                    "strs[i] consists of lowercase English letters."
                ],
                "test_cases": [
                    ("eat tea tan ate nat bat", "eat tea ate\ntan nat\nbat"),
                    ("", ""),
                    ("a", "a"),
                    ("cat act dog god", "cat act\ndog god"),
                    ("abc bca cab", "abc bca cab"),
                ]
            },
            {
                "title": "Pow(x, n)",
                "description": "Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).",
                "difficulty": "Medium",
                "input": "x = 2.00000, n = 10",
                "output": "1024.00000",
                "explanation": "2 raised to the power 10 is 1024.",
                "tags": ["math", "recursion"],
                "constraints": [
                    "-100.0 < x < 100.0",
                    "-2^31 <= n <= 2^31-1",
                    "-10^4 <= x^n <= 10^4"
                ],
                "test_cases": [
                    ("2.00000\n10", "1024.00000"),
                    ("2.10000\n3", "9.26100"),
                    ("2.00000\n-2", "0.25000"),
                    ("1.00000\n0", "1.00000"),
                    ("-2.00000\n2", "4.00000"),
                ]
            },
            {
                "title": "N-Queens",
                "description": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens threaten each other. Given an integer n, return all distinct solutions to the n-queens puzzle.",
                "difficulty": "Hard",
                "input": "n = 4",
                "output": "[['.Q..','...Q','Q...','..Q.'],['..Q.','Q...','...Q','.Q..']]",
                "explanation": "There are two distinct solutions to the 4-queens puzzle.",
                "tags": ["backtracking"],
                "constraints": [
                    "1 <= n <= 9"
                ],
                "test_cases": [
                    ("4", ".Q.. ...Q Q... ..Q.\n..Q. Q... ...Q .Q.."),
                    ("1", "Q"),
                    ("2", ""),
                    ("3", ""),
                    ("5", "Q.... .Q... ..Q.. ...Q. ....Q\nQ.... ..Q.. ...Q. ....Q .Q...\n.Q... Q.... ...Q. ....Q ..Q..\n.Q... ....Q ..Q.. Q.... ...Q.\n..Q.. Q.... ....Q .Q... ...Q.\n..Q.. ....Q Q.... ...Q. .Q...\n...Q. Q.... .Q... ....Q ..Q..\n...Q. ....Q .Q... Q.... ..Q..\n....Q .Q... Q.... ..Q.. ...Q.\n....Q ..Q.. Q.... .Q... ...Q."),
                ]
            },
            {
                "title": "N-Queens II",
                "description": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens threaten each other. Given an integer n, return the number of distinct solutions to the n-queens puzzle.",
                "difficulty": "Hard",
                "input": "n = 4",
                "output": "2",
                "explanation": "There are two distinct solutions to the 4-queens puzzle.",
                "tags": ["backtracking"],
                "constraints": [
                    "1 <= n <= 9"
                ],
                "test_cases": [
                    ("4", "2"),
                    ("1", "1"),
                    ("2", "0"),
                    ("3", "0"),
                    ("5", "10"),
                ]
            },
            {
                "title": "Spiral Matrix",
                "description": "Given an m x n matrix, return all elements of the matrix in spiral order.",
                "difficulty": "Medium",
                "input": "matrix = [[1,2,3],[4,5,6],[7,8,9]]",
                "output": "[1,2,3,6,9,8,7,4,5]",
                "explanation": "The elements are traversed in a spiral order.",
                "tags": ["array", "matrix"],
                "constraints": [
                    "m == matrix.length",
                    "n == matrix[i].length",
                    "1 <= m, n <= 10",
                    "-100 <= matrix[i][j] <= 100"
                ],
                "test_cases": [
                    ("1 2 3\n4 5 6\n7 8 9", "1 2 3 6 9 8 7 4 5"),
                    ("1", "1"),
                    ("1 2\n3 4", "1 2 4 3"),
                    ("1 2 3 4", "1 2 3 4"),
                    ("1\n2\n3", "1 2 3"),
                ]
            },
            {
                "title": "Maximum Subarray",
                "description": "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
                "difficulty": "Medium",
                "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                "output": "6",
                "explanation": "The subarray [4,-1,2,1] has the largest sum 6.",
                "tags": ["array", "dynamic programming"],
                "constraints": [
                    "1 <= nums.length <= 10^5",
                    "-10^4 <= nums[i] <= 10^4"
                ],
                "test_cases": [
                    ("-2 1 -3 4 -1 2 1 -5 4", "6"),
                    ("1", "1"),
                    ("-1", "-1"),
                    ("-2 -1", "-1"),
                    ("1 2 3", "6"),
                ]
            },
            {
                "title": "Jump Game III",
                "description": "Given an array of non-negative integers arr, you are initially positioned at index start. You can jump to index i + arr[i] or i - arr[i]. Determine if you can reach any index with value 0.",
                "difficulty": "Medium",
                "input": "arr = [4,2,3,0,3,1,2], start = 5",
                "output": "true",
                "explanation": "You can reach index 3 (value 0) from index 5.",
                "tags": ["array", "bfs", "dfs"],
                "constraints": [
                    "1 <= arr.length <= 5 * 10^4",
                    "0 <= arr[i] < arr.length",
                    "0 <= start < arr.length"
                ],
                "test_cases": [
                    ("4 2 3 0 3 1 2\n5", "true"),
                    ("4 2 3 0 3 1 2\n0", "true"),
                    ("3 0 2 1 2\n2", "false"),
                    ("0\n0", "true"),
                    ("1 0\n1", "true"),
                ]
            },
            {
                "title": "LRU Cache",
                "description": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the LRUCache class with the following methods: LRUCache(int capacity), int get(int key), void put(int key, int value).",
                "difficulty": "Medium",
                "input": "[['LRUCache','put','put','get','put','get','put','get','get','get'], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]]",
                "output": "[null,null,null,1,null,-1,null,-1,3,4]",
                "explanation": "The sequence of operations results in the specified outputs based on LRU cache rules.",
                "tags": ["design", "hashmap", "linked list"],
                "constraints": [
                    "1 <= capacity <= 3000",
                    "0 <= key <= 10^4",
                    "0 <= value <= 10^5",
                    "At most 2 * 10^5 calls will be made to get and put."
                ],
                "test_cases": [
                    ("2\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2\nput 4 4\nget 1\nget 3\nget 4", "null null 1 null -1 null -1 3 4"),
                    ("1\nput 1 1\nget 1", "null 1"),
                    ("2\nput 1 1\nput 1 2\nget 1", "null null 2"),
                    ("2\nput 1 1\nput 2 2\nget 1\nput 3 3", "null null 1 null"),
                    ("1\nput 1 1\nput 2 2\nget 2", "null null 2"),
                ]
            },
            {
                "title": "Min Stack",
                "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class with the following methods: MinStack(), void push(int val), void pop(), int top(), int getMin().",
                "difficulty": "Medium",
                "input": "[['MinStack','push','push','push','getMin','pop','top','getMin'], [[],[-2],[0],[-3],[-3],[],[-2],[-2]]]",
                "output": "[null,null,null,null,-3,null,0,-2]",
                "explanation": "The sequence of operations results in the specified outputs based on MinStack rules.",
                "tags": ["stack", "design"],
                "constraints": [
                    "-2^31 <= val <= 2^31 - 1",
                    "Methods pop, top and getMin operations will always be called on non-empty stacks.",
                    "At most 3 * 10^4 calls will be made to push, pop, top, and getMin."
                ],
                "test_cases": [
                    ("push -2\npush 0\npush -3\ngetMin\npop\ntop\ngetMin", "null null null -3 null 0 -2"),
                    ("push 1\ngetMin", "null 1"),
                    ("push 2\npush 1\npop\ngetMin", "null null null 2"),
                    ("push 0\npush -1\ntop\ngetMin", "null null 0 -1"),
                    ("push 3\npop", "null null"),
                ]
            },
            {
                "title": "Find Median from Data Stream",
                "description": "The median is the middle value in an ordered integer list. If the size of the list is even, the median is the average of the two middle numbers. Design a data structure that supports the following two operations: void addNum(int num), double findMedian().",
                "difficulty": "Hard",
                "input": "[['MedianFinder','addNum','addNum','findMedian','addNum','findMedian'], [[],[1],[2],[],[3],[]]]",
                "output": "[null,null,null,1.5,null,2.0]",
                "explanation": "The sequence of operations results in the specified median values.",
                "tags": ["design", "heap"],
                "constraints": [
                    "-10^5 <= num <= 10^5",
                    "There will be at least one element in the data structure before calling findMedian.",
                    "At most 5 * 10^4 calls will be made to addNum and findMedian."
                ],
                "test_cases": [
                    ("addNum 1\naddNum 2\nfindMedian\naddNum 3\nfindMedian", "null null 1.5 null 2.0"),
                    ("addNum 1\nfindMedian", "null 1.0"),
                    ("addNum 2\naddNum 3\nfindMedian", "null null 2.5"),
                    ("addNum 1\naddNum 1\nfindMedian", "null null 1.0"),
                    ("addNum 5\naddNum 10\naddNum 15\nfindMedian", "null null null 10.0"),
                ]
            },
            {
                "title": "Reverse Nodes in k-Group",
                "description": "Given a linked list, reverse the nodes of the list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.",
                "difficulty": "Hard",
                "input": "head = [1,2,3,4,5], k = 2",
                "output": "[2,1,4,3,5]",
                "explanation": "Reverse every group of 2 nodes, leaving the last node as is.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in the list is in the range [1, 5000].",
                    "1 <= k <= n",
                    "0 <= Node.val <= 1000"
                ],
                "test_cases": [
                    ("1 2 3 4 5\n2", "2 1 4 3 5"),
                    ("1 2 3 4 5\n3", "3 2 1 4 5"),
                    ("1\n1", "1"),
                    ("1 2\n2", "2 1"),
                    ("1 2 3\n4", "1 2 3"),
                ]
            },
            {
                "title": "Substring with Concatenation of All Words",
                "description": "You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.",
                "difficulty": "Hard",
                "input": "s = 'barfoothefoobarman', words = ['foo','bar']",
                "output": "[0,9]",
                "explanation": "The substrings starting at indices 0 and 9 are 'barfoo' and 'foobar', respectively.",
                "tags": ["string", "sliding window"],
                "constraints": [
                    "1 <= s.length <= 10^4",
                    "1 <= words.length <= 5000",
                    "1 <= words[i].length <= 30",
                    "s and words[i] consist of lowercase English letters."
                ],
                "test_cases": [
                    ("barfoothefoobarman\nfoo bar", "0 9"),
                    ("wordgoodgoodgoodbestword\nword good best word", "8"),
                    ("barfoo\nfoo bar", "0"),
                    ("a\na", "0"),
                    ("catfoxcat\ncat fox", "0 3"),
                ]
            },
            {
                "title": "Longest Valid Parentheses",
                "description": "Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.",
                "difficulty": "Hard",
                "input": "s = '(()'",
                "output": "2",
                "explanation": "The longest valid parentheses substring is '()'.",
                "tags": ["string", "stack", "dynamic programming"],
                "constraints": [
                    "0 <= s.length <= 3 * 10^4",
                    "s[i] is '(' or ')'."
                ],
                "test_cases": [
                    ("(()", "2"),
                    (")()())", "4"),
                    ("", "0"),
                    ("()(()", "2"),
                    ("()()", "4"),
                ]
            },
            {
                "title": "Search in Rotated Sorted Array II",
                "description": "There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-based). Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.",
                "difficulty": "Medium",
                "input": "nums = [2,5,6,0,0,1,2], target = 0",
                "output": "true",
                "explanation": "The target 0 is present in the array.",
                "tags": ["array", "binary search"],
                "constraints": [
                    "1 <= nums.length <= 5000",
                    "-10^4 <= nums[i] <= 10^4",
                    "nums is sorted and rotated.",
                    "-10^4 <= target <= 10^4"
                ],
                "test_cases": [
                    ("2 5 6 0 0 1 2\n0", "true"),
                    ("2 5 6 0 0 1 2\n3", "false"),
                    ("1\n1", "true"),
                    ("1 1 1\n1", "true"),
                    ("1 2 1\n2", "true"),
                ]
            },
            {
                "title": "Find First and Last Position of Element in Sorted Array",
                "description": "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].",
                "difficulty": "Medium",
                "input": "nums = [5,7,7,8,8,10], target = 8",
                "output": "[3,4]",
                "explanation": "The target 8 appears at indices 3 and 4.",
                "tags": ["array", "binary search"],
                "constraints": [
                    "0 <= nums.length <= 10^5",
                    "-10^9 <= nums[i] <= 10^9",
                    "nums is a non-decreasing array.",
                    "-10^9 <= target <= 10^9"
                ],
                "test_cases": [
                    ("5 7 7 8 8 10\n8", "3 4"),
                    ("5 7 7 8 8 10\n6", "-1 -1"),
                    ("1\n1", "0 0"),
                    ("", "-1 -1"),
                    ("1 1 1\n1", "0 2"),
                ]
            },
            {
                "title": "Combination Sum III",
                "description": "Find all valid combinations of k numbers that sum up to n such that the following conditions are true: Only numbers 1 through 9 are used. Each number is used at most once. Return a list of all possible valid combinations.",
                "difficulty": "Medium",
                "input": "k = 3, n = 7",
                "output": "[[1,2,4]]",
                "explanation": "The only valid combination is [1,2,4] which sums to 7.",
                "tags": ["array", "backtracking"],
                "constraints": [
                    "2 <= k <= 9",
                    "1 <= n <= 60"
                ],
                "test_cases": [
                    ("3\n7", "1 2 4"),
                    ("3\n9", "1 2 6\n1 3 5\n2 3 4"),
                    ("4\n1", ""),
                    ("2\n18", ""),
                    ("2\n9", "2 7\n3 6\n4 5"),
                ]
            },
            {
                "title": "Jump Game IV",
                "description": "Given an array of integers arr, you are initially positioned at the first index of the array. In one step you can jump to index i + 1, i - 1, or any index j where arr[i] == arr[j] and i != j. Return the minimum number of steps to reach the last index of the array.",
                "difficulty": "Hard",
                "input": "arr = [100,-23,-23,404,100,23,23,23,3,404]",
                "output": "3",
                "explanation": "You can reach the last index in 3 steps.",
                "tags": ["array", "bfs"],
                "constraints": [
                    "1 <= arr.length <= 5 * 10^4",
                    "-10^8 <= arr[i] <= 10^8"
                ],
                "test_cases": [
                    ("100 -23 -23 404 100 23 23 23 3 404", "3"),
                    ("7", "0"),
                    ("7 7 7", "1"),
                    ("11 22 11 22", "2"),
                    ("1 1 1 1", "1"),
                ]
            },
            {
                "title": "Next Permutation",
                "description": "Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The replacement must be in place and use only constant extra memory.",
                "difficulty": "Medium",
                "input": "nums = [1,2,3]",
                "output": "[1,3,2]",
                "explanation": "The next lexicographically greater permutation is [1,3,2].",
                "tags": ["array"],
                "constraints": [
                    "1 <= nums.length <= 100",
                    "0 <= nums[i] <= 100"
                ],
                "test_cases": [
                    ("1 2 3", "1 3 2"),
                    ("3 2 1", "1 2 3"),
                    ("1 1 5", "1 5 1"),
                    ("1", "1"),
                    ("1 3 2", "2 1 3"),
                ]
            },
            {
                "title": "Valid Number",
                "description": "A valid number can be split up into these components (in order): A decimal number or an integer, optionally followed by an 'e' or 'E' followed by an integer. A decimal number can be: a sign (+ or -), followed by digits, followed by a dot, followed by digits, or digits followed by a dot followed by digits, or a sign followed by digits followed by a dot, or a sign followed by a dot followed by digits. An integer can be: a sign (+ or -) followed by digits, or just digits. Given a string s, return true if s is a valid number.",
                "difficulty": "Hard",
                "input": "s = '0.1'",
                "output": "true",
                "explanation": "'0.1' is a valid decimal number.",
                "tags": ["string"],
                "constraints": [
                    "1 <= s.length <= 20",
                    "s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'."
                ],
                "test_cases": [
                    ("0.1", "true"),
                    ("abc", "false"),
                    ("1e10", "true"),
                    ("-90e3", "true"),
                    (".1", "true"),
                ]
            },
            {
                "title": "Wildcard Matching",
                "description": "Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where: '?' Matches any single character. '*' Matches any sequence of characters (including the empty sequence). The matching should cover the entire input string (not partial).",
                "difficulty": "Hard",
                "input": "s = 'aa', p = '*'",
                "output": "true",
                "explanation": "'*' matches the entire string 'aa'.",
                "tags": ["string", "dynamic programming"],
                "constraints": [
                    "0 <= s.length, p.length <= 2000",
                    "s contains only lowercase English letters.",
                    "p contains only lowercase English letters, '?' or '*'."
                ],
                "test_cases": [
                    ("aa\n*", "true"),
                    ("cb\n?a", "true"),
                    ("adceb\n*?*b", "true"),
                    ("acdcb\n*?*a", "false"),
                    ("\n", "true"),
                ]
            },
            {
                "title": "Largest Number",
                "description": "Given a list of non-negative integers nums, arrange them such that they form the largest number and return it as a string.",
                "difficulty": "Medium",
                "input": "nums = [10,2]",
                "output": "'210'",
                "explanation": "Arranging [10,2] as '210' forms the largest number.",
                "tags": ["string", "sort"],
                "constraints": [
                    "1 <= nums.length <= 100",
                    "0 <= nums[i] <= 10^9"
                ],
                "test_cases": [
                    ("10 2", "210"),
                    ("3 30 34 5 9", "9534330"),
                    ("0 0", "0"),
                    ("1", "1"),
                    ("23 32", "32323"),
                ]
            },
            {
                "title": "Binary Tree Zigzag Level Order Traversal",
                "description": "Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).",
                "difficulty": "Medium",
                "input": "root = [3,9,20,null,null,15,7]",
                "output": "[[3],[20,9],[15,7]]",
                "explanation": "The level order traversal alternates direction per level.",
                "tags": ["tree", "bfs"],
                "constraints": [
                    "The number of nodes in the tree is in the range [0, 2000].",
                    "-100 <= Node.val <= 100"
                ],
                "test_cases": [
                    ("3 9 20 null null 15 7", "3\n20 9\n15 7"),
                    ("1", "1"),
                    ("", ""),
                    ("1 2 3", "1\n3 2"),
                    ("1 2 3 4 null null 5", "1\n3 2\n4 5"),
                ]
            },
            {
                "title": "Course Schedule",
                "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array of prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses. Otherwise, return false.",
                "difficulty": "Medium",
                "input": "numCourses = 2, prerequisites = [[1,0]]",
                "output": "true",
                "explanation": "You can take course 0 and then course 1.",
                "tags": ["graph", "dfs", "bfs"],
                "constraints": [
                    "1 <= numCourses <= 2000",
                    "0 <= prerequisites.length <= 5000",
                    "prerequisites[i].length == 2",
                    "0 <= ai, bi < numCourses"
                ],
                "test_cases": [
                    ("2\n1 0", "true"),
                    ("2\n1 0\n0 1", "false"),
                    ("1\n", "true"),
                    ("3\n1 0\n2 1", "true"),
                    ("4\n1 0\n2 0\n0 3", "true"),
                ]
            },
            {
                "title": "Course Schedule II",
                "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array of prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.",
                "difficulty": "Medium",
                "input": "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]",
                "output": "[0,2,1,3]",
                "explanation": "One valid course order is [0,2,1,3].",
                "tags": ["graph", "dfs", "bfs"],
                "constraints": [
                    "1 <= numCourses <= 2000",
                    "0 <= prerequisites.length <= 5000",
                    "prerequisites[i].length == 2",
                    "0 <= ai, bi < numCourses"
                ],
                "test_cases": [
                    ("4\n1 0\n2 0\n3 1\n3 2", "0 2 1 3"),
                    ("2\n1 0", "0 1"),
                    ("2\n1 0\n0 1", ""),
                    ("1\n", "0"),
                    ("3\n1 0\n2 0", "0 1 2"),
                ]
            },
            {
                "title": "Add Binary",
                "description": "Given two binary strings a and b, return their sum as a binary string.",
                "difficulty": "Easy",
                "input": "a = '11', b = '1'",
                "output": "'100'",
                "explanation": "The binary sum of 11 and 1 is 100.",
                "tags": ["string", "math"],
                "constraints": [
                    "1 <= a.length, b.length <= 10^4",
                    "a and b consist only of '0' or '1' characters.",
                    "Each string does not contain leading zeros except for the zero itself."
                ],
                "test_cases": [
                    ("11\n1", "100"),
                    ("1010\n1011", "10101"),
                    ("0\n0", "0"),
                    ("1\n1", "10"),
                    ("1111\n1111", "11110"),
                ]
            },
            {
                "title": "Text Justification",
                "description": "Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.",
                "difficulty": "Hard",
                "input": "words = ['This','is','an','example','of','text','justification.'], maxWidth = 16",
                "output": "['This    is    an','example  of text','justification.  ']",
                "explanation": "The words are justified to fit maxWidth with even spacing.",
                "tags": ["string"],
                "constraints": [
                    "1 <= words.length <= 300",
                    "1 <= words[i].length <= 20",
                    "words[i] consists of only English letters and spaces.",
                    "1 <= maxWidth <= 100"
                ],
                "test_cases": [
                    ("This is an example of text justification.\n16", "This    is    an\nexample  of text\njustification.  "),
                    ("What must be acknowledgment shall be\n16", "What   must   be\nacknowledgment  \nshall be        "),
                    ("a\n1", "a"),
                    ("Science is a wonderful thing\n12", "Science  is a\nwonderful thing"),
                    ("word\n5", "word "),
                ]
            },
            {
                "title": "Sqrt(x)",
                "description": "Given a non-negative integer x, compute and return the square root of x. Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.",
                "difficulty": "Easy",
                "input": "x = 8",
                "output": "2",
                "explanation": "The square root of 8 is 2.82842..., and since we return the integer part, the answer is 2.",
                "tags": ["math", "binary search"],
                "constraints": [
                    "0 <= x <= 2^31 - 1"
                ],
                "test_cases": [
                    ("8", "2"),
                    ("4", "2"),
                    ("0", "0"),
                    ("1", "1"),
                    ("16", "4"),
                ]
            },
            {
                "title": "Climbing Stairs",
                "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
                "difficulty": "Easy",
                "input": "n = 3",
                "output": "3",
                "explanation": "There are 3 ways to climb to the top: [1,1,1], [1,2], [2,1].",
                "tags": ["dynamic programming"],
                "constraints": [
                    "1 <= n <= 45"
                ],
                "test_cases": [
                    ("3", "3"),
                    ("2", "2"),
                    ("1", "1"),
                    ("4", "5"),
                    ("5", "8"),
                ]
            },
            {
                "title": "Simplify Path",
                "description": "Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.",
                "difficulty": "Medium",
                "input": "path = '/home/'",
                "output": "'/home'",
                "explanation": "The path '/home/' is already simplified.",
                "tags": ["string", "stack"],
                "constraints": [
                    "1 <= path.length <= 3000",
                    "path consists of English letters, digits, period '.', slash '/', or '_'.",
                    "path is a valid absolute Unix path."
                ],
                "test_cases": [
                    ("/home/", "/home"),
                    ("/../", "/"),
                    ("/home//foo/", "/home/foo"),
                    ("/a/./b/../../c/", "/c"),
                    ("/.", "/"),
                ]
            },
            {
                "title": "Edit Distance",
                "description": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted: Insert a character, Delete a character, Replace a character.",
                "difficulty": "Hard",
                "input": "word1 = 'horse', word2 = 'ros'",
                "output": "3",
                "explanation": "The minimum operations to convert 'horse' to 'ros' are: replace 'h' with 'r', delete 'r', delete 'e'.",
                "tags": ["string", "dynamic programming"],
                "constraints": [
                    "0 <= word1.length, word2.length <= 500",
                    "word1 and word2 consist of lowercase English letters."
                ],
                "test_cases": [
                    ("horse\nros", "3"),
                    ("intention\nexecution", "5"),
                    ("a\nb", "1"),
                    ("\na", "1"),
                    ("", ""),
                ]
            },
            {
                "title": "Set Matrix Zeroes",
                "description": "Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. You must do it in place.",
                "difficulty": "Medium",
                "input": "matrix = [[1,1,1],[1,0,1],[1,1,1]]",
                "output": "[[1,0,1],[0,0,0],[1,0,1]]",
                "explanation": "The second row and second column are set to 0 because of the 0 at [1,1].",
                "tags": ["array", "matrix"],
                "constraints": [
                    "m == matrix.length",
                    "n == matrix[0].length",
                    "1 <= m, n <= 200",
                    "-2^31 <= matrix[i][j] <= 2^31 - 1"
                ],
                "test_cases": [
                    ("1 1 1\n1 0 1\n1 1 1", "1 0 1\n0 0 0\n1 0 1"),
                    ("0 1\n2 3", "0 0\n0 3"),
                    ("1", "1"),
                    ("0", "0"),
                    ("1 2\n3 0", "1 0\n0 0"),
                ]
            },
            {
                "title": "Search a 2D Matrix",
                "description": "Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.",
                "difficulty": "Medium",
                "input": "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3",
                "output": "true",
                "explanation": "The target 3 is found in the matrix.",
                "tags": ["array", "binary search"],
                "constraints": [
                    "m == matrix.length",
                    "n == matrix[i].length",
                    "1 <= m, n <= 100",
                    "-10^4 <= matrix[i][j], target <= 10^4"
                ],
                "test_cases": [
                    ("1 3 5 7\n10 11 16 20\n23 30 34 60\n3", "true"),
                    ("1 3 5 7\n10 11 16 20\n23 30 34 60\n13", "false"),
                    ("1\n1", "true"),
                    ("1 2\n3", "false"),
                    ("1 3\n3 5\n3", "true"),
                ]
            },
            {
                "title": "Sort Colors",
                "description": "Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.",
                "difficulty": "Medium",
                "input": "nums = [2,0,2,1,1,0]",
                "output": "[0,0,1,1,2,2]",
                "explanation": "The array is sorted by color: red (0), white (1), blue (2).",
                "tags": ["array", "two pointers"],
                "constraints": [
                    "n == nums.length",
                    "1 <= n <= 300",
                    "nums[i] is 0, 1, or 2."
                ],
                "test_cases": [
                    ("2 0 2 1 1 0", "0 0 1 1 2 2"),
                    ("2 0 1", "0 1 2"),
                    ("1", "1"),
                    ("0 0 0", "0 0 0"),
                    ("2 1", "1 2"),
                ]
            },
            {
                "title": "Minimum Size Subarray Sum",
                "description": "Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.",
                "difficulty": "Medium",
                "input": "target = 7, nums = [2,3,1,2,4,3]",
                "output": "2",
                "explanation": "The subarray [4,3] has the minimal length with sum >= 7.",
                "tags": ["array", "sliding window"],
                "constraints": [
                    "1 <= target <= 10^9",
                    "1 <= nums.length <= 10^5",
                    "1 <= nums[i] <= 10^5"
                ],
                "test_cases": [
                    ("7\n2 3 1 2 4 3", "2"),
                    ("4\n1 4 4", "1"),
                    ("11\n1 1 1 1 1 1 1 1", "0"),
                    ("1\n1", "1"),
                    ("15\n5 5 5", "3"),
                ]
            },
            {
                "title": "Word Search",
                "description": "Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.",
                "difficulty": "Medium",
                "input": "board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'",
                "output": "true",
                "explanation": "The word 'ABCCED' can be found in the board.",
                "tags": ["backtracking", "matrix"],
                "constraints": [
                    "m == board.length",
                    "n == board[i].length",
                    "1 <= m, n <= 6",
                    "1 <= word.length <= 15",
                    "board and word consist of only uppercase and lowercase English letters."
                ],
                "test_cases": [
                    ("A B C E\nS F C S\nA D E E\nABCCED", "true"),
                    ("A B C E\nS F C S\nA D E E\nSEE", "true"),
                    ("A B C E\nS F C S\nA D E E\nABCB", "false"),
                    ("A\nA", "true"),
                    ("A B\nC D\nABCD", "false"),
                ]
            },
            {
                "title": "Decode String",
                "description": "Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.",
                "difficulty": "Medium",
                "input": "s = '3[a]2[bc]'",
                "output": "'aaabcbc'",
                "explanation": "The string '3[a]2[bc]' decodes to 'aaabcbc'.",
                "tags": ["string", "stack"],
                "constraints": [
                    "1 <= s.length <= 30",
                    "s consists of lowercase English letters, digits, and square brackets '[]'.",
                    "s is guaranteed to be a valid input."
                ],
                "test_cases": [
                    ("3[a]2[bc]", "aaabcbc"),
                    ("3[a2[c]]", "accaccacc"),
                    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
                    ("abc", "abc"),
                    ("3[a]b", "aaab"),
                ]
            },
            {
                "title": "Validate IP Address",
                "description": "Given a string queryIP, return 'IPv4' if queryIP is a valid IPv4 address, 'IPv6' if queryIP is a valid IPv6 address, or 'Neither' if queryIP is not a valid address of either type.",
                "difficulty": "Medium",
                "input": "queryIP = '192.168.1.1'",
                "output": "'IPv4'",
                "explanation": "'192.168.1.1' is a valid IPv4 address.",
                "tags": ["string"],
                "constraints": [
                    "queryIP consists only of English letters, digits, and the characters '.' and ':'."
                ],
                "test_cases": [
                    ("192.168.1.1", "IPv4"),
                    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
                    ("256.256.256.256", "Neither"),
                    ("2001:0db8:85a3::8A2E:0370:7334", "Neither"),
                    ("1.1.1", "Neither"),
                ]
            },
            {
                "title": "Partition List",
                "description": "Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.",
                "difficulty": "Medium",
                "input": "head = [1,4,3,2,5,2], x = 3",
                "output": "[1,2,2,4,3,5]",
                "explanation": "All nodes with values less than 3 come before those greater than or equal to 3.",
                "tags": ["linked list", "two pointers"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 200].",
                    "-100 <= Node.val <= 100",
                    "-200 <= x <= 200"
                ],
                "test_cases": [
                    ("1 4 3 2 5 2\n3", "1 2 2 4 3 5"),
                    ("2 1\n2", "1 2"),
                    ("", "0"),
                    ("1\n1", "1"),
                    ("1 2 3\n4", "1 2 3"),
                ]
            },
            {
                "title": "Merge Sorted Array",
                "description": "You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should be stored in nums1.",
                "difficulty": "Easy",
                "input": "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3",
                "output": "[1,2,2,3,5,6]",
                "explanation": "The arrays are merged into nums1 in sorted order.",
                "tags": ["array", "two pointers"],
                "constraints": [
                    "nums1.length == m + n",
                    "nums2.length == n",
                    "0 <= m, n <= 200",
                    "1 <= m + n <= 200",
                    "-10^9 <= nums1[i], nums2[i] <= 10^9"
                ],
                "test_cases": [
                    ("1 2 3 0 0 0\n3\n2 5 6\n3", "1 2 2 3 5 6"),
                    ("1\n1\n\n0", "1"),
                    ("0\n0\n1\n1", "1"),
                    ("2 0\n1\n1 2\n2", "1 2 2"),
                    ("1 0\n1\n2\n1", "1 2"),
                ]
            },
            {
                "title": "Gray Code",
                "description": "An n-bit gray code sequence is a sequence of 2^n integers where every integer is in the range [0, 2^n - 1], the first integer is 0, each integer appears exactly once, and the binary representation of every pair of consecutive integers differs by exactly one bit. Given an integer n, return any valid n-bit gray code sequence.",
                "difficulty": "Medium",
                "input": "n = 2",
                "output": "[0,1,3,2]",
                "explanation": "The binary representations are [00,01,11,10], differing by one bit between consecutive numbers.",
                "tags": ["backtracking"],
                "constraints": [
                    "1 <= n <= 16"
                ],
                "test_cases": [
                    ("2", "0 1 3 2"),
                    ("1", "0 1"),
                    ("3", "0 1 3 2 6 7 5 4"),
                    ("4", "0 1 3 2 6 7 5 4 12 13 15 14 10 11 9 8"),
                    ("5", "0 1 3 2 6 7 5 4 12 13 15 14 10 11 9 8 24 25 27 26 30 31 29 28 20 21 23 22 18 19 17 16"),
                ]
            },
            {
                "title": "Subsets",
                "description": "Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.",
                "difficulty": "Medium",
                "input": "nums = [1,2,3]",
                "output": "[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]",
                "explanation": "All possible subsets of [1,2,3] are listed.",
                "tags": ["array", "backtracking"],
                "constraints": [
                    "1 <= nums.length <= 10",
                    "-10 <= nums[i] <= 10",
                    "All the numbers of nums are unique."
                ],
                "test_cases": [
                    ("1 2 3", "\n1\n2\n1 2\n3\n1 3\n2 3\n1 2 3"),
                    ("1", "\n1"),
                    ("1 2", "\n1\n2\n1 2"),
                    ("0", "\n0"),
                    ("1 2 3 4", "\n1\n2\n1 2\n3\n1 3\n2 3\n1 2 3\n4\n1 4\n2 4\n1 2 4\n3 4\n1 3 4\n2 3 4\n1 2 3 4"),
                ]
            },
            {
                "title": "Subsets II",
                "description": "Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.",
                "difficulty": "Medium",
                "input": "nums = [1,2,2]",
                "output": "[[],[1],[1,2],[1,2,2],[2],[2,2]]",
                "explanation": "All possible unique subsets of [1,2,2] are listed.",
                "tags": ["array", "backtracking"],
                "constraints": [
                    "1 <= nums.length <= 10",
                    "-10 <= nums[i] <= 10"
                ],
                "test_cases": [
                    ("1 2 2", "\n1\n2\n1 2\n2 2\n1 2 2"),
                    ("1 1", "\n1\n1 1"),
                    ("1", "\n1"),
                    ("1 1 1", "\n1\n1 1\n1 1 1"),
                    ("0 0", "\n0\n0 0"),
                ]
            },
            {
                "title": "Count and Say",
                "description": "The count-and-say sequence is a sequence of digit strings defined by the recursive formula: countAndSay(1) = '1', countAndSay(n) is the way you would 'say' the digit string from countAndSay(n-1), which is then converted into a different digit string. Given an integer n, return the nth term of the count-and-say sequence.",
                "difficulty": "Medium",
                "input": "n = 4",
                "output": "'1211'",
                "explanation": "The sequence is: 1, 11, 21, 1211. For n=4, the result is '1211'.",
                "tags": ["string"],
                "constraints": [
                    "1 <= n <= 30"
                ],
                "test_cases": [
                    ("4", "1211"),
                    ("1", "1"),
                    ("2", "11"),
                    ("3", "21"),
                    ("5", "111221"),
                ]
            },
            {
                "title": "Sudoku Solver",
                "description": "Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules: Each of the digits 1-9 must occur exactly once in each row, column, and 3x3 sub-box.",
                "difficulty": "Hard",
                "input": "board = [['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']]",
                "output": "[['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]",
                "explanation": "The input board is solved to satisfy all Sudoku rules.",
                "tags": ["backtracking"],
                "constraints": [
                    "board.length == 9",
                    "board[i].length == 9",
                    "board[i][j] is a digit or '.'."
                ],
                "test_cases": [
                    ("5 3 . . 7 . . . .\n6 . . 1 9 5 . . .\n. 9 8 . . . . 6 .\n8 . . . 6 . . . 3\n4 . . 8 . 3 . . 1\n7 . . . 2 . . . 6\n. 6 . . . . 2 8 .\n. . . 4 1 9 . . 5\n. . . . 8 . . 7 9", "5 3 4 6 7 8 9 1 2\n6 7 2 1 9 5 3 4 8\n1 9 8 3 4 2 5 6 7\n8 5 9 7 6 1 4 2 3\n4 2 6 8 5 3 7 9 1\n7 1 3 9 2 4 8 5 6\n9 6 1 5 3 7 2 8 4\n2 8 7 4 1 9 6 3 5\n3 4 5 2 8 6 1 7 9"),
                    (". . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .", "1 2 3 4 5 6 7 8 9\n4 5 6 7 8 9 1 2 3\n7 8 9 1 2 3 4 5 6\n2 1 4 3 6 5 8 9 7\n3 6 5 8 9 7 2 1 4\n8 9 7 2 1 4 3 6 5\n5 3 1 6 7 8 9 4 2\n6 7 8 9 4 2 5 3 1\n9 4 2 5 3 1 6 7 8"),
                    ("1 . .\n. . .\n. . .", "1 2 3\n4 5 6\n7 8 9"),
                    ("9 . .\n. . .\n. . .", "9 1 2\n3 4 5\n6 7 8"),
                    (". . 1\n. . .\n. . .", "1 2 3\n4 5 6\n7 8 9"),
                ]
            },
            {
                "title": "Remove Duplicates from Sorted List II",
                "description": "Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.",
                "difficulty": "Medium",
                "input": "head = [1,2,3,3,4,4,5]",
                "output": "[1,2,5]",
                "explanation": "Nodes with values 3 and 4 are removed as they are duplicates.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 300].",
                    "-100 <= Node.val <= 100",
                    "The list is guaranteed to be sorted in ascending order."
                ],
                "test_cases": [
                    ("1 2 3 3 4 4 5", "1 2 5"),
                    ("1 1 1 2 3", "2 3"),
                    ("1 1 1", ""),
                    ("1 2 3", "1 2 3"),
                    ("", ""),
                ]
            },
            {
                "title": "Remove Duplicates from Sorted List",
                "description": "Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.",
                "difficulty": "Easy",
                "input": "head = [1,1,2,3,3]",
                "output": "[1,2,3]",
                "explanation": "Duplicates are removed, leaving one instance of each value.",
                "tags": ["linked list"],
                "constraints": [
                    "The number of nodes in the list is in the range [0, 300].",
                    "-100 <= Node.val <= 100",
                    "The list is guaranteed to be sorted in ascending order."
                ],
                "test_cases": [
                    ("1 1 2 3 3", "1 2 3"),
                    ("1 1 1", "1"),
                    ("", ""),
                    ("1 2 3", "1 2 3"),
                    ("1 1 2 2 3", "1 2 3"),
                ]
            },
            {
                "title": "Reverse Integer",
                "description": "Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.",
                "difficulty": "Medium",
                "input": "x = 123",
                "output": "321",
                "explanation": "The digits of 123 are reversed to 321.",
                "tags": ["math"],
                "constraints": [
                    "-2^31 <= x <= 2^31 - 1"
                ],
                "test_cases": [
                    ("123", "321"),
                    ("-123", "-321"),
                    ("120", "21"),
                    ("0", "0"),
                    ("1534236469", "0"),
                ]
            },
            {
                "title": "Palindrome Number",
                "description": "Given an integer x, return true if x is a palindrome, and false otherwise.",
                "difficulty": "Easy",
                "input": "x = 121",
                "output": "true",
                "explanation": "121 reads the same forwards and backwards.",
                "tags": ["math"],
                "constraints": [
                    "-2^31 <= x <= 2^31 - 1"
                ],
                "test_cases": [
                    ("121", "true"),
                    ("-121", "false"),
                    ("10", "false"),
                    ("0", "true"),
                    ("12321", "true"),
                ]
            },
        ]
        for item in problems_data:
            if Problem.objects.filter(title=item['title']).exists():
                self.stdout.write(f"⏩ Skipped (already exists): {item['title']}")
                continue

            problem = Problem.objects.create(
                title=item['title'],
                description=item['description'].strip(),
                input_format=item.get('input', '').strip(),
                output_format=item.get('output', '').strip(),
                explanation=item.get('explanation', '').strip(),
                constraints='\n'.join(item.get('constraints', [])),
                difficulty=item['difficulty'],
                tags=', '.join(item.get('tags', []))
            )

            for input_data, expected_output in item.get("test_cases", []):
                TestCase.objects.create(
                    problem=problem,
                    input_data=input_data.strip(),
                    expected_output=expected_output.strip()
                )

            self.stdout.write(f"✅ Added: {problem.title}")