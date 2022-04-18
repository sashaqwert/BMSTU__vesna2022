# Каталог животных
Секция ГУИМЦ

Разработал студент группы ИУ5Ц-82Б Чиварзин Александр Евгеньевич

Научный руководитель: Доцент, к.т.н. Гапанюк Юрий Евгеньевич


# Требования для развёртывания

## Клиентскте устройства
* Android телефоны/планшеты. Android >= 5.0
* Доступ к прокси-серверу через интернет
* Доступ к серверам, хранящим фото животных, через интернет
* Установленное приложение `ru.sccraft.bmstulabs.rip.animals` версии 1.1 (сборка №2)

## Прокси-сервер
* Открытый HTTPS порт (обычно 443)
* Открытый порт HTTP (необязательно, но обеспечивает совместимость со старыми браузерами)
* Доступ к API-сервекру через локальную сеть, петлю (`127.0.0.0` - `127.255.255.255`)
* Привязка к доменному имени (Например, `subdomain.example.com`)
* SSL сертификат, выданный на домен прокси-сервера. Сертификату должны доверять все клиенты.
* Белый IP адрес (или проброс вышеуказанных портов на него)
* Возможность автоматически посылать запросы га выпуск SSL сертификатов в Let's Encrypt
* Пересылка всех запросов (кроме нужных Let's Encrypt) на API-сервер
* Пересылка ответов от API-сервера клиентам

## API-сервер
* Интерпритатор Python 3.10
* Открытый порт 8000 (Django)
* Установленный Django и библиотеки в виртуальное окружение Python (клон проекта из `/server`)

## Сервера хранения изображений
* Открытый HTTPS порт (обычно 443)
* Привязанное доменное имя
* Доверенный клменту SSL сертификат
* Постоянные прямые URL изображений
* Отсутствие запрета использования изображений в приложениях

# "Копия" репозитория

В связи с риском блокировки GitHub акаунта проект перенесён в BMSTU.codes https://bmstu.codes/a.chivarzin/vesna2022
