# 4. Comparação, justificativas e recomendações

Base: família de 3 pessoas em São Paulo, período de 12 meses. Os números vêm do notebook [`03_calculos.ipynb`](03_calculos.ipynb), e as fontes estão em [`02_dados_e_fontes.md`](02_dados_e_fontes.md).
> Todos os valores são **estimativas**. Não são resultados garantidos.

## 4.1 Quadro geral
| | Base | A: hábito | B: aquecedor solar | A + B |
|---|---|---|---|---|
| Energia (kWh/ano) | 990 | 408 | 297 | 129 |
| Conta do banho (R$/ano) | ~1.010 | ~417 | ~303 | ~132 |
| Economia sobre a base | — | 59% (~R$ 593/ano) | 70% (~R$ 706/ano) | 87% (~R$ 878/ano) |
| Investimento | — | R$ 0 | R$ 2.300 a 4.300 | R$ 2.300 a 4.300 |
| Tempo de retorno | — | imediato | 3,3 a 6,1 anos | 8,1 a 15,1 anos *(só do aquecedor, depois de A)* |
| CO₂ evitado | — | 22 kg/ano | 27 kg/ano | 33 kg/ano |
| Água economizada | — | ~21 mil L/ano* | não muda | ~21 mil L/ano* |
| Fonte renovável | não | não | **sim (sol)** | **sim (sol)** |

\* Estimativa nossa: a 3,9 L/min (conferência física do notebook), cada banho de 5 min a menos poupa ~19,5 L. Com 3 pessoas em 360 dias, dá ~21 mil litros por ano.

## 4.2 Custo
- **A não custa nada** e começa a dar resultado na conta do mês seguinte. Economiza cerca de **R$ 49 por mês**.
- **B economiza um pouco mais** (~R$ 59/mês), mas exige de R$ 2.300 a R$ 4.300 de investimento. O retorno vem em **3 a 6 anos**, dentro da vida útil dos coletores (15 a 25 anos). Em 15 anos, o saldo positivo fica entre **R$ 6.300 e R$ 8.300**.
- **Para quem já faz A, o aquecedor rende pouco a mais:** ~R$ 285 por ano. Nesse caso o retorno passa para **8 a 15 anos**. Isso mostra que, para a família de referência, o investimento só é claramente vantajoso quando:
  - o banho continua longo (com 15 min, o payback de B cai para 2,2 a 4,1 anos);
  - a família é maior (com 4 pessoas, 2,4 a 4,6 anos);
  - o equipamento sai mais barato (perto de R$ 2.300).
- **Tarifa Social (Lei 15.235/2025):** famílias do CadÚnico com renda de até ½ salário mínimo por pessoa não pagam a energia até 80 kWh/mês. Como o banho sozinho já gasta ~82 kWh/mês na situação base, a casa passa da faixa gratuita, e **cada kWh economizado continua reduzindo a conta**. Para muitas famílias, verificar se já têm direito à Tarifa Social é a forma mais rápida de pagar menos.

## 4.3 Viabilidade para o público
| Condição | A: hábito | B: aquecedor solar |
|---|---|---|
| Mora de aluguel | ✅ | ⚠️ precisa da autorização do dono, e o equipamento fica no imóvel |
| Mora em apartamento | ✅ | ⚠️ depende do condomínio e da área de telhado; a tubulação encarece |
| Casa própria com telhado livre e sem sombra | ✅ | ✅ |
| Sem dinheiro para investir | ✅ | ❌ precisa de R$ 2.300 a 4.300 |
| Precisa de instalador | não | sim (encanamento e telhado) |
| Peso no telhado | — | ⚠️ reservatório de 200 L cheio pesa mais de 200 kg; precisa avaliar a estrutura |
| Dias nublados e inverno | não afeta | ⚠️ o sol cobre ~58% no inverno e ~82% no verão; o chuveiro elétrico continua como apoio |
| Manutenção | nenhuma | limpeza dos coletores e revisão periódica; o reservatório dura de 10 a 15 anos |
| Depende de todos da casa colaborarem | ⚠️ sim | não |

**Conclusão de viabilidade:** A serve para praticamente todo o público. B serve para uma parte dele: quem tem casa própria, telhado adequado e acesso a dinheiro ou crédito.

## 4.4 Impacto ambiental
- **CO₂:** a redução é pequena, de 22 a 33 kg por ano. A eletricidade brasileira é majoritariamente renovável (0,0385 t CO₂/MWh em 2023, segundo o MCTI). Seria um erro "vender" essas alternativas como grandes cortes de CO₂.
- **Horário de pico:** o chuveiro elétrico puxa 5,5 kW, geralmente no fim da tarde. É o horário em que o sistema elétrico mais precisa de usinas extras, muitas delas térmicas e mais poluentes. A e B reduzem essa demanda:
  - A reduz o tempo ligado e a potência no verão;
  - B quase elimina o uso do chuveiro elétrico nos meses de sol forte.
  Este é o benefício ambiental mais relevante, mas não foi quantificado: os dados de emissão por horário não fazem parte deste trabalho.
- **Água:** A também economiza ~21 mil litros por ano, o que importa em São Paulo, que já passou por crises hídricas.
- **Fabricação do aquecedor:** coletores e reservatório usam cobre, alumínio, vidro e isolantes. O impacto da fabricação não foi calculado. É compensado ao longo de 15 a 25 anos de uso, mas fica registrado como limitação.

## 4.5 Recomendação final
Em ordem de prioridade, para o público de baixa renda:

1. **Comece pela mudança de hábito (A).** Banho de até 5 minutos e chave na posição verão nos meses quentes. É grátis, vale para qualquer casa e corta cerca de 60% do gasto com o banho.
2. **Confira se você tem direito à Tarifa Social.** Famílias do CadÚnico com renda de até ½ salário mínimo por pessoa não pagam a energia até 80 kWh/mês. A confirmação é com a distribuidora ou no CRAS.
3. **Considere o aquecedor solar (B) só se** você tem casa própria, telhado livre e sem sombra, e consegue investir ou financiar de R$ 2.300 a R$ 4.300. Ele compensa mais para famílias maiores ou para quem não consegue encurtar o banho.
4. **Se fizer as duas,** a economia chega a ~87%. Mas, se o hábito já mudou, o aquecedor leva mais tempo para se pagar (8 a 15 anos).

## 4.6 Regras que o assistente vai seguir (base para a etapa 5)
O assistente recebe só **minutos de banho** e **número de pessoas**, sem nenhum dado pessoal, e usa `estimar_para_usuario()`.

| Situação | O que o assistente recomenda |
|---|---|
| Sempre | Mostrar o gasto estimado do banho e a economia de A, com fonte, data e aviso de estimativa |
| Banho de 5 min ou menos | Elogiar o hábito, sugerir a posição verão e dizer que a economia extra é pequena |
| Usuário pergunta sobre aquecedor solar | Mostrar a economia de B e o payback, e listar as condições (casa própria, telhado, investimento) |
| Usuário diz que mora de aluguel ou em apartamento | Recomendar A e explicar por que B é difícil nesse caso |
| Usuário pergunta sobre conta alta ou desconto | Explicar a Tarifa Social e indicar a distribuidora ou o CRAS, **sem pedir CPF, NIS ou renda** |
| Pergunta fora do escopo (ex.: placa fotovoltaica, gás) | Dizer que essa análise não cobre o assunto e indicar fontes oficiais |

## 4.7 Limitações e condições das estimativas
- **Médias, não medições:** potência (5.500 W), tempo de banho, banhos por dia e redução da posição verão são médias ou estimativas. O chuveiro e os hábitos de cada casa mudam o resultado. A tabela de sensibilidade do notebook mostra o efeito.
- **Tarifa:** R$ 1,02/kWh é uma estimativa com impostos para a Enel SP. Não inclui bandeira tarifária nem iluminação pública. Outras distribuidoras têm outros valores.
- **Payback simples:** não considera juros, reajuste da tarifa nem custo de manutenção.
- **Fração solar:** a de 70% é a meta da norma NBR 15569 para sistemas bem dimensionados. Um sistema mal instalado, com sombra ou subdimensionado rende menos. A variação mês a mês é uma aproximação pela irradiação de cada estação.
- **Preços do aquecedor:** levantados em 2025 e 2026, em fontes secundárias. Podem variar por região e fornecedor.
- **Dados de sol e CO₂:** a irradiação é do Atlas INPE de 2006 e o fator de emissão é de 2023 (o mais recente encontrado).
- **Fora do escopo:** dimensionamento técnico do aquecedor, outros aparelhos da casa, placas fotovoltaicas e aquecimento a gás.
- **O assistente não é um canal oficial.** As orientações são educativas. Antes de investir, o usuário deve pedir orçamento a instaladores e confirmar tarifas com a distribuidora.
