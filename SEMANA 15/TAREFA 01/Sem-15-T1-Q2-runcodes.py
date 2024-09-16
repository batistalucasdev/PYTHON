def convert_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

def convert_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * 5/9

def sum_temperatures(temp1, temp2):
    value1, scale1 = temp1
    value2, scale2 = temp2
    
    if scale1 == scale2:
        result_value = value1 + value2
    else:
        if scale2 == 'C':
            value1_in_celsius = convert_to_celsius(value1) if scale1 == 'F' else value1
            result_value = value1_in_celsius + value2
        else:
            value1_in_fahrenheit = convert_to_fahrenheit(value1) if scale1 == 'C' else value1
            result_value = value1_in_fahrenheit + value2
    
    return round(result_value, 4), scale2

def get_temperature_input(prompt):
    while True:
        try:
            temp = float(input())
            scale = input().strip().upper()
            if scale not in ['C', 'F']:
                print("Escala inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
                continue
            return temp, scale
        except ValueError:
            print("Valor inválido. Digite um número válido para a temperatura.")

def main():
    temp1 = get_temperature_input("Primeira Temperatura")
    
    temp2 = get_temperature_input("Segunda Temperatura")
    
    result = sum_temperatures(temp1, temp2)
    print(f"({result[0]}, '{result[1]}')")

main()

