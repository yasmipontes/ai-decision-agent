import os
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools import calculadora_simples, contador_de_caracteres

#configuração da OpenIa
# os.environ["OPENAI_API_KEY"] = "SUA_KEY_AQUI" # Configurar isso para rodar

def main():
    print("--- Iniciando Agente Inteligente ---")
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    tools = [calculadora_simples, contador_de_caracteres]
    
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    
    pergunta = "Quanto é 25 vezes 4? E quantos caracteres tem o número resultante?"
    print(f"Pergunta: {pergunta}")
    
    try:
        agent.run(pergunta)
    except:
        print("Configure a API Key para ver a execução real.")

if __name__ == "__main__":
    main()
