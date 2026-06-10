## MBA em Data Science, Inteligência Artificial e Analytics
USP/Esalq · Turma 261 · 2026
Bruno Leandro Saraiva Ribeiro

## Sobre este repositório
Repositório de estudos do MBA em Data Science, IA e Analytics da USP/Esalq. Reúne notebooks, scripts e materiais produzidos ao longo do curso — funciona simultaneamente como caderno de estudos e portfólio técnico.
Linguagem principal: Python (pandas, numpy, scipy, scikit-learn, statsmodels, seaborn, matplotlib)
Ambiente: Jupyter Notebooks via VS Code · Ambiente virtual por módulo quando necessário
Versionamento: GitHub como fonte única de verdade — substitui OneNote, sticky notes e cadernos avulsos

## Estrutura do repositório
mba-data-science/
│
├── 00-modulo-introdutorio/
│   ├── 01-estatistica/
│   └── 02-python/
│
├── 01-tendencias-data-science/
│   ├── 03-data-wrangling/
│   ├── 04-analise-espacial/
│   ├── 05-bi-visualizacao/
│   └── 06-web-scraping/
│
├── 02-modelos-supervisionados-nao-supervisionados/
│   ├── 07-clustering/
│   ├── 08-fatorial-pca/
│   ├── 09-correspondencia/
│   ├── 10-regressao/
│   ├── 11-logistica/
│   ├── 12-contagem/
│   ├── 13-multinivel/
│   └── 14-series-temporais/
│
├── 03-data-science-ambiente-negocios/
│   ├── 15-metodologias-ageis/
│   └── 16-engenharia-dados/
│
├── 04-ml-ia/
│   ├── 17-arvores-ensemble/
│   ├── 18-intro-deep-learning/
│   ├── 19-deep-learning/
│   ├── 20-text-mining-nlp/
│   ├── 21-pesquisa-operacional/
│   └── 22-bigdata-deployment/
│
├── data/
│   ├── raw/          # dados brutos (não modificados)
│   └── processed/    # dados após limpeza/transformação
│
└── README.md

## Módulos e disciplinas
Módulo Introdutório
##DisciplinaTópicos principaisStatus01Fundamentos de EstatísticaEstatísticas descritivas; distribuições de probabilidade (Normal, t, Binomial, Poisson, Chi², F); testes de hipóteses; intervalos de confiança🟡 Em andamento02Introdução à Programação com PythonEstruturas de dados; variáveis e escalas; intro a ML supervisionado e não supervisionado✅ Concluído
Módulo — Tendências em Data Science e Analytics
#DisciplinaTópicos principaisStatus03Data WranglingManipulação com pandas; Jupyter Notebooks; GitHub para Data Science✅ Concluído04Análise Estatística EspacialShapefiles; imagens raster; análise exploratória espacial (LISA, autocorrelação)⬜ Pendente05Business Intelligence e Data VisualizationTipos de gráficos; Power BI; dashboards; mapeamento geográfico⬜ Pendente06Coleta de Dados: Crawlers e Web ScrapingHTML parsing; BeautifulSoup; crawlers; Scrapy; JavaScript; APIs🟡 Em andamento
Módulo — Modelos Supervisionados e Não Supervisionados de ML e IA
#DisciplinaTópicos principaisStatus07Unsupervised ML: ClusteringK-means; clusters hierárquicos; dendrograma; escalonamento multidimensional⬜ Pendente08Unsupervised ML: Análise Fatorial e PCAPCA; cargas fatoriais; mapa de cargas; criação de rankings⬜ Pendente09Unsupervised ML: Análise de CorrespondênciaTabelas de frequência; chi-quadrado; mapas perceptuais; ANACOR/MCA⬜ Pendente10Supervised ML: Regressão Simples e MúltiplaOLS; R²; Stepwise; Box-Cox; multicolinearidade; diagnósticos⬜ Pendente11Supervised ML: Modelos LogísticosRegressão logística binária e multinomial; curva ROC; confusion matrix; índice GINI⬜ Pendente12Supervised ML: Modelos para Dados de ContagemPoisson; Binomial Negativo; overdispersion; zero-inflated models⬜ Pendente13Supervised ML: Modelagem MultinívelGLMM; HLM; efeitos aleatórios; dados hierárquicos⬜ Pendente14Séries TemporaisHolt-Winters; ARIMA; decomposição sazonal; forecast⬜ Pendente
Módulo — Data Science e Big Data no Ambiente de Negócios
#DisciplinaTópicos principaisStatus15Metodologias ÁgeisScrum; Kanban; Lean; squads e tribos⬜ Pendente16Engenharia de DadosSQL; modelagem relacional; diagrama ER; álgebra relacional⬜ Pendente
Módulo — ML, IA e Tendências
#DisciplinaTópicos principaisStatus17Árvores, Redes e Ensemble ModelsDecision trees; random forest; bagging/boosting; validação cruzada; overfitting⬜ Pendente18Introdução ao Deep LearningRedes neurais artificiais; arquitetura básica; implementação sem frameworks⬜ Pendente19Deep LearningOtimização de redes; feed-forward; RNN; autoencoders; Boltzmann machines⬜ Pendente20Text Mining, Sentiment Analysis e NLPPré-processamento; Naive Bayes; análise de sentimentos; classificação de textos⬜ Pendente21Pesquisa Operacional e OtimizaçãoProgramação linear; função-objetivo; métodos de otimização; Monte Carlo⬜ Pendente22Big Data e Deployment de ModelosProcessamento distribuído; encapsulamento e deploy; modelo em produção⬜ Pendente

Stack técnica
ÁreaFerramentasLinguagemPython 3.xManipulação de dadospandas, numpyEstatísticascipy, statsmodels, pingouinMachine Learningscikit-learnDeep LearningTensorFlow / KerasVisualização (Python)matplotlib, seaborn, plotlyVisualização (BI)Microsoft Power BIWeb Scrapingrequests, BeautifulSoup4, Scrapy, SeleniumNLPNLTK, spaCyGeogeopandas, shapelyBanco de dadosSQLite, MySQL, MongoDBAmbienteJupyter Notebooks, VS CodeVersionamentoGit + GitHub

Referências principais

Fávero & Belfiore — Manual de Análise de Dados (GEN, 2024) · referência transversal do curso
Bruce, Bruce & Gedeck — Practical Statistics for Data Scientists (O'Reilly, 2020)
McKinney — Python for Data Analysis (O'Reilly, 2022)
Mitchell — Web Scraping with Python (O'Reilly, 2024)
Géron — Mãos à Obra: ML com Scikit-Learn, Keras & TensorFlow (Alta Books, 2021)
Nielsen — Análise Prática de Séries Temporais (Alta Books, 2021)
Fraga — Microsoft Power BI (Alta Books, 2019)


Legenda de status
ÍconeSignificado✅Concluído — notebooks buildados e commitados🟡Em andamento⬜Pendente

MBA DSIAe · USP/Esalq · github.com/blsribeiro83/mba-data-science

