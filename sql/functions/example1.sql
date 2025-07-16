CREATE OR REPLACE FUNCTION add_new_group (IN i_group_number INT)
RETURNS BIGINT
LANGUAGE plpgsql

AS $$
DECLARE
		v_group_id BIGINT;

BEGIN
		INSERT INTO training_data.dim_groups(group_number)
		VALUES (i_group_number)
		RETURNING group_id INTO v_group_id;

		RAISE NOTICE 'New group % added! ID = %',i_group_number, v_group_id;
		
		RETURN v_group_id;
END;
$$;

SELECT add_new_group (1111);

SELECT * FROM training_data.dim_groups;


