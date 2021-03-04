#!/home/vuko/.local/share/virtualenvs/raporty_glpi-khjiv4wF/bin/python
import pymysql as sql
import pymysql.cursors as sql_cur

conn = sql.connect(
    host="#######",
    user="############",
    passwd="########",
    db="#######",
    charset="utf8mb4",
    cursorclass=sql_cur.DictCursor,
)

try:
    with conn.cursor() as cursor:
        query = """SELECT
  CONCAT(glpi_users.realname, ' ', glpi_users.firstname) AS Nazwisko,
  SUM(glpi_tickettasks.actiontime/3600) AS Czas_h
FROM glpi_tickettasks
  INNER JOIN glpi_users
    ON glpi_tickettasks.users_id_tech = glpi_users.id
WHERE
  glpi_tickettasks.date_mod BETWEEN '2021-03-01 00:00:00' AND '2021-03-28 23:59:59'
  AND glpi_tickettasks.state = 2
  AND (glpi_users.name LIKE 'G.Chrzaszcz'
  OR glpi_users.name LIKE 'K.Juchniewicz'
  OR glpi_users.name LIKE 'M.Bilkiewicz'
  OR glpi_users.name LIKE 'm.banaszek')
GROUP BY CONCAT(glpi_users.realname, ' ', glpi_users.firstname)
ORDER BY CONCAT(glpi_users.realname, ' ', glpi_users.firstname) ASC"""
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(f'{row["Nazwisko"]} \t--> {row["Czas_h"]}')
except Exception as e:
    print(e)
finally:
    conn.close()
