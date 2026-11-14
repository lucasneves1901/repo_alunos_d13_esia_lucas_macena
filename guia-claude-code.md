# Começar no Claude Code

O Claude Code lê os arquivos de uma pasta e responde no terminal. Terminal é a janela onde se digitam comandos. Arquivo `.md` é texto simples com títulos e listas.

## Primeira tentativa, com o professor

1. Extraia o ZIP da turma numa pasta sua, separada de projetos de trabalho.
2. Abra o terminal nessa pasta e digite `claude`.
3. Envie o pedido abaixo. Quando o Claude Code pedir acesso a um arquivo, confira se o arquivo é o da tarefa.

```text
Leia apenas caso/regras.md. Explique a regra R2 em duas frases simples.
Mostre um exemplo com os estados aberto, em_andamento e fechado.
Não altere arquivos. Se faltar uma informação, diga qual é.
```

4. Abra `caso/regras.md` e confira: aberto e em_andamento entram, fechado fica fora.
5. Anote o modelo que aparece na tela. Se a versão não aparecer, escreva "versão não informada".

Não conseguiu ler o arquivo? Confira se o terminal está na pasta do kit. Não conseguiu salvar? Copie o texto para o editor e salve por lá.

## Comandos que vamos usar

| Comando | Para quê | Aula |
|---|---|---|
| `claude` | Iniciar uma conversa na pasta atual | 1 |
| `/model` | Ver e trocar o modelo | 2 e 5 |
| `/clear` | Começar outra conversa; salve antes o que precisa | 2 e 5 |
| `/usage` | Ver o consumo, quando a conta mostrar | 2 e 5 |
| `/context` | Ver quanto da janela está ocupado | 5 |
| `/memory` | Ver quais instruções foram carregadas | 6 |

As telas mudam conforme a versão. A documentação oficial está nas [referências](referencias.md).

## Ao comparar resultados

- Abra uma conversa nova a cada tentativa. Mantenha tarefa, critérios e modelo; mude só o que a atividade compara.
- Tempo: do envio do primeiro pedido até a resposta final.
- Consumo: o número que a conta mostra, com a unidade. Sem número, escreva N/D. Nunca use zero para o que você não mediu.
- Caracteres medem o tamanho de um arquivo; não são tokens.

## Sem acesso

Acompanhe a execução de um colega e marque "execução observada". Sem nenhuma execução, use [as respostas simuladas](apoio/contingencia.md) e marque "simulação". O professor completa a comparação que faltar.
