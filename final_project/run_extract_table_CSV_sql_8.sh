#!/bin/bash
MY_CWD=$(pwd)

psql -U postgres -f extract_table_CSV.sql
exit
