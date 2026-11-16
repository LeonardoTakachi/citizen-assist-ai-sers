# 6. Testes com usuários — roteiro

**Objetivo:** verificar se as pessoas **entendem** as orientações de energia e se elas são **úteis**, registrando as situações testadas, os comentários e os ajustes feitos (exigência do enunciado).

**Quem:** pelo menos **5 pessoas de fora do grupo**. Podem ser as mesmas dos testes da GS de Prompt, na mesma sessão.
**Duração:** cerca de 10 minutos por pessoa.
**Material:** notebook com o terminal aberto em `energia/` rodando `python assistente_energia.py`, cronômetro do celular e as planilhas desta pasta.

## Privacidade (ler antes de começar)
- **Não anote nome, idade, telefone nem nada que identifique a pessoa.** Use só "P1", "P2"...
- As tarefas usam **casas fictícias** (cartões abaixo), para a pessoa não precisar falar da própria casa ou da renda.
- Se a pessoa digitar algum dado pessoal no assistente, não registre esse texto. Anote só "digitou dado pessoal".
- Não grave a tela com o rosto ou a voz da pessoa sem permissão.

## Fala de abertura (ler para o participante)
> "Estamos testando um assistente que dá dicas para gastar menos energia no banho. Quem está sendo testado é o assistente, não você. Não existe resposta errada. Vou te pedir 3 tarefas e cronometrar. Pense em voz alta, se quiser. Não vou anotar seu nome. Pode usar só o teclado. Topa?"

## As 3 tarefas
Entregue um cartão por vez. Comece o cronômetro quando a pessoa terminar de ler e pare quando ela disser a resposta. Se passar de **3 minutos**, encerre a tarefa e marque "não concluiu".

| Tarefa | Cartão (ler para a pessoa) | Concluiu se disser... |
|---|---|---|
| **T1 — Gasto do banho** | "A família da Ana tem **4 pessoas**. Cada banho dura **12 minutos**. Descubra quanto o banho custa por mês e quanto ela economizaria com banhos mais curtos." | ~R$ 135 por mês e economia de ~R$ 88 por mês |
| **T2 — Aquecedor solar** | "O Seu João **mora de aluguel** e quer instalar aquecedor solar. Descubra o que o assistente recomenda para ele." | É difícil por ser aluguel (precisa de autorização do dono); o melhor é mudar o hábito |
| **T3 — Desconto na conta** | "A Dona Maria acha que a conta de luz está cara e ouviu falar de um desconto do governo. Descubra **como se chama o desconto** e **onde ela deve procurar**." | Tarifa Social; procurar a distribuidora (e o CRAS para o CadÚnico) |

> Os valores de T1 vêm de `estimar_para_usuario(12, 4)`. Se as premissas mudarem, confira antes do teste.

**O que observar e anotar em cada tarefa** (em `ficha_registro.csv`):
- tempo em segundos;
- concluiu: `sim`, `com ajuda` ou `nao`;
- usou o **menu** (número) ou **escreveu a pergunta**;
- travadas, por exemplo: "não sabia o que digitar", "achou o texto longo", "não entendeu kWh";
- frase marcante que a pessoa disse (sem identificar a pessoa).

## Perguntas de compreensão (depois das tarefas)
Faça oralmente, sem o assistente aberto, e marque **certo/errado** em `questionario.csv`.

| # | Pergunta | Resposta certa |
|---|---|---|
| C1 | Qual atitude economiza energia **sem gastar dinheiro**? | Banho curto (até 5 min) e/ou posição verão |
| C2 | Os valores que o assistente mostrou são **garantidos**? | Não, são estimativas |
| C3 | Para quem o aquecedor solar **faz mais sentido**? | Casa própria, com telhado e dinheiro ou crédito para investir |
| C4 | O assistente é um **canal oficial** do governo ou da distribuidora? | Não |

## Questionário rápido (nota de 1 a 5)
1 = discordo totalmente, 5 = concordo totalmente.

| # | Afirmação |
|---|---|
| Q1 | Foi fácil usar o assistente. |
| Q2 | Entendi as respostas sem precisar de ajuda. |
| Q3 | As dicas são úteis para uma família de verdade. |
| Q4 | Confio nos números porque o assistente mostra a fonte e avisa que são estimativas. |
| Q5 | Eu indicaria este assistente para alguém da minha família. |

**Perguntas abertas:**
- O que ficou confuso ou difícil?
- O que faltou ou o que você mudaria?

## Depois dos testes
1. Preencha `ficha_registro.csv` e `questionario.csv` (já estão com o cabeçalho e as linhas de P1 a P5).
2. Rode `python analisar_testes.py`. Ele gera `resultados_testes.md` com tempos médios, taxa de conclusão, acertos e notas.
3. Junte os problemas repetidos em `registro_ajustes.md`, decida o ajuste de cada um e me envie os arquivos para aplicarmos as mudanças no assistente.
4. Se der tempo, teste de novo com 1 ou 2 pessoas depois dos ajustes ("antes e depois").
