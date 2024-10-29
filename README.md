# Clicker Game

Este é um jogo de contador interativo desenvolvido com Kivy, uma biblioteca Python para criar interfaces gráficas. O aplicativo permite que os usuários cliquem em um botão para aumentar um contador, acompanhar sua pontuação e progredir em níveis e multiplicadores.

## Funcionalidades

- **Contador Interativo**: Clique no botão para incrementar um contador.
- **Pontuação**: A pontuação total é calculada com base no contador e no multiplicador.
- **Níveis e Multiplicadores**: O usuário pode ganhar multiplicadores e avançar de nível ao alcançar certos marcos no contador.
- **Barra de Experiência**: Uma barra de progresso indica a experiência restante para o próximo nível.
- **Mensagens de Bônus**: O aplicativo exibe mensagens quando bônus são concedidos após clickar 10x em um local específico.

## Estrutura do Código

### Importações
O código começa com a importação das bibliotecas necessárias:
python
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window

Classe CounterApp
A classe principal do aplicativo, CounterApp, herda de BoxLayout e contém toda a lógica do aplicativo. Na inicialização, diversos componentes são criados, como rótulos (Label), uma barra de progresso (ProgressBar) e botões (Button).

Variáveis de Estado
As variáveis que armazenam o estado do jogo incluem:

counter: contador que é incrementado ao clicar.
history_count: número de cliques no botão.
multiplier: multiplicador de pontos.
score: pontuação total do jogador.
Métodos
Os principais métodos da classe incluem:

increment_counter: Incrementa o contador e atualiza a pontuação.
update_score: Atualiza a pontuação total.
update_level: Atualiza o nível do jogador com base no contador.
gain_multiplier: Permite ganhar um multiplicador ao atingir certos pontos no contador.
reset_counter: Reseta todos os valores para o padrão inicial.

Execução do App
A classe MyApp é a classe principal que inicializa e executa o aplicativo:

if __name__ == '__main__':
    MyApp().run()

Como Executar o Aplicativo
Clone o Repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Instale as Dependências: Certifique-se de ter o Python e o Kivy instalados. Você pode instalar o Kivy com o seguinte comando:

pip install kivy
Execute o Aplicativo: Navegue até o diretório do repositório e execute:
python main.py
