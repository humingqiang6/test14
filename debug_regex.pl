#!/usr/bin/perl
use strict;
use warnings;

my $text = 'Please contact us at support@example.com or sales@company.org for more information. Invalid: @.com, also invalid: user@@domain.net';

# Используем регулярное выражение в списочном контексте
my @matches = $text =~ /(?<!\S)([\w\.\-]+@[\w\-]+(\.[\w\-]+)+)(?!\S)/g;

print "Raw matches found: ", scalar(@matches), "\n";
for my $match (@matches) {
    print "Match: '$match'\n";
}