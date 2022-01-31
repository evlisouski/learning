import matplotlib.pyplot as plt
import nltk

# region ВЫЗВАТЬ GUI для загрузки модулей и библиотек
is_handle = input("Для загрузки моделей, модулей в GUI режиме введите Y: ")
if is_handle == "Y":
    while is_handle == "Y":
        nltk.download()
        is_handle = input(
            "Для повторной загрузки GUI введите Y, для продолжения программы введиле любое другое значение: ")
        if is_handle != "Y":
            break
# endregion


text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

from nltk.tokenize import word_tokenize

word_tokenized = word_tokenize(text)

from nltk.probability import FreqDist

fd = FreqDist(word_tokenized)
print(fd.most_common(3))
fd.plot(30, cumulative=False)
plt.show()
