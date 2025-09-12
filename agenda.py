class Agenda:
    """Gerencia a lista de contatos."""
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone, email):
        if telefone in self.contatos:
            return f"Erro: O contato com o telefone '{telefone}' já existe."
        
        self.contatos[telefone] = {
            "nome": nome,
            "email": email
        }
        return f"Contato '{nome}' adicionado com sucesso!"

    def exibir_contatos(self):
        return self.contatos

    def remover_contato(self, telefone):
        if telefone in self.contatos:
            del self.contatos[telefone]
            return f"Contato com o telefone '{telefone}' removido com sucesso."
        return f"Erro: O contato com o telefone '{telefone}' não foi encontrado."