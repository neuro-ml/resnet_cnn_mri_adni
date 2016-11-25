## Residual and Plain Convolutional Neural Networks for 3D Brain MRI Classification

### Rerun experiments for training
1. Install `cuda==7.5` and `cudnn==5.0`.
2. Install the necessary python packages including Lasagne and Theano with `pip install -r requirements.txt`
3. Put your `metadata.csv` in `data` folder. It should have `Label` and `Path` columns for file retrieval and class labels.
4. Run `resnet_train.ipynb` or `vgg_like_train.ipynb` notebook to get classification results in `results_resnet` or `results_cnn` folder.

Note: Resnet code takes up about 2.7GB of video memory per sample in batch.

### Plot results of training
Use `resnet_plot_results.ipynb` or `vgg_like_plot_results.ipynb`

### Plot heatmap of resnet attention
Use `resnet_plot_heatmap.ipynb`
