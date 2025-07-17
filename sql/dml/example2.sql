WITH update_stmt AS
(
	UPDATE city
	SET city = cr.new_name
	FROM city_renames cr
	WHERE cr.city_id = city.city_id
	RETURNING *
)

SELECT 'Update city name from' || old_name || ' to ' || new_name
FROM update_stmt;