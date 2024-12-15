import torch
from torchvision.utils import make_grid
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import torchvision.transforms as transforms
import torchvision
import os
import matplotlib.pyplot as plt
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def dataloader(batch_size):
  folder = 'picFolder'
  dataroot = os.getcwd() + "/" + folder
  if not os.path.exists(dataroot):
    os.makedirs(dataroot)
  transform=transforms.Compose([ transforms.Resize(64),transforms.CenterCrop(64),transforms.ToTensor(),transforms.Normalize((0.5),(0.5))])
  dataset=torchvision.datasets.MNIST(root=dataroot, train=True,transform=transform, download=True)
  data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
  return data_loader

def show_and_save(file_name, img):
    npimg = np.transpose(img.numpy(), (1, 2, 0))
    f = "./%s.png" % file_name
    fig = plt.figure(dpi=200)
    fig.suptitle(file_name, fontsize=14, fontweight='bold')
    plt.imshow(npimg)
    plt.imsave(f, npimg)


def plot_loss(loss_list):
    plt.figure(figsize=(10, 5))
    plt.title("Loss During Training")
    plt.plot(loss_list, label="Loss")

    plt.xlabel("iterations")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

def vae_gan_training(gen, discrim, data_loader, epochs, lr, alpha, gamma, device, real_batch, max_train_size):

    criterion = nn.BCELoss().to(device)
    optim_E = torch.optim.RMSprop(gen.encoder.parameters(), lr=lr)
    optim_D = torch.optim.RMSprop(gen.decoder.parameters(), lr=lr)
    optim_Dis = torch.optim.RMSprop(discrim.parameters(), lr=lr * alpha)
    z_fixed = Variable(torch.randn((64, 128))).to(device)
    x_fixed = Variable(real_batch[0]).to(device)

    for epoch in range(epochs):
        prior_loss_list, gan_loss_list, recon_loss_list = [], [], []
        dis_real_list, dis_fake_list, dis_prior_list = [], [], []
        for i, (data, _) in enumerate(data_loader, 0):
            if i > max_train_size:
                break
            bs = data.size()[0]

            ones_label = Variable(torch.ones(bs, 1)).to(device)
            zeros_label = Variable(torch.zeros(bs, 1)).to(device)
            zeros_label1 = Variable(torch.zeros(64, 1)).to(device)
            datav = Variable(data).to(device)
            mean, logvar, rec_enc = gen(datav)
            z_p = Variable(torch.randn(64, 128)).to(device)
            x_p_tilda = gen.decoder(z_p)

            output = discrim(datav)[0]
            errD_real = criterion(output, ones_label)
            dis_real_list.append(errD_real.item())
            output = discrim(rec_enc)[0]
            errD_rec_enc = criterion(output, zeros_label)
            dis_fake_list.append(errD_rec_enc.item())
            output = discrim(x_p_tilda)[0]
            errD_rec_noise = criterion(output, zeros_label1)
            dis_prior_list.append(errD_rec_noise.item())
            gan_loss = errD_real + errD_rec_enc + errD_rec_noise
            gan_loss_list.append(gan_loss.item())
            optim_Dis.zero_grad()
            gan_loss.backward(retain_graph=True)
            optim_Dis.step()

            output = discrim(datav)[0]
            errD_real = criterion(output, ones_label)
            output = discrim(rec_enc)[0]
            errD_rec_enc = criterion(output, zeros_label)
            output = discrim(x_p_tilda)[0]
            errD_rec_noise = criterion(output, zeros_label1)
            gan_loss = errD_real + errD_rec_enc + errD_rec_noise

            x_l_tilda = discrim(rec_enc)[1]
            x_l = discrim(datav)[1]
            rec_loss = ((x_l_tilda - x_l) ** 2).mean()
            err_dec = gamma * rec_loss - gan_loss
            recon_loss_list.append(rec_loss.item())
            optim_D.zero_grad()
            err_dec.backward(retain_graph=True)
            optim_D.step()

            mean, logvar, rec_enc = gen(datav)
            x_l_tilda = discrim(rec_enc)[1]
            x_l = discrim(datav)[1]
            rec_loss = ((x_l_tilda - x_l) ** 2).mean()
            prior_loss = 1 + logvar - mean.pow(2) - logvar.exp()
            prior_loss = (-0.5 * torch.sum(prior_loss)) / torch.numel(mean.data)
            prior_loss_list.append(prior_loss.item())
            err_enc = prior_loss + 5 * rec_loss

            optim_E.zero_grad()
            err_enc.backward(retain_graph=True)
            optim_E.step()

            if i % 100 == 0:
                print(
                    '[%d/%d][%d/%d]\tLoss_gan: %.4f\tLoss_prior: %.4f\tRec_loss: %.4f\tdis_real_loss: %0.4f\tdis_fake_loss: %.4f\tdis_prior_loss: %.4f'
                    % (epoch, epochs, i, len(data_loader),
                       gan_loss.item(), prior_loss.item(), rec_loss.item(), errD_real.item(), errD_rec_enc.item(),
                       errD_rec_noise.item()))

        b = gen(x_fixed)[2]
        b = b.detach()
        c = gen.decoder(z_fixed)
        c = c.detach()
        show_and_save('MNISTrec_noise_epoch_%d.png' % epoch, make_grid((c * 0.5 + 0.5).cpu(), 8))
        show_and_save('MNISTrec_epoch_%d.png' % epoch, make_grid((b * 0.5 + 0.5).cpu(), 8))

    plot_loss(prior_loss_list)
    plot_loss(recon_loss_list)
    plot_loss(gan_loss_list)