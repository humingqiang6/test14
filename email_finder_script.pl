#!/usr/bin/perl
use strict;
use warnings;

# A sample text containing email addresses
my $text = 'Please contact us at support@example.com or sales@example.org for more information. You can also try invalid@.com or user@sub.domain.co.uk';

# Regular expression to find email addresses
# This is a basic pattern: word characters, dots, hyphens, followed by @, then more characters, a dot, and a domain ending.
my @emails = $text =~ /[\w\.\-]+@[\w\-]+\.[\w\-]+/g;

print "Found the following email addresses:\n";
foreach my $email (@emails) {
    print "  - $email\n";
}
