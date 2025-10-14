const std = @import("std");

pub const Point = struct {
    x: f32,
    y: f32,

    pub fn init(x: f32, y: f32) Point {
        return Point{ .x = x, .y = y };
    }

    pub fn writeToFile(self: Point, allocator: std.mem.Allocator, directory: []const u8) !void {
        const random = std.crypto.random;
        var file_name_buffer: [16]u8 = undefined;
        const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        for (&file_name_buffer) {
            |*byte| byte.* = charset[random.uintLessThan(usize, charset.len)];
        }
        const file_name = try std.fmt.allocPrint(allocator, "{s}/point_{}.bin", .{ directory, file_name_buffer });
        defer allocator.free(file_name);

        const file = try std.fs.cwd().createFile(file_name, .{});
        defer file.close();

        const writer = file.writer();
        try writer.writeAll(std.mem.asBytes(&self.x));
        try writer.writeAll(std.mem.asBytes(&self.y));
        std.debug.print("Point saved to {s}\n", .{file_name});
    }
};