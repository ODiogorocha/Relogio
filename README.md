
Relógio Digital com Tkinter
Este projeto implementa um relógio digital simples utilizando a biblioteca Tkinter do Python. O relógio exibe o horário atual e é atualizado a cada segundo.

Requisitos
Python 3.x instalado em seu sistema.
Biblioteca Tkinter (geralmente incluída na instalação padrão do Python).
Estrutura do Código
Importações Necessárias

python
Copiar código
from tkinter import *
from time import strftime
Função para Atualizar o Relógio

python
Copiar código
def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)
A função atualizar_relogio obtém o horário atual usando strftime, atualiza o texto do rótulo rotulo_relogio e agenda uma nova atualização após 1000 milissegundos (1 segundo).

Criação da Janela Principal

python
Copiar código
janela = Tk()
janela.title("Relógio Digital")
Criação e Configuração do Rótulo

python
Copiar código
rotulo_relogio = Label(
    janela,
    font=("Arial", 100, "bold"),
    background="black",
    foreground="white"
)
rotulo_relogio.pack(anchor="center")
Inicialização da Atualização do Relógio

python
Copiar código
atualizar_relogio()
Início do Loop Principal da Interface Gráfica

python
Copiar código
janela.mainloop()
Como Executar
Certifique-se de ter o Python instalado em seu sistema.
Copie o código acima para um arquivo chamado relogio_digital.py.
Abra um terminal ou prompt de comando.
Navegue até o diretório onde o arquivo relogio_digital.py está salvo.
Execute o script usando o comando:
bash
Copiar código
python relogio_digital.py
Resultado
Uma janela será exibida com um relógio digital centralizado, mostrando a hora atual em formato de 12 horas com AM/PM. O relógio será atualizado automaticamente a cada segundo.

Personalização
Fonte e Tamanho: Altere o parâmetro font na criação do Label para modificar a fonte e o tamanho do texto.
Cores: Modifique os parâmetros background e foreground para alterar as cores de fundo e do texto, respectivamente.
Formato da Hora: Modifique o formato de strftime na função atualizar_relogio para personalizar a exibição da hora.
