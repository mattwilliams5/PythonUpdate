-- customers date_of_birth
-- depends: 20211107_01_xppef-customers-table
ALTER TABLE customers
    ADD COLUMN date_of_birth TIMESTAMP;
