# Функция для решения квадратного уравнения ax^2 + bx + c = 0
function solve_quadratic(a, b, c)
    # Проверка на нулевой коэффициент a
    if a == 0
        if b == 0
            # Если a и b равны нулю, уравнение не имеет решений (c != 0) или имеет бесконечное число решений (c == 0)
            return c == 0 ? "Infinite solutions" : "No solutions"
        else
            # Линейное уравнение bx + c = 0
            return [-c / b]
        end
    end

    # Вычисление дискриминанта
    discriminant = b^2 - 4*a*c

    if discriminant > 0
        # Два различных действительных корня
        sqrt_discriminant = sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return [x1, x2]
    elseif discriminant == 0
        # Один действительный корень (кратный)
        x = -b / (2*a)
        return [x]
    else
        # Комплексные корни
        real_part = -b / (2*a)
        imag_part = sqrt(-discriminant) / (2*a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
        return [x1, x2]
    end
end

# Примеры использования
println("Примеры решения квадратных уравнений:")
println("x^2 - 5x + 6 = 0 -> ", solve_quadratic(1, -5, 6))
println("x^2 - 4x + 4 = 0 -> ", solve_quadratic(1, -4, 4))
println("x^2 + 1 = 0 -> ", solve_quadratic(1, 0, 1))
println("2x + 6 = 0 -> ", solve_quadratic(0, 2, 6))