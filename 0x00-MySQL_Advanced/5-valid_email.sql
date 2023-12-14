-- 5-valid_email.sql
DROP TRIGGER IF EXISTS resetEmail
DELIMITER $$
CREATE TRIGGER resetEmail
BEFORE UPDATE ON users
FOR EACH ROW 
BEGIN
        IF NEW.email != OLD.email THEN
            SET valid_email = 0;
        END IF;
END$$
DELIMITER ;
