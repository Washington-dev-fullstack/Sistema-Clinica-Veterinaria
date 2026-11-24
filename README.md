# Sistema Clinica Veterinaria
Um sistema para uma clinica veterinária feita em python, no terminal. Permite cadastrar um animal, agendar consulta, além de exibir um resumo de todas as consultas.

## Como rodar

```bash
python main.py
```

## O que o código mostra

- Uma classe abstrata `Animal`, com nome e especie, e o método abstrato `emitir_som()`.
- Classes concretas Cachorro, Gato e Passaro, cada uma com sua implementação de emitir_som()
- Classe Consulta com atributos animal (objeto), veterinario (str) e data. Método realizar() que
imprime os dados.
- Tratamento de exceções para entradas inválidas.
- Encapsulamento com @property nos atributos sensíveis.
- Arrays para interação com o sistema
- Uso da biblioteca "os" para apagar prints antigos.

## Sobre

Exercício de programação orientada a objetos em Python (2026), de **Washington Gabriel** ([GitHub](https://github.com/Washington-dev-fullstack)).