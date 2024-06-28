# dashboard-projeto5

Este aplicativo pode ser executado com o Streamlit em um servidor local ou com o Render: 
https://Dashboard-projeto-5.onrender.com/

A seguir, detalhamos a hierarquia do projeto:
├── README.md
├── app.py
├── vehicles_us.csv
└── notebooks
    └── EDA.ipynb
└── .streamlit
    └── config.toml
└── .conda
└── ...
├── .gitignore

O README.md é o arquivo atual, que detalha tudo no projeto. O arquivo app.py contém o código Python usado para executar o aplicativo. Você pode executar o aplicativo a partir do console do seu sistema com o comando "$ streamlit app.py run". O arquivo EDA.ipynb é um arquivo Jupyter Notebook que realiza análise exploratória de dados básica no conjunto de dados, plotando histogramas e exibindo informações dos dados. O arquivo vehicles_us.csv contém o conjunto de dados para este projeto, detalhando cerca de 51.000 pontos de dados diferentes para veículos, e colunas para:
- preço
- ano do modelo
- modelo
- condição
- cilindros
- combustível
- odômetro
- transmissão
- tipo
- cor da pintura
- é 4WD
- data de publicação
- dias listados

Todos os outros arquivos são funções de fundo para a execução do projeto.
