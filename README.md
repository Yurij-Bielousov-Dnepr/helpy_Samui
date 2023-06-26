
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)
# PROJECT-DIPLOM

Рестарт проекта 22-06-23

DIPLOM PROJECT

of Python 23 IT Step University

Yurij-Bielousov Сайт поиска помогаек

    Работа над ошибками:
В первой версии:
- сайт только на английском языке, но с при целом на перевод на 7 языков(версия 2).
Планы на 2 версию:
- Модифицировать чат-Бот.
- добавить фичи: 
- разделить отзывы на статьи и события, новые модели:

class Review_Article(Review):
    article_title = models.CharField(max_length=255)
    article_author = models.CharField(max_length=255)

    class Meta:
        unique_together = (("article_title", "article_author", "reviewer_name"),)
- разобраться с sponsor куда помещать урл сайта?


class Review_Event(Review):
    event_title = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)

    class Meta:
        unique_together = (("event_title", "event_location", "reviewer_name"),)
соответствующим образом модернизировать модерицию и т.д. ...
-подобрать рабочее сочетание версий пакетов 
pyTelegramBotAPI==4.11.0
python-telegram-bot==20.3
django-telegram-bot==0.6.0

Извлеченные уроки:
- не косячить с именами шаблонов, форм и урлов, сразу создавать таблицу "Связи в проекте" проектировать и вести Имена в ней
- надо разделить каждую страницу на отдельное приложение(views.py на 600 строк не устраивает)