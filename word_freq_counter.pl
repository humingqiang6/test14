#!/usr/bin/env perl
use strict;
use warnings;

my $filename = $ARGV[0] or die "Usage: $0 <filename>\n";

open(my $fh, '<', $filename) or die "Could not open file '$filename' $!";

my %word_count;
while (my $line = <$fh>) {
    chomp $line;
    $line =~ s/[[:punct:]]/ /g; # Remove punctuation
    my @words = split /\s+/, lc $line; # Split on whitespace and convert to lowercase
    for my $word (@words) {
        next if $word eq ""; # Skip empty strings
        $word_count{$word}++;
    }
}

close $fh;

for my $word (sort keys %word_count) {
    print "$word: $word_count{$word}\n";
}