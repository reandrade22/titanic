# Titanic
---
Este projeto tem como objetivo descrever os passos em um processo de criação de um modelo de Machine Learning. Para tal, será utilizado o dataset Titanic, do Kaggle (https://www.kaggle.com/c/titanic).

Os processos aqui descritos **não** tem como objetivo encontrar o modelo com melhor acurácia e sim servir como um guideline para projetos futuros.

As técnicas sugeridas aqui não são a única forma possível de tratar os dados. Outras técnicas e algoritmos podem ser utilizados, possivelmente com um resultado de acurácia superior ao descrito.

Uma análise de dados mais profunda (com feature engineering, por exemplo) pode também resultar em modelos de melhor desempenho. Os notebook tratam os dados para que eles possam ser usados por um modelo, mas tratamentos diferentes podem ser mais adequados a depender do modelo sendo treinado.

## O Problema
---
O dataset Titanic consiste em um conjunto de atributos que descrevem passageiros à bordo do navio. São fornecidos dois conjuntos de dados: uma para treinamento e outro para teste, sendo este o último o que deve ser submetido na plataforma para avaliação. 

Cada instância do *dataset* representa um passageiro e a coluna "Survived" indica se esta pessoa sobreviveu ou não à tragédia. Esta coluna está presente apenas no conjunto de treinamento. Outras 11 colunas estão presentes em ambos os conjuntos de dados - treinamento e teste - e representam atributos de tipos variados: categóricos, textuais e numéricos.

O objetivo do conjunto é, dadas as caractericas de uma passageiro, prever se o mesmo sobreviveu ou não ao naufrágio. Se trata de um problema de classificacão binária. 

## Métricas de Avaliação
---
A métrica utilizada no Kaggle para avaliação do problema é a acurácia, ou simplesmente a porcentagem de passageiros aos quais foram atribuídos a classe correta. Por esta ser a métrica utilizada no desafio, os notebooks aqui contidos a utilizam como avaliação de performance de um modelo.

Esta, apesar de uma das métricas mais simples, não é adequada ao problema. Não é adequada pois Titanic é um problema de classificação desbalanceado. Isso significa que o número de instâncias no dataset pertencentes a uma classe não é equivalente ao número de instâncias das outras classes do problema.

Métricas mais adequadas nesta situção seriam a área sob a curva ROC ou o f-score, por exemplo.

## Machine Learning in Production
---
Antes de seguir os passos aqui descritos em um projeto real de Machine Learning alguns pontos precisam ser levados em consideração:
* Por se tratar de um problema fechado e bem definido a etapa de entendimento do problema acaba sendo subestimada. Em um projeto real esta é uma das etapas mais importantes.
* No Titanic já tinhamos acesso ao conjunto de treinamento e ao cojunto de testes no início do problema. Este não é o caso na maioria dos projetos, onde só se conhece os verdadeiros dados de 'teste' quando o modelo começa a ser executado. Pensando nessa situação, um tratamento adequado deve ser dados na manipulação dos dados. Como exemplo, é possível citar o preenchimento de missing values, que muitas vezes precisa ser baseado apenas no conjunto de treinamento, uma vez que as instâncias de teste nãos não conhecidas.
* É possível que em um projeto real o modelo treinado precise ser reproduzido. Como alguns modelos possuem componentes aleatórios associados, a capacidade de reprodução dos resultados pode ser prejudicada. Para evitar esta situação é possíve, por exemplo, setar a random seed na maioria das bibliotecas de machine learning.
* Atenção deve ser dada à divisão dos conjuntos de treino, validacão e teste em projetos reais, evitando data leakage.
* Outros fatores e dificuldades podem existir a depender do problema.
