# Write your MySQL query statement below
# filter for pids that have the same tiv2015 as one or more other pids and lat/lon is different 

WITH 
    a AS(SELECT DISTINCT i1.pid
        FROM Insurance AS i1
        JOIN Insurance AS i2
        WHERE i1.pid != i2.pid AND i1.lat = i2.lat AND i1.lon = i2.lon),
    b AS(SELECT DISTINCT i3.pid, i3.tiv_2016
        FROM Insurance AS i3
        JOIN Insurance AS i4
        WHERE i3.pid != i4.pid AND i3.tiv_2015 = i4.tiv_2015)

SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM b
WHERE b.pid NOT IN (SELECT a.pid FROM a)





