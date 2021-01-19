from vocab import Vocabulary
import evaluation

print ('Extracting features for CTC SPLITS!')
evaluation.extract_feats("/SSD/VSRN/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/Coco-Text/ST_CMR_testdataset/New_Split/Flickr_Format/', split="dev", fold5=False)
evaluation.extract_feats("/SSD/VSRN/runs/full_model3_newfeats/model_best.pth.tar", data_path='/SSD/Datasets/Coco-Text/ST_CMR_testdataset/New_Split/Flickr_Format/', split="test", fold5=False)
