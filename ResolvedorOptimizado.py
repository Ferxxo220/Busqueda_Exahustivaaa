import math

class ExhaustiveOptimizer:

    def __init__(self, a: float, b: float, precision: float = 0.001):
        
        self.__a = a
        self.__b = b
        self.__precision = precision
        self.__n = self.__calculate_n()

    def __calculate_n(self):
        
        return math.ceil((self.__b - self.__a) / self.__precision)

    def solve(self, objective_function):
      
        delta_x = (self.__b - self.__a) / self.__n
        
        best_x = self.__a
        min_f = objective_function(self.__a)

        
        for i in range(1, self.__n + 1):
            current_x = self.__a + (i * delta_x)
            current_f = objective_function(current_x)

            if current_f < min_f:
                min_f = current_f
                best_x = current_x
        
        return best_x, min_f



if __name__ == "__main__":
    
    test_cases = [
        {
            "nombre": "Cuadrática Básica",
            "func": lambda x: x**2 - 4*x + 4,
            "intervalo": [0, 5]
        },
        {
            "nombre": "Trigonométrica Múltiples valles",
            "func": lambda x: x + math.sin(x),
            "intervalo": [0, 10]
        },
        {
            "nombre": "Polinomial Precisión",
            "func": lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x,
            "intervalo": [0, 5]
        },
        {
            "nombre": "Múltiples Valles Suma Senos",
            "func": lambda x: math.sin(x) + math.sin(2*x),
            "intervalo": [0, 5]
        },
        {
            "nombre": "Punto No Diferenciable Abs",
            "func": lambda x: abs(x - 3.14159),
            "intervalo": [0, 5]
        },
        {
        "nombre": "Frontera Derecha Exponencial",
        "func": lambda x: math.exp(-x),
        "intervalo": [0, 2]
        }
    ]

    print(f"{'Función':<30} | {'Óptimo x':<10} | {'f(x)':<10}")
    print("-" * 55)

    for case in test_cases:
        a, b = case["intervalo"]
        optimizer = ExhaustiveOptimizer(a, b)
        x_opt, f_opt = optimizer.solve(case["func"])
        
        print(f"{case['nombre']:<30} | {x_opt:<10.4f} | {f_opt:<10.4f}")