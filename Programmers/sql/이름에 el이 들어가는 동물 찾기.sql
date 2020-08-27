SELECT animal_id, name
FROM animal_ins
WHERE name like "%EL%" and animal_type = "Dog"
ORDER BY name