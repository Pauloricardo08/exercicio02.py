  usuarios = []
  
  def cadastrar_usuario(email, senha):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    novo_usuario = {"email": email, "senha": senha}
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

    def fazer_login(email, senha):
      email = input("Digite seu email: ")
      senha = input("Digite sua senha: ")

      for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
          print("Login bem-sucedido!")
          return
      print("Email ou senha incorretos.")

      alimentos = []  

def registrar_alimento(titulo, preco, descricao):
    
    def validar_texto(texto, minimo, campo):
        
        texto = texto.strip()
        if len(texto) < minimo:
            raise ValueError(f"{campo} deve possuir no mínimo {minimo} caracteres.")
        return texto

    def validar_preco(valor):
        
        try:
            return float(str(valor).replace(",", "."))
        except ValueError:
            raise ValueError("Preço deve ser um número decimal (float).")

    alimento = {
        "titulo": validar_texto(titulo, 2, "Título"),
        "preco": validar_preco(preco),
        "descricao": validar_texto(descricao, 5, "Descrição"),
    }
    alimentos.append(alimento)
    return alimento


def listar_alimentos():
    
    if not alimentos:
        print("\nNenhum alimento cadastrado.")
        return
    print("\n--- Alimentos cadastrados ---")
    for i, a in enumerate(alimentos, start=1):
        print(f"{i}. {a['titulo']} | R$ {a['preco']:.2f} | {a['descricao']}")


def menu():
    while True:
        print("\n1 - Cadastrar alimento\n2 - Listar alimentos\n0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            titulo = input("Título: ")
            preco = input("Preço: ")
            descricao = input("Descrição: ")
            try:
                registrar_alimento(titulo, preco, descricao)
                print("Alimento cadastrado com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")
        elif opcao == "2":
            listar_alimentos()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
