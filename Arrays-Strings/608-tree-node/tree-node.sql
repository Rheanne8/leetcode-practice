# Write your MySQL query statement below
WITH a AS (
    SELECT p_id, COUNT(DISTINCT id) AS num_children
    FROM Tree
    GROUP BY p_id

),

b AS(
    SELECT t.p_id, t.id, a.num_children
    FROM Tree as t
    LEFT JOIN a
    ON a.p_id = t.id
)

SELECT b.id,
    CASE 
        WHEN p_id is NULL THEN 'Root'
        WHEN p_id is NOT NULL AND num_children > 0 THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM b