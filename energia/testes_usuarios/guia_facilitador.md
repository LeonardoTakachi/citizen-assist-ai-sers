# Guia do facilitador (para você)

Use com a **folha do participante** (`folha_participante.pdf`). Esta folha tem as respostas certas, então **não mostre para o participante**.

---

## Parte 1: um dia antes
- [ ] Convidar **5 pessoas de fora do grupo**. Reservar cerca de 10 minutos para cada uma (cerca de 20 se juntar com a GS de Prompt).
- [ ] Imprimir **5 cópias** da folha do participante (ou usar uma só e anotar as respostas você mesmo).
- [ ] Imprimir **este guia** ou deixá-lo aberto no celular.
- [ ] No notebook, testar se tudo roda: na pasta `energia`, rodar `python assistente_energia.py`.
- [ ] Fazer as 3 tarefas sozinho uma vez, como ensaio.

## Parte 2: no dia, antes de cada pessoa
- [ ] Notebook carregado, com fonte grande no terminal (Ctrl + "+" aumenta).
- [ ] Terminal na pasta `energia`, com `python assistente_energia.py` rodando e o menu aparecendo.
- [ ] Cronômetro do celular zerado.
- [ ] Folha de anotação com o código da pessoa: **P1** (depois P2, P3...).

## Parte 3: com a pessoa (cerca de 10 minutos)

### Passo 1: abertura (1 minuto)
Leia em voz alta:
> "Estamos testando um assistente que dá dicas para gastar menos energia no banho. Quem está sendo testado é o assistente, não você. Não existe resposta errada. Vou te pedir 3 tarefas e marcar o tempo. Pode pensar em voz alta. Não vou anotar seu nome nem nada sobre você. Use só o teclado. Topa?"

Se a pessoa não topar, agradeça e encerre. Não anote nada.

### Passo 2: as 3 tarefas (cerca de 6 minutos)
Para **cada** tarefa:

1. Mostre o cartão da tarefa na folha do participante e deixe a pessoa ler.
2. Quando ela começar a digitar, **comece o cronômetro**.
3. **Não ajude.** Se travar, espere 30 segundos. Se ainda precisar, dê uma dica curta (ex.: "tem um menu com números") e marque **com ajuda**.
4. **Pare o cronômetro** quando a pessoa disser a resposta em voz alta.
5. Se passar de **3 minutos**, encerre a tarefa e marque **não concluiu**.
6. Antes da próxima tarefa, digite `0` e rode `python assistente_energia.py` de novo.

**Respostas certas (só para você):**

| Tarefa | Conta como concluída se a pessoa disser |
|---|---|
| T1 | O banho custa **cerca de R$ 135 por mês** e economizaria **cerca de R$ 88 por mês** |
| T2 | É difícil porque ele **mora de aluguel** (precisa de autorização do dono); o melhor é **mudar o hábito** (banho curto e posição verão) |
| T3 | O desconto é a **Tarifa Social**; ela deve procurar a **distribuidora de energia** (ou o **CRAS**, para o CadÚnico) |

**Anote em cada tarefa:**

- tempo em segundos;
- concluiu: `sim`, `com ajuda` ou `nao`;
- usou `menu` (número) ou `texto` (escreveu a pergunta);
- onde travou (ex.: "não sabia o que digitar");
- frase marcante (ex.: "não sei o que é kWh").

> Se a pessoa digitar algum dado pessoal de verdade, **não copie o que ela digitou**. Anote só "digitou dado pessoal".

### Passo 3: perguntas de compreensão (1 minuto)
Feche o assistente. A pessoa responde às perguntas 1 a 4 da folha dela (colunas C1 a C4). Depois, marque **certo** ou **errado**:

| # | Resposta certa |
|---|---|
| C1 | Banho curto (até 5 minutos) e/ou chave na posição verão |
| C2 | Não, são estimativas |
| C3 | Casa própria, com telhado e dinheiro ou crédito para investir |
| C4 | Não, não é canal oficial |

### Passo 4: notas e comentários (2 minutos)
A pessoa marca as notas de 1 a 5 nas frases A a E (colunas Q1 a Q5) e responde às 2 perguntas abertas na folha. Se preferir falar, anote do jeito que ela disser.

### Passo 5: encerramento
> "Obrigado! Sua ajuda vai melhorar o assistente."

Recolha a folha. **Ela não tem nome**, só o código P1, P2...

## Parte 4: depois das 5 pessoas
Exemplo de como fica cada linha nas planilhas:

```
ficha_registro.csv  ->  P1,T1,95,sim,texto,demorou para achar onde digitar,"achou R$ 135 rápido"
questionario.csv    ->  P1,certo,certo,errado,certo,4,4,5,3,5,o que é kWh,mostrar quanto é por banho
```

1. Abra `ficha_registro.csv` e `questionario.csv` no Excel e preencha com as anotações. Na folha do participante, as **perguntas 1 a 4** são as colunas **C1 a C4**, e as **frases A a E** são as colunas **Q1 a Q5**.
2. No terminal, dentro de `energia/testes_usuarios`, rode: `python analisar_testes.py`.
3. **Mande para o Claude** as duas planilhas e o `resultados_testes.md`. Ele ajusta o assistente e preenche o `registro_ajustes.md`.
4. Se der tempo, teste de novo com 1 ou 2 pessoas depois dos ajustes (antes e depois).
5. Guarde as folhas em papel até o fim da disciplina e depois descarte.

## Juntando com a GS de Prompt
Use as **mesmas pessoas e os mesmos códigos** (P1 a P5). Faça primeiro as tarefas de uma GS e depois as da outra, sem misturar.
