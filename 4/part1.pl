#!/usr/bin/perl
use warnings;
use strict;

my $filename = '4/input.txt';

open(FH, '<', $filename) or die $!;

my $total = 0; 
while(my $line =<FH>){
    chomp $line;
    my @elves = split(",", $line);
    my @elve1 = split("-",$elves[0]);
    my @elve2 = split("-",$elves[1]);
    if(($elve1[0]<=$elve2[0] && $elve1[1]>=$elve2[1] )|| ($elve2[0]<=$elve1[0] && $elve2[1]>=$elve1[1])){
        $total = $total + 1;
    }
}

print($total);

close(FH);