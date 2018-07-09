squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb.html
python squiggle_vectors.py
python squiggle_bases.py
squiggle ../../example_seqs/human_HBB.fasta -d 650 650 -o human_hbb_gates.html  --method=gates
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_yau.html --method=yau
python yau_bases.py
python yau-bp_bases.py
squiggle ../../example_seqs/test.fasta -d 650 325 -o randic_example.html -t "GATC" --method=randic
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_randic.html --method=randic --skip
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_qi.html --method=qi --skip
squiggle ../../example_seqs/human_HBB.fasta ../../example_seqs/chimpanzee_HBB.fasta ../../example_seqs/norway_rat_HBB.fasta ../../example_seqs/rhesus_HBB.fasta -d 650 550 -o multiple.html
squiggle ../../example_seqs/human_HBB.fasta ../../example_seqs/chimpanzee_HBB.fasta -d 325 200 -o separate.html --separate
squiggle ../../example_seqs/human_HBB.fasta ../../example_seqs/chimpanzee_HBB.fasta -d 325 200 -o no-link-x.html --separate --no-link-x
squiggle ../../example_seqs/human_HBB.fasta ../../example_seqs/chimpanzee_HBB.fasta -d 650 325 -p Accent -o colors.html
squiggle ../../example_seqs/human_HBB.fasta -d 650 150 -o dimensions.html
squiggle ../../example_seqs/human_HBB.fasta  -d 650 325 -o title.html -t β-globin
