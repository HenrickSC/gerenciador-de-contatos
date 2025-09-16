from supabase_client import supabase

class Agenda:

    def adicionar_contato(self, nome, telefone, email):
        """Adiciona um novo contato ao banco de dados."""
        response = supabase.table('contacts').select('telefone').eq('telefone', telefone).execute()
        if response.data:
            return f"Erro: O contato com o telefone '{telefone}' já existe."
        data = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
        response = supabase.table('contacts').insert(data).execute()

        if response.data:
            return f"{nome} adicionado com sucesso!"
        else:
            return "Erro: Não foi possível adicionar o contato."

    def exibir_contatos(self) -> list:
        """Busca e retorna todos os contatos do banco de dados."""
        response = supabase.table('contacts').select('*').execute()
        return response.data

    def remover_contato(self, telefone):
        """Remove um contato do banco de dados usando o telefone como filtro."""
        response = supabase.table('contacts').delete().eq('telefone', telefone).execute()
        if response.data:
            return "Contato removido com sucesso!"
        else:
            return "Erro: Não foi possível remover o contato."