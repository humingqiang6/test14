function avg = calculateMean(vec)
% Функция для вычисления среднего значения вектора или массива
% Вход:
%   vec - вектор или массив чисел
% Выход:
%   avg - среднее значение элементов vec

    if isempty(vec)
        avg = NaN; % Возвращаем NaN, если входной массив пуст
        return;
    end

    avg = sum(vec(:)) / numel(vec); % Вычисляем среднее
end