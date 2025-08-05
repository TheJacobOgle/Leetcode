### Two Pointers
```
# Two Pointer Techniques - ASCII Visuals

1. Opposite Ends Strategy
--------------------------
Use two pointers starting from both ends and moving toward the center.

Example:
[ 2, 4, 6, 8, 10, 12 ]
  ^               ^
 left           right

// Move inward based on condition (e.g. sum check)

Use Cases:
- Palindrome check
- Two Sum (sorted array)
- Reverse array in-place

--------------------------------------------------

2. Same Direction / Sliding Window
-----------------------------------
Use two pointers moving in the same direction.

Example:
[ 1, 3, 5, 7, 9, 11 ]
  ^  ^
 left right

// Expand/shrink window depending on condition

Use Cases:
- Longest substring with K distinct chars
- Max subarray sum of size K
- Minimum window substring

--------------------------------------------------

3. Fast & Slow Pointers
------------------------
One pointer moves faster than the other.

Example:
[ 3, 1, 4, 1, 5, 9, 2 ]
  ^     ^
 slow   fast

// fast moves 2 steps, slow moves 1 step

Use Cases:
- Detect cycle in linked list (Floyd’s Algorithm)
- Find middle of linked list
- Remove N-th node from end of list

```
