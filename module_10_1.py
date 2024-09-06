from time import sleep, time
from threading import Thread

def write_words(word_count, fname):
    with open(fname, 'w', encoding='UTF-8') as f:
        for j in range(1, word_count + 1):
            f.write(f'Какое-то слово № {j}\n')
            sleep(0.02)
    print(f'Завершилась запись в файл {fname}')

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        tau = -time()
        func(*args, **kwargs)
        tau += time()
        print(f'Время выполнения: {tau} с')

    return wrapper

@timing_decorator
def main_via_functions():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

@timing_decorator
def main_with_threads():
    thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
    thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
    thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
    thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

def main():
    print('Последовательные вызовы функций:')
    main_via_functions()
    print('\nС использованием потоков:')
    main_with_threads()

if __name__ == '__main__':
    main()
