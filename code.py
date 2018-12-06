{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## МатеМаркетинг 2018"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Применение Python в аналитике "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Александр Швец "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### https://fb.com/ashwets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Программирование для аналитика становится незаменимым инструментом, который приходит на помощь, когда другие средства уже испробованы. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Пример – отсортировать пользователей по длине цепочки"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Скачать логи из Метрики"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 395,
   "metadata": {},
   "outputs": [],
   "source": [
    "BASE_API_URL = 'https://api-metrika.yandex.ru/management/v1'\n",
    "COUNTER_ID = ''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Создать приложение"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Управление приложениями: https://oauth.yandex.ru/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [],
   "source": [
    "APP_ID = ''\n",
    "APP_SECRET = ''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Пройти по ссылке и получить код\n",
    "\n",
    "https://oauth.yandex.ru/authorize?response_type=code&client_id={APP_ID}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 396,
   "metadata": {},
   "outputs": [],
   "source": [
    "CODE = ''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Получить access_token"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 397,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.post(\n",
    "    'https://oauth.yandex.ru/token',\n",
    "    data = {\n",
    "        'grant_type': 'authorization_code',\n",
    "        'code': CODE,\n",
    "        'client_id': APP_ID,\n",
    "        'client_secret': APP_SECRET\n",
    "    }\n",
    ")\n",
    "data = r.json()\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "access_token = data['access_token']\n",
    "access_token"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4. Отправить запрос на получение логов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://tech.yandex.ru/metrika/doc/api2/logs/fields/hits-docpage/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 400,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'log_request': {'request_id': 1722716,\n",
       "  'counter_id': 48976394,\n",
       "  'source': 'hits',\n",
       "  'date1': '2018-10-01',\n",
       "  'date2': '2018-10-31',\n",
       "  'fields': ['ym:pv:watchID',\n",
       "   'ym:pv:date',\n",
       "   'ym:pv:dateTime',\n",
       "   'ym:pv:URL',\n",
       "   'ym:pv:browser',\n",
       "   'ym:pv:ipAddress',\n",
       "   'ym:pv:regionCity',\n",
       "   'ym:pv:regionCountry',\n",
       "   'ym:pv:UTMSource',\n",
       "   'ym:pv:UTMMedium',\n",
       "   'ym:pv:goalsID',\n",
       "   'ym:pv:clientID'],\n",
       "  'status': 'created'}}"
      ]
     },
     "execution_count": 400,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "start_date = '2018-10-01'\n",
    "end_date = '2018-10-31'\n",
    "fields = (\n",
    "    'ym:pv:watchID,ym:pv:date,ym:pv:dateTime'\n",
    "    ',ym:pv:URL,ym:pv:browser,ym:pv:ipAddress'\n",
    "    ',ym:pv:regionCity,ym:pv:regionCountry'\n",
    "    ',ym:pv:UTMSource,ym:pv:UTMMedium'\n",
    "    ',ym:pv:goalsID,ym:pv:clientID'\n",
    ")\n",
    "\n",
    "r = requests.post(\n",
    "    BASE_API_URL + \n",
    "    f'/counter/{COUNTER_ID}/logrequests'\n",
    "    f'?date1={start_date}&date2={end_date}'\n",
    "    f'&fields={fields}'\n",
    "    f'&source=hits&oauth_token={access_token}'\n",
    ")\n",
    "data = r.json()\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "metadata": {},
   "outputs": [],
   "source": [
    "request_id = data['log_request']['request_id']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5. Проверить готовность"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 402,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'log_request': {'request_id': 1722716,\n",
       "  'counter_id': 48976394,\n",
       "  'source': 'hits',\n",
       "  'date1': '2018-10-01',\n",
       "  'date2': '2018-10-31',\n",
       "  'fields': ['ym:pv:watchID',\n",
       "   'ym:pv:date',\n",
       "   'ym:pv:dateTime',\n",
       "   'ym:pv:URL',\n",
       "   'ym:pv:browser',\n",
       "   'ym:pv:ipAddress',\n",
       "   'ym:pv:regionCity',\n",
       "   'ym:pv:regionCountry',\n",
       "   'ym:pv:UTMSource',\n",
       "   'ym:pv:UTMMedium',\n",
       "   'ym:pv:goalsID',\n",
       "   'ym:pv:clientID'],\n",
       "  'status': 'processed',\n",
       "  'size': 404385,\n",
       "  'parts': [{'part_number': 0, 'size': 404385}]}}"
      ]
     },
     "execution_count": 402,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r = requests.get(\n",
    "    BASE_API_URL + \n",
    "    f'/counter/{COUNTER_ID}'\n",
    "    f'/logrequest/{request_id}'\n",
    "    f'?oauth_token={access_token}'\n",
    ")\n",
    "data = r.json()\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6. Скачать файл"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 403,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.get(\n",
    "    BASE_API_URL + \n",
    "    f'/counter/{COUNTER_ID}'\n",
    "    f'/logrequest/{request_id}'\n",
    "    f'/part/0/download'\n",
    "    f'?oauth_token={access_token}'\n",
    ")\n",
    "\n",
    "with open(\"logs.csv\", \"w+\") as f:\n",
    "    f.write(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 404,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ym:pv:watchID\tym:pv:date\tym:pv:dateTime\tym:pv:URL\tym:pv:browser\tym:pv:ipAddress\tym:pv:regionCity\tym:pv:regionCountry\tym:pv:UTMSource\tym:pv:UTMMedium\tym:pv:goalsID\tym:pv:clientID\r\n",
      "6169566724246146523\t2018-10-19\t2018-10-19 12:30:29\thttps://digitalgod.be/tilda/popup/rec55736042/opened\tyandex_browser\t37.190.76.xxx\tMoscow\tRussia\t\t\t[38936770]\t1538573450747324629\r\n",
      "6169576288183848411\t2018-10-19\t2018-10-19 12:31:05\thttps://digitalgod.be/policy\tyandex_browser\t37.190.76.xxx\tMoscow\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6169578335461641691\t2018-10-19\t2018-10-19 12:31:13\thttps://digitalgod.be/oferta_pdf\tyandex_browser\t37.190.76.xxx\tMoscow\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6169629121979551071\t2018-10-19\t2018-10-19 12:34:27\thttps://digitalgod.be/pay?amount=4000000&order_id=2018101801\tyandex_browser\t37.190.76.xxx\tMoscow\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6174028643877195353\t2018-10-19\t2018-10-19 17:14:10\thttps://digitalgod.be/policy\tyandex_browser\t178.57.86.xxx\tPodolsk\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6174030139163086425\t2018-10-19\t2018-10-19 17:14:15\thttps://digitalgod.be/\tyandex_browser\t178.57.86.xxx\tPodolsk\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6174034073746345561\t2018-10-19\t2018-10-19 17:14:30\thttps://digitalgod.be/\tyandex_browser\t178.57.86.xxx\tPodolsk\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6175321529871437632\t2018-10-19\t2018-10-19 18:36:22\thttps://digitalgod.be/digital-rockstar\tyandex_browser\t178.57.86.xxx\tPodolsk\tRussia\t\t\t[]\t1538573450747324629\r\n",
      "6175325465391599424\t2018-10-19\t2018-10-19 18:36:37\thttps://digitalgod.be/digital-rockstar\tyandex_browser\t178.57.86.xxx\tPodolsk\tRussia\t\t\t[]\t1538573450747324629\r\n"
     ]
    }
   ],
   "source": [
    "!head logs.csv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Загрузить данные в Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 405,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 406,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ym:pv:watchID</th>\n",
       "      <th>ym:pv:date</th>\n",
       "      <th>ym:pv:dateTime</th>\n",
       "      <th>ym:pv:URL</th>\n",
       "      <th>ym:pv:browser</th>\n",
       "      <th>ym:pv:ipAddress</th>\n",
       "      <th>ym:pv:regionCity</th>\n",
       "      <th>ym:pv:regionCountry</th>\n",
       "      <th>ym:pv:UTMSource</th>\n",
       "      <th>ym:pv:UTMMedium</th>\n",
       "      <th>ym:pv:goalsID</th>\n",
       "      <th>ym:pv:clientID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6169566724246146523</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>2018-10-19 12:30:29</td>\n",
       "      <td>https://digitalgod.be/tilda/popup/rec55736042/...</td>\n",
       "      <td>yandex_browser</td>\n",
       "      <td>37.190.76.xxx</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>Russia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[38936770]</td>\n",
       "      <td>1538573450747324629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6169576288183848411</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>2018-10-19 12:31:05</td>\n",
       "      <td>https://digitalgod.be/policy</td>\n",
       "      <td>yandex_browser</td>\n",
       "      <td>37.190.76.xxx</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>Russia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[]</td>\n",
       "      <td>1538573450747324629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>6169578335461641691</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>2018-10-19 12:31:13</td>\n",
       "      <td>https://digitalgod.be/oferta_pdf</td>\n",
       "      <td>yandex_browser</td>\n",
       "      <td>37.190.76.xxx</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>Russia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[]</td>\n",
       "      <td>1538573450747324629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>6169629121979551071</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>2018-10-19 12:34:27</td>\n",
       "      <td>https://digitalgod.be/pay?amount=4000000&amp;order...</td>\n",
       "      <td>yandex_browser</td>\n",
       "      <td>37.190.76.xxx</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>Russia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[]</td>\n",
       "      <td>1538573450747324629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6174028643877195353</td>\n",
       "      <td>2018-10-19</td>\n",
       "      <td>2018-10-19 17:14:10</td>\n",
       "      <td>https://digitalgod.be/policy</td>\n",
       "      <td>yandex_browser</td>\n",
       "      <td>178.57.86.xxx</td>\n",
       "      <td>Podolsk</td>\n",
       "      <td>Russia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>[]</td>\n",
       "      <td>1538573450747324629</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         ym:pv:watchID  ym:pv:date       ym:pv:dateTime  \\\n",
       "0  6169566724246146523  2018-10-19  2018-10-19 12:30:29   \n",
       "1  6169576288183848411  2018-10-19  2018-10-19 12:31:05   \n",
       "2  6169578335461641691  2018-10-19  2018-10-19 12:31:13   \n",
       "3  6169629121979551071  2018-10-19  2018-10-19 12:34:27   \n",
       "4  6174028643877195353  2018-10-19  2018-10-19 17:14:10   \n",
       "\n",
       "                                           ym:pv:URL   ym:pv:browser  \\\n",
       "0  https://digitalgod.be/tilda/popup/rec55736042/...  yandex_browser   \n",
       "1                       https://digitalgod.be/policy  yandex_browser   \n",
       "2                   https://digitalgod.be/oferta_pdf  yandex_browser   \n",
       "3  https://digitalgod.be/pay?amount=4000000&order...  yandex_browser   \n",
       "4                       https://digitalgod.be/policy  yandex_browser   \n",
       "\n",
       "  ym:pv:ipAddress ym:pv:regionCity ym:pv:regionCountry ym:pv:UTMSource  \\\n",
       "0   37.190.76.xxx           Moscow              Russia             NaN   \n",
       "1   37.190.76.xxx           Moscow              Russia             NaN   \n",
       "2   37.190.76.xxx           Moscow              Russia             NaN   \n",
       "3   37.190.76.xxx           Moscow              Russia             NaN   \n",
       "4   178.57.86.xxx          Podolsk              Russia             NaN   \n",
       "\n",
       "  ym:pv:UTMMedium ym:pv:goalsID       ym:pv:clientID  \n",
       "0             NaN    [38936770]  1538573450747324629  \n",
       "1             NaN            []  1538573450747324629  \n",
       "2             NaN            []  1538573450747324629  \n",
       "3             NaN            []  1538573450747324629  \n",
       "4             NaN            []  1538573450747324629  "
      ]
     },
     "execution_count": 406,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('logs.csv', sep='\\t')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Сгруппировать по clientID и посчитать сумму"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 407,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"2\" halign=\"left\">ym:pv:dateTime</th>\n",
       "      <th>ym:pv:watchID</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>min</th>\n",
       "      <th>max</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ym:pv:clientID</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15385140039013017</th>\n",
       "      <td>2018-10-03 00:00:03</td>\n",
       "      <td>2018-10-03 00:00:18</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15385628009721447</th>\n",
       "      <td>2018-10-03 13:33:44</td>\n",
       "      <td>2018-10-03 13:39:38</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15394424317172889</th>\n",
       "      <td>2018-10-13 17:53:50</td>\n",
       "      <td>2018-10-13 17:54:39</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15395235382904960</th>\n",
       "      <td>2018-10-14 16:25:44</td>\n",
       "      <td>2018-10-14 16:26:27</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15405533795557369</th>\n",
       "      <td>2018-10-26 14:29:39</td>\n",
       "      <td>2018-10-26 14:36:27</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        ym:pv:dateTime                      ym:pv:watchID\n",
       "                                   min                  max         count\n",
       "ym:pv:clientID                                                           \n",
       "15385140039013017  2018-10-03 00:00:03  2018-10-03 00:00:18             2\n",
       "15385628009721447  2018-10-03 13:33:44  2018-10-03 13:39:38             3\n",
       "15394424317172889  2018-10-13 17:53:50  2018-10-13 17:54:39             3\n",
       "15395235382904960  2018-10-14 16:25:44  2018-10-14 16:26:27             2\n",
       "15405533795557369  2018-10-26 14:29:39  2018-10-26 14:36:27             5"
      ]
     },
     "execution_count": 407,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = df.groupby('ym:pv:clientID').agg(\n",
    "    {'ym:pv:dateTime': ['min', 'max'], 'ym:pv:watchID': 'count'})\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 408,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2.columns = ['min_date', 'max_date', 'event_count']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 409,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>min_date</th>\n",
       "      <th>max_date</th>\n",
       "      <th>event_count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ym:pv:clientID</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15385140039013017</th>\n",
       "      <td>2018-10-03 00:00:03</td>\n",
       "      <td>2018-10-03 00:00:18</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15385628009721447</th>\n",
       "      <td>2018-10-03 13:33:44</td>\n",
       "      <td>2018-10-03 13:39:38</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15394424317172889</th>\n",
       "      <td>2018-10-13 17:53:50</td>\n",
       "      <td>2018-10-13 17:54:39</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15395235382904960</th>\n",
       "      <td>2018-10-14 16:25:44</td>\n",
       "      <td>2018-10-14 16:26:27</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15405533795557369</th>\n",
       "      <td>2018-10-26 14:29:39</td>\n",
       "      <td>2018-10-26 14:36:27</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              min_date             max_date  event_count\n",
       "ym:pv:clientID                                                          \n",
       "15385140039013017  2018-10-03 00:00:03  2018-10-03 00:00:18            2\n",
       "15385628009721447  2018-10-03 13:33:44  2018-10-03 13:39:38            3\n",
       "15394424317172889  2018-10-13 17:53:50  2018-10-13 17:54:39            3\n",
       "15395235382904960  2018-10-14 16:25:44  2018-10-14 16:26:27            2\n",
       "15405533795557369  2018-10-26 14:29:39  2018-10-26 14:36:27            5"
      ]
     },
     "execution_count": 409,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Сортируем и смотрим"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 411,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>min_date</th>\n",
       "      <th>max_date</th>\n",
       "      <th>event_count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ym:pv:clientID</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1538606015954062469</th>\n",
       "      <td>2018-10-04 01:33:34</td>\n",
       "      <td>2018-10-31 16:54:30</td>\n",
       "      <td>154</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1538573450747324629</th>\n",
       "      <td>2018-10-03 16:30:49</td>\n",
       "      <td>2018-10-31 21:42:01</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1527249799944773995</th>\n",
       "      <td>2018-10-01 11:10:16</td>\n",
       "      <td>2018-10-26 12:26:15</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1540299424761676344</th>\n",
       "      <td>2018-10-23 15:57:03</td>\n",
       "      <td>2018-10-31 16:14:44</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1535444819483699699</th>\n",
       "      <td>2018-10-03 11:51:54</td>\n",
       "      <td>2018-10-31 11:48:04</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1539354733205066788</th>\n",
       "      <td>2018-10-12 17:32:12</td>\n",
       "      <td>2018-10-20 12:21:16</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1539767234985239045</th>\n",
       "      <td>2018-10-17 12:07:14</td>\n",
       "      <td>2018-10-31 19:37:02</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15354432301048978497</th>\n",
       "      <td>2018-10-03 16:21:15</td>\n",
       "      <td>2018-10-10 12:20:10</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1535637578238807740</th>\n",
       "      <td>2018-10-12 20:16:49</td>\n",
       "      <td>2018-10-28 13:39:14</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1533833331979449812</th>\n",
       "      <td>2018-10-02 09:23:43</td>\n",
       "      <td>2018-10-30 21:37:00</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 min_date             max_date  event_count\n",
       "ym:pv:clientID                                                             \n",
       "1538606015954062469   2018-10-04 01:33:34  2018-10-31 16:54:30          154\n",
       "1538573450747324629   2018-10-03 16:30:49  2018-10-31 21:42:01           75\n",
       "1527249799944773995   2018-10-01 11:10:16  2018-10-26 12:26:15           60\n",
       "1540299424761676344   2018-10-23 15:57:03  2018-10-31 16:14:44           28\n",
       "1535444819483699699   2018-10-03 11:51:54  2018-10-31 11:48:04           27\n",
       "1539354733205066788   2018-10-12 17:32:12  2018-10-20 12:21:16           26\n",
       "1539767234985239045   2018-10-17 12:07:14  2018-10-31 19:37:02           23\n",
       "15354432301048978497  2018-10-03 16:21:15  2018-10-10 12:20:10           23\n",
       "1535637578238807740   2018-10-12 20:16:49  2018-10-28 13:39:14           22\n",
       "1533833331979449812   2018-10-02 09:23:43  2018-10-30 21:37:00           21"
      ]
     },
     "execution_count": 411,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.sort_values('event_count', ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Как посмотреть хвост?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x127bf6eb8>"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "df2[df2.event_count < 15].groupby('event_count').count().plot.bar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Не хотите париться с обновлением данных? Используйте Rockstat!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://rock.st/docs/intro/getting-started/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"https://rock.st/static/images/docs/schemas/request-lifecycle.svg\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Подключаемся к безе с помощью clickhouse_driver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 412,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "from clickhouse_driver import Client\n",
    "client = Client('localhost', port=9000, database='stats')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Смотрим, сколько событий есть в базе"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 413,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(755883,)]"
      ]
     },
     "execution_count": 413,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "client.execute('select count(*) from stats.events')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### А как устроена сама табличка?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 414,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('id', 'UInt64', '', ''),\n",
       " ('uid', 'UInt64', '', ''),\n",
       " ('date', 'Date', '', ''),\n",
       " ('dateTime', 'DateTime', '', ''),\n",
       " ('timestamp', 'UInt64', '', ''),\n",
       " ('channel', 'String', '', ''),\n",
       " ('projectId', 'UInt32', '', ''),\n",
       " ('name', 'String', '', ''),\n",
       " ('service', 'String', '', ''),\n",
       " ('td_ip', 'String', '', ''),\n",
       " ('td_ua', 'String', '', ''),\n",
       " ('td_fpid', 'UInt64', '', ''),\n",
       " ('page_url', 'String', '', ''),\n",
       " ('page_ref', 'String', '', ''),\n",
       " ('page_title', 'String', '', ''),\n",
       " ('page_domain', 'String', '', ''),\n",
       " ('page_scheme', 'String', '', ''),\n",
       " ('page_query_utm_source', 'String', '', ''),\n",
       " ('page_query_utm_campaign', 'String', '', ''),\n",
       " ('page_query_utm_medium', 'String', '', ''),\n",
       " ('page_query_utm_content', 'String', '', ''),\n",
       " ('page_query_utm_term', 'String', '', ''),\n",
       " ('page_query_gclid', 'String', '', ''),\n",
       " ('page_query_yclid', 'String', '', ''),\n",
       " ('page_query_extra.key', 'Array(String)', '', ''),\n",
       " ('page_query_extra.value', 'Array(String)', '', ''),\n",
       " ('sess_type', 'String', '', ''),\n",
       " ('sess_engine', 'String', '', ''),\n",
       " ('sess_num', 'UInt16', '', ''),\n",
       " ('sess_hasMarks', 'UInt8', '', ''),\n",
       " ('sess_pageNum', 'UInt16', '', ''),\n",
       " ('sess_eventNum', 'UInt16', '', ''),\n",
       " ('sess_marks_utm_source', 'String', '', ''),\n",
       " ('sess_marks_utm_campaign', 'String', '', ''),\n",
       " ('sess_marks_utm_medium', 'String', '', ''),\n",
       " ('sess_marks_utm_content', 'String', '', ''),\n",
       " ('sess_marks_utm_term', 'String', '', ''),\n",
       " ('sess_marks_has_gclid', 'Int8', 'DEFAULT', '-1'),\n",
       " ('sess_marks_has_yclid', 'Int8', 'DEFAULT', '-1'),\n",
       " ('sess_marks_extra.key', 'Array(String)', '', ''),\n",
       " ('sess_marks_extra.value', 'Array(String)', '', ''),\n",
       " ('sess_start', 'UInt64', '', ''),\n",
       " ('sess_refhost', 'String', '', ''),\n",
       " ('lib_id', 'String', '', ''),\n",
       " ('lib_v', 'Float32', '', ''),\n",
       " ('lib_sv', 'Float32', '', ''),\n",
       " ('scroll_dh', 'UInt16', '', ''),\n",
       " ('scroll_ch', 'UInt16', '', ''),\n",
       " ('scroll_to', 'Int32', '', ''),\n",
       " ('scroll_cs', 'UInt16', '', ''),\n",
       " ('scroll_ms', 'UInt16', '', ''),\n",
       " ('browser_if1', 'Int8', '', ''),\n",
       " ('browser_if2', 'Int8', '', ''),\n",
       " ('browser_w', 'Int16', '', ''),\n",
       " ('browser_h', 'Int16', '', ''),\n",
       " ('browser_tw', 'Int16', '', ''),\n",
       " ('browser_th', 'Int16', '', ''),\n",
       " ('browser_aw', 'Int16', '', ''),\n",
       " ('browser_ah', 'Int16', '', ''),\n",
       " ('browser_sopr', 'Int16', '', ''),\n",
       " ('browser_soa', 'Int16', '', ''),\n",
       " ('browser_sot', 'String', '', ''),\n",
       " ('browser_plt', 'String', '', ''),\n",
       " ('browser_prd', 'String', '', ''),\n",
       " ('sxgeo_country_iso', 'String', '', ''),\n",
       " ('sxgeo_country_ru', 'String', '', ''),\n",
       " ('sxgeo_country_en', 'String', '', ''),\n",
       " ('sxgeo_region_iso', 'String', '', ''),\n",
       " ('sxgeo_region_ru', 'String', '', ''),\n",
       " ('sxgeo_region_en', 'String', '', ''),\n",
       " ('sxgeo_city_ru', 'String', '', ''),\n",
       " ('sxgeo_city_en', 'String', '', ''),\n",
       " ('mmgeo_country_iso', 'String', '', ''),\n",
       " ('mmgeo_country_ru', 'String', '', ''),\n",
       " ('mmgeo_country_en', 'String', '', ''),\n",
       " ('mmgeo_region_iso', 'String', '', ''),\n",
       " ('mmgeo_region_ru', 'String', '', ''),\n",
       " ('mmgeo_region_en', 'String', '', ''),\n",
       " ('mmgeo_city_ru', 'String', '', ''),\n",
       " ('mmgeo_city_en', 'String', '', ''),\n",
       " ('uaparser_is_bot', 'Int8', '', ''),\n",
       " ('uaparser_is_mob', 'Int8', '', ''),\n",
       " ('uaparser_is_pc', 'Int8', '', ''),\n",
       " ('uaparser_browser_family', 'String', '', ''),\n",
       " ('uaparser_browser_version', 'Array(Int16)', '', ''),\n",
       " ('uaparser_os_family', 'String', '', ''),\n",
       " ('uaparser_os_version', 'Array(Int16)', '', ''),\n",
       " ('uaparser_device_family', 'String', '', ''),\n",
       " ('uaparser_device_brand', 'String', '', ''),\n",
       " ('uaparser_device_model', 'String', '', ''),\n",
       " ('user_tz', 'String', '', ''),\n",
       " ('user_ts', 'UInt64', '', ''),\n",
       " ('user_tzo', 'Int32', '', ''),\n",
       " ('user_id', 'String', '', ''),\n",
       " ('user_gaId', 'String', '', ''),\n",
       " ('user_ymId', 'String', '', ''),\n",
       " ('user_extra.key', 'Array(String)', '', ''),\n",
       " ('user_extra.value', 'Array(String)', '', ''),\n",
       " ('data_extra.key', 'Array(String)', '', ''),\n",
       " ('data_extra.value', 'Array(String)', '', ''),\n",
       " ('char_ls', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('char_ae', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('char_pr', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('char_sb', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('char_ab', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('char_wp', 'Int16', 'DEFAULT', \"CAST(-1, 'Int16')\"),\n",
       " ('perf_cs', 'Int16', '', ''),\n",
       " ('perf_scs', 'Int16', '', ''),\n",
       " ('perf_dl', 'Int16', '', ''),\n",
       " ('perf_dc', 'Int16', '', ''),\n",
       " ('perf_di', 'Int16', '', ''),\n",
       " ('perf_rqs', 'Int16', '', ''),\n",
       " ('perf_rss', 'Int16', '', ''),\n",
       " ('perf_rse', 'Int16', '', ''),\n",
       " ('perf_ce', 'Int16', '', ''),\n",
       " ('td_ref', 'String', '', ''),\n",
       " ('td_extra.key', 'Array(String)', '', ''),\n",
       " ('td_extra.value', 'Array(String)', '', ''),\n",
       " ('uaparser_is_tablet', 'Int8', '', '')]"
      ]
     },
     "execution_count": 414,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "columns = client.execute('describe stats.events')\n",
    "columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns_names = [c[0] for c in columns]\n",
    "columns_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "row = client.execute('select * from stats.events limit 1')[0]\n",
    "row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dict(zip(columns_names, row))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Сколько событий приходится на пользователя?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 418,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(6429106493513007104, 2754),\n",
       " (4802820771467024644, 2398),\n",
       " (4902632813516717324, 2349),\n",
       " (6450654288413720576, 2189),\n",
       " (4848992795889329028, 2024),\n",
       " (6438378184260976640, 1379),\n",
       " (4802795175135142680, 1243),\n",
       " (6456157835024662528, 1128),\n",
       " (4859329238762284997, 765),\n",
       " (4838260717241739745, 745)]"
      ]
     },
     "execution_count": 418,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "client.execute('select uid, count(*) cnt from stats.events group by uid order by cnt desc limit 10')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Выберем уникальные каналы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "client.execute(\n",
    "    \"select groupUniqArray(concat(extract(page_url, 'utm_source=([^&]*)'), '/', extract(page_url, 'utm_medium=([^&]*)'))) from stats.events limit 5\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Сколько пользователей у нас в выборке?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 420,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(82425,)]"
      ]
     },
     "execution_count": 420,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "client.execute('select count(*) from (select uid from stats.events group by uid)')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Какие события есть?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 421,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('field_blur', 22513),\n",
       " ('session', 148899),\n",
       " ('page', 178125),\n",
       " ('field_invalid', 146),\n",
       " ('field_change', 14525),\n",
       " ('page_loaded', 153839),\n",
       " ('form_submit', 4912),\n",
       " ('link_click', 129242),\n",
       " ('field_focus', 25819),\n",
       " ('page_unload', 77863)]"
      ]
     },
     "execution_count": 421,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = client.execute(\n",
    "    \"select name, count(*)\"\n",
    "    \" from stats.events\"\n",
    "    \" group by name\"\n",
    ")\n",
    "data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## А теперь самый смак! Динамическая атрибуция!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Выберем пользователей с цепочками каналов"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 423,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(6445752572006367232,\n",
       "  'yandex/cpc',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 19, 21, 7, 27)),\n",
       " (6456110767337897984,\n",
       "  'yandex/cpc',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 11, 11, 19, 18)),\n",
       " (6455300595598229504,\n",
       "  'yandex/cpc',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 9, 5, 43, 1)),\n",
       " (6455421778679300096,\n",
       "  'devina/sms',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 9, 13, 42, 42)),\n",
       " (6455731130443235328,\n",
       "  'yandex/cpc',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 10, 10, 10, 46)),\n",
       " (6456220148545093632, '/', 0, datetime.datetime(2018, 10, 11, 18, 33, 55)),\n",
       " (6458257014127591424, '/', 0, datetime.datetime(2018, 10, 17, 9, 28, 5)),\n",
       " (4878189615918466984,\n",
       "  '/,sailplay/email',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 18, 13, 59, 43)),\n",
       " (6456909424182165504,\n",
       "  'yandex/cpc',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 13, 16, 13)),\n",
       " (6452748257373192192,\n",
       "  'facebook/smm',\n",
       "  0,\n",
       "  datetime.datetime(2018, 10, 2, 4, 38, 7))]"
      ]
     },
     "execution_count": 423,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = client.execute(\n",
    "    \"select uid, arrayStringConcat(groupUniqArray(\"\n",
    "        \"concat(\"\n",
    "            \"extract(page_url, 'utm_source=([^&]*)'), '/', extract(page_url, 'utm_medium=([^&]*)')))\"\n",
    "        \", ',')\"\n",
    "    \", sum(name = 'form_submit'), max(dateTime)\"\n",
    "    \" from stats.events group by uid\"\n",
    ")\n",
    "data[:10]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Сформируем данные для обучения"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 424,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'channel_yandex/cpc': 1, 'time': datetime.datetime(2018, 10, 19, 21, 7, 27)},\n",
       " {'channel_yandex/cpc': 1,\n",
       "  'time': datetime.datetime(2018, 10, 11, 11, 19, 18)},\n",
       " {'channel_yandex/cpc': 1, 'time': datetime.datetime(2018, 10, 9, 5, 43, 1)},\n",
       " {'channel_devina/sms': 1, 'time': datetime.datetime(2018, 10, 9, 13, 42, 42)},\n",
       " {'channel_yandex/cpc': 1,\n",
       "  'time': datetime.datetime(2018, 10, 10, 10, 10, 46)},\n",
       " {'channel_/': 1, 'time': datetime.datetime(2018, 10, 11, 18, 33, 55)},\n",
       " {'channel_/': 1, 'time': datetime.datetime(2018, 10, 17, 9, 28, 5)},\n",
       " {'channel_/': 1,\n",
       "  'channel_sailplay/email': 1,\n",
       "  'time': datetime.datetime(2018, 10, 18, 13, 59, 43)},\n",
       " {'channel_yandex/cpc': 1, 'time': datetime.datetime(2018, 10, 13, 16, 13)},\n",
       " {'channel_facebook/smm': 1, 'time': datetime.datetime(2018, 10, 2, 4, 38, 7)}]"
      ]
     },
     "execution_count": 424,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "channels_by_user = []\n",
    "conversions = []\n",
    "for u in data:\n",
    "    (uid, channels, cvs, time) = u\n",
    "    r = {'channel_' + c: 1 for c in channels.split(',') if len(c) < 15}\n",
    "    r['time'] = time\n",
    "    channels_by_user.append(r)\n",
    "    conversions.append(1 if cvs > 0 else 0)\n",
    "channels_by_user[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 425,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 82425, 3458)"
      ]
     },
     "execution_count": 425,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conversions[:10], len(conversions), sum(conversions)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Получаем датасет"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 426,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>channel_/</th>\n",
       "      <th>channel_/sms</th>\n",
       "      <th>channel_2gis/organic</th>\n",
       "      <th>channel_Hybrid/banner</th>\n",
       "      <th>channel_Hybrid/cpc</th>\n",
       "      <th>channel_Hybrid/cpm</th>\n",
       "      <th>channel_InMobi_hr/cpm</th>\n",
       "      <th>channel_Mobiads/banner</th>\n",
       "      <th>channel_SailPlay/email</th>\n",
       "      <th>channel_TopFace/banner</th>\n",
       "      <th>...</th>\n",
       "      <th>channel_vk.com/cpc</th>\n",
       "      <th>channel_vk/</th>\n",
       "      <th>channel_vk/cpc</th>\n",
       "      <th>channel_vk/smm</th>\n",
       "      <th>channel_ya-direct/cpc</th>\n",
       "      <th>channel_yandex/cpc</th>\n",
       "      <th>channel_yandex/maps</th>\n",
       "      <th>channel_youtube/smm</th>\n",
       "      <th>channel_yp.ru/</th>\n",
       "      <th>time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-19 21:07:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-11 11:19:18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-09 05:43:01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-09 13:42:42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-10 10:10:46</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 49 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   channel_/  channel_/sms  channel_2gis/organic  channel_Hybrid/banner  \\\n",
       "0        NaN           NaN                   NaN                    NaN   \n",
       "1        NaN           NaN                   NaN                    NaN   \n",
       "2        NaN           NaN                   NaN                    NaN   \n",
       "3        NaN           NaN                   NaN                    NaN   \n",
       "4        NaN           NaN                   NaN                    NaN   \n",
       "\n",
       "   channel_Hybrid/cpc  channel_Hybrid/cpm  channel_InMobi_hr/cpm  \\\n",
       "0                 NaN                 NaN                    NaN   \n",
       "1                 NaN                 NaN                    NaN   \n",
       "2                 NaN                 NaN                    NaN   \n",
       "3                 NaN                 NaN                    NaN   \n",
       "4                 NaN                 NaN                    NaN   \n",
       "\n",
       "   channel_Mobiads/banner  channel_SailPlay/email  channel_TopFace/banner  \\\n",
       "0                     NaN                     NaN                     NaN   \n",
       "1                     NaN                     NaN                     NaN   \n",
       "2                     NaN                     NaN                     NaN   \n",
       "3                     NaN                     NaN                     NaN   \n",
       "4                     NaN                     NaN                     NaN   \n",
       "\n",
       "          ...          channel_vk.com/cpc  channel_vk/  channel_vk/cpc  \\\n",
       "0         ...                         NaN          NaN             NaN   \n",
       "1         ...                         NaN          NaN             NaN   \n",
       "2         ...                         NaN          NaN             NaN   \n",
       "3         ...                         NaN          NaN             NaN   \n",
       "4         ...                         NaN          NaN             NaN   \n",
       "\n",
       "   channel_vk/smm  channel_ya-direct/cpc  channel_yandex/cpc  \\\n",
       "0             NaN                    NaN                 1.0   \n",
       "1             NaN                    NaN                 1.0   \n",
       "2             NaN                    NaN                 1.0   \n",
       "3             NaN                    NaN                 NaN   \n",
       "4             NaN                    NaN                 1.0   \n",
       "\n",
       "   channel_yandex/maps  channel_youtube/smm  channel_yp.ru/  \\\n",
       "0                  NaN                  NaN             NaN   \n",
       "1                  NaN                  NaN             NaN   \n",
       "2                  NaN                  NaN             NaN   \n",
       "3                  NaN                  NaN             NaN   \n",
       "4                  NaN                  NaN             NaN   \n",
       "\n",
       "                 time  \n",
       "0 2018-10-19 21:07:27  \n",
       "1 2018-10-11 11:19:18  \n",
       "2 2018-10-09 05:43:01  \n",
       "3 2018-10-09 13:42:42  \n",
       "4 2018-10-10 10:10:46  \n",
       "\n",
       "[5 rows x 49 columns]"
      ]
     },
     "execution_count": 426,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame(channels_by_user)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 427,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(82425, 49)"
      ]
     },
     "execution_count": 427,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 428,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>channel_/</th>\n",
       "      <th>channel_/sms</th>\n",
       "      <th>channel_2gis/organic</th>\n",
       "      <th>channel_Hybrid/banner</th>\n",
       "      <th>channel_Hybrid/cpc</th>\n",
       "      <th>channel_Hybrid/cpm</th>\n",
       "      <th>channel_InMobi_hr/cpm</th>\n",
       "      <th>channel_Mobiads/banner</th>\n",
       "      <th>channel_SailPlay/email</th>\n",
       "      <th>channel_TopFace/banner</th>\n",
       "      <th>...</th>\n",
       "      <th>channel_vk.com/cpc</th>\n",
       "      <th>channel_vk/</th>\n",
       "      <th>channel_vk/cpc</th>\n",
       "      <th>channel_vk/smm</th>\n",
       "      <th>channel_ya-direct/cpc</th>\n",
       "      <th>channel_yandex/cpc</th>\n",
       "      <th>channel_yandex/maps</th>\n",
       "      <th>channel_youtube/smm</th>\n",
       "      <th>channel_yp.ru/</th>\n",
       "      <th>time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2018-10-19 21:07:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2018-10-11 11:19:18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2018-10-09 05:43:01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2018-10-09 13:42:42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2018-10-10 10:10:46</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 49 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   channel_/  channel_/sms  channel_2gis/organic  channel_Hybrid/banner  \\\n",
       "0        0.0           0.0                   0.0                    0.0   \n",
       "1        0.0           0.0                   0.0                    0.0   \n",
       "2        0.0           0.0                   0.0                    0.0   \n",
       "3        0.0           0.0                   0.0                    0.0   \n",
       "4        0.0           0.0                   0.0                    0.0   \n",
       "\n",
       "   channel_Hybrid/cpc  channel_Hybrid/cpm  channel_InMobi_hr/cpm  \\\n",
       "0                 0.0                 0.0                    0.0   \n",
       "1                 0.0                 0.0                    0.0   \n",
       "2                 0.0                 0.0                    0.0   \n",
       "3                 0.0                 0.0                    0.0   \n",
       "4                 0.0                 0.0                    0.0   \n",
       "\n",
       "   channel_Mobiads/banner  channel_SailPlay/email  channel_TopFace/banner  \\\n",
       "0                     0.0                     0.0                     0.0   \n",
       "1                     0.0                     0.0                     0.0   \n",
       "2                     0.0                     0.0                     0.0   \n",
       "3                     0.0                     0.0                     0.0   \n",
       "4                     0.0                     0.0                     0.0   \n",
       "\n",
       "          ...          channel_vk.com/cpc  channel_vk/  channel_vk/cpc  \\\n",
       "0         ...                         0.0          0.0             0.0   \n",
       "1         ...                         0.0          0.0             0.0   \n",
       "2         ...                         0.0          0.0             0.0   \n",
       "3         ...                         0.0          0.0             0.0   \n",
       "4         ...                         0.0          0.0             0.0   \n",
       "\n",
       "   channel_vk/smm  channel_ya-direct/cpc  channel_yandex/cpc  \\\n",
       "0             0.0                    0.0                 1.0   \n",
       "1             0.0                    0.0                 1.0   \n",
       "2             0.0                    0.0                 1.0   \n",
       "3             0.0                    0.0                 0.0   \n",
       "4             0.0                    0.0                 1.0   \n",
       "\n",
       "   channel_yandex/maps  channel_youtube/smm  channel_yp.ru/  \\\n",
       "0                  0.0                  0.0             0.0   \n",
       "1                  0.0                  0.0             0.0   \n",
       "2                  0.0                  0.0             0.0   \n",
       "3                  0.0                  0.0             0.0   \n",
       "4                  0.0                  0.0             0.0   \n",
       "\n",
       "                 time  \n",
       "0 2018-10-19 21:07:27  \n",
       "1 2018-10-11 11:19:18  \n",
       "2 2018-10-09 05:43:01  \n",
       "3 2018-10-09 13:42:42  \n",
       "4 2018-10-10 10:10:46  \n",
       "\n",
       "[5 rows x 49 columns]"
      ]
     },
     "execution_count": 428,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.fillna(0)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Выделем фичи по дню недели"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 429,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['dow'] = df.time.apply(lambda x: x.dayofweek)\n",
    "df_days = pd.get_dummies(df.dow, prefix='dow')\n",
    "df = pd.concat([df, df_days], axis=1) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Выделим фичи по часам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 430,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['hour'] = df.time.apply(lambda x: x.hour)\n",
    "df_hours = pd.get_dummies(df.hour, prefix='hour')\n",
    "df = pd.concat([df, df_hours], axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Удалим лишние колонки"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 431,
   "metadata": {},
   "outputs": [],
   "source": [
    "del df['hour']\n",
    "del df['dow']\n",
    "del df['time']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Переведем все в целые числа"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 432,
   "metadata": {},
   "outputs": [],
   "source": [
    "for c in df.columns:\n",
    "    df[c] = pd.to_numeric(df[c], downcast='integer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 433,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>channel_/</th>\n",
       "      <th>channel_/sms</th>\n",
       "      <th>channel_2gis/organic</th>\n",
       "      <th>channel_Hybrid/banner</th>\n",
       "      <th>channel_Hybrid/cpc</th>\n",
       "      <th>channel_Hybrid/cpm</th>\n",
       "      <th>channel_InMobi_hr/cpm</th>\n",
       "      <th>channel_Mobiads/banner</th>\n",
       "      <th>channel_SailPlay/email</th>\n",
       "      <th>channel_TopFace/banner</th>\n",
       "      <th>...</th>\n",
       "      <th>hour_14</th>\n",
       "      <th>hour_15</th>\n",
       "      <th>hour_16</th>\n",
       "      <th>hour_17</th>\n",
       "      <th>hour_18</th>\n",
       "      <th>hour_19</th>\n",
       "      <th>hour_20</th>\n",
       "      <th>hour_21</th>\n",
       "      <th>hour_22</th>\n",
       "      <th>hour_23</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 79 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   channel_/  channel_/sms  channel_2gis/organic  channel_Hybrid/banner  \\\n",
       "0          0             0                     0                      0   \n",
       "1          0             0                     0                      0   \n",
       "2          0             0                     0                      0   \n",
       "3          0             0                     0                      0   \n",
       "4          0             0                     0                      0   \n",
       "\n",
       "   channel_Hybrid/cpc  channel_Hybrid/cpm  channel_InMobi_hr/cpm  \\\n",
       "0                   0                   0                      0   \n",
       "1                   0                   0                      0   \n",
       "2                   0                   0                      0   \n",
       "3                   0                   0                      0   \n",
       "4                   0                   0                      0   \n",
       "\n",
       "   channel_Mobiads/banner  channel_SailPlay/email  channel_TopFace/banner  \\\n",
       "0                       0                       0                       0   \n",
       "1                       0                       0                       0   \n",
       "2                       0                       0                       0   \n",
       "3                       0                       0                       0   \n",
       "4                       0                       0                       0   \n",
       "\n",
       "    ...     hour_14  hour_15  hour_16  hour_17  hour_18  hour_19  hour_20  \\\n",
       "0   ...           0        0        0        0        0        0        0   \n",
       "1   ...           0        0        0        0        0        0        0   \n",
       "2   ...           0        0        0        0        0        0        0   \n",
       "3   ...           0        0        0        0        0        0        0   \n",
       "4   ...           0        0        0        0        0        0        0   \n",
       "\n",
       "   hour_21  hour_22  hour_23  \n",
       "0        1        0        0  \n",
       "1        0        0        0  \n",
       "2        0        0        0  \n",
       "3        0        0        0  \n",
       "4        0        0        0  \n",
       "\n",
       "[5 rows x 79 columns]"
      ]
     },
     "execution_count": 433,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 434,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "channel_/                 int8\n",
       "channel_/sms              int8\n",
       "channel_2gis/organic      int8\n",
       "channel_Hybrid/banner     int8\n",
       "channel_Hybrid/cpc        int8\n",
       "channel_Hybrid/cpm        int8\n",
       "channel_InMobi_hr/cpm     int8\n",
       "channel_Mobiads/banner    int8\n",
       "channel_SailPlay/email    int8\n",
       "channel_TopFace/banner    int8\n",
       "channel_adprofy/cpc       int8\n",
       "channel_adsniper/cpm      int8\n",
       "channel_brodude/cpm       int8\n",
       "channel_devina/           int8\n",
       "channel_devina/sms        int8\n",
       "channel_devino/sms        int8\n",
       "channel_email/sailplay    int8\n",
       "channel_facebook/cpc      int8\n",
       "channel_facebook/fbot     int8\n",
       "channel_facebook/smm      int8\n",
       "channel_fb/smm            int8\n",
       "channel_google/           int8\n",
       "channel_google/cpc        int8\n",
       "channel_hell/forever      int8\n",
       "channel_insta/smm         int8\n",
       "channel_mamba/banner      int8\n",
       "channel_mirtesen/cpc      int8\n",
       "channel_popup/popup       int8\n",
       "channel_pushk.in/push     int8\n",
       "channel_sailplay/email    int8\n",
       "                          ... \n",
       "dow_1                     int8\n",
       "dow_2                     int8\n",
       "dow_3                     int8\n",
       "dow_4                     int8\n",
       "dow_5                     int8\n",
       "dow_6                     int8\n",
       "hour_0                    int8\n",
       "hour_1                    int8\n",
       "hour_2                    int8\n",
       "hour_3                    int8\n",
       "hour_4                    int8\n",
       "hour_5                    int8\n",
       "hour_6                    int8\n",
       "hour_7                    int8\n",
       "hour_8                    int8\n",
       "hour_9                    int8\n",
       "hour_10                   int8\n",
       "hour_11                   int8\n",
       "hour_12                   int8\n",
       "hour_13                   int8\n",
       "hour_14                   int8\n",
       "hour_15                   int8\n",
       "hour_16                   int8\n",
       "hour_17                   int8\n",
       "hour_18                   int8\n",
       "hour_19                   int8\n",
       "hour_20                   int8\n",
       "hour_21                   int8\n",
       "hour_22                   int8\n",
       "hour_23                   int8\n",
       "Length: 79, dtype: object"
      ]
     },
     "execution_count": 434,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Готовим выбору для тренировки и валидации"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 435,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 436,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df\n",
    "y = conversions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 394,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Обучаем модель!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 437,
   "metadata": {},
   "outputs": [],
   "source": [
    "from xgboost import XGBClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 438,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,\n",
       "       colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0,\n",
       "       max_depth=3, min_child_weight=1, missing=None, n_estimators=100,\n",
       "       n_jobs=1, nthread=None, objective='binary:logistic', random_state=0,\n",
       "       reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,\n",
       "       silent=True, subsample=1)"
      ]
     },
     "execution_count": 438,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xgb_model = XGBClassifier()\n",
    "xgb_model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Определяем важность фич"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 439,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.13030303, 0.        , 0.01060606, 0.        , 0.00606061,\n",
       "       0.        , 0.        , 0.        , 0.03181818, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.16363636,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.03484849,\n",
       "       0.        , 0.        , 0.07424243, 0.        , 0.06212121,\n",
       "       0.        , 0.        , 0.03030303, 0.        , 0.02272727,\n",
       "       0.02272727, 0.        , 0.        , 0.        , 0.04545455,\n",
       "       0.        , 0.        , 0.        , 0.01363636, 0.        ,\n",
       "       0.        , 0.        , 0.01666667, 0.        , 0.07878788,\n",
       "       0.        , 0.        , 0.        , 0.00757576, 0.02424242,\n",
       "       0.02272727, 0.02727273, 0.01363636, 0.02575758, 0.00606061,\n",
       "       0.01666667, 0.        , 0.        , 0.        , 0.01212121,\n",
       "       0.0030303 , 0.        , 0.00151515, 0.        , 0.00909091,\n",
       "       0.01818182, 0.01060606, 0.        , 0.        , 0.        ,\n",
       "       0.00151515, 0.00757576, 0.00151515, 0.00909091, 0.00606061,\n",
       "       0.01666667, 0.00606061, 0.00909091, 0.        ], dtype=float32)"
      ]
     },
     "execution_count": 439,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xgb_model.feature_importances_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Выделяем фичи каналов"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 440,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>channel</th>\n",
       "      <th>importance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>channel_/sms</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>channel_2gis/organic</td>\n",
       "      <td>1.060606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>channel_Hybrid/banner</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>channel_Hybrid/cpc</td>\n",
       "      <td>0.606061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>channel_Hybrid/cpm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>channel_InMobi_hr/cpm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>channel_Mobiads/banner</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>channel_SailPlay/email</td>\n",
       "      <td>3.181818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>channel_TopFace/banner</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>channel_adprofy/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>channel_adsniper/cpm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>channel_brodude/cpm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>channel_devina/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>channel_devina/sms</td>\n",
       "      <td>16.363636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>channel_devino/sms</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>channel_email/sailplay</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>channel_facebook/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>channel_facebook/fbot</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>channel_facebook/smm</td>\n",
       "      <td>3.484848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>channel_fb/smm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>channel_google/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>channel_google/cpc</td>\n",
       "      <td>7.424243</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>channel_hell/forever</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>channel_insta/smm</td>\n",
       "      <td>6.212121</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>channel_mamba/banner</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>channel_mirtesen/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>channel_popup/popup</td>\n",
       "      <td>3.030303</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>channel_pushk.in/push</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>channel_sailplay/email</td>\n",
       "      <td>2.272727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>channel_sailplay/smm</td>\n",
       "      <td>2.272727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>channel_site/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>channel_site/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>channel_site/email</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>channel_site/smm</td>\n",
       "      <td>4.545455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>channel_striptalk/cpm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>channel_telegram/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>channel_telegram/tg</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>channel_viber/chatbot</td>\n",
       "      <td>1.363636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>channel_vk.com/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>channel_vk/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>channel_vk/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>channel_vk/smm</td>\n",
       "      <td>1.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>channel_ya-direct/cpc</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>channel_yandex/cpc</td>\n",
       "      <td>7.878788</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>channel_yandex/maps</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>channel_youtube/smm</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>channel_yp.ru/</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   channel  importance\n",
       "1             channel_/sms    0.000000\n",
       "2     channel_2gis/organic    1.060606\n",
       "3    channel_Hybrid/banner    0.000000\n",
       "4       channel_Hybrid/cpc    0.606061\n",
       "5       channel_Hybrid/cpm    0.000000\n",
       "6    channel_InMobi_hr/cpm    0.000000\n",
       "7   channel_Mobiads/banner    0.000000\n",
       "8   channel_SailPlay/email    3.181818\n",
       "9   channel_TopFace/banner    0.000000\n",
       "10     channel_adprofy/cpc    0.000000\n",
       "11    channel_adsniper/cpm    0.000000\n",
       "12     channel_brodude/cpm    0.000000\n",
       "13         channel_devina/    0.000000\n",
       "14      channel_devina/sms   16.363636\n",
       "15      channel_devino/sms    0.000000\n",
       "16  channel_email/sailplay    0.000000\n",
       "17    channel_facebook/cpc    0.000000\n",
       "18   channel_facebook/fbot    0.000000\n",
       "19    channel_facebook/smm    3.484848\n",
       "20          channel_fb/smm    0.000000\n",
       "21         channel_google/    0.000000\n",
       "22      channel_google/cpc    7.424243\n",
       "23    channel_hell/forever    0.000000\n",
       "24       channel_insta/smm    6.212121\n",
       "25    channel_mamba/banner    0.000000\n",
       "26    channel_mirtesen/cpc    0.000000\n",
       "27     channel_popup/popup    3.030303\n",
       "28   channel_pushk.in/push    0.000000\n",
       "29  channel_sailplay/email    2.272727\n",
       "30    channel_sailplay/smm    2.272727\n",
       "31           channel_site/    0.000000\n",
       "32        channel_site/cpc    0.000000\n",
       "33      channel_site/email    0.000000\n",
       "34        channel_site/smm    4.545455\n",
       "35   channel_striptalk/cpm    0.000000\n",
       "36       channel_telegram/    0.000000\n",
       "37     channel_telegram/tg    0.000000\n",
       "38   channel_viber/chatbot    1.363636\n",
       "39      channel_vk.com/cpc    0.000000\n",
       "40             channel_vk/    0.000000\n",
       "41          channel_vk/cpc    0.000000\n",
       "42          channel_vk/smm    1.666667\n",
       "43   channel_ya-direct/cpc    0.000000\n",
       "44      channel_yandex/cpc    7.878788\n",
       "45     channel_yandex/maps    0.000000\n",
       "46     channel_youtube/smm    0.000000\n",
       "47          channel_yp.ru/    0.000000"
      ]
     },
     "execution_count": 440,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_features = pd.DataFrame()\n",
    "df_features[\"channel\"] = df.columns\n",
    "df_features[\"importance\"] = xgb_model.feature_importances_ * 100\n",
    "df_features = df_features[df_features.channel.str.startswith('channel_')]\n",
    "df_features = df_features[df_features.channel != 'channel_/']\n",
    "df_features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 441,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'channel_/sms': 0.0,\n",
       " 'channel_2gis/organic': 1.0606061220169067,\n",
       " 'channel_Hybrid/banner': 0.0,\n",
       " 'channel_Hybrid/cpc': 0.6060605645179749,\n",
       " 'channel_Hybrid/cpm': 0.0,\n",
       " 'channel_InMobi_hr/cpm': 0.0,\n",
       " 'channel_Mobiads/banner': 0.0,\n",
       " 'channel_SailPlay/email': 3.1818180084228516,\n",
       " 'channel_TopFace/banner': 0.0,\n",
       " 'channel_adprofy/cpc': 0.0,\n",
       " 'channel_adsniper/cpm': 0.0,\n",
       " 'channel_brodude/cpm': 0.0,\n",
       " 'channel_devina/': 0.0,\n",
       " 'channel_devina/sms': 16.363636016845703,\n",
       " 'channel_devino/sms': 0.0,\n",
       " 'channel_email/sailplay': 0.0,\n",
       " 'channel_facebook/cpc': 0.0,\n",
       " 'channel_facebook/fbot': 0.0,\n",
       " 'channel_facebook/smm': 3.4848484992980957,\n",
       " 'channel_fb/smm': 0.0,\n",
       " 'channel_google/': 0.0,\n",
       " 'channel_google/cpc': 7.424242973327637,\n",
       " 'channel_hell/forever': 0.0,\n",
       " 'channel_insta/smm': 6.21212100982666,\n",
       " 'channel_mamba/banner': 0.0,\n",
       " 'channel_mirtesen/cpc': 0.0,\n",
       " 'channel_popup/popup': 3.0303030014038086,\n",
       " 'channel_pushk.in/push': 0.0,\n",
       " 'channel_sailplay/email': 2.2727272510528564,\n",
       " 'channel_sailplay/smm': 2.2727272510528564,\n",
       " 'channel_site/': 0.0,\n",
       " 'channel_site/cpc': 0.0,\n",
       " 'channel_site/email': 0.0,\n",
       " 'channel_site/smm': 4.545454502105713,\n",
       " 'channel_striptalk/cpm': 0.0,\n",
       " 'channel_telegram/': 0.0,\n",
       " 'channel_telegram/tg': 0.0,\n",
       " 'channel_viber/chatbot': 1.3636363744735718,\n",
       " 'channel_vk.com/cpc': 0.0,\n",
       " 'channel_vk/': 0.0,\n",
       " 'channel_vk/cpc': 0.0,\n",
       " 'channel_vk/smm': 1.6666667461395264,\n",
       " 'channel_ya-direct/cpc': 0.0,\n",
       " 'channel_yandex/cpc': 7.878787994384766,\n",
       " 'channel_yandex/maps': 0.0,\n",
       " 'channel_youtube/smm': 0.0,\n",
       " 'channel_yp.ru/': 0.0}"
      ]
     },
     "execution_count": 441,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "importance_by_channel = dict(zip(df_features.channel, df_features.importance))\n",
    "importance_by_channel"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Посчитаем конверсии по каждому каналу"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 442,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'channel_/sms': 0,\n",
       " 'channel_2gis/organic': 12.78721339665995,\n",
       " 'channel_Hybrid/banner': 0,\n",
       " 'channel_Hybrid/cpc': 25.839120270400745,\n",
       " 'channel_Hybrid/cpm': 0,\n",
       " 'channel_InMobi_hr/cpm': 0,\n",
       " 'channel_Mobiads/banner': 0,\n",
       " 'channel_SailPlay/email': 19.899396894418803,\n",
       " 'channel_TopFace/banner': 0,\n",
       " 'channel_adprofy/cpc': 0,\n",
       " 'channel_adsniper/cpm': 0,\n",
       " 'channel_brodude/cpm': 0,\n",
       " 'channel_devina/': 0,\n",
       " 'channel_devina/sms': 1760.4861082944851,\n",
       " 'channel_devino/sms': 0,\n",
       " 'channel_email/sailplay': 0,\n",
       " 'channel_facebook/cpc': 0,\n",
       " 'channel_facebook/fbot': 0,\n",
       " 'channel_facebook/smm': 13.484741344958604,\n",
       " 'channel_fb/smm': 0,\n",
       " 'channel_google/': 0,\n",
       " 'channel_google/cpc': 565.5831206886361,\n",
       " 'channel_hell/forever': 0,\n",
       " 'channel_insta/smm': 23.2669581936117,\n",
       " 'channel_mamba/banner': 0,\n",
       " 'channel_mirtesen/cpc': 0,\n",
       " 'channel_popup/popup': 135.03927806417965,\n",
       " 'channel_pushk.in/push': 0,\n",
       " 'channel_sailplay/email': 97.0557870030273,\n",
       " 'channel_sailplay/smm': 46.83081204331277,\n",
       " 'channel_site/': 0,\n",
       " 'channel_site/cpc': 0,\n",
       " 'channel_site/email': 0,\n",
       " 'channel_site/smm': 53.34172473534504,\n",
       " 'channel_striptalk/cpm': 0,\n",
       " 'channel_telegram/': 0,\n",
       " 'channel_telegram/tg': 0,\n",
       " 'channel_viber/chatbot': 11.515333242835775,\n",
       " 'channel_vk.com/cpc': 0,\n",
       " 'channel_vk/': 0,\n",
       " 'channel_vk/cpc': 0,\n",
       " 'channel_vk/smm': 55.28672309691368,\n",
       " 'channel_ya-direct/cpc': 0,\n",
       " 'channel_yandex/cpc': 803.5836827312147,\n",
       " 'channel_yandex/maps': 0,\n",
       " 'channel_youtube/smm': 0,\n",
       " 'channel_yp.ru/': 0}"
      ]
     },
     "execution_count": 442,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conversions_by_channel = {c: 0 for c in df_features.channel}\n",
    "for u in data:\n",
    "    (uid, channels, cvs, time) = u\n",
    "    sum_importance = 0\n",
    "    for c in channels.split(','):\n",
    "        sum_importance += importance_by_channel.get('channel_' + c, 0)\n",
    "    for c in channels.split(','):\n",
    "        i = importance_by_channel.get('channel_' + c, 0)\n",
    "        if i:\n",
    "            conversions_by_channel['channel_' + c] += cvs * i / sum_importance\n",
    "conversions_by_channel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 385,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3602.0000000000005"
      ]
     },
     "execution_count": 385,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(conversions_by_channel.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 386,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 443,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>channel</th>\n",
       "      <th>conversions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>channel_devina/sms</td>\n",
       "      <td>1760.486108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>channel_google/cpc</td>\n",
       "      <td>565.583121</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>channel_popup/popup</td>\n",
       "      <td>135.039278</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>channel_sailplay/email</td>\n",
       "      <td>97.055787</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>channel_site/smm</td>\n",
       "      <td>53.341725</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>channel_vk/smm</td>\n",
       "      <td>55.286723</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>channel_yandex/cpc</td>\n",
       "      <td>803.583683</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   channel  conversions\n",
       "13      channel_devina/sms  1760.486108\n",
       "21      channel_google/cpc   565.583121\n",
       "26     channel_popup/popup   135.039278\n",
       "28  channel_sailplay/email    97.055787\n",
       "33        channel_site/smm    53.341725\n",
       "41          channel_vk/smm    55.286723\n",
       "43      channel_yandex/cpc   803.583683"
      ]
     },
     "execution_count": 443,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conversions_by_channel_df = pd.DataFrame()\n",
    "conversions_by_channel_df['channel'] = conversions_by_channel.keys()\n",
    "conversions_by_channel_df['conversions'] = conversions_by_channel.values()\n",
    "conversions_by_channel_df = conversions_by_channel_df[conversions_by_channel_df.conversions > 50]\n",
    "conversions_by_channel_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 444,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1080 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,15))\n",
    "plt.pie(conversions_by_channel_df.conversions, labels=conversions_by_channel_df.channel, autopct='%1.1f%%')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
