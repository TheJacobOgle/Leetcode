-- 1757. Recyclable and Low Fat Products
-- Easy
-- https://leetcode.com/problems/recyclable-and-low-fat-products/description/

select product_id from Products where low_fats = 'Y' and recyclable = 'Y';
