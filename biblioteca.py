import json


class Livro:
    """Classe que representa um livro."""

    def __init__(self, titulo, autor, editora, categoria, num_copias):
        """
        Inicializa uma instância da classe Livro.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
            editora (str): A editora do livro.
            categoria (str): A categoria do livro.
            num_copias (int): O número de cópias disponíveis do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.num_copias = num_copias

    def para_o_dict(self):
        """Retorna uma representação do livro em formato de dicionário."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "editora": self.editora,
            "categoria": self.categoria,
            "num_copias": self.num_copias
        }


class Biblioteca:
    """Classe que representa uma biblioteca."""

    def __init__(self):
        """Inicializa uma instância da classe Biblioteca."""
        self.livros = []

    def adicionar_livro(self, livro):
        """
        Adiciona um livro à biblioteca.

        Args:
            livro (Livro): O livro a ser adicionado.
        """
        self.livros.append(livro)

    def listar_livros(self):
        """Exibe todos os livros da biblioteca."""
        print("Livros na biblioteca:")
        for livro in self.livros:
            print(f"- {livro.titulo}")

    def buscar_livro_por_autor(self, autor):
        """
        Busca livros na biblioteca pelo autor.

        Args:
            autor (str): O autor do livro a ser buscado.

        Returns:
            list: Uma lista de livros encontrados.
        """
        encontrados = []
        for livro in self.livros:
            if autor.lower() in livro.autor.lower():
                encontrados.append(livro)
        return encontrados

    def buscar_livro_por_categoria(self, categoria):
        """
        Busca livros na biblioteca pela categoria.

        Args:
            categoria (str): A categoria do livro a ser buscado.

        Returns:
            list: Uma lista de livros encontrados.
        """
        encontrados = []
        for livro in self.livros:
            if categoria.lower() in livro.categoria.lower():
                encontrados.append(livro)
        return encontrados

    def salvar_biblioteca(self, arquivo):
        """
        Salva os livros da biblioteca em um arquivo JSON.

        Args:
            arquivo (str): O nome do arquivo de destino.
        """
        lista_livros = [livro.para_o_dict() for livro in self.livros]
        with open(arquivo, 'w') as f:
            json.dump(lista_livros, f)

    def carregar_biblioteca(self, arquivo):
        """
        Carrega os livros da biblioteca a partir de um arquivo JSON.

        Args:
            arquivo (str): O nome do arquivo a ser carregado.
        """
        try:
            with open(arquivo, 'r') as f:
                lista_livros = json.load(f)
                for livro_dict in lista_livros:
                    livro = Livro(
                        livro_dict["titulo"],
                        livro_dict["autor"],
                        livro_dict["editora"],
                        livro_dict["categoria"],
                        livro_dict["num_copias"]
                    )
                    self.adicionar_livro(livro)
            print(f"Biblioteca carregada a partir do arquivo '{arquivo}'.")
        except FileNotFoundError:
            print(f"O arquivo '{arquivo}' não foi encontrado.")
        except json.JSONDecodeError:
            print(f"O arquivo '{arquivo}' não contém um formato JSON válido.")


class Usuario:
    """Classe que representa um usuário."""

    def __init__(self, nome):
        """
        Inicializa uma instância da classe Usuario.

        Args:
            nome (str): O nome do usuário.
        """
        self.nome = nome
        self.historico_emprestimos = []

    def emprestar_livro(self, livro):
        """
        Registra um livro emprestado pelo usuário.

        Args:
            livro (Livro): O livro emprestado.
        """
        self.historico_emprestimos.append(livro)

    def ver_historico_emprestimos(self):
        """Exibe o histórico de empréstimos do usuário."""
        if len(self.historico_emprestimos) == 0:
            print("O usuário não possui histórico de empréstimos.")
        else:
            print("Histórico de empréstimos do usuário:")
            for livro in self.historico_emprestimos:
                print(f"- {livro.titulo}")


# Exemplo de uso:

biblioteca = Biblioteca()

while True:
    print("\n=== MENU ===")
    print("1. Adicionar livro")
    print("2. Listar livros disponíveis")
    print("3. Buscar livro por autor")
    print("4. Buscar livro por categoria")
    print("5. Emprestar livro")
    print("6. Ver histórico de empréstimos")
    print("7. Salvar biblioteca")
    print("8. Carregar biblioteca")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        editora = input("Digite a editora do livro: ")
        categoria = input("Digite a categoria do livro: ")
        try:
            num_copias = int(input("Digite o número de cópias disponíveis do livro: "))
            livro = Livro(titulo, autor, editora, categoria, num_copias)
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")
        except ValueError:
            print("O número de cópias disponíveis deve ser um valor inteiro.")

    elif opcao == "2":
        biblioteca.listar_livros()

    elif opcao == "3":
        autor = input("Digite o nome do autor a ser buscado: ")
        livros_autor = biblioteca.buscar_livro_por_autor(autor)
        if len(livros_autor) == 0:
            print("Nenhum livro do autor foi encontrado.")
        else:
            print(f"Livros do autor '{autor}' encontrados: {len(livros_autor)}")
            for livro in livros_autor:
                print(livro.titulo)

    elif opcao == "4":
        categoria = input("Digite o nome da categoria a ser buscada: ")
        livros_categoria = biblioteca.buscar_livro_por_categoria(categoria)
        if len(livros_categoria) == 0:
            print("Nenhum livro da categoria foi encontrado.")
        else:
            print(f"Livros da categoria '{categoria}' encontrados: {len(livros_categoria)}")
            for livro in livros_categoria:
                print(livro.titulo)

    elif opcao == "5":
        nome_usuario = input("Digite o nome do usuário: ")
        usuario = Usuario(nome_usuario)
        titulo_livro = input("Digite o título do livro a ser emprestado: ")
        livro_encontrado = None
        for livro in biblioteca.livros:
            if livro.titulo.lower() == titulo_livro.lower() and livro.num_copias > 0:
                livro_encontrado = livro
                break
        if livro_encontrado is None:
            print("O livro não está disponível para empréstimo.")
        else:
            livro_encontrado.num_copias -= 1
            usuario.emprestar_livro(livro_encontrado)
            print(f"O livro '{livro_encontrado.titulo}' foi emprestado para o usuário '{usuario.nome}'.")

    elif opcao == "6":
        nome_usuario = input("Digite o nome do usuário: ")
        usuario = Usuario(nome_usuario)
        usuario.ver_historico_emprestimos()

    elif opcao == "7":
        nome_arquivo = input("Digite o nome do arquivo para salvar a biblioteca: ")
        biblioteca.salvar_biblioteca(nome_arquivo)
        print("Biblioteca salva com sucesso!")

    elif opcao == "8":
        nome_arquivo = input("Digite o nome do arquivo para carregar a biblioteca: ")
        biblioteca.carregar_biblioteca(nome_arquivo)

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Digite um número válido.")

print("Saindo do programa...")
