# Local do arquivo: VarifocalNet/configs/puerta_de_oro/vfnet_meu_dataset.py

# Herda todas as configurações padrão da VFNet com backbone ResNet-50
_base_ = '../vfnet/vfnet_r50_fpn_1x_coco.py'

data_root = '/home/altave/projects/dataset_puerta_de_oro_termal_v2/' 

metainfo = {
    'classes': ('pessoa', 'veiculo'),
    'palette': [(220, 20, 60), (119, 11, 32)]
}
num_classes = 2 

#atualiza a "CABEÇA" do modelo
model = dict(
    bbox_head=dict(num_classes=num_classes)
)

train_dataloader = dict(
    batch_size=4, 
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/instances_train.json',
        data_prefix=dict(img='images/train/')
    )
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/instances_val.json',
        data_prefix=dict(img='images/val/')
    )
)

val_evaluator = dict(ann_file=data_root + 'annotations/instances_val.json')
# test_dataloader = val_dataloader  
# test_evaluator = val_evaluator   

#PESOS PRÉ-TREINADOS (TRANSFER LEARNING)
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/vfnet/vfnet_r50_fpn_1x_coco/vfnet_r50_fpn_1x_coco_20201027-38db6f58.pth'
