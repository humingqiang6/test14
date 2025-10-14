const std = @import("std");
const Point = @import("point.zig").Point;

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    const my_point = Point.init(3.14, 2.71);

    try my_point.writeToFile(allocator, "data");
}