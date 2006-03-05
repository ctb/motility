from motility import IUPAC, find_iupac

class TestIupacSearch:
    def setUp(self):
        self.misc_motifs = ('ACGARATRAWGCNA',
                            'WGATAR',
                            'A', 'C', 'G', 'T', 'N',
                            'TRAWGGAATRW')

    def tearDown(self):
        pass

    def test_len(self):
        for motif in self.misc_motifs:
            motif_obj = IUPAC(motif)
            assert len(motif_obj) == len(motif)

    def test_max(self):
        for motif in self.misc_motifs:
            motif_obj = IUPAC(motif)
            assert motif_obj.max_score() == len(motif)

    def test_min(self):
        for motif in self.misc_motifs:
            motif_obj = IUPAC(motif)
            assert motif_obj.min_score() == motif.count('N')

    def test_a(self):
        motif = 'A'
        motif_obj = IUPAC(motif)

        assert len(find_iupac('A', motif)) == 1
        assert len(motif_obj.find('A')) == 1
        assert motif_obj.calc_score('A') == 1
        
        assert len(find_iupac('C', motif)) == 0
        assert len(motif_obj.find('C')) == 0
        assert motif_obj.calc_score('C') == 0

        assert len(find_iupac('G', motif)) == 0
        assert len(motif_obj.find('G')) == 0
        assert motif_obj.calc_score('G') == 0

        assert len(find_iupac('T', motif)) == 1
        assert len(motif_obj.find('T')) == 1
        assert motif_obj.calc_score('T') == 0 # DOES NOT do RC

        assert len(find_iupac('N', motif)) == 0
        assert len(motif_obj.find('N')) == 0
        assert motif_obj.calc_score('N') == 0

    def test_t(self):
        motif = 'T'
        motif_obj = IUPAC(motif)

        assert len(find_iupac('A', motif)) == 1
        assert len(motif_obj.find('A')) == 1
        assert motif_obj.calc_score('A') == 0 # DOES NOT do RC
        
        assert len(find_iupac('C', motif)) == 0
        assert len(motif_obj.find('C')) == 0
        assert motif_obj.calc_score('C') == 0

        assert len(find_iupac('G', motif)) == 0
        assert len(motif_obj.find('G')) == 0
        assert motif_obj.calc_score('G') == 0

        assert len(find_iupac('T', motif)) == 1
        assert len(motif_obj.find('T')) == 1
        assert motif_obj.calc_score('T') == 1

        assert len(find_iupac('N', motif)) == 0
        assert len(motif_obj.find('N')) == 0
        assert motif_obj.calc_score('N') == 0

    def test_c(self):
        motif = 'C'
        motif_obj = IUPAC(motif)

        assert len(find_iupac('A', motif)) == 0
        assert len(motif_obj.find('A')) == 0
        assert motif_obj.calc_score('A') == 0

        assert len(find_iupac('C', motif)) == 1
        assert len(motif_obj.find('C')) == 1
        assert motif_obj.calc_score('C') == 1

        assert len(find_iupac('G', motif)) == 1
        assert len(motif_obj.find('G')) == 1
        assert motif_obj.calc_score('G') == 0 # DOES NOT do RC

        assert len(find_iupac('T', motif)) == 0
        assert len(motif_obj.find('T')) == 0
        assert motif_obj.calc_score('T') == 0

        assert len(find_iupac('N', motif)) == 0
        assert len(motif_obj.find('N')) == 0
        assert motif_obj.calc_score('N') == 0

    def test_g(self):
        motif = 'G'
        motif_obj = IUPAC(motif)

        assert len(find_iupac('A', motif)) == 0
        assert len(motif_obj.find('A')) == 0
        assert motif_obj.calc_score('A') == 0

        assert len(find_iupac('C', motif)) == 1
        assert len(motif_obj.find('C')) == 1
        assert motif_obj.calc_score('C') == 0 # DOES NOT do RC

        assert len(find_iupac('G', motif)) == 1
        assert len(motif_obj.find('G')) == 1
        assert motif_obj.calc_score('G') == 1

        assert len(find_iupac('T', motif)) == 0
        assert len(motif_obj.find('T')) == 0
        assert motif_obj.calc_score('T') == 0

        assert len(find_iupac('N', motif)) == 0
        assert len(motif_obj.find('N')) == 0
        assert motif_obj.calc_score('N') == 0

    def test_n(self):
        motif = 'N'
        motif_obj = IUPAC(motif)

        assert len(find_iupac('A', motif)) == 1
        assert len(motif_obj.find('A')) == 1
        assert motif_obj.calc_score('A') == 1

        assert len(find_iupac('C', motif)) == 1
        assert len(motif_obj.find('C')) == 1
        assert motif_obj.calc_score('C') == 1

        assert len(find_iupac('G', motif)) == 1
        assert len(motif_obj.find('G')) == 1
        assert motif_obj.calc_score('G') == 1

        assert len(find_iupac('T', motif)) == 1
        assert len(motif_obj.find('T')) == 1
        assert motif_obj.calc_score('T') == 1

        assert len(find_iupac('N', motif)) == 1
        assert len(motif_obj.find('N')) == 1
        assert motif_obj.calc_score('N') == 1

    def test_mismatches(self):
        motif = 'WGATAR'
        motif_obj = IUPAC(motif)

        assert len(motif_obj.find_with_mismatches('NGATAN', 0)) == 0
        assert len(motif_obj.find_with_mismatches('NGATAN', 1)) == 0
        assert len(motif_obj.find_with_mismatches('NGATAN', 2)) == 1
        assert len(motif_obj.find_with_mismatches('NGATAN', 3)) == 1
        assert len(motif_obj.find_with_mismatches('NGATAN', 4)) == 2 # finds RC

        try:
            motif_obj.find_with_mismatches('NGATAN', 6)
            assert 0
        except Exception, e:
            pass

        try:
            motif_obj.find_with_mismatches('NGATAN', 7)
            assert 0
        except Exception, e:
            pass
