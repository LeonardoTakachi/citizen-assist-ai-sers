# 2. Dados e fontes

Todos os números usados nos cálculos estão em [`dados/premissas.csv`](dados/premissas.csv), cada um com unidade, tipo e fonte.
**Data de consulta das fontes: 13/11/2026.** Cidade de referência: **São Paulo (SP)**, distribuidora **Enel SP**. A cidade de Aurora é fictícia, por isso tarifa, clima e preços vêm de São Paulo.

## Como classificamos cada dado
| Tipo | Significado |
|---|---|
| **OFICIAL** | Vem de órgão público, lei ou norma (IBGE, ANEEL, MCTI, Lei 15.235/2025, NBR 15569) |
| **SECUNDÁRIA** | Vem de estudo acadêmico, Idec, fabricante ou site especializado que cita a origem |
| **ESTIMADO** | Calculado ou escolhido pelo grupo a partir de uma faixa publicada. Sempre indicamos a faixa |
| **PREMISSA** | Simplificação do modelo (ex.: 30 dias por mês). O usuário pode mudar na calculadora |

## Família de referência
- **3 pessoas.** O Censo 2022 do IBGE mostra média de 2,79 moradores por domicílio no Brasil e 2,69 no Sudeste.
- **1 banho por pessoa por dia.** A pesquisa de hábitos (PPH) registra 1,67 declarado, então 1 é uma escolha conservadora: o consumo real pode ser maior.
- **Chuveiro de 5.500 W**, potência comum em modelos de 127 V, segundo os manuais Lorenzetti.

## Conceitos usados
- **Potência (W ou kW):** a "força" do aparelho, o quanto de energia ele usa por unidade de tempo.
- **Energia (kWh):** é o que a conta de luz cobra. `Energia (kWh) = Potência (kW) × Tempo de uso (h)`.
  Exemplo: 5,5 kW × 10 min (0,167 h) = **0,92 kWh por banho**.
- **Fração solar:** a parte da energia de aquecimento da água que o sol fornece. O resto vem do chuveiro elétrico, que fica de apoio.
- **Fator de emissão:** quantos kg de CO₂ a rede elétrica emite para gerar 1 kWh.

## O que os dados já mostram (prévia, o cálculo completo é a etapa 3)
| Cenário (12 meses, 3 pessoas) | kWh/ano | R$/ano* | kg CO₂/ano |
|---|---|---|---|
| Base: 10 min, posição inverno o ano todo | 990 | ~1.010 | 38 |
| A: 5 min + posição verão por 6 meses | 408 | ~417 | 16 |
| B: aquecedor solar (70% solar) + chuveiro de apoio | 297 | ~303 | 11 |

\* Tarifa estimada com impostos: R$ 1,02/kWh, sem bandeira tarifária.

**Conferência:** o payback do aquecedor solar fica entre 3,3 e 6,1 anos (investimento de R$ 2.300 a R$ 4.300 e economia de cerca de R$ 707 por ano). O Idec cita de 2 a 7 anos, então a ordem de grandeza bate.

## Dois achados que vão aparecer nas recomendações
1. **Tarifa Social muda a conta, mas não zera a economia.** Pela Lei 15.235/2025, famílias do CadÚnico com renda de até meio salário mínimo por pessoa não pagam a energia até 80 kWh/mês, e pagam o excedente. Só o banho da família de referência já usa 82,5 kWh/mês. Somado à geladeira, à iluminação e ao resto da casa, o consumo passa de 80 kWh. Por isso, cada kWh economizado no banho continua saindo da parte cobrada da conta.
2. **No Brasil, o ganho ambiental principal não é o CO₂.** A rede elétrica brasileira é muito renovável: 0,0385 t CO₂/MWh em 2023, segundo o MCTI. Por isso a redução de CO₂ é pequena, de 22 a 27 kg por ano. O benefício ambiental mais relevante é reduzir o consumo **no horário de pico**, porque o chuveiro liga no fim da tarde, quando o sistema mais precisa de usinas extras. Isso será explicado como limitação e como contexto.

## Para conferir antes da entrega
A professora pediu que o grupo verifique os dados. Estes 4 itens vieram de fontes secundárias ou antigas e valem uma conferência no navegador:
- [ ] **Tarifa Enel SP:** abrir a Resolução Homologatória ANEEL nº 3.596/2026 e conferir TE + TUSD da classe B1 (R$ 0,78938/kWh).
- [ ] **Fator de emissão:** no SIRENE/MCTI, ver se já saiu a média anual de 2024 ou 2025 e trocar o valor de 2023, se houver.
- [ ] **Irradiação de São Paulo:** no CRESESB SunData, digitar as coordenadas de São Paulo (−23,55; −46,63) e anotar a média anual do plano inclinado.
- [ ] **Posição verão:** no manual de um chuveiro de 5.500 W, ver a potência da posição verão ou morno e confirmar a redução de cerca de 35%.

## Referências
- IBGE, Censo 2022, moradores por domicílio, via [Metrópoles, 28/06/2023](https://www.metropoles.com/brasil/familias-encolhem-em-media-ha-menos-de-3-pessoas-por-domicilio)
- [Câmara dos Deputados: Lei 15.235/2025 (Tarifa Social)](https://www.camara.leg.br/noticias/1209764-entra-em-vigor-lei-que-estabelece-conta-de-luz-gratuita-para-familias-de-baixa-renda/)
- [Enel SP: Tarifa Social Baixa Renda](https://www.enel.com.br/pt-saopaulo/Para_Voce/Tarifa_Social_Baixa_Renda.html)
- [Valor do kWh da Enel SP em 2026 (cita ANEEL REH 3.596/2026)](https://calculakwh.com.br/artigos/valor-do-kwh-enel-sp/)
- [Apontasol: tarifa Enel SP com impostos](https://apontasol.com.br/tarifa/enel-sp)
- [MCTI/SIRENE: fatores de emissão](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-ferramentas/fatores-de-emissao), valor de 2023 via [eixos](https://eixos.com.br/energia-eletrica/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/)
- [Chagas, PUC-Rio (2015): hábitos de banho e consumo do chuveiro](https://www.maxwell.vrac.puc-rio.br/25584/25584.PDF)
- [Altoé, Oliveira Filho e Carlo (2012), Ambiente Construído: aquecimento solar e fração solar (NBR 15569)](https://seer.ufrgs.br/ambienteconstruido/article/download/25706/21162)
- [Idec: economia com aquecedor solar](https://idec.org.br/dicas-e-direitos/economia-com-aquecedor-solar)
- [Idec: vilões de consumo no inverno (Sabesp e ANEEL)](https://idec.org.br/consultas/dicas-e-direitos/saiba-quais-so-os-viloes-de-consumo-de-energia-no-inverno)
- [Cronoshare: preço de aquecedor solar termossifão (2026)](https://www.cronoshare.com.br/quanto-custa/instalar-aquecedor-solar-agua-termossifao)
- [TNH1: economia da posição verão](https://www.tnh1.com.br/tnh1-variedades/habitos-durante-o-banho-ajudam-a-diminuir-o-consumo-do-chuveiro-eletrico-na-conta-de-luz/)
- [Manual Lorenzetti Top Jet](https://www.lorenzetti.com.br/manuais/topjet/manual.pdf)
- [Energia Solar Paulista, SEE-SP (2013): irradiação de São Paulo, com dados do Atlas INPE](https://www.absolar.org.br/wp-content/uploads/2021/02/S%C3%A3o%20Paulo.pdf)
- [CRESESB SunData](http://www.cresesb.cepel.br/index.php?section=sundata)
