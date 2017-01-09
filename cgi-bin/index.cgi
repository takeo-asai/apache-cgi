#!/usr/bin/perl
package Linter;

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/local/lib/perl5";
use Perl::Lint;
use Data::Dumper;

our $VERSION = '0.1';

print "Content-type: text/html\n\n";
print 'Hello, World.';

my $linter = Perl::Lint->new;
my $target_files = ['index.cgi'];
my $violations   = $linter->lint($target_files);

print {*Dumper} $violations;

1;
