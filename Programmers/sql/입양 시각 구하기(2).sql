SET @hour := -1;

SELECT
    (@hour := @hour + 1), 
    (SELECT count(*) FROM animal_outs WHERE hour(datetime) = @hour)
FROM ANIMAL_OUTS
where @hour < 23

