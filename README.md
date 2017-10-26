# Решатель квадратных уравнений

Скрипт для решения квадратного уравнения вида a*x**2 + b*x + c = 0

# Как использовать

Модуль quadratic_equation.py содержит функцию get_roots(a, b, c), возвращающую корни квадратного уравнения a*x**2 + b*x + c = 0

Возвращает кортеж (root1, root2). Для случая слившихся корней (единый корень) - root2 принимет значение None. Если уравнение не имеет корней, возвращается (None, None)

Пример использования:

    from quadratic_equation import get_roots
    
    root1, root2 = get_roots(1, 2, -3)
    
Для тестирования и примеров вызова можно использовать модуль tests.py из этого же репозитория.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
