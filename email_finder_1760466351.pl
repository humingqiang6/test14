#!/usr/bin/perl
use strict;
use warnings;

# Текст для поиска
my $text = 'Please contact us at support@example.com or sales@company.org for more information. Invalid: @.com, also invalid: user@@domain.net';

# Регулярное выражение для поиска email
# (?<!\S) - отрицательное утверждение назад (не может быть непробельного символа перед)
# (?!\S) - отрицательное утверждение вперёд (не может быть непробельного символа после)
my @emails = $text =~ /(?<!\S)[\w\.\-]+@[\w\-]+(?:\.[\w\-]+)+(?!\S)/g;

# Вывод найденных email
print "Found emails: ", join(", ", @emails), "\n";