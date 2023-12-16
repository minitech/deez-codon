This is an implementation of DeeZ, a reference-based compression algorithm in the programming language Codon

Compression benchmark for the quality scores of the *E. coli* DH10B MiSeq sample MiSeq_Ecoli_DH10B_110721_PF:

|                       | Size        | Compression time |
| --------------------: | ----------: | ---------------: |
| Uncompressed          | 1.8 GiB     |                  |
| DeeZ                  | 681 MiB     | 2m 20s           |
| deez-codon (no index) | 651 MiB     | 3m 22s           |
