# check_guest.py
# Script para verificar se um nome está na lista de convidados.

def check_guest(name, guest_list):
    # Verifica se o nome fornecido está na lista de convidados.
    if name not in guest_list:
        print("Acesso negado por não estar na lista de convidados.")
    else:
        # Solicita ao usuário que digite a idade
        age = int(input("Digite a idade do convidado: "))

        # Verifica se idade é maior ou igual a 18.
        if age >= 18:
            print(f"O convidado {name} tem acesso permitido e é maior de idade.")
        else:
            print(f"O convidado {name} não tem acesso por ser menor de idade.")

def main():
    # Lista de convidados autorizados
    guest_list = ["Pedro", "Matheus", "Italo", "Milton", "Giovani", "Paulo", "Bruno"]

    # Solicita ao usuário que digite um nome
    name = input("Digite o nome do convidado: ")
    
    # Chama a função de verificação
    check_guest(name, guest_list)

if __name__ == "__main__":
    main()