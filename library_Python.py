import random

# Define the cute emojis
country_emojis = ['', '', '']

# Define the heart emojis
heart_emojis = ['❤️', '💕', '💖', '❤️‍🩹', '🫀', '🫶🏼', '💗', '💙', '💜', '💕', '💞', '❤️❤️']

# Define a function to print a message with an emoji
def print_emoji(message, emoji_list, emoji_index):
    chosen_emoji = emoji_list[emoji_index]
    print(f'{message} {chosen_emoji}')

# Define uma função para escolher aleatoriamente um emoji de uma lista
def choose_random_emoji(emoji_list):
    return random.choice(emoji_list)

# Define uma função para imprimir um emoji aleatório com uma mensagem
def print_random_emoji(message, emoji_list):
    random_emoji = choose_random_emoji(emoji_list)
    print(f'{message} {random_emoji}')

#Função lista_emoji
def lista_emoji:
    print("Emojis de coração:")
    for emoji in heart_emoji
    print emoji

#mostrar com posição
def mostrar_lista(nome, lista)
    print(f"Emojis de {nome}:")
    for i, emoji in enumerate(lista,1):
     print(f"{i}.{emoji})

#site
def print_site_list():
    print('www.mycuteemojipy.com.br')
