create database bestproducts;

use bestproducts;

INSERT INTO items VALUES('2021114418','[디스커버리](공용) 비글 V2 DXSHE1031DXSHE2031', 54500, 40330, 26, '롯데백화점1관');

INSERT INTO ranking (main_category, sub_category, item_ranking, item_code) VALUES('ALL','ALL', '1', '2021114418');

select * from items;

delete from ranking where item_code = '2021114418';

delete from items where item_code = '2021114418';
