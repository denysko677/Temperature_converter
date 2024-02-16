def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    print("Вітаємо у конверторі температури!")
    print("Оберіть опцію:")
    print("1. Фаренгейт в Цельсій")
    print("2. Цельсій в Фаренгейт")
    
    choice = input("Ваш вибір (1 або 2): ")
    
    if choice == '1':
        fahrenheit = float(input("Введіть температуру в Фаренгейтах: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} градусів Фаренгейта дорівнює {celsius} градусів Цельсія.")
    elif choice == '2':
        celsius = float(input("Введіть температуру в Цельсіях: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} градусів Цельсія дорівнює {fahrenheit} градусів Фаренгейта.")
    else:
        print("Невірний вибір. Будь ласка, введіть 1 або 2.")

if __name__ == "__main__":
    main()
