## Residual and Plain Convolutional Neural Networks for 3D Brain MRI Classification

https://arxiv.org/abs/1701.06643

Authors:
[Sergey Korolev](https://github.com/libfun), [Amir Safiullin](https://github.com/amigoml), [Mikhail Belyaev](https://github.com/mibel), [Yulia Dodonova](https://github.com/YuliaD)

____

Scripts for training without Docker image are located in `scripts` folder

____

### Install docker-jupyter

Install Docker https://docs.docker.com/engine/installation/

Install nvidia-docker https://github.com/NVIDIA/nvidia-docker/wiki/Installation

### Howto run docker-jupyter

Clone:
``` bash
git clone https://github.com/neuro-ml/resnet_cnn_mri.git

cd resnet_cnn_mri
```

Build:
```bash
[sudo] docker build -t dl_isbi:repr -f Dockerfile .
```

Run container:
```bash
[sudo] nvidia-docker run -it -p 8809:8888 -v ~/absolute/path/to_data:/scripts/data/ dl_isbi:repr bash

```

where ```~/absolute/path/to_data``` is absolute path on your local machine to folder with adni data.

Run notebook inside the container:
```bash
jupyter notebook
```

Open `http://localhost:8809` on your local machine.

_______
#### Data

Place all the .nii files and metadata.csv inside ```~/absolute/path/to_data``` (on your local machine).

metadata.csv should have `Label` and `Path` columns for file retrieval and class labels (you can find sample /scripts/data/metadata.csv).
`Path` value shoult be `data/some/path/to_scan.nii`
