const std = @import("std");
const print = std.debug.print;

// Определяем структуру Point
const Point = struct {
    x: f32,
    y: f32,

    // Функция для вывода информации о точке
    pub fn printPoint(self: Point) void {
        print("Point: x={}, y={}\n", .{ self.x, self.y });
    }
};

pub fn main() !void {
    // Инициализируем точку
    const p = Point{ .x = 3.14, .y = 2.71 };

    // Выведем информацию о точке в консоль (для отладки)
    p.printPoint();

    // Генерируем случайное имя файла (упрощённо, используя фиксированное имя с суффиксом)
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const prefix = "point_data_";
    const suffix = ".txt"; // Расширение файла
    var random_part: u32 = undefined;
    std.rand.DefaultPrng.init(@intCast(std.time.microTimestamp())).random().fill(&random_part);
    const filename = try std.fmt.allocPrint(allocator, "{s}{d}{s}", .{ prefix, random_part, suffix });

    // Открываем файл для записи
    const file = try std.fs.cwd().createFile(filename, .{ .read = true });

    // Записываем информацию о точке в файл
    try file.writer().print("Point coordinates:\nx: {d:.2}\ny: {d:.2}\n", .{ p.x, p.y });

    // Закрываем файл
    file.close();

    print("Point data written to file: {s}\n", .{filename});
}
