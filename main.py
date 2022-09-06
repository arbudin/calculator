def main():
    print("Привет, я калькулятор :)")

    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")

        action = input("Действие: ")

        if action == "q":
            print("Выход из программы")
            break
        # Если action равен +, -, *, /, то
        if action in ('+', "-", '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))

            if action == "+":
                print("%.2f + %.2f = %.2f" % (x, y, x + y))

            elif action == "-":
                print("%.2f - %.2f = %.2f" % (x, y, x - y))

            elif action == "*":
                print("%.2f * %.2f = %.2f" % (x, y, x * y))

            elif action == "/":
                if action != y:
                    print("%.2f / %.2f = %.2f" % (x, y, x / y))
                else:
                    print("На ноль не делим, увы")

if __name__ == '__main__':
    main()