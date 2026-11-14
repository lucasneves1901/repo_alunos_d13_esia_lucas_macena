# Aula 5: a mesma pergunta com quatro contextos

## Pergunta fixa

```text
Use somente entrada.md. Para uma pessoa da Oficina, liste os chamados
ativos que ela pode visualizar, com ID e prioridade, na ordem de entrada.
Se faltar regra necessária, diga qual falta. Não invente regra,
não leia outros arquivos e não altere arquivos.
```

Envie a pergunta sem mudar nenhuma palavra.

## As quatro pastas

| Pasta | Conteúdo | O que muda em relação à completa |
|---|---|---|
| `minima` | R1, R2 e dados | Falta R3, a regra de visibilidade |
| `completa` | R1, R2, R3 e dados | Nada: é a referência |
| `invertida` | Os mesmos blocos da completa | Só a ordem dos blocos |
| `ruido` | A completa e 24 notas sem relação com a tarefa | Material irrelevante a mais |

O tamanho de cada arquivo está em `experimentos/tamanhos.md`. Caracteres medem o arquivo; não são tokens.

## Como rodar cada condição

1. Copie a pasta da condição para fora do kit. Ela contém só `entrada.md`.
2. Abra o terminal dentro dessa cópia e inicie o Claude Code com `claude`.
3. Envie a pergunta fixa. Anote o tempo do envio até a resposta final.
4. Salve a resposta antes de sair. Para a próxima condição, abra outra conversa em outra pasta.

Se o Claude Code ler outro arquivo, marque a tentativa como contaminada.

## Critérios

| Critério | Vale 1 quando |
|---|---|
| Q1 | A resposta usa só o material recebido e aponta lacunas sem inventar regra |
| Q2 | Aplica os estados ativos de R2 e preserva a ordem |
| Q3 | As prioridades seguem as somas de R1 |
| Q4 | Aplica R3 e entrega a lista final T1 alta, T4 baixa, T6 alta |

Qualidade é a soma de Q1 a Q4, de 0 a 4. Marque à parte se a tarefa foi concluída. Na mínima, apontar a falta de R3 vale Q1, mas a tarefa fica incompleta. Uma suposição sobre R3 não conta como regra.

## Registro

Use `exercicios/aula-5/registro.md`. Campo sem medida recebe N/D, nunca zero. O gráfico de [comparar-contextos.html](comparar-contextos.html) usa tamanho no eixo horizontal e qualidade no vertical. Oito pontos mostram uma tendência local, não um resultado geral.
