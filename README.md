# Async Timer (Django)

Projeto Django com uma view assíncrona de contador de tempo.

## Como rodar

1. Crie e ative o ambiente virtual (opcional) e instale dependências:

```
pip install -r requirements.txt
```

2. Rode o servidor:

```
python manage.py runserver
```

3. Acesse a view de contador (padrão: 5 segundos):

```
http://127.0.0.1:8000/timer/
```

Para definir a duração, use `seconds`:

```
http://127.0.0.1:8000/timer/?seconds=10
```

A resposta será JSON com `elapsed_seconds` e uma mensagem de conclusão.

## Endpoints

- `GET /timer/` — contador assíncrono padrão (5s).
- `GET /timer/?seconds=N` — contador assíncrono por N segundos.
