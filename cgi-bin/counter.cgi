#!/usr/bin/perl
package Counter;

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/local/lib/perl5";
use Imager;
our $VERSION = '0.1';

# constants
my $number_of_digits = 10;
my $digit_width = 10;
my $digit_height = 10;


# counter
# No Lock may crash data
open(IN, "counter.dat");
my $counter = <IN>;
close(IN);
$counter++;
open(OUT, "> counter.dat");
print OUT $counter;
close(OUT);

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

# output
print "Content-type: image/bmp\n\n";
my $data;
$blank->write(data => \$data, type => 'bmp') or die $blank->errstr;
print $data;

1;
