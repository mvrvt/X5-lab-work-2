# Лабораторная работа №2 — Асинхронность в Python

Практическая работа по `asyncio`: сравнение последовательного и конкурентного выполнения, эмуляция обработки запросов сервера и исследование блокировки event loop.

## Требования

- Python 3.10+
- Сторонние библиотеки не нужны

## Содержание

| Файл | Описание |
| --- | --- |
| `starter/step1_sync.py` | Синхронное выполнение 10 операций (`time.sleep`), ~10 с |
| `starter/step2_async.py` | Конкурентное выполнение через `asyncio.gather`, ~1 с |
| `starter/step3_server.py` | Синхронная обработка пяти клиентов, ~7 с |
| `starter/step3_server_async.py` | Асинхронная обработка пяти клиентов, ~5 с |
| `starter/step4_blocking.py` | Демонстрация блокировки event loop вычислениями |
| `starter/step4_thread.py` | Вынос вычислений Bob в поток (`asyncio.to_thread`) |
| `starter/step4_process.py` | Вынос вычислений Bob в процесс (`ProcessPoolExecutor`) |
| `starter/step4_thread_three.py` | Три вычислительные задачи в потоках |
| `starter/step4_process_three.py` | Три вычислительные задачи в процессах |
| `starter/timer.py` | Вспомогательные функции измерения времени и логирования |
| `answers.md` | Ответы на обязательные письменные вопросы |

## Запуск

Откройте терминал в корне проекта и выполните, например:

```bash
python starter/step1_sync.py
python starter/step2_async.py
python starter/step3_server.py
python starter/step3_server_async.py
```

Для дополнительного шага 4:

```bash
python starter/step4_blocking.py
python starter/step4_thread.py
python starter/step4_process.py
python starter/step4_thread_three.py
python starter/step4_process_three.py
```

На macOS/Linux при необходимости используйте `python3` вместо `python`.

## Вывод

`asyncio` позволяет выполнять другие задачи во время ожидания, но синхронные вычисления могут заблокировать event loop. `asyncio.to_thread()` освобождает цикл событий, а `ProcessPoolExecutor` позволяет выполнять CPU-bound вычисления параллельно в отдельных процессах. Фактическое время зависит от компьютера.
