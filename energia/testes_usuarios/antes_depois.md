# Antes e depois dos ajustes

As entradas abaixo foram **reconstruídas a partir das anotações** dos testes com usuários (`ficha_registro.csv`).
Cada uma foi enviada à versão do assistente usada nos testes (antes) e à versão ajustada (depois), em 13/11/2026.
Os testes automáticos `test_ajuste*` em `testes/test_assistente_energia.py` conferem estas mudanças.

## P2, T1: Escreveu o número por extenso

**Entrada:** 'banho de doze minutos, somos quatro'

**Antes:**
```
Para calcular, quantos minutos dura cada banho, em média?
```

**Depois:**
```
Sua casa: 4 pessoas, banho de 12 minutos.

GASTO HOJE: cerca de R$ 135 por mês só com o banho.
VOCÊ PODE ECONOMIZAR: cerca de R$ 88 por mês, sem gastar nada.
Como: banho de até 5 minutos e chave na posição verão nos meses quentes.

(O banho gasta cerca de 132 kWh por mês. kWh é a medida de energia que aparece na conta de luz. O valor em dinheiro é o R$.)
Quer saber se um aquecedor solar vale a pena para a sua casa? Digite 3.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```

## P3, T1: Três valores de economia no mesmo resultado

**Entrada:** '4 pessoas 12 minutos'

**Antes:**
```
Estimativa para 4 pessoas, 1 banho por dia de 12 minutos, chuveiro de 5.500 W:
- Hoje: cerca de 132 kWh e R$ 135 por mês só com o banho.
- Com banho de até 5 minutos e posição verão nos meses quentes: economia de cerca de R$ 88 por mês (66%). Não custa nada.
- Com aquecedor solar: economia de cerca de R$ 94 por mês (70%). Custa de R$ 2.300 a R$ 4.300 e se paga em 2,0 a 3,8 anos.
Dica: comece pelo banho curto. É grátis e vale para qualquer casa.

Fonte: ficha FC-08, verificada em 13/11/2026. Os valores são estimativas, não são garantidos.
Este assistente é um protótipo educacional, não é um canal oficial. Confirme tarifas e direitos com a sua distribuidora de energia.
```

**Depois:**
```
Sua casa: 4 pessoas, banho de 12 minutos.

GASTO HOJE: cerca de R$ 135 por mês só com o banho.
VOCÊ PODE ECONOMIZAR: cerca de R$ 88 por mês, sem gastar nada.
Como: banho de até 5 minutos e chave na posição verão nos meses quentes.

(O banho gasta cerca de 132 kWh por mês. kWh é a medida de energia que aparece na conta de luz. O valor em dinheiro é o R$.)
Quer saber se um aquecedor solar vale a pena para a sua casa? Digite 3.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```

## P4, T1: Confundiu kWh com reais

**Entrada:** '1' → '12' → '4'

**Antes:**
```
Estimativa para 4 pessoas, 1 banho por dia de 12 minutos, chuveiro de 5.500 W:
- Hoje: cerca de 132 kWh e R$ 135 por mês só com o banho.
- Com banho de até 5 minutos e posição verão nos meses quentes: economia de cerca de R$ 88 por mês (66%). Não custa nada.
- Com aquecedor solar: economia de cerca de R$ 94 por mês (70%). Custa de R$ 2.300 a R$ 4.300 e se paga em 2,0 a 3,8 anos.
Dica: comece pelo banho curto. É grátis e vale para qualquer casa.

Fonte: ficha FC-08, verificada em 13/11/2026. Os valores são estimativas, não são garantidos.
Este assistente é um protótipo educacional, não é um canal oficial. Confirme tarifas e direitos com a sua distribuidora de energia.
```

**Depois:**
```
Sua casa: 4 pessoas, banho de 12 minutos.

GASTO HOJE: cerca de R$ 135 por mês só com o banho.
VOCÊ PODE ECONOMIZAR: cerca de R$ 88 por mês, sem gastar nada.
Como: banho de até 5 minutos e chave na posição verão nos meses quentes.

(O banho gasta cerca de 132 kWh por mês. kWh é a medida de energia que aparece na conta de luz. O valor em dinheiro é o R$.)
Quer saber se um aquecedor solar vale a pena para a sua casa? Digite 3.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```

## P3, T3: Perguntou da conta cara

**Entrada:** 'minha conta de luz está cara'

**Antes:**
```
Para calcular, quantos minutos dura cada banho, em média?
```

**Depois:**
```
Conta de luz cara? Duas coisas podem ajudar:
1. DESCONTO: se sua família está no CadÚnico e tem renda baixa, você pode ter direito à Tarifa Social. Procure a sua distribuidora de energia. Para saber mais, digite 4.
2. BANHO: o chuveiro é um dos aparelhos que mais gastam. Banho de até 5 minutos e posição verão podem cortar mais da metade desse gasto. Para calcular na sua casa, digite 1.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```

## P4, T2: Não percebeu a condição de casa própria

**Entrada:** '3'

**Antes:**
```
O aquecedor solar usa placas no telhado para esquentar a água com a luz do sol. O chuveiro elétrico fica só de apoio.
- Economia: cerca de 70% do gasto com o banho (cerca de R$ 59 por mês para 3 pessoas).
- Custo: de R$ 2.300 a R$ 4.300, instalado. Se paga em 3 a 6 anos.
- No inverno o sol é mais fraco: ele cobre cerca de 58% do aquecimento.
Ele faz sentido se você tem casa própria, telhado sem sombra que aguente o peso, e dinheiro ou crédito para investir.
Se você já toma banho curto, o ganho extra é menor: ele pode levar de 8 a 15 anos para se pagar.
Antes de comprar, peça orçamento a instaladores.

Fonte: ficha FC-08, verificada em 13/11/2026. Os valores são estimativas, não são garantidos.
Este assistente é um protótipo educacional, não é um canal oficial. Confirme tarifas e direitos com a sua distribuidora de energia.
```

**Depois:**
```
RESPOSTA CURTA: o aquecedor solar só vale a pena se você tem CASA PRÓPRIA, telhado sem sombra e dinheiro ou crédito para investir.
Se você mora de aluguel ou em apartamento, o melhor é o banho curto (opção 2).

Detalhes:
- Ele esquenta a água com a luz do sol. O chuveiro elétrico fica só de apoio.
- Economiza cerca de R$ 59 por mês para 3 pessoas.
- Custa de R$ 2.300 a R$ 4.300, instalado. Se paga em 3 a 6 anos.
- Para quem já toma banho curto, demora mais: de 8 a 15 anos.
Antes de comprar, peça orçamento a instaladores.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```

## P5, T3: Tarifa Social cheia de siglas

**Entrada:** '4'

**Antes:**
```
Tarifa Social de Energia Elétrica (Lei 15.235/2025):
- Famílias no CadÚnico com renda de até meio salário mínimo por pessoa, ou com alguém que recebe o BPC, não pagam a energia até 80 kWh por mês. O que passar disso é cobrado.
- Renda entre meio e um salário mínimo por pessoa: não paga a parte chamada CDE até 120 kWh por mês.
Para saber se você tem direito, fale com a sua distribuidora de energia. Para entrar no CadÚnico, procure o CRAS da sua cidade.
Não informe CPF, NIS ou renda aqui. Este assistente não consulta cadastros.
Dica: o banho pode passar de 80 kWh por mês sozinho. Economizar no chuveiro continua baixando a conta.

Fonte: ficha FC-08, verificada em 13/11/2026. Os valores são estimativas, não são garantidos.
Este assistente é um protótipo educacional, não é um canal oficial. Confirme tarifas e direitos com a sua distribuidora de energia.
```

**Depois:**
```
RESPOSTA CURTA: se sua família está no CadÚnico e tem renda baixa, você pode ter direito à TARIFA SOCIAL. Com ela, a energia é grátis até 80 kWh por mês.
ONDE PROCURAR: na sua distribuidora de energia (a empresa da conta de luz). Se ainda não está no CadÚnico, procure o CRAS da sua cidade.

Detalhes:
- CadÚnico é o cadastro do governo para programas sociais.
- Tem direito quem ganha até meio salário mínimo por pessoa da casa, ou tem alguém que recebe o BPC (benefício para idosos e pessoas com deficiência).
- Quem ganha até 1 salário mínimo por pessoa tem um desconto menor.
- O que passar de 80 kWh é cobrado. Por isso, banho curto continua ajudando.
Não informe CPF, NIS ou renda aqui. Este assistente não consulta cadastros.

ATENÇÃO: os valores são estimativas, não são garantidos.
ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.
Fonte: ficha FC-08, verificada em 13/11/2026.
```
