SELECT hour(datetime), count(*)
FROM animal_outs
WHERE hour(datetime) >= 9 and hour(datetime) <= 19
GROUP BY hour(datetime)

/*
SET @hour := 8;

SELECT
    (@hour := @hour + 1),
    (SELECT count(*) FROM animal_outs WHERE hour(datetime) = @hour)
FROM animal_outs
WHERE @hour < 19
*/