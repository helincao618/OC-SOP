<div align="center">
  <h1 align="center">OC-SOP: Enhancing Vision-Based 3D Semantic Occupancy Prediction by Object-Centric Awareness</h1>

  <p align="center">
    <a href="https://helincao618.github.io/">Helin Cao</a> and <a href=https://www.ais.uni-bonn.de/behnke/ target=_blank rel=noopener>Sven Behnke</a>
      <br>
      University of Bonn and Lamarr Institute, Bonn, Germany
    <br />
    <strong>SMC 2025</strong>
    <br />
    <a href="https://arxiv.org/abs/2506.18798">Arxiv</a> | <a href="https://sites.google.com/view/ocsop">Project page</a>
    <br />
  </p>
</div>

# Teaser

<img src="./teaser/ocsop.png"  />

# Table of Content
- [Preparing](#preparing)
  - [Setup](#setup)  
  - [Datasets](#datasets)
- [Scripts](#scripts)
  - [Training](#training)
  - [Evaluation](#evaluation)
  - [Visualization](#visualization)
- [Citation](#citation)
- [License and Acknowledgement](#license-and-acknowledgement)

# Preparing

## Setup

We recommend you to use [anaconda](https://www.anaconda.com/) to manage dependencies. You may need to change the torch and cuda version according to your computer.

1. Create conda environment:
```
$ conda create -y -n ocsop python=3.8
$ conda activate ocsop
```

2. Please install [PyTorch](https://pytorch.org/): 
```
conda install pytorch=1.13.0 torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

3. Install the additional dependencies:
```
cd OC-SOP/
pip install -r requirements.txt
```

4. We use [dvis](https://github.com/SirWyver/dvis) for visualization, which is a lightweight but efficient tool with a web server. We recommend you to use another conda environment to visualize the result. 

```
conda create --name dvis python=3.8 requests matplotlib pyyaml tqdm imageio
conda activate dvis
pip install visdom
git clone git@github.com:SirWyver/dvis.git
cd dvis
pip install .
```
## Datasets
- The **Semantic Scene Completion dataset v1.1** (SemanticKITTI voxel data (700 MB)) from [SemanticKITTI website](http://www.semantic-kitti.org/dataset.html#download)
-  The **KITTI Odometry Benchmark calibration data** (Download odometry data set (calibration files, 1 MB)) and the **RGB images** (Download odometry data set (color, 65 GB)) from [KITTI Odometry website](http://www.cvlibs.net/datasets/kitti/eval_odometry.php).
- The dataset folder at **/path/to/semantic_kitti** should have the following structure:
    ```
    └── /path/to/semantic_kitti/
      └── dataset
        └── sequences
          ├── 00
          | ├── image_2
          | ├── labels
          | ├── velodyne
          | ├── voxels
          | ├── calib.txt
          | ├── poses.txt
          | └── times.txt
          ├── 01
          ...
    ```
- The **KITTI 3D Object Detection dataset** (Download left color images (12 GB), Velodyne point clouds (29 GB), calibration files, and training labels (5 MB)) from [KITTI Object Detection website](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d).  

# Scripts
All the scripts is controlled by the `/OC-SOP/ocsop/config/`

## Training
To train the diffusion model, adjust the configuration file at `config/ocsop.yaml`, then start the training process with:

```
python train.py
```

## Evaluation
Put the checkpoints in the `/path/to/kitti/logdir/trained_models/kitti.ckpt`, then run:
```
python evaluation.py
```

## Visualization
Please follow the guide of [dvis](https://github.com/SirWyver/dvis), you need to setup the server before running the script.
```
python visualization.py
```

## Citation
If you find this work or code useful, please cite our paper and give this repo a star :)
```
@inproceedings{cao2025ocsop,
  title = {{OC-SOP}: Enhancing {Vision-Based} 3D Semantic Occupancy Prediction by {Object-Centric} Awareness},
  author = {Cao, Helin and Behnke, Sven},
  booktitle = {IEEE Int. Conf. on Systems, Man, and Cybernetics (SMC)},
  year = {2025},
}
```

# License and Acknowledgement
OC-SOP is released under the [MIT license](./LICENSE). Our code follows several awesome repositories. We appreciate them for making their codes available to public.
- [MonoScene](https://github.com/astra-vision/MonoScene)
- [DVIS](https://github.com/SirWyver/dvis)
- [SemanticKitti](https://github.com/PRBonn/semantic-kitti-api)