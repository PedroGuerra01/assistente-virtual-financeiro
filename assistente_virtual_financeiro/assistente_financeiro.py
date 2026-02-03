# ==============================
# ASSISTENTE VIRTUAL FINANCEIRO
# Projeto Final - IA Generativa
# ==============================

class AssistenteFinanceiro:
    def __init__(self):
        self.contexto = {
            "nome": None,
            "ultimo_calculo": None
        }

    def responder(self, mensagem):
        msg = mensagem.lower()

        if "meu nome é" in msg:
            return self.salvar_nome(msg)

        if "cartão de crédito" in msg:
            return self.explicar_cartao()
        if "conta corrente" in msg:
            return self.explicar_conta()
        if "empréstimo" in msg:
            return self.explicar_emprestimo()

        if "juros" in msg:
            return self.simular_juros()
        if "parcelamento" in msg:
            return self.simular_parcelamento()

        if "meu nome" in msg:
            return self.mostrar_nome()
        if "último cálculo" in msg or "ultimo calculo" in msg:
            return self.mostrar_ultimo_calculo()

        if "ajuda" in msg:
            return self.menu_ajuda()

        return self.resposta_padrao()

    def salvar_nome(self, msg):
        nome = msg.split("meu nome é")[-1].strip().title()
        self.contexto["nome"] = nome
        return f"Prazer, {nome}! Como posso te ajudar hoje?"

    def mostrar_nome(self):
        if self.contexto["nome"]:
            return f"Seu nome é {self.contexto['nome']}."
        return "Ainda não sei seu nome."

    def mostrar_ultimo_calculo(self):
        if self.contexto["ultimo_calculo"]:
            return f"Seu último cálculo foi: {self.contexto['ultimo_calculo']}."
        return "Você ainda não realizou nenhum cálculo."

    def explicar_cartao(self):
        return "Cartão de crédito permite compras agora e pagamento posterior."

    def explicar_conta(self):
        return "Conta corrente é usada para movimentação financeira diária."

    def explicar_emprestimo(self):
        return "Empréstimo é um valor cedido pelo banco com pagamento em parcelas."

    def simular_juros(self):
        try:
            valor = float(input("Valor inicial (R$): "))
            taxa = float(input("Taxa (%): "))
            tempo = int(input("Tempo (meses): "))

            juros = valor * (taxa / 100) * tempo
            total = valor + juros
            resultado = f"Juros: R$ {juros:.2f} | Total: R$ {total:.2f}"
            self.contexto["ultimo_calculo"] = resultado
            return resultado
        except:
            return "Erro ao calcular juros."

    def simular_parcelamento(self):
        try:
            valor = float(input("Valor da compra (R$): "))
            parcelas = int(input("Parcelas: "))

            parcela = valor / parcelas
            resultado = f"{parcelas}x de R$ {parcela:.2f}"
            self.contexto["ultimo_calculo"] = resultado
            return resultado
        except:
            return "Erro no parcelamento."

    def menu_ajuda(self):
        return "Digite: cartão de crédito, juros, parcelamento, ajuda ou sair."

    def resposta_padrao(self):
        return "Não entendi. Digite 'ajuda'."


def main():
    assistente = AssistenteFinanceiro()
    print("Assistente Financeiro iniciado!")
    while True:
        msg = input("Você: ")
        if msg.lower() == "sair":
            print("Até logo!")
            break
        print("Assistente:", assistente.responder(msg))


if __name__ == "__main__":
    main()
