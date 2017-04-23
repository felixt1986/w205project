#!/bin/bash
MY_CWD=$(pwd)

psql -U postgres -f create_asset_employee_table.sql
exit
