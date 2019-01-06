# Testar uma classe é semelhante a testar uma função – boa parte de seu
# trabalho envolve testar o comportamento dos métodos da classe. Porém,
# há algumas diferenças


class AnonymousSurvey:
    # """ Coleta respostas anônimas para uma pergunta de uma pesquisa."""
    def __init__(self, question):
        # """Armazena uma pergunta e se prepara para armazenar as respostas."""
        self.question = question
        self.responses = []

    def show_question(self):
        # """ Mostra a pergunta da pesquisa."""
        print(question)

    def store_response(self, new_response):
        # """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response)

    def show_results(self):
        # """Mostra todas as respostas dadas."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)