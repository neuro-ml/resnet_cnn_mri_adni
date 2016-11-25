import numpy as np

def iterate_minibatches_train(inputs, targets, batchsize, shuffle=False):
    """Iterate minibatches on train subset.

    Parameters
    ----------
    inputs : numpy.ndarray
        Numpy array of input images.
    targets : numpy.ndarray
        Numpy array of binary labels.
    batchsize : integer
        Size of the output array batches.
    shuffle : bool, optional
        Whether to shuffle input before sampling. Default is False.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        inputs, targets for given batch.
    """
    assert len(inputs) == len(targets)
    indices = np.arange(len(inputs))
    if shuffle:
        np.random.shuffle(indices)
    m_len = np.min([sum(targets == 1), sum(targets == 0)])
    targets = targets[indices]
    pos = inputs[indices][np.where(targets == 1)[0][:m_len]]
    neg = inputs[indices][np.where(targets == 0)[0][:m_len]]
    pos_t = targets[np.where(targets == 1)[0][:m_len]]
    neg_t = targets[np.where(targets == 0)[0][:m_len]]
    inputs = np.insert(pos, np.arange(len(neg)), neg, axis=0)
    targets = np.insert(pos_t, np.arange(len(neg_t)), neg_t, axis=0)

    assert len(inputs) == len(targets)
    indices = np.arange(len(inputs))
    if shuffle:
        np.random.shuffle(indices)
    if batchsize > len(indices):
        sys.stderr.write('BatchSize out of index size')
        batchsize = len(indices)
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]


def iterate_minibatches(inputs, targets, batchsize, shuffle=False):
    """Iterate minibatches.

    Parameters
    ----------
    inputs : numpy.ndarray
        Numpy array of input images.
    targets : numpy.ndarray
        Numpy array of class labels.
    batchsize : integer
        Size of the output array batches.
    shuffle : bool, optional
        Whether to shuffle input before sampling. Default is False.

    Returns
    -------
    numpy.ndarray, numpy.ndarray
        inputs, targets for given batch.
    """
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]