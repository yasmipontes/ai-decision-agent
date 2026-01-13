from langchain.tools import tool

@tool
def calculadora_simples(expressao: str) -> str:
    """Realiza cálculos matemáticos simples. Entrada ex: '2 + 2'."""
    try:
        return str(eval(expressao))
    except:
        return "Erro ao calcular."

@tool
def contador_de_caracteres(texto: str) -> str:
    """Conta caracteres de uma palavra ou frase."""
    return str(len(texto))