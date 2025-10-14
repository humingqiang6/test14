function avg = compute_average(vec)
%COMPUTE_AVERAGE Вычисляет среднее значение вектора.
%   AVG = COMPUTE_AVERAGE(VEC) возвращает среднее значение элементов вектора VEC.

    if isempty(vec)
        error('Input vector is empty.');
    end

    avg = sum(vec) / length(vec);
end