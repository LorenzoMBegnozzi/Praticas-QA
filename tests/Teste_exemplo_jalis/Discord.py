import pyautogui
import time

imagem_config = 'config.png'
botao_entrar = 'entrar.png'
imagem_verificacao = 'imagem_verificacao.png'
imagem_minhaconta = 'minhaconta.png'

# ============================= FUNÇÕES AUXILIARES ============================
def esperar_imagem_aparecer(imagem, confidence=0.8, timeout=30):
    print(f"Aguardando a imagem {imagem} aparecer...")
    start_time = time.time()
    while True:
        posicao = pyautogui.locateOnScreen(imagem, confidence=confidence)
        if posicao is not None:
            print(f"Imagem {imagem} encontrada!")
            return posicao
        if time.time() - start_time > timeout:
            print(f"Tempo limite atingido para a imagem {imagem}.")
            return None
        time.sleep(1)

def localizar_centro_imagem(imagem, confidence=0.8):
    posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
    if posicao:
        print(f"Centro da imagem {imagem} encontrado em: {posicao}")
        return posicao
    else:
        print(f"Imagem {imagem} não encontrada.")
        return None

# ============================= FUNÇÕES PRINCIPAIS ============================
def abrir_discord():
    print("Abrindo Discord...")
    pyautogui.press('win')
    pyautogui.write('discord')
    pyautogui.press('enter')
    time.sleep(10)

def login():
    print("Iniciando login...")
    pyautogui.write('lorenzobegnozzi@hotmail.com')
    pyautogui.press('tab')
    pyautogui.write('Lorenzo0911@')
    botao_discord = localizar_centro_imagem(botao_entrar)
    if botao_discord:
        pyautogui.click(botao_discord)
        print("Login realizado.")
    else:
        print("Erro: Botão de login não encontrado!")

def configuracoes():
    print("Abrindo configurações...")
    clicar_botao_config = localizar_centro_imagem(imagem_config, confidence=0.9)
    if clicar_botao_config:
        pyautogui.click(clicar_botao_config)
        print("Configurações acessadas.")
    else:
        print("Erro: Botão de configurações não encontrado!")


def main():
    abrir_discord()
    time.sleep(10)
    if esperar_imagem_aparecer(imagem_verificacao, confidence=0.8, timeout=30):
        login()
        time.sleep(3)
        configuracoes()
        time.sleep(3)
        if esperar_imagem_aparecer(imagem_minhaconta, confidence=0.8, timeout=30):
            print("Minha conta acessada com sucesso.")
        else:
            print("Erro: Não foi possível acessar a página 'Minha Conta'.")
    else:
        print("Erro: Discord não foi iniciado ou não apareceu na tela.")
        
# ============================= EXECUÇÃO ============================
main()
