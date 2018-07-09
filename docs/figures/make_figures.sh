squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb.html -t "Human β-globin"
python squiggle_vectors.py
python squiggle_bases.py
squiggle ../../example_seqs/human_HBB.fasta -d 650 650 -o human_hbb_gates.html -t "Human β-globin" --method=gates
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_yau.html -t "Human β-globin" --method=yau
python yau_bases.py
squiggle ../../example_seqs/test.fasta -d 650 325 -o randic_example.html -t "GATC" --method=randic
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_randic.html -t "Human β-globin" --method=randic --skip
squiggle ../../example_seqs/human_HBB.fasta -d 650 325 -o human_hbb_qi.html -t "Human β-globin" --method=qi --skip
