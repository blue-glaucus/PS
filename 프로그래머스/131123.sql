-- 프로그래머스 No.131123 즐겨찾기가 가장 많은 식당 정보 출력하기
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES from rest_info
    where (food_type, favorites) in (select food_type, max(favorites) from rest_info group by food_type)
    order by food_type desc
;