\c projectdatabase

create table assets_banks (company varchar(200), assets_billions int);
create table num_emp_banks (company varchar(200), num_emp int);

\copy assets_banks FROM '/home/w205/w205project/final_project/non_critical_datasource/assets_banks.csv' WITH DELIMITER ',' CSV HEADER
\copy num_emp_banks FROM '/home/w205/w205project/final_project/non_critical_datasource/num_emp_banks.csv' WITH DELIMITER ',' CSV HEADER

update assets_banks set company = 'JPMorgan Chase & Co.' where company = 'JPMorgan Chase';

update assets_banks set company = 'Wells Fargo & Company' where company = 'Wells Fargo';

update assets_banks set company = 'Citibank' where company = 'Citigroup';

update assets_banks set company = 'Goldman Sachs Bank USA' where company = 'Goldman Sachs';

update assets_banks set company = 'BNY Mellon' where company = 'The Bank of New York Mellon';

update assets_banks set company = 'HSBC North America Holdings Inc.' where company = 'HSBC Bank USA';

update assets_banks set company = 'Charles Schwab Bank' where company = 'Charles Schwab Corporation';

update assets_banks set company = 'BB&T Financial' where company = 'BB&T';

update assets_banks set company = 'SunTrust Banks, Inc.' where company = 'SunTrust Banks';

update assets_banks set company = 'Ally Financial Inc.' where company = 'Ally Financial';

update assets_banks set company = 'Union Bank' where company = 'MUFG Union Bank';

update assets_banks set company = 'Citizens Financial Group, Inc.' where company = 'Citizens Financial Group';

update assets_banks set company = 'USAA Savings' where company = 'USAA';

update assets_banks set company = 'Santander Bank US' where company = 'Santander Bank';

update assets_banks set company = 'BMO Harris' where company = 'BMO Harris Bank';

update assets_banks set company = 'M&T Bank Corporation' where company = 'M&T Bank';

update assets_banks set company = 'The Northern Trust Company' where company = 'Northern Trust Corporation';

update assets_banks set company = 'The Huntington National Bank' where company = 'Huntington Bancshares';

update assets_banks set company = 'Discover' where company = 'Discover Financial';

update assets_banks set company = 'Zions Bancorporation' where company = 'Zions Bancorp';

update assets_banks set company = 'E*Trade Bank' where company = 'E-Trade';

update assets_banks set company = 'Fifth Third Financial Corporation' where company = 'Fifth Third Bank';

update assets_banks set company = 'New York Community Bank' where company = 'New York Community Bancorp';

create table join_assets_banks_1 as select c.company, issue, state, product,assets_billions from ccdata n join assets_banks c on n.company = c.company;

create table issues_count_assets as select company,count(issue),assets_billions from join_assets_banks_1 group by company,assets_billions order by count(issue) DESC;

update num_emp_banks set company = 'JPMorgan Chase & Co.' where company = 'JPMorgan Chase Bank';

update num_emp_banks set company = 'U.S. Bancorp' where company = 'U.S. Bank';

update num_emp_banks set company = 'Wells Fargo & Company' where company = 'Wells Fargo Bank';

update num_emp_banks set company = 'PNC Bank N.A.' where company = 'PNC Bank';

update num_emp_banks set company = 'BNY Mellon' where company = 'The Bank of New York Mellon';

update num_emp_banks set company = 'TD Bank N.A.' where company = 'TD Bank';

update num_emp_banks set company = 'SunTrust Banks, Inc.' where company = 'SunTrust Bank';

update num_emp_banks set company = 'Regions Financial Corporation' where company = 'Regions Bank';

update num_emp_banks set company = 'KeyCorp' where company = 'KeyBank';

update num_emp_banks set company = 'Fifth Third Financial Corporation' where company = 'Fifth Third Bank';

update num_emp_banks set company = 'Citizens Financial Group, Inc.' where company = 'Citizens Bank';

create table join_num_emp_banks_1 as select c.company, issue, state, product, num_emp from ccdata n join num_emp_banks c on n.company = c.company;

create table issues_count_num_emp as select company,count(issue),num_emp from join_num_emp_banks_1 group by company,num_emp order by count(issue) DESC;


