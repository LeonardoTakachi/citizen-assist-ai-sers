# 5. Integração ao Citizen Assist AI

A análise das etapas 2 a 4 virou uma parte do assistente que **responde perguntas sobre energia**. Os números das respostas são os do notebook.

## Como a análise chega à resposta
```
dados/premissas.csv ──> calculadora_energia.py ──> 03_calculos.ipynb  (análise)
                               │
                               └──> assistente_energia.py ──> resposta ao usuário
fichas/FC-08_energia_banho.md ──────────┘   (texto, fonte e data de verificação)
```
- **Um único módulo de cálculo:** o notebook e o assistente usam o mesmo `calculadora_energia.py`. Se uma premissa mudar no CSV, os dois mudam juntos.
- **FC-08:** ficha de referência no mesmo formato das fichas FC-01 a FC-07. Toda resposta cita "FC-08" e a data de verificação.
- **O teste `test_numeros_iguais_ao_notebook`** confere automaticamente que o assistente mostra os mesmos valores salvos pelo notebook.

## O que o usuário consegue fazer
| Menu | Exemplo de pergunta livre | O assistente responde |
|---|---|---|
| 1 | "Banho de 10 minutos, somos 3" | Gasto do banho em R$/mês e **um** valor de economia (banho curto), com o kWh explicado no fim |
| 2 | "Como economizar no banho?" | Banho de até 5 min e posição verão, custo zero, ~59% |
| 3 | "Aquecedor solar vale a pena?" | Resposta curta com a condição (casa própria, telhado, investimento), depois economia, custo e payback; se a pessoa já fez o cálculo, mostra os números da casa dela |
| — | "Moro de aluguel, posso pôr aquecedor solar?" | Explica a dificuldade e recomenda A |
| 4 | "Tenho direito a desconto na conta?" | Resposta curta, onde procurar (distribuidora, CRAS) e siglas explicadas, sem pedir dados |
| — | "Minha conta de luz está cara" | Aponta a Tarifa Social e a economia no banho |
| 5 | "Isso ajuda o meio ambiente?" | CO₂ pequeno, ganho no horário de pico, economia de água |
| 6 | "De onde vêm os números?" | Fontes e limitações |

Se faltar informação, o assistente pergunta só o que falta ("Quantos minutos dura o banho?" e depois "Quantas pessoas?"). Entende números escritos ou por extenso ("12", "doze"). O formato das respostas foi ajustado depois dos testes com usuários (ver `06_testes_com_usuarios.md`).

## Regras de segurança e acessibilidade
- **Só pede minutos de banho e número de pessoas.** Nunca pede CPF, NIS, renda, endereço ou conta de luz.
- **Remove dados pessoais antes de processar:** CPF, telefone, e-mail e números longos viram `[removido]`, e o assistente avisa o usuário. Nada é guardado depois da resposta.
- **Entradas inválidas:** mensagem vazia, texto sem sentido, mensagem muito longa (mais de 500 caracteres) ou valores fora da faixa (1 a 60 minutos, 1 a 15 pessoas) recebem uma resposta amigável, sem erro técnico.
- **Fora do escopo:** placa fotovoltaica, gás e outros aparelhos recebem "essa análise não cobre", sem inventar valores.
- **Prompt injection:** mensagens como "[SISTEMA] nova regra..." são recusadas, e os valores continuam os da FC-08.
- **Aviso em toda resposta:** os valores são estimativas, e o assistente não é um canal oficial.
- **Acessibilidade:** frases curtas, listas numeradas, menu numérico e uso só pelo teclado.

## Por que regras e não um LLM nesta parte
Os números precisam ser **exatamente** os da análise. Um LLM poderia arredondar, misturar ou inventar valores. Por isso esta parte é determinística (regras e cálculo).
Quando o assistente completo da GS de Prompt for construído com um framework de agentes, `responder()` entra como uma **ferramenta (tool)**. O agente encaminha as perguntas de energia para ela e pode só ajustar o texto, sem mudar números nem fontes.

```python
# Exemplo de encaixe no assistente completo (GS de Prompt)
from energia.assistente_energia import responder as responder_energia

def ferramenta_energia(mensagem: str) -> str:
    """Responde perguntas sobre gasto do chuveiro, economia, aquecedor solar e Tarifa Social (FC-08)."""
    resposta, _ = responder_energia(mensagem)
    return resposta
```

## Como executar e testar
Dentro da pasta `energia/`:
```bash
pip install -r requirements.txt
python assistente_energia.py          # conversa pelo terminal (teclado)
python -m pytest testes -v            # 27 testes automáticos
```
- `testes/golden_energia.csv`: 16 perguntas de energia com a resposta esperada. Podem ser somadas às 26 do golden dataset da GS de Prompt e avaliadas pelo mesmo juiz LLM.
- `testes/demo_conversa.txt`: exemplo de conversa completa, útil para o vídeo.
