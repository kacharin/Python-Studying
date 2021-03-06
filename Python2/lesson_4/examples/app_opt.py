

# ---- Обзор некоторых возможностей модулей logging и inspect ----

# * Logging Cookbook: https://docs.python.org/3/howto/logging-cookbook.html

# logging - стандартный модуль для организации логгирования
import logging      

# inspect - стандартный модуль для для сбора информации о существующих объектах
# (имена и значения атрибутов, строки документирования,
# исходный программный код, кадры стеков и прочее)
import inspect      

# wraps служит, чтобы переопределить внутренние атрибуты декоратора 
# атрибутами декорируемой функции (__doc__, __name__)
from functools import wraps


# Быстрая настройка логгирования может быть выполнена так:
# logging.basicConfig(filename="gui.log",
#     format="%(levelname)-10s %(asctime)s %(message)s",
#     level = logging.INFO
# )

# Можно выполнить более расширенную настройку логгирования.
# Создаём объект-логгер с именем db_admin_gui:
logger = logging.getLogger('db_admin_gui')

# Создаём объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Возможные настройки для форматирования:
# -----------------------------------------------------------------------------
# | Формат         | Описание
# -----------------------------------------------------------------------------
# | %(name)s       | Имя регистратора.
# | %(levelno)s    | Числовой уровень важности.
# | %(levelname)s  | Символическое имя уровня важности.
# | %(pathname)s   | Путь к исходному файлу, откуда была выполнена запись в журнал.
# | %(filename)s   | Имя исходного файла, откуда была выполнена запись в журнал.
# | %(funcName)s   | Имя функции, выполнившей запись в журнал.
# | %(module)s     | Имя модуля, откуда была выполнена запись в журнал.
# | %(lineno)d     | Номер строки, откуда была выполнена запись в журнал.
# | %(created)f    | Время, когда была выполнена запись в журнал. Значением
# |                | должно быть число, такое как возвращаемое функцией time.time().
# | %(asctime)s    | Время в формате ASCII, когда была выполнена запись в журнал.
# | %(msecs)s      | Миллисекунда, когда была выполнена запись в журнал.
# | %(thread)d     | Числовой идентификатор потока выполнения.
# | %(threadName)s | Имя потока выполнения.
# | %(process)d    | Числовой идентификатор процесса.
# | %(message)s    | Текст журналируемого сообщения (определяется пользователем).
# -----------------------------------------------------------------------------

# Создаём файловый обработчик логгирования (можно задать кодировку):
fh = logging.FileHandler("gui.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логгирования
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

# Возможные уровни логгирования:
# -----------------------------------------------------------------------------
# | Уровень важности | Использование
# -----------------------------------------------------------------------------
# | CRITICAL         | log.critical(fmt [, *args [, exc_info [, extra]]])
# | ERROR            | log.error(fmt [, *args [, exc_info [, extra]]])
# | WARNING          | log.warning(fmt [, *args [, exc_info [, extra]]])
# | INFO             | log.info(fmt [, *args [, exc_info [, extra]]])
# | DEBUG            | log.debug(fmt [, *args [, exc_info [, extra]]])
# -----------------------------------------------------------------------------


def log_it(func):
    """ Декоратор для логгирования декорируемой функции
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        # Возможности модуля inspect позволяют узнать,
        # из какой функции была вызвана данная функция.

        # Получаем стековый фрейм текущей функции:
        curframe = inspect.currentframe()  

        # Получаем список записей из текущего кадра стека и всех объемлющих кадров.
        # Каждая запись является кортежем из 6 элементов (frame, filename, lineno, funcname, code_context, index)        
        callframe = inspect.getouterframes(curframe, 2)

        # В логгирование передаем имя текущей функции и имя вызвавшей функции
        logger.info('Функция {} вызвана из {}'.format(func.__name__,  callframe[1][3]))
        return func(*args, **kwargs)

    return decorated    


@log_it
def usefull_func():
    print('Тестовая функция')
    return True


def main():
    # Очистим все обработчики событий
    logger.handlers = []

    # Создадим обработчит только для этого модуля
    fh = logging.FileHandler("app_log.log", encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    print("Запущен внутренний модуль логгирования")
    usefull_func()


if __name__ == '__main__':
    main()
