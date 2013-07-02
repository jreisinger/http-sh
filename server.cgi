#!/usr/bin/env perl

package HttpRex;
use Web::Simple;

my $file = "/tmp/http-rex";

sub dispatch_request {

    sub (GET + ?:out=) {
      write_f($_{out});
    },

    sub (GET) {
      [ 200,
        ['Content-type' => 'text/plain'],
        read_f(),
      ];
    },
}

sub read_f {
    open my $fh, "<", $file or die $!;
    my @lines = <$fh>;
    close $fh;
    return \@lines;
}

sub write_f {
    open my $fh, ">>", $file or die $!;
    print $fh $_ for @_;
    print $fh "\n" . "-" x 80 . "\n";
    close $fh;
}

HttpRex->run_if_script;