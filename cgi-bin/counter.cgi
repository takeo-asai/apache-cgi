#!/usr/bin/perl
package Counter;

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/local/lib/perl5";
use Imager;

# constants
my $number_of_digits = 10;
my $digit_width = 10;
my $digit_height = 10;


my $counter = 76156;

# load digit images
my @numbers = ();
for (my $i = 0; $i < 10; $i++) {
    my $n = Imager->new;
    $n->read(file => "imgs/$i.bmp") or die $n->errstr;
    push(@numbers, $n);
}

# create counter
my $counter_width = $digit_width * $number_of_digits;
my $blank = Imager->new(xsize=>$counter_width, ysize=>$digit_height);
$blank->box(filled=>1, color=>'#FFFFFF');
my $i = 0;
foreach my $char ( split //, sprintf("%0".$number_of_digits."d", $counter) ) {
  $blank = $blank->paste(left => $counter_width - $digit_width*($number_of_digits-$i), top  => 0, img  => $numbers[$char+0]);
  $i++;
}
$blank->write( file => 'after_test.bmp') or die $blank->errstr;

our $VERSION = '0.1';

print "Content-type: text/html\n\n";
print 'Hello, World.';

1;
