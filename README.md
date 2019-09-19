# CAMAL: Context-Aware Multi-scale Attention framework for Lightweight Visual Place Recognition

- Three benchmark datasets tested on the proposed methodology:

1) SPEDTest
2) St Lucia
3) Synthesized Nordland


If you use the datasets/results, please cite the following publication:

```
@misc{1909.08153,
Author = {Ahmad Khaliq and Shoaib Ehsan and Michael Milford and Klaus McDonald-Maier},
Title = {CAMAL: Context-Aware Multi-scale Attention framework for Lightweight Visual Place Recognition},
Year = {2019},
Eprint = {arXiv:1909.08153},
}
```

- Each dataset contains two traverses of the same route under different conditions and viewpoint
	- A "VPR_Results" folder in each dataset contains CSV files of all the evaluated VPR technqiues
		- All the CSV files have same pattern; each row contains four paramters i.e. (Test Image number, Retrieved Image number, Score, Matched(1/0)?)
		- The user needs to use the Score and Matched values for drawing the PR-curves

- Another "Vocabulary" folder contains N=300 and V=128 clustered regional dictionary trained using 3K images for VLAD retrieval.

- A python script "produceResults.py" can generate the AUC-PR. 

Configuration : N = 300, V=128
 	(AUC-PR Results)

1) SPEDTest: 0.837
2) St Lucia: 0.747
3) Synthesized Nordland: 0.737

