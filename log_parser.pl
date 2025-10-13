#!/usr/bin/perl
use strict;
use warnings;

my $log_file = 'error.log';
my $error_count = 0;

open(my $fh, '<', $log_file) or die "Could not open file '$log_file' $!";

while (my $line = <$fh>) {
    chomp $line;
    if ($line =~ /ERROR/) {
        $error_count++;
    }
}

close($fh);

print "Total ERROR entries found: $error_count\n";

# Write the result to a new file with a random name
my @chars = ('a'..'z', 'A'..'Z', '0'..'9');
my $random_filename = 'result_';
for (1..8) {
    $random_filename .= $chars[rand @chars];
}
$random_filename .= '.pl';

open(my $out_fh, '>', $random_filename) or die "Could not create output file '$random_filename' $!";
print $out_fh "#!/usr/bin/perl\n";
print $out_fh "# This file contains the log parsing result.\n";
print $out_fh "# Total ERROR entries found: $error_count\n";
close($out_fh);

print "Results saved to: $random_filename\n";