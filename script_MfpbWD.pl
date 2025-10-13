my $error_count = 0;
open my $fh, "<", "/workspace/error.log" or die "Cannot open log file: $!";
while (my $line = <$fh>) {
    if ($line =~ /ERROR/) {
        $error_count++;
    }
}
close $fh;
print "Total errors found: $error_count\n";
