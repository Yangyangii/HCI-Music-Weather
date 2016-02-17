- cnt_artist_all_rm_2015 : 2015년 12월 31일까지 아티스트별 진입 총 횟수, 2 이상의 cnt 값은 1로 지정

- cnt_title_all_rm_2015 : 2015년 12월 31일까지 타이틀별 진입 총 횟수, 2 이상의 cnt 값은 1로 지정

- logistic_section_THW : integrated에서 진입 횟수에서 2이상을 가지던 ID 들의 값을 모두 1로 지정, THW를 section별로 구분한 값 추가.

- mania_data_revised : 매니아차트 데이터 2012년 1월 1일 부터 2015년 12월 31일까지의 데이터

- weather_to2015 : 날씨 데이터 2015년 12월 31일까지의 데이터

- RESULT_SectTHW_SsRaSnMonthWc : 
	*** features = 'T0 + T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + H0 + H1 + H2 + H3 + H4 + H5 + H6 + H7 + H8 + H9 + W0 + W1 + Season + Rain + Snow + Month + wind_chill
	위의 features로 logistic regression을 수행한 값.
	랜덤 샘플을 0과 1에서 100개씩 뽑아서 set과 model을 만들었는데, 진입횟수가 2이상의 데이터가 들어간 곡, 아티스트에서 날짜별 진입횟수가 100회가 나오지 않는 경우가 생겼다. 그에 따른 곡들 및 가수들은 값이 -1로 지정해서 출력되어 있다.