# CAMAL: Context-Aware Multi-scale Attention framework for Lightweight Visual Place Recognition

- Three benchmark datasets tested on the proposed methodology:

1) SPEDTest
2) St Lucia
3) Synthesized Nordland


If you use the datasets/results, please cite the following publication:

```
@article{khaliq2019camal,
  title={CAMAL: Context-Aware Multi-scale Attention framework for Lightweight Visual Place Recognition},
  author={Khaliq, Ahmad and Ehsan, Shoaib and Milford, Michael and McDonald-Maier, Klaus},
  journal={arXiv preprint arXiv:1909.08153},
  year={2019}
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

