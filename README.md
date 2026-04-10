# 💰 BIA do Futuro - Agente Financeiro com IA Local

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte de um laboratório prático da DIO, com o objetivo de construir um agente inteligente capaz de auxiliar usuários em dúvidas sobre finanças pessoais.

A aplicação utiliza um modelo de linguagem rodando localmente (LLaMA via Ollama), permitindo interações em tempo real sem dependência de APIs externas pagas.

---

## 🚀 Tecnologias Utilizadas

* Python
* Streamlit
* Ollama

---

## 🧠 Como Funciona

O sistema consiste em um agente que recebe perguntas do usuário através de uma interface web simples e retorna respostas geradas por um modelo de linguagem executado localmente.

A comunicação com o modelo é feita via API local disponibilizada pelo Ollama (`localhost:11434`).

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

git clone https://github.com/seu-usuario/dio-lab-bia-do-futuro.git

### 2. Acessar a pasta

cd dio-lab-bia-do-futuro/src

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Instalar e rodar o Ollama

curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama serve

### 5. Executar a aplicação

streamlit run app.py

---

## 💡 Diferenciais do Projeto

* Execução 100% local (sem uso de APIs pagas)
* Integração com modelo LLM moderno (LLaMA 3)
* Interface simples e funcional com Streamlit
* Aplicação prática voltada para educação financeira

---

## 📈 Possíveis Melhorias

* Implementação de memória de conversa
* Personalização da personalidade do agente
* Integração com APIs financeiras reais
* Melhorias na interface do usuário

---



