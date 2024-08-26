# Port Scanner Application

## Descrição

Este projeto é uma aplicação de escaneamento de portas desenvolvida em Python, que permite aos usuários verificar portas abertas e serviços disponíveis em um host ou rede. A aplicação utiliza uma interface gráfica amigável para facilitar o uso.

## Funcionalidades

- **Escaneamento de Portas TCP**: Verifica as portas TCP abertas em um host ou rede.
- **Interface Gráfica (GUI)**: Interface fácil de usar, desenvolvida com a biblioteca Tkinter.
- **Intervalo de Portas Personalizável**: Permite ao usuário definir um intervalo específico de portas a serem escaneadas.
- **Identificação de Serviços**: Relaciona as portas escaneadas com serviços conhecidos (Well-Known Ports) e apresenta o número da porta e o nome do serviço associado.

## Pré-requisitos

- Python 3.x
- Biblioteca Tkinter (geralmente incluída com a instalação padrão do Python)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/port-scanner.git

2. **Instale as dependências**:
    Este projeto não possui dependências externas além do Tkinter, que já está incluído na maioria das distribuições Python.

## Uso

1. **Execute o script**:
   ```bash
   python port_scanner.py

2. **Digite o endereço IP ou nome do host**:
    Insira o endereço IP ou o nome do host que deseja escanear.

3. **Defina o intervalo de portas**:
    Especifique o intervalo de portas que deseja escanear. Por padrão, o intervalo é de 0 a 1024.

4. **Inicie o escaneamento**:
    Clique no botão "Scan" para iniciar o escaneamento de portas.

5. **Visualize os resultados**:
    As portas abertas e os serviços associados serão exibidos na interface gráfica.

## Fontes de Informação
A lista de Well-Known Ports (WKP) usada neste projeto foi extraída da página da Wikipedia sobre [Portas TCP e UDP](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers).
<br>
<br>
#### Este projeto e README foi desenvolvido com a ajuda do ChatGPT da OpenAI.