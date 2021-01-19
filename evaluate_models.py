import torch
from vocab import Vocabulary
import evaluation_models
import evaluation

# for flickr
print('\nEvaluation on Flickr30K:')
evaluation.evalrank("/SSD/VSRN_CTC/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/Flickr30K/data/', split="test", fold5=False)


# for TextCaps Validation set
print('\nEvaluation on TextCaps Validation set:')
evaluation.evalrank("/SSD/VSRN/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/TextCaps/Flickr_Format/', split="dev", fold5=False)

# for NewSplit STACMR set
print('\nEvaluation on STACMR:')
evaluation.evalrank("/SSD/VSRN_CTC/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/Coco-Text/ST_CMR_testdataset/New_Split/Flickr_Format/', split="dev", fold5=False)
evaluation.evalrank("/SSD/VSRN_CTC/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/Coco-Text/ST_CMR_testdataset/New_Split/Flickr_Format/', split="test", fold5=False)
