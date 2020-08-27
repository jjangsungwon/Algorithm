SELECT name, count(*)
FROM animal_ins
GROUP BY name HAVING count(name) >= 2