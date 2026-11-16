# 1. Contexto: banho quente em famílias de baixa renda

> Contribuição da disciplina **Soluções em Energias Renováveis e Sustentáveis** ao Citizen Assist AI.

## Público
Famílias de baixa renda que procuram a Central do Cidadão, o mesmo público do Citizen Assist AI. Muitas já usam o atendimento para tirar documentos (CPF, RG, certidões) e têm pouca margem no orçamento para gastos inesperados, como uma conta de luz alta.

## Necessidade energética
**Aquecer a água do banho.** Em grande parte das casas brasileiras isso é feito com chuveiro elétrico, um dos aparelhos de maior potência da casa. Ele fica ligado só alguns minutos por dia, mas todos os dias, por todos os moradores e, em boa parte do país, no horário de pico (fim da tarde).

Pergunta que o trabalho responde:
> *"Quanto o banho pesa na minha conta de luz e o que eu posso fazer para pagar menos?"*

## Alternativas comparadas
Todas atendem à **mesma necessidade** (banho quente para a mesma família) e são comparadas no **mesmo período de referência: 12 meses**.

| | Alternativa | Tipo | Ideia |
|---|---|---|---|
| Base | Situação atual | — | Chuveiro elétrico usado sem cuidado (banho longo, posição "inverno" o ano todo) |
| A | Mudança de hábito | Economia de energia | Banho mais curto e posição "verão" nos meses quentes. Custo zero |
| B | Aquecedor solar de água | Fonte renovável | Placas coletoras e reservatório térmico aquecem a água com energia do sol, e o chuveiro elétrico fica só como apoio em dias nublados |

Para cada uma serão calculados: **consumo (kWh)**, **custo na conta (R$)**, **investimento e tempo de retorno**, **emissões evitadas (kg de CO₂)** e **viabilidade** para o público.

## Como as orientações ajudam
O usuário pergunta ao assistente sobre conta de luz ou banho e recebe:
1. Uma estimativa de quanto o banho custa por mês, com base em poucos dados que ele mesmo informa (minutos de banho, número de pessoas), sem pedir nenhum dado pessoal.
2. Quanto poderia economizar com a alternativa A, que pode começar hoje e não custa nada.
3. Quando a alternativa B vale a pena e quais são as condições (casa própria, telhado, investimento inicial).
4. A fonte de cada número e o aviso de que tudo é **estimativa, não resultado garantido**.

## Definições para a etapa 2 (dados)
- **Família de referência:** 3 pessoas. O Censo 2022 do IBGE dá média de 2,79 moradores por domicílio (ver etapa 2).
- **Local da tarifa e da irradiação solar:** São Paulo (SP), distribuidora Enel SP, porque Aurora é fictícia.
- **Tarifa:** considerar também a **Tarifa Social de Energia Elétrica**, já que parte do público tem direito a desconto, o que muda a economia em reais.
- **Valores a coletar, todos com fonte:** potência do chuveiro nas posições inverno e verão, tempo médio de banho, tarifa (R$/kWh), irradiação solar local, preço e vida útil de um aquecedor solar pequeno e fator de emissão de CO₂ da rede elétrica.

## Fora do escopo
- Instalação ou dimensionamento técnico detalhado do aquecedor solar.
- Consulta à conta de luz real do usuário. O assistente não pede nem guarda dados pessoais.
- Outros aparelhos da casa (geladeira, iluminação etc.).
