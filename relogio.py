from tkinter import *
from time import strftime

#função que atualiza o relogio
def atualizar_relogio():
  horario_atual = strftime("%H:%M:%S %p")
  rotulo_relogio.config(text=horario_atual)
  rotulo_relogio.after(1000,atualizar_relogio)

#criação da janela principal
janela = Tk()
janela.title("Relogiuo Digital")

#criação do rotulo
rotulo_relogio = Label(
  janela,
  font=("Arial",100,"bold"),
  background="black",
  foreground="white"
)

#posiciona o rotulo no centro da janela
rotulo_relogio.pack(anchor="center")

#inicia a atualização do relogio
atualizar_relogio()

#inicia o loop principal da interface grafica
janela.mainloop()