# 6. Testes com usuários

**Objetivo:** verificar se as orientações de energia são **compreendidas** e **úteis** para o público.
**Como foi feito:** 5 pessoas de fora do grupo, identificadas só como P1 a P5. Cada uma fez 3 tarefas cronometradas no assistente, usando **casas fictícias**, para que ninguém precisasse informar dados da própria casa ou renda. Depois respondeu a 4 perguntas de compreensão e deu notas de 1 a 5 para 5 afirmações. Roteiro completo em [`testes_usuarios/roteiro.md`](testes_usuarios/roteiro.md).
**Dados pessoais:** nenhum foi registrado. As planilhas têm só códigos, tempos, acertos, notas e comentários sem identificação.

## Situações testadas
| Tarefa | Situação |
|---|---|
| T1 | Família de 4 pessoas, banho de 12 min: quanto gasta e quanto economizaria |
| T2 | Pessoa que mora de aluguel e quer aquecedor solar: o que o assistente recomenda |
| T3 | Conta de luz cara e um "desconto do governo": como se chama e onde procurar |

## Resultados (versão testada)
Resumo gerado por [`testes_usuarios/analisar_testes.py`](testes_usuarios/analisar_testes.py). Os detalhes estão em [`testes_usuarios/resultados_testes.md`](testes_usuarios/resultados_testes.md).

| Tarefa | Tempo médio | Concluiu sozinho | Com ajuda | Não concluiu |
|---|---|---|---|---|
| T1 Gasto do banho | 113 s | 3/5 | 2/5 | 0/5 |
| T2 Aquecedor solar (aluguel) | 72 s | 4/5 | 0/5 | 1/5 |
| T3 Desconto na conta | 59 s | 5/5 | 0/5 | 0/5 |

- **Compreensão:** C1 (atitude sem custo) 4/5, C2 (valores são estimativas) 4/5, C3 (para quem o solar serve) 4/5, C4 (não é canal oficial) 3/5.
- **Notas (1 a 5):** fácil de usar 4,0; entendi sem ajuda **3,4**; dicas úteis 4,0; confio nos números 3,8; indicaria 4,4. Média geral: 3,9.

**Leitura:** as pessoas acharam as dicas úteis e indicariam o assistente. A nota mais baixa foi **"entendi sem ajuda"**, e os problemas se concentraram na **forma de apresentar os números**, não nos números em si:
- três valores de economia na mesma resposta;
- kWh confundido com reais;
- condição do aquecedor solar escondida no meio do texto;
- siglas na Tarifa Social.

## Principais comentários
- "Tem três valores aqui, qual é o meu?" (P3, T1)
- "Mas eu já falei doze" (P2, T1, número por extenso)
- "Eu perguntei da conta, não do banho" (P3, T3)
- P4 disse "132" como valor da conta: era o kWh.
- P4 concluiu que o aquecedor "vale a pena, se paga em 3 a 6 anos", sem perceber a condição de casa própria.
- "Responder primeiro em uma frase se a pessoa tem direito e depois o detalhe" (P5)

## Ajustes feitos
8 ajustes no assistente a partir dos testes com usuários, mais 2 que vieram de testes automáticos e do ensaio. Cada um tem um teste automático que confere a mudança. A lista completa está em [`testes_usuarios/registro_ajustes.md`](testes_usuarios/registro_ajustes.md).

1. Entende números por extenso ("doze", "vinte e cinco").
2. Responde "minha conta está cara" com a Tarifa Social e a dica do banho.
3. O resultado do cálculo mostra **um só** valor de economia, o do banho curto, em destaque. O aquecedor solar foi para a opção 3, com os números da casa da pessoa.
4. Reais primeiro. O kWh aparece só no fim, com explicação.
5. Avisos de estimativa e de "não é canal oficial" mais visíveis.
6. Aquecedor solar e Tarifa Social começam com uma **resposta curta** e a condição principal. Os detalhes vêm depois e as siglas são explicadas.

O texto antes e depois de cada mudança, com as entradas reconstruídas a partir das anotações, está em [`testes_usuarios/antes_depois.md`](testes_usuarios/antes_depois.md).

## Limitações dos testes
- Só 5 participantes, escolhidos por conveniência e não por sorteio no público-alvo.
- Usamos casas fictícias. A reação diante da própria conta de luz pode ser diferente.
- O **reteste** com usuários depois dos ajustes ainda não foi feito. A melhora foi verificada com as entradas reconstruídas e com testes automáticos.
- O pedido de letra maior não foi atendido no terminal. Fica para a interface do assistente completo.
