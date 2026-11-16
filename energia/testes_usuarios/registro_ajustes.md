# Registro de ajustes

Cada linha liga um problema encontrado a uma mudança no assistente. **Origem** diz de onde veio o problema: teste automático, ensaio ou teste com usuários (participante e tarefa).
O texto antes e depois de cada mudança está em [`antes_depois.md`](antes_depois.md). Cada ajuste tem um teste automático em `testes/test_assistente_energia.py`.

| # | Origem | Problema encontrado | Ajuste feito | Teste automático | Situação |
|---|---|---|---|---|---|
| 1 | Teste automático | Quando o assistente perguntava "quantas pessoas?" e o usuário digitava "4", ele abria a opção 4 do menu (Tarifa Social) | Quando o assistente espera uma resposta, um número sozinho é a resposta, não a opção do menu ("0" continua saindo) | `test_conversa_em_etapas` | Corrigido |
| 2 | Ensaio da tarefa T3 | "Tem algum desconto **do governo**?" recebia "não sou canal oficial" | A regra de canal oficial passou a exigir frases como "você é do governo?" | `test_desconto_do_governo_e_tarifa_social` | Corrigido |
| 3 | P2, T1 | Escreveu "doze" por extenso. O assistente não entendeu e perguntou os minutos de novo ("mas eu já falei doze") | Números por extenso de 1 a 69 viram algarismos antes da leitura ("doze", "vinte e cinco", "meia hora") | `test_ajuste3_numero_por_extenso` | Corrigido |
| 4 | P3, T3 | "Minha conta de luz está cara" era tratada como pedido de cálculo do banho ("eu perguntei da conta, não do banho") | Nova resposta para conta cara ou alta: aponta a Tarifa Social (opção 4) e o banho (opção 1) | `test_ajuste4_conta_cara` | Corrigido |
| 5 | P1 e P3, T1 | Três valores de economia no mesmo resultado. P3 respondeu R$ 94 (aquecedor) em vez de R$ 88 (banho curto) | O resultado mostra só **um** valor de economia, o do banho curto, em destaque ("VOCÊ PODE ECONOMIZAR"). O aquecedor solar fica na opção 3, que agora usa os números da casa da pessoa | `test_ajuste5_um_valor_de_economia` | Corrigido |
| 6 | P4, T1 | Confundiu kWh com reais e disse "132" como valor da conta | O valor em R$ vem primeiro. O kWh aparece só no fim, entre parênteses, com a explicação "kWh é a medida de energia... o valor em dinheiro é o R$" | `test_ajuste6_reais_antes_de_kwh` | Corrigido |
| 7 | P2 e P3, perguntas C2 e C4 | 2 pessoas não lembraram que o assistente não é oficial e 1 achou que os valores eram garantidos. O aviso ficava num parágrafo longo no fim | Rodapé mais curto, com duas linhas começando por "ATENÇÃO:" e "NÃO" em maiúsculas | `test_ajuste7_aviso_visivel` | Corrigido |
| 8 | P2 e P4, T2 | Texto do aquecedor solar comprido. P4 leu "se paga em 3 a 6 anos" e concluiu que valia a pena, sem ver a condição de casa própria (tarefa não concluída) | A resposta começa com "RESPOSTA CURTA" e a condição em maiúsculas ("só vale a pena se você tem CASA PRÓPRIA"). Aluguel e apartamento aparecem na segunda linha. Detalhes depois | `test_ajuste8_condicao_do_solar_primeiro` | Corrigido |
| 9 | P4 e P5, T3 | Tarifa Social "cheia de sigla". P4 perguntou o que é CDE. P5 pediu "responder primeiro em uma frase se a pessoa tem direito" | Resposta começa com uma frase curta e "ONDE PROCURAR". CadÚnico e BPC são explicados. "CDE" foi retirado e virou "desconto menor" | `test_ajuste9_tarifa_social_simples` | Corrigido |
| 10 | P2, pergunta aberta | Pediu letra maior | **Não aplicado no código.** No terminal, o tamanho da letra depende do programa: orientamos usar Ctrl + (ou Cmd +) para aumentar. Fica como requisito para a interface do assistente completo (GS de Prompt) | — | Registrado como limitação |

**Próximo passo recomendado:** repetir as tarefas T1 e T2 com 1 ou 2 pessoas novas para confirmar a melhora com usuários reais. A comparação em `antes_depois.md` mostra a mudança no texto, mas não substitui o reteste.
