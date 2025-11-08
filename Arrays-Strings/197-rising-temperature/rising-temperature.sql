# Write your MySQL query statement below
SELECT w1.id 
FROM Weather AS w1
JOIN Weather AS w2
WHERE w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY) AND w1.temperature > w2.temperature