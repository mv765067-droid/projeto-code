## ##controle de estoque
from curses.ascii import preços


nomedo_grupo  = ["manuelvinicius","eduardo","tiago","robeto ","matheus"]
produtos = ["teclado", "mouse", "monitor", "headset", "webcam"]
preço = {"teclado": "120,00", "mouse": "80,00", "monitor": "100,00", "headset": "220,00", "webcam": "150,00"}






# Integrantes do grupo: manuelvinicius, eduardo, tiago, robeto, matheus

class Produto:
    """
    Classe que representa um produto individual.
    Invariantes mantidas:
    1. O preço deve ser estritamente maior que zero.
    2. A quantidade em estoque não pode ser negativa.
    """
    def __init__(self, nome: str, preco: float, quantidade_inicial: int = 0):
        self._nome = nome
        self._preco = 0.0
        self._quantidade = 0
        
        # Uso dos setters para validar invariantes na inicialização
        self.preco = preco
        self.quantidade = quantidade_inicial

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor: float):
        # Invariante: Preço deve ser positivo
        if valor <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        self._preco = float(valor)

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        # Invariante: Quantidade não pode ser negativa
        if valor < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa.")
        self._quantidade = int(valor)

    def adicionar_estoque(self, qtd: int):
        if qtd <= 0:
            raise ValueError("A quantidade adicionada deve ser maior que zero.")
        self._quantidade += qtd

    def remover_estoque(self, qtd: int):
        if qtd <= 0:
            raise ValueError("A quantidade removida deve ser maior que zero.")
        # Invariante: Não é possível remover mais unidades do que as disponíveis
        if qtd > self._quantidade:
            raise ValueError(f"Estoque insuficiente de '{self._nome}'. Disponível: {self._quantidade}")
        self._quantidade -= qtd

    def __repr__(self):
        return f"{self._nome.capitalize()}: R$ {self._preco:.2f} | Unidades em estoque: {self._quantidade}"


class ControleEstoque:
    """
    Classe responsável pelo gerenciamento do catálogo de produtos.
    Encapsula o dicionário de produtos para controlar adições e modificações.
    """
    def __init__(self):
        self.__produtos = {}  # Atributo estritamente privado

    def cadastrar_produto(self, nome: str, preco: float, quantidade: int = 0):
        chave = nome.lower().strip()
        if chave in self.__produtos:
            raise KeyError(f"Produto '{nome}' já está cadastrado.")
        self.__produtos[chave] = Produto(nome, preco, quantidade)

    def obter_produto(self, nome: str) -> Produto:
        chave = nome.lower().strip()
        if chave not in self.__produtos:
            raise KeyError(f"Produto '{nome}' não encontrado no estoque.")
        return self.__produtos[chave]

    def listar_estoque(self):
        print("\n--- Relatório de Estoque ---")
        if not self.__produtos:
            print("Estoque vazio.")
            return
        for produto in self.__produtos.values():
            print(produto)
        print("----------------------------\n")


# --- Inicialização e Validação dos Dados do Grupo ---

estoque = ControleEstoque()

# Dados fornecidos pelo grupo com correção dos preços para float
dados_iniciais = {
    "teclado": 120.00,
    "mouse": 80.00,
    "monitor": 1000.00,  # Ajustado para valor plausível
    "headset": 220.00,
    "webcam": 150.00
}

# Cadastrando os produtos com estoque inicial zerado
for produto, preco in dados_iniciais.items():
    estoque.cadastrar_produto(nome=produto, preco=preco, quantidade=10)

# Exibe o estoque inicial
estoque.listar_estoque()

# Exemplo de operações respeitando o encapsulamento e as invariantes:
try:
    # Adicionando unidades ao mouse
    p_mouse = estoque.obter_produto("mouse")
    p_mouse.adicionar_estoque(5)

    # Vendendo/Removendo unidades do teclado
    p_teclado = estoque.obter_produto("teclado")
    p_teclado.remover_estoque(3)

    # Exibe o estoque atualizado
    estoque.listar_estoque()

    # Tentativa de violação de invariante (Descomente para testar o erro):
    # p_teclado.remover_estoque(100) # Gera ValueError: Estoque insuficiente
    # p_mouse.preco = -50.0          # Gera ValueError: O preço deve ser maior que zero

except (ValueError, KeyError) as e:
    print(f"Erro de Validação: {e}")