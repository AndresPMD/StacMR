# StacMR (Scene Text Aware Cross Modal Retrieval)

Dataset and code based on our WACV 2021 Accepted Paper: https://arxiv.org/abs/2012.04329

Official Website is online! https://europe.naverlabs.com/research/computer-vision/stacmr-scene-text-aware-cross-modal-retrieval/

Task:

<a href="url"><img src="paper_images/Figure1.png" align="center" height="450" width="450" ></a>
<p></p>

## Install Environment 

Create Conda environment

    $ conda env create -f environment.yml

Activate the environment

    $ conda activate scan


## Coco-Text Captioned (CTC) Dataset:

<a href="url"><img src="paper_images/Figure2.png" align="center" height="240" width="360"  ></a>
<p></p>

To Download the CTC (Coco-Text Captioned) images, simply run:

    $ python CTC_img_downlader.py
 
The annotations are provided within this repo in a json format as CTC_anns.json


## Trained Model Weights

<a href="url"><img src="paper_images/Figure6.png" align="center" height="350" width="400" ></a>
<p></p>

Download Weights: 

https://drive.google.com/file/d/1araiEIbbLdiIzPWzGCWRIz4PEQuftgFb/view?usp=sharing



