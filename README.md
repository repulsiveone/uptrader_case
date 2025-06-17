# Django Tree Menu  

Это Django-приложение для создания и отображения древовидных меню на веб-страницах. 

Приложение позволяет:

- Создавать несколько независимых меню через административную панель Django
- Отображать меню на страницах с помощью простого тега шаблона
- Автоматически определять активный пункт меню на основе текущего URL
- Управлять отображением вложенных пунктов меню в соответствии с активным пунктом

## Установка

1. Клонирование репозитория

```git clone https://github.com/repulsiveone/uptrader_case.git```

2. Установка зависимостей

 ```pip install -r requirements.txt```
 
3. Переход в директорию src

```cd src```

4. Запуск приложения

```python manage.py runserver```

## Установка с помощью Docker

1. Клонирование репозитория

```git clone https://github.com/repulsiveone/uptrader_case.git```

2. Запуск приложения
   
```docker-compose up --build```

Для корректной работы приложения необходимо использовать настройки Docker-контейнера вместо локальных для базы данных:

Пример для текущего docker-compose:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uptrader_db',      # Имя базы данных (должно совпадать с docker-compose)
        'USER': 'postgres',         # Стандартный пользователь PostgreSQL
        'PASSWORD': 'ABD24B7D',     # Пароль
        'HOST': 'uptraderdb',       # Имя сервиса из docker-compose.yml
        'PORT': '5432',             # Стандартный порт PostgreSQL
    }
}
```

## Пример использования на HTML странице:
```HTML
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```


# 📷 Демонстрация работы приложения

## 🛠 Административная панель
Админка позволяет управлять структурой меню, создавать и редактировать пункты.

### Редактирование пункта меню
<p align="center">
  <img src="https://github.com/user-attachments/assets/13266358-8e3f-4cae-822f-05634b7471a1" alt="Админка - список меню" width="80%" />
</p>

### Список меню
<p align="center">
  <img src="https://github.com/user-attachments/assets/aee30253-3bc9-499c-a332-a16d726e3742" alt="Админка - редактирование пункта" width="80%" />
</p>

## Древовидное меню
Меню автоматически подсвечивает текущий раздел.

### Примеры работы:

<div align="center">
  <div style="margin-bottom: 20px;">
    <strong>Текущая страница: "Option 1"</strong><br>
    <img src="https://github.com/user-attachments/assets/06b5c98b-277a-449e-b8bc-67f782fa9b37" alt="Меню - активна Option 1" width="45%" style="display: block; margin: 0 auto;" />
  </div>
  
  <div>
    <strong>Текущая страница: "Option 1.2"</strong><br>
    <img src="https://github.com/user-attachments/assets/9d869cfa-7a08-4239-9e46-c34a61c298f2" alt="Меню - активна Option 1.2" width="45%" style="display: block; margin: 0 auto;" />
  </div>
</div>
