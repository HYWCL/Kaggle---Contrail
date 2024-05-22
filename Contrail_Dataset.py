import torch
import numpy as np
import torchvision.transforms as T
import albumentations as A

class ContrailsDataset(torch.utils.data.Dataset):
    def __init__(self, df, image_size=256, train=True):
        self.df = df
        self.trn = train
        self.normalize_image = T.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
        self.imaeg_size = image_size

        if image_size != 256:
            self.resize_image = T.transforms.Resize(image_size)

    def __getitem__(self, index):
        row = self.df.iloc[index]
        con_path = row.path
        con = np.load(str(con_path))

        img = con[..., :-1]
        label = con[..., :-1]

        if self.trn == True:
            augmentation = self.get_training_augmnetation()(image=img, label=label)
            img, label = augmentation['image'], augmentation['label']

        img = torch.tensor(np.reshape(img, (256, 256, 3))).to(torch.float32).permute(2, 0, 1)
        label = torch.tensor(label)

        if self.image_size != 256:
            img = self.resize_image(img)

        img = self.normalize_image(img)

        return img.float(), label.float()
    
    def __len__(self):
        return len(self.df)
    
    def get_training_augmentation(self):
        train_transform = A.Compose([
            A.OneOf([A.HorizontalFlip(p=1),
                     A.VerticalFlip(p=1),
                     A.RandomRotate90(p=1)],
                     p = 0.2)
        ])
        return train_transform