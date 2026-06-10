🕷️ Coleta de Dados: Crawlers e Web Scraping
MBA em Data Science, Inteligência Artificial e Analytics
USP/Esalq · 2026

Sobre este módulo
Este módulo cobre a coleta automatizada de dados da web — desde os fundamentos de como o protocolo HTTP funciona até a construção de crawlers capazes de navegar por múltiplas páginas, lidar com JavaScript client-side e persistir dados estruturados.
O referencial técnico principal é Mitchell, R. — Web Scraping with Python (3ª ed., O'Reilly, 2024).

Stack utilizada
BibliotecaFunçãorequestsCliente HTTP — fazer requisições GET/POSTBeautifulSoup4Parsing de HTML/XMLlxmlParser alternativo (mais rápido que html.parser)ScrapyFramework para crawlers complexos e escaláveisSelenium / PlaywrightAutomação de browser para páginas com JavaScriptpandasLimpeza e estruturação dos dados coletadosSQLite / MongoDBPersistência dos dados

Estrutura do módulo
web-scraping/
├── notebooks/
│   ├── 01_http_e_html.ipynb          # Como a internet funciona; estrutura HTML
│   ├── 02_primeiro_scraper.ipynb     # requests + BeautifulSoup; tratamento de erros
│   ├── 03_parsing_avancado.ipynb     # CSS selectors, navegação na árvore DOM
│   ├── 04_crawlers.ipynb             # Crawling de múltiplas páginas; controle de estado
│   ├── 05_scrapy.ipynb               # Spiders, pipelines, configuração
│   ├── 06_javascript.ipynb           # Selenium/Playwright para páginas dinâmicas
│   ├── 07_apis.ipynb                 # REST APIs como alternativa ao scraping
│   ├── 08_persistencia.ipynb         # CSV, SQLite, MongoDB
│   └── 09_boas_praticas.ipynb        # robots.txt, rate limiting, ética e legalidade
├── data/
│   └── raw/                          # Dados coletados (não versionados se grandes)
└── README.md

Ementa do curso (tópicos cobertos)

Introdução ao HTML e estrutura do DOM
HTML Parsing com BeautifulSoup
Escrevendo um scraper com Python
Crawlers: navegação automatizada entre páginas
Coleta em páginas com JavaScript (rendering client-side)
Consumo de APIs REST
Persistência e estruturação dos dados coletados
Aspectos legais e éticos da coleta de dados


Referências

Mitchell, R. Web Scraping with Python: Collecting More Data from the Modern Web. 3ª ed. O'Reilly, 2024. ← referência principal
Silva, M. S. Fundamentos de HTML5 e CSS3. Novatec, 2015.
Munzert, S. et al. Automated Data Collection with R. Wiley, 2015.
Amaral, F. Aprenda Mineração de Dados: Teoria e Prática. Alta Books, 2019.


Notas de estudo

robots.txt primeiro. Antes de qualquer scraper, verificar dominio.com/robots.txt e os Termos de Serviço do site.


API > scraper quando possível. Se existe uma API pública, ela é mais estável, mais rápida e mais ética do que raspar o HTML.


Rate limiting é respeito, não só precaução. Delays entre requisições protegem o servidor e reduzem risco de bloqueio.


Repositório de estudos — MBA DSIAe · Bruno Ribeiro · github.com/blsribeiro83/mba-data-scienc