#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/../local/lib/perl5";
use Test::More;

ok(1 == 1);

require_ok('Perl::Lint');

done_testing();
