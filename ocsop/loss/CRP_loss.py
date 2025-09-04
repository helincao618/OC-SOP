import torch

def compute_super_CP_multilabel_loss(pred_logits, CP_mega_matrices):
    CP_mega_matrices, mask = CP_mega_matrices[:, :, :, :-1].long(), CP_mega_matrices[:, :, :, -1].bool()
    n_relations = CP_mega_matrices.shape[3]
    valid_mask = mask.reshape(-1)
    logits = pred_logits.reshape(-1, n_relations)[valid_mask]
    labels = CP_mega_matrices.reshape(-1, n_relations)[valid_mask]

    cnt_neg = (labels == 0).sum()
    cnt_pos = labels.sum()
    pos_weight = cnt_neg / cnt_pos
    criterion = torch.nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    loss_bce = criterion(logits, labels.float())
    return loss_bce