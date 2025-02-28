def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift_base = ord('А') if char.isupper() else ord('а')  # Определяем базу для сдвига (заглавные или строчные)
            result += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            result += char  # Если символ не буква, оставляем его без изменений
    return result

# Введите своё ФИО
fio = input("Введите своё ФИО: ")

# Сдвиг (например, на 3 буквы вперёд)
shift = 3

# Шифруем
encrypted_fio = caesar_cipher(fio, shift)
print(f"Зашифрованное ФИО: {encrypted_fio}")
