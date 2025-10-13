function avg = calculate_average(numbers)
    % Вычисляет среднее значение массива чисел.
    %
    % Входы:
    %   numbers - вектор или массив чисел
    %
    % Выходы:
    %   avg - среднее значение элементов в numbers

    if isempty(numbers)
        avg = NaN; % или 0, в зависимости от предпочтений
    else
        avg = sum(numbers(:)) / numel(numbers);
    end
end