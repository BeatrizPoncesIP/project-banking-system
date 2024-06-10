**Sistema Bancário em Python**

Este é um software de sistema bancário simples implementado em Python que permite realizar operações básicas como depósito, saque e exibição de extrato.

### Funcionalidades:

1. **Depósito:** Permite ao usuário depositar uma certa quantia em sua conta bancária.
2. **Saque:** Permite ao usuário sacar uma certa quantia de sua conta bancária, desde que haja saldo suficiente.
3. **Extrato:** Exibe o extrato da conta bancária, mostrando o histórico de transações realizadas.

### Requisitos:

- Python 3.11 instalado no sistema.

### Como Usar:

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/BeatrizPoncesIP/sistema-bancario.git
   ```

2. **Executar o Programa:**
   ```bash
   cd sistema-bancario
   python app.py
   ```

3. **Seguir as Instruções:**
   - O programa irá solicitar que você escolha uma operação: depósito, saque ou extrato.
   - Dependendo da operação escolhida, siga as instruções na tela para completar a transação.
   - Após cada transação, o programa exibirá o saldo atual da conta.

### Exemplo de Uso:

```
Bem-vindo ao Banco Ponce!

Escolha uma operação:

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> 1

Informe o valor do depósito: 10000

Depósito realizado com sucesso!

Escolha uma operação:

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> 2

Informe o valor do saque: 100

Saque realizado com sucesso!

Escolha uma operação:

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> 2

Informe o valor do saque: 50

Saque realizado com sucesso!

Escolha uma operação:

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> 3

===================  EXTRATO  ====================

Depósito:           R$                    10000.00
Saque:              R$                      100.00
Saque:              R$                       50.00


Saldo:              R$                     9850.00

==================================================

Escolha uma operação:

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> 0

Obrigado por utilizar o Banco Python!
```

### Contribuindo:

Se desejar contribuir com melhorias ou correções, sinta-se à vontade para enviar uma solicitação de pull.

### Autor:

Beatriz Ponces <beatrizponces.oficial@gmail.com>

### Licença:

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
