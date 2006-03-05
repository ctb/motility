use motility_ext;

$a = motility_ext::find_iupac("ACGGT", "G", 0);

foreach $item (@$a) {
    print "(";
    print $item->{"start"}, ", ";
    print $item->{"end"}, ", ";
    print $item->{"orientation"}, ", ";
    print "'", $item->{"match"}, "'";
    print ")\n";
}

print "---\n";

$pwm = [ { A => 0.0, C => 0.0, G => 1.0, T => 0.0, N => 0.0 } ];

$a = motility_ext::find_pwm("ACGTG", $pwm, 1);
foreach $item (@$a) {
    print "(";
    print $item->{"start"}, ", ";
    print $item->{"end"}, ", ";
    print $item->{"orientation"}, ", ";
    print "'", $item->{"match"}, "'";
    print ")\n";
}

print "---\n";

$op_en = [ { A => 1.0, C => 1.0, G => 0.0, T => 1.0, N => 1.0 } ];

$a = motility_ext::find_energy("ACGTG", $op_en, 0);
foreach $item (@$a) {
    print "(";
    print $item->{"start"}, ", ";
    print $item->{"end"}, ", ";
    print $item->{"orientation"}, ", ";
    print "'", $item->{"match"}, "'";
    print ")\n";
}

