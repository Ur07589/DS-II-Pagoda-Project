# DS II Project - Final Project 

# What is a Pagoda?

Pagoda is a selection algorithm. In computer science, a selection algorithm is an algorithm for finding the kth smallest value in a collection of ordered values, such as numbers. Selection includes as special cases the problems of finding the minimum, median, and maximum element in the collection. Pagodas are remarkably efficient in their average behavior with respect to the number of comparisons.

# Structure
The pagoda is an implementation of a priority queue in a binary tree. The binary tree is constrained to have priority queue ordering (parent larger than descendants). The structure of the pointers in the pagoda is peculiar; we have the following organization:

(1) the root pointers point to the leftmost and to the rightmost nodes;

(2) the right link of a right descendant points to its parent and its left link to its leftmost descendant;

(3) the left link of a left descendant points to its parent and its right link to its rightmost descendant. 

The basic operation in a pagoda is merging two disjoint pagodas, which can be done very efficiently. An insertion is achieved by merging a single element with the main structure; an extraction is done by merging the two descendants of the root. Merging pagodas is done bottom-up, merging the leftmost path of one with the rightmost path of the other.

# Time Complexity
The time complexity of a Pagoda is O(Log(n)). Pagoda also adds the elements ranked by priority. 

# Resources 
https://dl.acm.org/doi/10.1109/SFCS.1978.13
https://dl.acm.org/doi/proceedings/10.5555/1382432
https://www.geeksforgeeks.org/implementing-pagoda-in-java/

# Usecase
The root will always have the value with highest priority. Getting max can be accomplished in O(1).

