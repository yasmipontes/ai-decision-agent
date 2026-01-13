# 🤖 AI Decision Agent (ReAct Pattern)

Este projeto implementa um **Agente de IA Autônomo** utilizando o padrão de arquitetura **ReAct (Reasoning + Acting)**. O objetivo principal é demonstrar a capacidade de **LLMs (Large Language Models)** atuarem não apenas como geradores de texto, mas como orquestradores lógicos capazes de utilizar ferramentas externas para resolver problemas complexos e multifacetados.

## 🎯 Objetivo do Projeto

Em cenários reais de negócios, LLMs puros possuem limitações (como alucinação em cálculos matemáticos ou falta de acesso a dados em tempo real). Este agente resolve isso conectando o "cérebro" da IA a "ferramentas" programáticas (Tools), permitindo automação inteligente e tomada de decisão estruturada.

## 🚀 Tecnologias e Conceitos

O projeto foi construído sobre uma stack moderna de Engenharia de IA:

* **Python 3.10+**: Desenvolvimento das ferramentas e lógica de controle.
* **LangChain (Agents Module)**: Framework para implementação do ciclo de vida do agente (Thought -> Action -> Observation).
* **OpenAI GPT-3.5/4**: Modelo base utilizado para o raciocínio lógico e interpretação de comandos.
* **Custom Tools**: Ferramentas desenvolvidas em Python puro para estender as capacidades da IA.

## ⚙️ Arquitetura: Como o Agente Pensa?

O sistema utiliza o fluxo **ReAct**, onde o agente segue um loop contínuo até chegar na resposta final:

1.  **Input**: Recebe uma solicitação complexa (ex: "Calcule X e conte os caracteres do resultado").
2.  **Thought (Pensamento)**: O LLM analisa o pedido e decide qual o próximo passo lógico.
3.  **Action (Ação)**: O agente seleciona a ferramenta adequada (`calculadora` ou `contador`).
4.  **Observation (Observação)**: Ele lê o output da ferramenta.
5.  **Repeat/Final Answer**: Ele repete o processo se necessário ou formula a resposta final para o usuário.

## 📂 Estrutura do Projeto

A organização do código segue boas práticas de separação de responsabilidades:

```bash
ai-decision-agent/
├── src/
│   ├── main.py        # Ponto de entrada: Inicialização do Agente e Loop de Execução
│   └── tools.py       # Definição das Ferramentas (@tool decorators) e lógica funcional
├── requirements.txt   # Dependências do projeto (LangChain, OpenAI, etc.)
└── README.md          # Documentação Técnica