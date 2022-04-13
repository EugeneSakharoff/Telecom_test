# Telecom_test
Competition task for Institure of Telecommunication
Основные размышления по анализу данных, подбору модели, комментарии, графики и пр. содержатся в jupyter notebook-е pm1.ipynb
  	pm1.py содержит код для запуска готовых моделей для прогнозирования на датасете data.xlsx и сохраняет результат в result.xlsx согласно заданию. Он, по сути копирует код из pm1.ipynb, так что все пояснения и комментарии в первом файле. Для работы необходимы NeuralNet.pkl, XGBoost.pkl, Forest.pkl, encoder.pkl, scaler.pkl
	pm2.py содержит код для вывода содержимого таблиц базы данных database.db согласно заданию: 
После запуска ПМ, программа находится в режиме ожидания команды от оператора. 
3) В случае консольного исполнения при вводе цифирного значения и нажатия «Enter», ПМ делает соответствующий запрос в БД (Рисунок 2) и формирует ответ с выводом в терминал.
4) Примеры запросов пользователя и ответы ПМ представлены следующим перечнем:
	1 – Ответ ПМ: Выводит все последние записи (см. последнюю временную метку TYME) вида
ID – B – A
с сортировкой по увеличению значения D 
	2 –  Ответ ПМ: Вывести последнюю запись (см. последнюю временную метку TYME) вида
					//Ф/Ф/Ф – Ф+Ф
	9 – закончить выполнение 2-го ПМ.


	data.xlsx - датасет для обучения
	result.xlsl - результат согласно требованиям задания
	NeuralNet.pkl, XGBoost.pkl, Forest.pkl, encoder.pkl, scaler.pkl - обученные модели нейросети, градиентного бустинга и случайного леса, а также параметры препроцессинга.
(ПРИМЕЧАНИЕ: Forest.pkl оказался слишком большим для загрузки на гитхаб. Пришлю его отдельно)
	database.db - база данных с тремя таблицами, согласно требованиям задания

Таблицы в базе данных созданы следующим образом:
  CREATE TABLE A ( id INTEGER PRIMARY KEY, A INTEGER);
  CREATE TABLE I ([//I/I/I] TEXT, [I+I] TEXT);
CREATE TABLE BD (id INTEGER PRIMARY KEY, B INTEGER, D REAL, TYME TEXT);
Запросы к БД выполняются следующие:
SELECT A.id,BD.B,A.A 
FROM BD JOIN A ON BD.id=A.id 
WHERE BD.TYME = (SELECT MAX(BD.TYME) FROM BD) 
ORDER BY D;

SELECT [//I/I/I]||'-'||[I+I] FROM I ORDER BY rowid DESC LIMIT 1